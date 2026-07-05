# OpenVGAL Evaluation

## What It Is
OpenVGAL is a free, open-source 3D virtual gallery generator built on Babylon.js. You upload image folders, it auto-generates walkable 3D rooms with frames, lighting, and navigation, and outputs a static ZIP you host anywhere.

## Test Results

### Strengths
- Fastest path to a gallery: upload images → generate → download ZIP → serve
- Free, open-source, self-hosted (no platform lock-in)
- Babylon.js engine with PBR materials looks professional
- Static output means it works on any web server

### Limitations for Our Exhibition
- **No native audio support** — would need manual code injection
- **No native video support** — same issue
- **No text panels** — only images on walls with basic labels
- **No custom room layouts** — auto-generated rooms follow templates
- **Limited customization** — to add our physics/music/connection panels, we'd need to extensively edit the generated Babylon.js code
- **Different 3D engine** — Babylon.js, not Three.js, so expertise doesn't transfer to A-Frame

### Verdict
OpenVGAL is excellent for pure image galleries but **not suitable for our exhibition** because:
1. We need audio players, video embeds, and rich text panels at every station
2. We need a custom three-panel layout (Physics | Connection | Music)
3. We need control over room sequence and visitor path
4. The amount of post-generation customization needed would exceed building from scratch in A-Frame

**Score: Not advancing to full comparison.** OpenVGAL solves a different problem (quick image galleries). Our exhibition needs the flexibility of A-Frame.

## Recommendation

Replace OpenVGAL in the POC comparison with a direct **A-Frame vs Three.js** comparison. A-Frame wins on development speed, media support, and extensibility. Three.js wins on visual control but at 2x the development time.

**Final platform choice: A-Frame.**
