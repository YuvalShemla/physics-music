# Waves, Particles, and Sound — Exhibition

## How to View

```bash
cd /Users/yuvalshemla/Desktop/music_hum/final_project/exhibition
python3 -m http.server 8080
```

Then open: **http://localhost:8080**

Deep-link to any station: `http://localhost:8080/?station=4` (0 = rotunda center, 1-10 = stations, 11 = the Great Door).

## Layout: The Rotunda

The exhibition is a circular hall. You start at the **center dais**, surrounded by a ring of
ten giant glowing **years** (1894 → 2023) floating above the station walls. Straight ahead is
the **Great Door** — a monumental golden double door marking where the circle begins *and* ends,
flanked by the intro panel ("Before You Begin," beside 1894) and the epilogue panel
("After the Circle," beside 2023). Walk to the door, then follow the circle clockwise through
time; after Station 10 the circle returns you to the door.

## Controls

| Input | Action |
|---|---|
| **W A S D** | Walk |
| **Mouse** | Look around (click the scene to capture the cursor) |
| **N / B** | Jump to next / previous station |
| **Space** | Play / pause this station's music (once audio files are added) |
| **V** | Play / pause this station's video (once video files are added) |
| **Esc** | Free the cursor (to click menus and buttons) |
| **MAP** button | Teleport to any station |
| **Next / Back** buttons | Step through stations without the keyboard |

## Station Order (strictly chronological by musical work)

| # | Station | Physics | Music | Year | Mood |
|---|---------|---------|-------|------|------|
| 01 | The Anatomy of a Single Tone | Helmholtz acoustics (1863) | Debussy, *Prélude à l'après-midi d'un faune* | 1894 | Amber |
| 02 | Sound in Motion | Doppler effect (1842) | Ives, *The Unanswered Question* | 1908 | Twilight blue |
| 03 | Simultaneous Perspectives | Special Relativity (1905) + Cubism | Stravinsky, *The Rite of Spring* | 1913 | Fractured red |
| 04 | Music from Thin Air | Electromagnetism | Theremin / Clara Rockmore | 1920 | Violet |
| 05 | The Sound of Nothing | Quantum vacuum | Cage, *4'33"* | 1952 | White |
| 06 | Music by Probability | Statistical mechanics (1860s) | Xenakis, *Pithoprakta* | 1955 | Green |
| 07 | Sound After the Unthinkable | Nuclear fission (1945) | Penderecki, *Threnody* | 1960 | Ash |
| 08 | The Room Reveals Itself | Room acoustics / standing waves | Lucier, *I Am Sitting in a Room* | 1969 | Gold |
| 09 | Orchestrating the Spectrogram | Fourier analysis (1822) | Grisey, *Partiels* | 1975 | Ocean blue |
| 10 | Quantum Duet | Quantum computing | Miranda, *Qubism* | 2023 | Magenta/cyan |

## Local Media (images / audio / video)

The exhibition auto-detects media files in `assets/`. See **`assets/ASSETS_NEEDED.md`** for the
exact filenames, what to download, and source URLs for every station. No code changes needed —
drop files in, reload, and they appear in the frames / enable the play buttons.

Until files are added, frames show labeled placeholders, and each station links out to
verified YouTube performances and physics explainers.

## Architecture Notes

- Single self-contained `index.html` (A-Frame 1.6). All 10 stations generate from one `stations`
  data array — edit text/colors/links in one place near the top of the `<script>` section.
- Circular geometry: 11 slots of 360/11°; the Great Door at slot 0, stations 1-10 on the rest.
  Station walls at radius 25, visitor viewing ring at radius 16. Teleporting turns you to face
  the station; walking updates the active station by your angle around the room.
- Media auto-pauses when you move to a different station.
- Info panel at the bottom follows you: full panel text in three tabs (Physics / Connection / Music),
  matching the exhibition design document.

## Verified (July 5, 2026)

- JavaScript syntax (node --check)
- Rotunda layout renders in headless Chrome with WebGL (center, Great Door, stations 1 and 6 screenshot-verified)
- Asset auto-detection tested end-to-end with a generated test image
- All YouTube links taken from the verified research files
