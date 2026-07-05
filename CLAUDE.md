# CLAUDE.md — Working Guide

## What this is

"Waves, Particles, and Sound" — a 3D virtual exhibition on how physics shaped Western music.
Final project for Columbia University Music Humanities (Summer A 2026, Prof. Peter M. Susser),
**due Sunday July 6, 2026**, 40% of the grade. The format requirement: NOT a paper.

The entire exhibition is **one self-contained file**: `exhibition/index.html` (A-Frame 1.6 from CDN).
No build step, no dependencies, no framework. Edit the file, refresh the browser.

Deployed on **GitHub Pages** from the `main` branch root: https://yuvalshemla.github.io/physics-music/
(the root `index.html` is only a redirect into `exhibition/`). Pushing to `main` redeploys automatically
(allow ~1 minute). `.nojekyll` keeps Pages from running Jekyll.

## Layout: the rotunda

- Circular hall, 11 slots of `STEP = 360/11` degrees. Slot 0 is the **Great Door** (golden double door,
  arch "MDCCCXCIV -- MMXXIII", INTRODUCTION panel to its right, EPILOGUE panel to its left) — it is both
  the beginning and the end. Stations 1–10 fill the remaining slots **chronologically clockwise**:
  Debussy 1894 (right of the door) → … → Miranda 2023 (left of the door).
- Geometry constants at the top of the script: `WALL_R = 25` (station walls), `STAND_R = 16` (visitor
  ring). Station roots sit at radius 20 with rotation `-angle`, so the local wall plane (z = −5) lands at
  radius 25 facing the center. Helper: `slotXZ(angleDeg, radius)`.
- Room shell: floor/ceiling circles r=28, wall cylinder r=27 h=9, timeline torus y=7.5, oculus overhead,
  warm house light at center (#ffe3b0). Center dais uses the door's gold palette (#b08850 ring,
  #e6c98a lettering).
- Yaw math: position `(R sinφ, 0, −R cosφ)`; facing outward = yaw `−φ`. Proximity angle = `atan2(x, −z)`.
  Camera within r<7 of center → station 0; otherwise nearest slot by angle; slot 0 → station id 11 (door).

## Station anatomy (built by `buildStation(s)`)

Everything is generated from the single **`stations` array** — the single source of truth for all content.
Each station has: giant year floating above the wall (ring of dates), header (number, name, date),
THE PHYSICS / THE MUSIC section headers, three framed media slots (physics left, center, music right),
captions on small wooden plaques, and three wall paragraphs (`wallPhysics`, `wallConnection`, `wallMusic`)
on framed wooden boards. Station lights are colored per station (`s.color`).

**Wooden plaques** (`addPlaque` / `fitPlaques`): every caption and wall paragraph gets a wood frame
(#4a3620) + dark inner panel (#15100a) behind it. Boards are **auto-sized to the rendered text** after the
font loads (THREE.Box3 on the text mesh, converted to station-root local space) — retried at 400/1200/2500/
5000 ms after scene `loaded`. If you add new wall text, call `addPlaque(root, textEl, zFrame, pad)`.

**Images are unlit**: media planes use `shader: flat` so station-colored lights never tint them — they
read as if the picture is the light source. Keep this when touching materials. Renderer has
`anisotropy: 16` to prevent texture shimmer at a distance.

## Media assets

- Per-station folders: `exhibition/assets/sNN/` with exact names `sNN_physics.jpg`, `sNN_music.jpg`,
  `sNN_center.jpg` (optional), `sNN_audio.mp3`, `sNN_video.mp4` (optional). Formats are strict:
  `.jpg` / `.mp3` / `.mp4` (H.264). Convert PNGs with `sips -s format jpeg in.png --out out.jpg`.
- `detectAssets()` HEAD-fetches each candidate URL on load and swaps textures / enables audio buttons.
  **Requires HTTP** — never open via `file://`. Missing files are fine; placeholders show instead.
- Audio **auto-plays 3 s after arriving** at a station (`dwellTimer` in `setStation`). Station 05 (Cage,
  4′33″) deliberately has **no audio** — do not add any.
- `exhibition/assets/ASSETS_NEEDED.md` is the download manifest with verified source URLs — the YouTube
  IDs in the stations array were verified; **do not re-guess them**.
- s03 is complete. Its audio is the full Rite (86 MB) — GitHub's hard limit is 100 MB/file; trim long
  excerpts (60–120 s is the target) before committing more audio.

## UI systems (all in the same file)

- **Bottom info panel**: shows only `connection` + `instruction` + media buttons + "Watch Performance ↗"
  YouTube link. The 3D wall carries short captions; depth lives in the letter.
- **Read More curator letter**: `#letter-overlay`, paper-styled ("Dear visitor," … "— The Curator").
  Contents: full `physics` + `music` + `connection` + `why` (academic rationale, ~120 words/station).
  Opens via **R**, sidebar button, or panel button; closes via Esc/×/click-outside.
- **Keys**: N/B next/back, Space audio pause/resume, V video, R letter. Deep links `?station=0..11`.
- Teleporting sets rig position AND yaw via `faceYaw()` (resets look-controls yawObject/pitchObject and
  camera local position — do not bypass it or the old walking-offset bug returns).

## A-Frame gotchas

- `a-text` values use **literal `\n`** in attribute strings for manual line breaks; rotation order is YXZ;
  floor text = rotation `-90 <yaw> 0`. Long panel texts use `baseline: top` so headings don't collide.
- Browser autoplay is unlocked by the "Enter Exhibition" click; deep-link entry may silently block the
  first auto-play (caught, harmless).

## Verification workflow

```bash
# serve
cd exhibition && python3 -m http.server 8080

# syntax-check the inline JS (from exhibition/)
python3 -c "
import re,subprocess,tempfile,os
h=open('index.html').read()
s=re.findall(r'<script>(.*?)</script>',h,re.S)[0]
f=tempfile.NamedTemporaryFile('w',suffix='.js',delete=False); f.write(s); f.close()
print(subprocess.run(['node','--check',f.name],capture_output=True,text=True))
os.unlink(f.name)"

# headless screenshot of any station (run alone, generous timeout; needs the server running)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --use-gl=swiftshader --enable-unsafe-swiftshader --window-size=1400,900 \
  --virtual-time-budget=15000 --screenshot=out.png "http://localhost:8080/?station=3"
```

Always run the syntax check after editing the script, and screenshot at least one station + the door
(`?station=11`) + the center (`?station=0`) after visual changes.

## Writing style — important

The author is sensitive to **AI-cliché / lyrical phrasing**. All visible text (wall panels, letters, door
panels, essay) is in a plain academic register. Avoid: "Listen for it", "collisions between laboratory and
concert hall", breathless em-dash aphorisms, "journey", "tapestry". Say what the physics is, what the music
does, and what kind of connection holds — each station names its own connection type (direct application /
instrument / parallel response / structural analogy / moral response).

The user's own ideas are embedded and should be preserved: the Theremin seen at the Met (s04), the Doppler
effect from class lecture (s02), the quantum vacuum (s05), Picasso's *Guitar* (s03 center).

## Companion pieces

- `essay/exhibition_essay.tex` — academic essay matching the exhibition text. **No local LaTeX compiler**;
  compile on Overleaf.
- `exhibition_design/EXHIBITION_TEXT.md` — full panel text; `research/` — the curatorial research base.

## Current state / pending

- Exhibition complete and deployed; s03 (Stravinsky) has full media; s01–s02, s04–s10 still need images
  and audio per `ASSETS_NEEDED.md` (drop into `assets/sNN/`, exact names — auto-detected).
- Pending: compile essay PDF on Overleaf; final submission packaging; optional walkthrough video.
