# Stage 3: Build the Full Exhibition

## Status: PENDING — Begins after Stages 1 and 2 are complete

This plan will be finalized after:
1. **Stage 1** delivers the final 10 selected works with all media and text
2. **Stage 2** delivers the winning platform choice from the POC comparison

---

## What We Know Now

### From Stage 1 (expected outputs):
- 10 selected stations, chronologically ordered
- For each: physics explainer text, music description text, connection text
- For each: image URLs, audio/video URLs, excerpt timestamps
- A clear narrative arc from classical acoustics to quantum computing

### From Stage 2 (expected outputs):
- Winning platform (likely A-Frame based on preliminary assessment)
- Lessons learned from the POC about what works and what needs improvement
- Confirmed approach for images, audio, video, and text panels

---

## Preliminary Build Plan (to be refined)

### 1. Design the Gallery Layout
- Choose a layout: **corridor with alcoves** (recommended for clear path), connected rooms, or circular path
- Sketch the floor plan — where each station sits
- Plan the visitor flow: entrance → Station 1 → ... → Station 10 → exit
- Design the transition between stations (doorways, open walkways, visual dividers)

### 2. Build the Shell
- Create the gallery room geometry (walls, floor, ceiling)
- Set up lighting (ambient + spotlights for each station)
- Configure camera and first-person navigation
- Add a sky/background color that sets the mood (dark gallery ambiance)
- Optional: import a pre-made gallery 3D model from Sketchfab for polish

### 3. Populate Each Station
For each of the 10 stations:
- Place the physics image/diagram on the left wall
- Place the music image (composer photo, score excerpt, performance still) on the right wall
- Add the text panels (physics, music, connection)
- Embed the audio player (plays on approach or click)
- Optionally embed a video player for select stations
- Add station number/title as a header

### 4. Add Navigation Aids
- Station titles visible from a distance (like museum room labels)
- Optional minimap or progress indicator
- Clear visual cues guiding the visitor forward
- Introductory text at the entrance explaining the exhibition thesis

### 5. Polish
- Adjust lighting per station for mood (warm for Debussy, harsh for Penderecki, cool/blue for quantum)
- Add subtle ambient sound (low drone or silence between stations)
- Test on multiple browsers and screen sizes
- Optimize asset loading (compress images, lazy-load audio)

### 6. Deploy
- Host on GitHub Pages, Netlify, or Vercel (all free)
- Generate a shareable URL
- Test the URL on a phone, tablet, and laptop
- Create a short "how to navigate" instruction overlay for first-time visitors

---

## Timeline Constraint

The final project is due **Sunday, July 6, 2026**. Stage 3 must be completed before then. Given the tight deadline:
- Stage 1 and Stage 2 should complete within 1 day
- Stage 3 (full build) should take 1-2 days
- Leave the final day for testing and polish

---

## Deliverable

A single URL that opens a browser-based 3D exhibition. No app install required. The professor and class can walk through the gallery, read the panels, listen to the music, and understand how physics shaped Western music from Helmholtz to quantum computers.
