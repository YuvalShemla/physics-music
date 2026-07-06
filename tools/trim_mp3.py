"""Cut an MP3 by copying whole frames (no re-encode, frame-accurate ~26ms).

Usage:
  python3 tools/trim_mp3.py in.mp3 out.mp3 <seconds>            # first N seconds
  python3 tools/trim_mp3.py in.mp3 out.mp3 START-END [...]      # one or more segments

Times are seconds (float) or M:SS / H:MM:SS. An open end ("START-") runs to EOF.
Segments are concatenated in the order given. The source's Xing/Info/VBRI
header frame is dropped so players report the real trimmed duration.
"""
import sys


def parse_time(t):
    parts = t.split(':')
    if len(parts) == 1:
        return float(parts[0])
    return sum(float(p) * 60 ** i for i, p in enumerate(reversed(parts)))


src, dst = sys.argv[1], sys.argv[2]
segments = []
for arg in sys.argv[3:]:
    if '-' in arg:
        a, b = arg.split('-', 1)
        segments.append((parse_time(a), parse_time(b) if b else float('inf')))
    else:
        segments.append((0.0, parse_time(arg)))

data = open(src, 'rb').read()

# Skip ID3v2 tag if present
pos = 0
if data[:3] == b'ID3':
    size = (data[6] << 21) | (data[7] << 14) | (data[8] << 7) | data[9]
    pos = 10 + size

BITRATES = {0b0001:32,0b0010:40,0b0011:48,0b0100:56,0b0101:64,0b0110:80,0b0111:96,
            0b1000:112,0b1001:128,0b1010:160,0b1011:192,0b1100:224,0b1101:256,0b1110:320}
SAMPLERATES = {0b00:44100,0b01:48000,0b10:32000}

# Index every frame: (offset, length, start_time)
frames = []
elapsed = 0.0
first_audio = True
while pos + 4 <= len(data):
    b0, b1, b2 = data[pos], data[pos+1], data[pos+2]
    if not (b0 == 0xFF and (b1 & 0xE0) == 0xE0):
        pos += 1
        continue
    version = (b1 >> 3) & 0b11
    layer = (b1 >> 1) & 0b11
    if version != 0b11 or layer != 0b01:
        pos += 1
        continue
    br_bits = (b2 >> 4) & 0b1111
    sr_bits = (b2 >> 2) & 0b11
    if br_bits not in BITRATES or sr_bits not in SAMPLERATES:
        pos += 1
        continue
    bitrate = BITRATES[br_bits] * 1000
    sr = SAMPLERATES[sr_bits]
    padding = (b2 >> 1) & 1
    flen = (144 * bitrate) // sr + padding
    if pos + flen > len(data):
        break
    # Drop the Xing/Info/VBRI header frame (else players report source duration)
    if first_audio:
        first_audio = False
        body = data[pos:pos+flen]
        if b'Xing' in body or b'Info' in body or b'VBRI' in body:
            pos += flen
            continue
    frames.append((pos, flen, elapsed))
    pos += flen
    elapsed += 1152.0 / sr

out = bytearray()
kept = 0
for start, end in segments:
    for off, flen, t in frames:
        if start <= t < end:
            out += data[off:off+flen]
            kept += 1

open(dst, 'wb').write(bytes(out))
total = kept * 1152.0 / (SAMPLERATES.get(0b00, 44100))
print(f"segments={segments} frames={kept} ~{total:.1f}s bytes={len(out)} ({len(out)/1e6:.1f} MB)")
