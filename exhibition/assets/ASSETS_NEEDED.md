# Media Assets — COMPLETE (updated July 5, night)

**✅ ALL IMAGES DONE** (s01–s10, reviewed and approved).
**✅ ALL AUDIO DONE** — trimmed frame-accurately with `tools/trim_mp3.py` and live.
s05 (Cage) has **no audio by design** — the station instruction directs the visitor
to listen to their own room.

## What each station plays

| Station | File | Excerpt (times in the full work) | Length |
|---|---|---|---|
| s01 Debussy | `s01_audio.mp3` | 0:09–3:09 | 3:00 |
| s02 Ives | `s02_audio.mp3` | 0:00–3:00 (opening) | 3:00 |
| s03 Stravinsky | `s03_audio.mp3` | 0:40–3:00 of Part I | 2:20 |
| s04 Rockmore | `s04_audio.mp3` | complete performance | 2:53 |
| s05 Cage | — | silence, by design | — |
| s06 Xenakis | `s06_audio.mp3` | 1:00–4:00 | 3:00 |
| s07 Penderecki | `s07_audio.mp3` | 0:00–3:01 (opening) | 3:01 |
| s08 Lucier | `s08_audio.mp3` | spliced: 0:00–1:15 + 8:08–9:23 + 44:08–45:24 | 3:47 |
| s09 Grisey | `s09_audio.mp3` | 2:38–5:38 | 3:00 |
| s10 Miranda | `s10_audio.mp3` | 1:40–3:40 | 2:00 |

These excerpt timings are shown in the exhibition's info panel with a link to
the full performance (`ytMusic` per station).

## Trimming tool

```bash
python3 tools/trim_mp3.py in.mp3 out.mp3 <seconds>          # first N seconds
python3 tools/trim_mp3.py in.mp3 out.mp3 0:40- 8:08-9:23    # segments, M:SS, open end ok
```

No re-encode, frame-accurate (~26 ms), auto-strips the Xing/Info header so players
report the trimmed duration. Verify: `afinfo out.mp3 | grep duration`.

## Optional remaining: video (`sNN_video.mp4`, H.264), in priority order
1. **s04** Theremin — seeing hands play the air IS the exhibit: https://www.youtube.com/watch?v=pSzTPGlNa5U
2. **s07** Penderecki — gerubach animated graphic score: https://www.youtube.com/watch?v=HilGthRhwP8
3. **s06** Xenakis — animated score shows the particle cloud moving: https://www.youtube.com/watch?v=nvH2KYYJg-o
4. **s03** Rite of Spring — visceral orchestra footage: https://www.youtube.com/watch?v=EkwqPJZe8ms

## Testing
Serve over HTTP (not file://): `cd exhibition && python3 -m http.server 8080`.
Live site: https://yuvalshemla.github.io/physics-music/
