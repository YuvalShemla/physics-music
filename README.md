# Waves, Particles, and Sound

**A virtual 3D exhibition on physics and music**
Columbia University — Music Humanities, Summer A 2026 (Prof. Peter M. Susser)

**🌐 Live exhibition: https://yuvalshemla.github.io/physics-music/**

---

## Concept

A browser-based 3D rotunda that traces how developments in physics — from Helmholtz's acoustics to quantum computing — altered the materials, methods, and meaning of Western music. Ten stations are arranged chronologically in a circle, each pairing a physical development with a musical work. A golden Great Door marks both the beginning (1894) and the end (2023) of the sequence.

> Every major expansion of musical possibility happens when musicians learn to control a new physical system.

## The Ten Stations

| # | Year | Physics | Music |
|---|------|---------|-------|
| 01 | 1894 | Helmholtz — overtones & timbre | Debussy, *Prélude à l'après-midi d'un faune* |
| 02 | 1908 | Doppler effect — sound in space | Ives, *The Unanswered Question* |
| 03 | 1913 | Relativity & the loss of a single viewpoint | Stravinsky, *The Rite of Spring* |
| 04 | 1920 | Electromagnetism | Theremin & Clara Rockmore |
| 05 | 1952 | The impossibility of silence | Cage, *4′33″* |
| 06 | 1955 | Statistical mechanics | Xenakis, *Pithoprakta* |
| 07 | 1960 | Waveforms & tone clusters | Penderecki, *Threnody* |
| 08 | 1969 | Resonant frequencies of a room | Lucier, *I Am Sitting in a Room* |
| 09 | 1975 | Spectral analysis | Grisey, *Partiels* |
| 10 | 2023 | Quantum computing | Miranda, *Qubism* |

## Viewing

**Online:** open the [live exhibition](https://yuvalshemla.github.io/physics-music/) in a desktop browser (Chrome/Edge/Firefox/Safari).

**Locally:**

```bash
cd exhibition
python3 -m http.server 8080
# open http://localhost:8080
```

A local server is required (not `file://`) — the exhibition auto-detects media files over HTTP.

### Controls

| Input | Action |
|---|---|
| WASD / arrow keys + mouse drag | Walk & look |
| **N** / **B** | Next / previous station (teleport) |
| **Space** | Pause / resume the station's music (auto-plays 3 s after arrival) |
| **V** | Play station video (where available) |
| **R** | Open the curator's letter (full discussion of the station) |
| **Esc** | Close overlays |

Deep links: `?station=1` … `?station=10`, `?station=0` (center dais), `?station=11` (the Great Door).

## Repository Structure

```
index.html                 → redirects to exhibition/ (GitHub Pages entry)
exhibition/                THE EXHIBITION — one self-contained A-Frame page
  index.html               all scene code, station data, and UI in one file
  assets/sNN/              per-station media (images .jpg, audio .mp3, video .mp4)
  assets/ASSETS_NEEDED.md  manifest of required media + download sources
essay/exhibition_essay.tex companion essay (compile on Overleaf)
exhibition_design/         full panel text for all stations
research/                  curatorial research (candidate works, media sources)
poc/                       platform prototypes (A-Frame vs Three.js vs OpenVGAL)
CLAUDE.md                  working guide for AI-assisted development
```

## Course Connections

The exhibition engages composers and concepts from the Music Humanities syllabus — Debussy, Stravinsky (Week 4), Cage (Week 6), and Ives's spatial music discussed in lecture — and extends the course's chronological arc by revealing a hidden spine: physics as a driver of musical change.

## Credits

Curated and built by Yuval Shemla. Rendering: [A-Frame 1.6](https://aframe.io). All images, audio, and video excerpts are used for educational purposes within a university course project; sources are listed in `exhibition/assets/ASSETS_NEEDED.md` and on each station's panel.
