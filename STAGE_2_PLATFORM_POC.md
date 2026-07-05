# Stage 2: Platform POC — Choosing the 3D Exhibition Technology

## Goal
Build minimal proof-of-concept prototypes on 3 platforms (A-Frame, Three.js, OpenVGAL), compare them side by side, and choose the best one for the full exhibition build. Each POC creates one room with one artwork station (image + audio + text panel) to test the core exhibition experience.

---

## 1. Why POC First?

Building a full exhibition on the wrong platform wastes days. A 2-hour POC on each of 3 platforms reveals:
- How hard is it to create a walkable 3D space?
- Can we embed video/audio/images and text panels on walls?
- Does it look good enough to impress a professor and class?
- Can we share it via URL (no app install)?
- How much control do we have over layout, lighting, and aesthetics?

---

## 2. Platform Candidates

After research, three platforms emerge as the strongest candidates for this project. Each represents a different trade-off:

### Option A: A-Frame (HTML-based WebXR)

**What it is:** An open-source web framework by Mozilla alumni for building 3D/VR experiences using HTML tags. Built on top of Three.js but much simpler to use.

**Why it's a strong candidate:**
- Free, open-source (MIT license)
- Works in any browser — just an HTML file, no build step needed
- Declarative HTML syntax: `<a-box>`, `<a-image>`, `<a-video>`, `<a-sound>`, `<a-text>`
- Built-in first-person navigation (WASD + mouse look)
- Built-in support for images, video, audio, and 3D text
- Used by CERN, Google, NASA, Washington Post for web experiences
- Can be hosted on any static hosting (GitHub Pages, Netlify, even a simple file server)
- Current version: 1.8.0
- Large community, extensive documentation, many examples

**Potential concerns:**
- Requires writing HTML/code (not drag-and-drop)
- Default aesthetics are basic — need custom lighting and textures for a polished look
- Building a realistic gallery room requires either modeling it in Blender or constructing it from primitives

**Best for:** Maximum control, free hosting, code-based customization

### Option B: Three.js (Custom JavaScript 3D)

**What it is:** The dominant JavaScript 3D library. Powers most browser-based 3D experiences. A-Frame is actually built on top of Three.js.

**Why it's a strong candidate:**
- Free, open-source (MIT license), current version r185
- Maximum possible control over every visual detail
- Professional-quality rendering (WebGL/WebGPU)
- Can create photorealistic gallery spaces with proper lighting
- Huge ecosystem of examples, including virtual museum demos
- Can load 3D models (GLTF/GLB format) for pre-built gallery rooms
- Built-in audio support (positional audio via Web Audio API)

**Potential concerns:**
- Significantly more code than A-Frame — need to write JavaScript, not just HTML
- First-person controls require manual setup (PointerLockControls, collision detection)
- Steeper learning curve
- Building a gallery from scratch takes more time

**Best for:** Best visual quality, but highest development effort

### Option C: OpenVGAL (Free, Open-Source 3D Gallery Generator)

**What it is:** An open-source virtual gallery generator built on Babylon.js. Upload images in folders (each folder = one room), click generate, and download a self-hosted ZIP of static files. No accounts, no subscriptions.

**Why it's a strong candidate:**
- Completely free and open-source (GitHub: lbartworks/openvgal)
- Generates walkable 3D gallery rooms automatically from images
- Outputs a static ZIP — host anywhere (GitHub Pages, Netlify, any web server)
- Real-time 3D (WebGL via Babylon.js)
- Rooms, lighting, frames, and navigation configured automatically
- No backend or database required
- Full ownership — no platform lock-in, no risk of service shutdown
- Can be customized by editing the generated code

**How it works:**
1. Upload images (each folder = a room)
2. One click generates rooms, lighting, frames, navigation
3. Download a ZIP of static files
4. Upload to any web server

**Potential concerns:**
- Primarily designed for image galleries — audio/video support may be limited
- Generated gallery rooms follow standard templates — less control over custom room shapes
- May need manual code edits to add audio players, video embeds, or physics diagrams
- Newer project, smaller community than A-Frame or Three.js

**Best for:** Fast, free, self-hosted gallery with room for code-level customization

### Option D: Kunstmatrix (No-Code Commercial Platform)

**What it is:** A purpose-built commercial platform for virtual 3D art exhibitions.

**Why considered:** Pre-designed rooms, supports art/audio/video, has educational tier (KUNSTMATRIX.EDU).

**Pricing:** Free tier has 0 public exhibitions. Basic plan €10/month for 5 public exhibitions.

**Why it's the backup, not a main POC:** Free tier doesn't allow sharing. Limited customization. Monthly cost. Can't add custom interactive elements for physics visualizations. But if all code-based options fail, it's a reliable fallback.

### Also Discovered: Shapespark, Exhibbit, ArtPlacer

- **Shapespark**: High-quality 3D walkthrough software used by museums. 30-day free trial. But requires desktop software installation and 3D modeling skills. Overkill for this project.
- **Exhibbit**: Purpose-built for virtual exhibitions with audio/video support. 7-day free trial. Subscription-based. Professional quality but costs money.
- **ArtPlacer**: Virtual gallery builder. Good quality but focused on art sales, not educational exhibitions.

---

## 3. Other Platforms Considered (and why they're not in the POC)

| Platform | Why excluded from POC |
|---|---|
| **Artsteps** | Free tier, good for simple galleries, but JS-heavy SPA that's hard to customize; limited media types |
| **Spatial.io** | Gaming/social platform, not curated exhibitions; free tier feels like a game, not a gallery |
| **Mozilla Hubs** | Mozilla shut down the hosted service in 2024; self-hosting requires infrastructure |
| **Matterport** | Designed for scanning real spaces (digital twins), not creating fictional spaces; expensive |
| **FrameVR** | VR-focused, built on Vuetify; less suited for a traditional walkthrough gallery |
| **Oncyber** | Parent company Cyber Meta Inc. was dissolved ~end of 2024; platform may be unstable |
| **Exhibit.so** | 2D linear stories (like a scrolling webpage), not a true 3D walkable space |
| **Shapespark** | Requires desktop software install + 3D modeling. 30-day trial, then €260/month for self-hosting. Overkill |
| **Kunstmatrix** | Free tier = 0 public exhibitions. €10+/month. Good quality but no code control |

---

## 4. POC Specification

Each POC must implement the **exact same test station** so we can compare apples to apples.

### The Test Station: "The Theremin — Electromagnetism Becomes Music"

This was chosen as the POC test case because:
- It has a clear image (photo of Leon Theremin playing)
- It has a clear audio clip (Clara Rockmore performance, ~60 seconds)
- It has a physics diagram (electromagnetic field diagram)
- It needs a text panel (explaining how the instrument works)
- It's visually interesting and tests all media types

### POC Requirements Checklist

Each POC must demonstrate:

| # | Requirement | Details |
|---|---|---|
| 1 | **Gallery room** | A simple rectangular room with walls, floor, ceiling. Muted colors (dark gray/charcoal walls, lighter floor). |
| 2 | **Image on wall** | A framed image of Leon Theremin playing the instrument, hung on the left wall |
| 3 | **Audio player** | A playable audio clip (Clara Rockmore theremin performance). Should play when visitor approaches or clicks. |
| 4 | **Text panel** | A text panel on the right wall with ~100 words explaining the physics of the theremin |
| 5 | **Second image** | A diagram of electromagnetic fields / theremin circuit on the right wall above the text |
| 6 | **First-person navigation** | WASD keys + mouse to walk through the room and look around |
| 7 | **Lighting** | Ambient lighting + spotlight on the artwork (gallery-style) |
| 8 | **Shareable** | Must be viewable via a URL in any modern browser |

---

## 5. POC Implementation Plans

### POC A: A-Frame

**Setup:** Single HTML file, no build tools needed.

**File structure:**
```
poc/aframe/
  index.html          ← The entire exhibition in one file
  assets/
    theremin-photo.jpg
    theremin-diagram.png
    clara-rockmore.mp3
```

**Implementation approach:**
1. Create an `<a-scene>` with a sky color (dark gallery ambiance)
2. Build the room using `<a-box>` primitives for walls, floor, and ceiling
3. Place `<a-image>` entities on the walls for the photos
4. Add `<a-text>` entity for the text panel (A-Frame has built-in SDF text)
5. Add `<a-sound>` for the audio clip (can be positional or ambient)
6. Set up `<a-light>` components — ambient + directional spotlights
7. Camera with `wasd-controls` and `look-controls` is automatic in A-Frame
8. Host on GitHub Pages or open locally via a simple HTTP server

**Key A-Frame elements to test:**
```html
<a-scene>
  <!-- Room -->
  <a-box position="0 2.5 -5" width="10" height="5" depth="0.1" color="#333"></a-box>

  <!-- Image on wall -->
  <a-image src="assets/theremin-photo.jpg" position="-3 2 -4.9" width="2" height="2.5"></a-image>

  <!-- Text panel -->
  <a-text value="The Theremin..." position="2 2 -4.9" width="3" color="#fff"></a-text>

  <!-- Audio -->
  <a-sound src="assets/clara-rockmore.mp3" position="0 2 -4.9"></a-sound>

  <!-- Lighting -->
  <a-light type="ambient" intensity="0.3"></a-light>
  <a-light type="spot" position="-3 4 -3" target="#theremin-photo"></a-light>
</a-scene>
```

**Estimated effort:** 2-3 hours
**Hosting:** GitHub Pages (free) or `python -m http.server`

---

### POC B: Three.js

**Setup:** HTML + JavaScript, may use Vite for dev server.

**File structure:**
```
poc/threejs/
  index.html
  main.js             ← Three.js scene setup
  assets/
    theremin-photo.jpg
    theremin-diagram.png
    clara-rockmore.mp3
```

**Implementation approach:**
1. Initialize a Three.js scene, camera (PerspectiveCamera), and WebGL renderer
2. Build the room using `BoxGeometry` or `PlaneGeometry` for walls/floor/ceiling
3. Load textures for the artwork using `TextureLoader`, apply to planes on walls
4. Create text using `CSS2DRenderer` (overlaid HTML text) or a canvas-based texture
5. Set up `PointerLockControls` for first-person mouse look
6. Implement WASD movement manually (keyboard event listeners + velocity)
7. Add collision detection (raycasting to walls) to prevent walking through walls
8. Set up lights: `AmbientLight` + `SpotLight` aimed at artwork
9. Add audio using Three.js `AudioListener` + `PositionalAudio`

**Key complexity points:**
- First-person controls require more manual code than A-Frame
- Text rendering in 3D is non-trivial in raw Three.js
- Collision detection needs explicit implementation

**Estimated effort:** 4-6 hours
**Hosting:** GitHub Pages or Netlify (free)

---

### POC C: OpenVGAL

**Setup:** Web-based generator, outputs static files.

**File structure:**
```
poc/openvgal/
  (generated output)/
    index.html
    assets/
    ...
```

**Implementation approach:**
1. Go to openvgal.com
2. Create a folder with the theremin photo and diagram images
3. Upload the folder → generator creates a room with images framed on walls
4. Download the generated ZIP
5. Unzip and serve locally (`python -m http.server`)
6. Test navigation, image quality, lighting
7. Manually edit the generated HTML/JS to add:
   - Audio player (HTML `<audio>` element overlaid or injected into the 3D scene)
   - Text panel (may need to add as a textured plane or HTML overlay)
8. Evaluate how much manual customization is needed beyond the auto-generated gallery

**Estimated effort:** 1-2 hours (generation) + 1-2 hours (customization)
**Hosting:** Any static server — GitHub Pages, Netlify, or `python -m http.server`

---

## 6. Evaluation Criteria

After building all 3 POCs, score each on these criteria (1-5 scale):

| Criterion | Weight | What we're evaluating |
|---|---|---|
| **Visual Quality** | 25% | Does the gallery look professional? Good lighting? Immersive? |
| **Media Support** | 20% | How well does it handle images, audio, video, and text together? |
| **Customizability** | 20% | Can we create custom room shapes, add interactive physics diagrams, control the visitor path? |
| **Ease of Development** | 15% | How quickly can we build the full 10-station exhibition? |
| **Shareability** | 10% | Can we share a single URL? No login required? Works on mobile? |
| **Cost** | 10% | Is it free? If not, is the cost reasonable for a student? |

### Scoring Template

| Criterion | Weight | A-Frame | Three.js | OpenVGAL |
|---|---|---|---|---|
| Visual Quality | 25% | ? | ? | ? |
| Media Support | 20% | ? | ? | ? |
| Customizability | 20% | ? | ? | ? |
| Ease of Development | 15% | ? | ? | ? |
| Shareability | 10% | ? | ? | ? |
| Cost | 10% | ? | ? | ? |
| **WEIGHTED TOTAL** | 100% | ? | ? | ? |

---

## 7. Preliminary Assessment (Pre-POC)

Based on research before building:

**A-Frame is likely the winner** because:
- Free and open-source
- HTML-based — faster than raw Three.js, more customizable than no-code platforms
- Built-in first-person navigation (no manual control code)
- Native support for images, video, audio, and text via HTML tags
- Can host on GitHub Pages for free (shareable URL)
- Enough control to create custom physics visualizations and interactive elements
- Can import 3D gallery models from free sources (Sketchfab, Poly Haven) for a polished look
- Active community; used by CERN, NASA, Google, Washington Post
- Multiple existing virtual museum projects on GitHub built with A-Frame + Three.js

**Three.js is the power option** if A-Frame's visual quality isn't sufficient. It offers the most control (see GitHub projects like Byron's Virtual Museum, Threejs-museum, and the DEV Community 3D Virtual Art Museum). But it requires significantly more code — manual first-person controls, collision detection, text rendering.

**OpenVGAL is the speed option** — generates a complete gallery from images in minutes. Free, self-hosted, open-source. The question is whether it supports enough customization for audio, video, and physics visualizations. The POC will test this.

---

## 8. Pre-POC Setup Steps

Before building the POCs:

1. **Gather test assets:**
   - Download a public-domain photo of Leon Theremin
   - Find a royalty-free Clara Rockmore theremin recording (or use a short excerpt for private educational use)
   - Create or find a simple electromagnetic field diagram
   - Write the ~100-word text panel content

2. **Set up development environment:**
   - Ensure Node.js is installed (for local dev servers)
   - Create the `poc/` directory structure
   - Set up a simple HTTP server for testing (Python or Node)

3. **Set up hosting:**
   - Create a GitHub repo (or use GitHub Pages from existing repo)
   - Or use Netlify drop (drag a folder to deploy)

---

## 9. After the POC

Once all three POCs are built and scored:

1. **Choose the winning platform** based on weighted scores
2. **Document the decision** with screenshots/recordings of each POC
3. **Identify improvements needed** — what the POC revealed about the full build
4. **Proceed to Stage 3** — design and build the full 10-station exhibition

The POC phase should take no more than one day. Speed matters — the final project is due July 6.

---

## 10. A-Frame Quick Reference (Likely Winner)

If A-Frame wins (as expected), here are key resources for the full build:

- **Docs:** https://aframe.io/docs/1.8.0/introduction/
- **Primitives:** `<a-box>`, `<a-plane>`, `<a-image>`, `<a-video>`, `<a-sound>`, `<a-text>`, `<a-sky>`, `<a-light>`
- **Navigation:** Built-in `wasd-controls` + `look-controls` on `<a-camera>`
- **Gallery room models:** Can import GLTF models from Sketchfab (many free gallery/museum models)
- **Text:** A-Frame uses MSDF text rendering — supports word wrapping, alignment, fonts
- **Audio:** `<a-sound>` supports positional audio, autoplay, loop, volume
- **Hosting:** Any static file host (GitHub Pages, Netlify, Vercel — all free)
- **No build step:** Just open the HTML file with a local server

### Gallery Layout Strategy for A-Frame
For the full exhibition, the gallery could be:
- A **long corridor** with alcoves for each station (simplest to navigate, clear path)
- Connected **rooms** with doorways (more immersive, harder to build)
- A **circular path** that returns to the entrance (thematic — science progresses in spirals)

The corridor approach is recommended for clarity and ease of construction.
