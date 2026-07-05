# POC Results — Platform Selection

## Test Conducted
Built the same exhibition station (Station 2: Theremin / Electromagnetism) on three platforms:
1. **A-Frame** — HTML-based WebXR framework (built on Three.js)
2. **Three.js** — Raw JavaScript 3D library
3. **OpenVGAL** — Auto-generated gallery from images (evaluated, not fully built)

## Scoring

| Criterion | Weight | A-Frame | Three.js | OpenVGAL |
|-----------|--------|---------|----------|----------|
| Visual Quality | 25% | 4 | 5 | 3 |
| Media Support (audio/video/text) | 20% | 5 | 4 | 1 |
| Customizability | 20% | 4 | 5 | 2 |
| Ease of Development | 15% | 5 | 3 | 4 |
| Shareability | 10% | 5 | 5 | 5 |
| Cost | 10% | 5 | 5 | 5 |
| **WEIGHTED TOTAL** | 100% | **4.55** | **4.35** | **2.85** |

## Decision: A-Frame

### Why A-Frame Wins

1. **Built-in media primitives**: `<a-image>`, `<a-video>`, `<a-sound>`, `<a-text>` — adding media to a station is one HTML tag, not 20 lines of JavaScript
2. **Declarative HTML**: Each station can be a reusable HTML block. Adding station 3 = copying the station 2 template and changing the content
3. **Automatic navigation**: WASD + mouse look work out of the box. No PointerLockControls setup needed
4. **Development speed**: The A-Frame POC took ~2 hours vs ~4 hours for Three.js, and produces a visually comparable result
5. **Community assets**: A-Frame components for environment, particle effects, and teleportation are available as npm packages
6. **Can import 3D models**: For a polished gallery, we can import a GLTF model from Sketchfab (pre-built gallery room) and place our content inside it
7. **Free, self-hosted**: Deploy as static HTML on GitHub Pages

### Why Not Three.js
Three.js produces slightly better visual quality (tone mapping, shadow control), but:
- 2x development time for the same content
- Manual text rendering (canvas textures) is tedious
- Manual collision detection needed
- Every media type requires manual implementation
- For a deadline-driven project (July 6), speed matters

### Why Not OpenVGAL
OpenVGAL doesn't support audio, video, or text panels natively. Our exhibition needs rich multimedia at every station. The amount of post-generation customization would exceed building from scratch.

## Next Step
Proceed to Stage 3: Build the full 10-station exhibition using A-Frame.
