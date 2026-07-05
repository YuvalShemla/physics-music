# POC Demos — How to Run

## Quick Start

Open a terminal in this directory and run:

```bash
cd /Users/yuvalshemla/Desktop/music_hum/final_project/poc
python3 -m http.server 8080
```

Then open in your browser:
- **A-Frame POC:** http://localhost:8080/aframe/
- **Three.js POC:** http://localhost:8080/threejs/

## What Each POC Shows

Both POCs implement the same test station: **Station 2 — The Theremin (Electromagnetism Becomes Music)**

### A-Frame POC (`aframe/index.html`)
- Built with HTML tags only (declarative)
- ~250 lines of HTML
- Built-in WASD + mouse controls (automatic)
- Fog, spotlights (blue for physics, warm for music)
- Three-panel layout: Physics | Connection | Music
- Click-to-play audio button (Wikimedia theremin sample)
- Gallery-style dark room with accent lighting

### Three.js POC (`threejs/index.html`)
- Built with JavaScript + Three.js module imports
- ~300 lines of JavaScript
- PointerLockControls (click to enter, ESC to exit)
- Canvas-rendered text (word-wrapped)
- Same layout and content as A-Frame version
- Collision boundaries (can't walk through walls)
- ACES filmic tone mapping for better lighting

## How to Compare

| Feature | A-Frame | Three.js |
|---------|---------|----------|
| Lines of code | ~250 | ~300 |
| Setup complexity | None (CDN script tag) | Import maps + modules |
| Navigation | Automatic WASD+mouse | Manual PointerLockControls |
| Text rendering | Built-in `<a-text>` | Canvas textures (manual) |
| Visual quality | Good | Slightly better (tone mapping) |
| Audio | HTML5 Audio + button | Same |
| Collision detection | None (walk through walls) | Basic bounds clamping |
| Time to build | ~2 hours | ~4 hours |
| Extensibility | High (components) | Highest (raw API) |

## Verdict

Both work well. A-Frame is recommended for the full exhibition build because:
1. Much less code for the same result
2. Adding new stations = adding HTML blocks (not JS functions)
3. Media primitives built-in (`<a-image>`, `<a-video>`, `<a-sound>`)
4. Community components for extras (environment, particle effects)
5. Faster iteration during the tight deadline
