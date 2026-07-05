"""Trim an MP3 to the first N seconds by copying whole frames (no re-encode)."""
import sys

src, dst, seconds = sys.argv[1], sys.argv[2], float(sys.argv[3])
data = open(src, 'rb').read()

# Skip ID3v2 tag if present
pos = 0
if data[:3] == b'ID3':
    size = (data[6] << 21) | (data[7] << 14) | (data[8] << 7) | data[9]
    pos = 10 + size
header_end = pos

BITRATES = {0b0001:32,0b0010:40,0b0011:48,0b0100:56,0b0101:64,0b0110:80,0b0111:96,
            0b1000:112,0b1001:128,0b1010:160,0b1011:192,0b1100:224,0b1101:256,0b1110:320}
SAMPLERATES = {0b00:44100,0b01:48000,0b10:32000}

elapsed = 0.0
frames = 0
while pos + 4 <= len(data) and elapsed < seconds:
    b0,b1,b2,b3 = data[pos:pos+4]
    # sync: 11 set bits, MPEG1 Layer III
    if not (b0 == 0xFF and (b1 & 0xE0) == 0xE0):
        pos += 1  # resync
        continue
    version = (b1 >> 3) & 0b11      # 3 = MPEG1
    layer   = (b1 >> 1) & 0b11      # 1 = Layer III
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
    pos += flen
    frames += 1
    elapsed += 1152.0 / sr

open(dst, 'wb').write(data[:pos])
print(f"frames={frames} elapsed={elapsed:.1f}s bytes={pos} ({pos/1e6:.1f} MB)")
