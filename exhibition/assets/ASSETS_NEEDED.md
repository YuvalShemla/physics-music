# Media Assets — Remaining: AUDIO ONLY (updated July 5, evening)

**✅ ALL IMAGES DONE.** Every station (s01–s10) has its physics / center / music images
in `exhibition/assets/sNN/`, reviewed and approved. Sources are documented in the
review sheet and the git history.

What remains is **audio** (and optional video). Drop files into `exhibition/assets/sNN/`
with the exact filenames below — the exhibition auto-detects them on page load.

**Formats:** audio `.mp3`, video `.mp4` (H.264).
**Trim to the best 60–120 seconds** with the repo tool (no re-encode, frame-accurate):

```bash
python3 tools/trim_mp3.py in.mp3 out.mp3 <seconds>
afinfo out.mp3 | grep duration   # must report the trimmed length, not the original
```

(Keep files well under 50 MB — GitHub hard limit is 100 MB.)

## Audio checklist

```
s01/s01_audio.mp3   Debussy      — needed
s02/s02_audio.mp3   Ives         — needed
s03/s03_audio.mp3   Stravinsky   ✅ done (3:00 trim)
s04/s04_audio.mp3   Rockmore     — needed
s05/                Cage         — NO AUDIO BY DESIGN (do not add)
s06/s06_audio.mp3   Xenakis      — needed
s07/s07_audio.mp3   Penderecki   — needed
s08/s08_audio.mp3   Lucier       — needed
s09/s09_audio.mp3   Grisey       — needed
s10/s10_audio.mp3   Miranda      — needed
```

## What to extract, per station

| File | Excerpt | Source |
|---|---|---|
| `s01_audio.mp3` | Opening flute solo of *Prélude à l'après-midi d'un faune* (~90s from the start) | https://www.youtube.com/watch?v=-YazhxBA7oo |
| `s02_audio.mp3` | *The Unanswered Question* — trumpet question + woodwind answer (~90s) | https://www.youtube.com/watch?v=vXD4tIp59L0 (Bernstein/NYP) |
| `s04_audio.mp3` | Clara Rockmore, "The Swan" — **use the full ~2min, no trim** | https://www.youtube.com/watch?v=pSzTPGlNa5U |
| `s06_audio.mp3` | *Pithoprakta* — the glissandi cloud section (~90s) | https://www.youtube.com/watch?v=nvH2KYYJg-o |
| `s07_audio.mp3` | *Threnody* opening scream (~60–90s from the start) | https://www.youtube.com/watch?v=Dp3BlFZWJNA (Wit/Polish RSO) |
| `s08_audio.mp3` | *I Am Sitting in a Room* — iteration 1 (clear speech, ~30s) + a late iteration (pure tones, ~45s), spliced or two cuts | https://www.youtube.com/watch?v=fAxHlLK3Oyk |
| `s09_audio.mp3` | *Partiels* opening — trombone E blooming into the ensemble (~2min from the start) | https://www.youtube.com/watch?v=4Db_uz1a2v8 (Dal Niente) |
| `s10_audio.mp3` | *Swirling Qubits* / *Qubism* track excerpt (~90s) | https://soundcloud.com/51beats/sets/51bts080-eduardo-reck-miranda-qubism or https://www.youtube.com/watch?v=5PilN5ynYv8 |

Note: `tools/trim_mp3.py` trims **from the start**. For mid-piece excerpts (s06 cloud
section, s08 late iteration), download and give Claude the file + the start time —
or ask for the start-offset option to be added to the tool.

## Optional video (`sNN_video.mp4`), in priority order
1. **s04** Theremin — seeing hands play the air IS the exhibit (same YouTube video as the audio)
2. **s07** Penderecki — gerubach animated graphic score: https://www.youtube.com/watch?v=HilGthRhwP8
3. **s06** Xenakis — animated score shows the particle cloud moving (same video as audio)
4. **s03** Rite of Spring — visceral orchestra footage (full performance: https://www.youtube.com/watch?v=EkwqPJZe8ms)

## Testing
After adding files, reload the page (must be served over HTTP, not file://) —
Play buttons light up at each station automatically. Then push and verify live at
https://yuvalshemla.github.io/physics-music/
