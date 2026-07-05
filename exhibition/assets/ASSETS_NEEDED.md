# Media Assets to Download — Curated List (revised July 5)

Each station has its own subfolder: drop files into `exhibition/assets/sNN/` with the
**exact filenames** below (e.g. `assets/s03/s03_audio.mp3`).
The exhibition auto-detects them on page load — no code changes needed.

**Done so far:** ✅ s03 complete (physics, music, center images + audio).

## The curatorial logic (read this before downloading)

Each wall is a **triptych** you look at *while the music plays*:

- **Left (The Physics)** — the physical phenomenon made visible: apparatus, experiment, field.
- **Center (largest frame)** — the hinge where physics and music fuse. This is the image a
  visitor stares at for 90 seconds while listening, so it carries the most weight: an artwork,
  a score-as-image, an inventor mid-gesture.
- **Right (The Music)** — the human being: composer or performer.

Two walls are deliberately symmetric portraits-flanking-an-artwork: s03 (Einstein | Picasso's
*Guitar* | Stravinsky) and s09 (Fourier | spectrogram-becomes-score | Grisey). Two walls rhyme
left-to-center: s06 (Perrin's Brownian particle tracks look like Xenakis's glissandi graph) and
s08 (Chladni sand patterns ↔ speech dissolving into resonance).

**Formats:** images must be `.jpg`, audio `.mp3`, video `.mp4` (H.264).
Convert PNGs: `sips -s format jpeg in.png --out out.jpg`.
**Audio:** trim to the best 60–120 seconds. (GitHub limit: keep files well under 50 MB.)

## Required-files checklist

```
s01/  s01_physics.jpg  s01_center.jpg  s01_music.jpg  s01_audio.mp3   (Debussy)
s02/  s02_physics.jpg  s02_center.jpg  s02_music.jpg  s02_audio.mp3   (Ives)
s03/  ✅ DONE
s04/  s04_physics.jpg  s04_center.jpg  s04_music.jpg  s04_audio.mp3   (Theremin/Rockmore)
s05/  s05_physics.jpg  s05_center.jpg  s05_music.jpg  — no audio —    (Cage: silence)
s06/  s06_physics.jpg  s06_center.jpg  s06_music.jpg  s06_audio.mp3   (Xenakis)
s07/  s07_physics.jpg  s07_center.jpg  s07_music.jpg  s07_audio.mp3   (Penderecki)
s08/  s08_physics.jpg  s08_center.jpg  s08_music.jpg  s08_audio.mp3   (Lucier)
s09/  s09_physics.jpg  s09_center.jpg  s09_music.jpg  s09_audio.mp3   (Grisey)
s10/  s10_physics.jpg  s10_center.jpg  s10_music.jpg  s10_audio.mp3   (Miranda)
```

Center images were optional before; after this revision they are **strongly recommended** —
the center frame is the curatorial argument of each wall.

---

## Station 01 — Helmholtz / Debussy (amber)

**The wall:** brass resonator → the Faun himself, in color → the composer.
While the flute solo plays you look at Bakst's watercolor of Nijinsky as the Faun — the
sensuous body the music became. Far stronger than the previous overtone-series diagram.

| File | What to get | Source |
|---|---|---|
| `s01_physics.jpg` | Helmholtz resonator — brass sphere photo or 19th-c. plate | https://www.phys.unsw.edu.au/jw/Helmholtz.html or https://cdn.britannica.com/27/4327-004-832F17F1/Helmholtz-resonator-V-volume-neck-area-A.jpg |
| `s01_center.jpg` | **Léon Bakst, Nijinsky as the Faun (1912) — watercolor** | https://upload.wikimedia.org/wikipedia/commons/d/d4/Bakst_Nizhinsky.jpg (alt: de Meyer photo https://upload.wikimedia.org/wikipedia/commons/9/99/Nijinsky_as_the_faun%2C_photographs_by_Adolf_de_Meyer_1912.jpg) |
| `s01_music.jpg` | Debussy portrait (Nadar, 1908, public domain) | https://commons.wikimedia.org/wiki/File:Claude_Debussy_ca_1908,_foto_av_F%C3%A9lix_Nadar.jpg |
| `s01_audio.mp3` | Opening flute solo of *Prélude à l'après-midi d'un faune* (~90s) | From https://www.youtube.com/watch?v=-YazhxBA7oo |

## Station 02 — Doppler / Ives (twilight blue)

**The wall:** the wave diagram → the father who marched bands past each other → the son.
George Ives, Danbury's Civil War bandmaster, staged the moving-bands experiments that taught
Charles to hear position in space. His photograph is the human hinge of this station.

| File | What to get | Source |
|---|---|---|
| `s02_physics.jpg` | Doppler effect wave diagram (compressed ahead / stretched behind) | https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Redshift.svg/500px-Redshift.svg.png (convert to .jpg) |
| `s02_center.jpg` | **George Ives, bandmaster (Civil War CDV / period photo)** | https://www.waroftherebellion.com/product-page/cdv-famous-connecticut-band-leader-george-e-ives or images in https://newenglandhistoricalsociety.com/charles-ives-new-england-holidays-a-danbury-childhood-set-to-music (fallback: three-groups spatial diagram from https://www.youtube.com/watch?v=WBiL0VEttZw) |
| `s02_music.jpg` | Charles Ives portrait | Wikimedia Commons "Charles Ives" |
| `s02_audio.mp3` | *The Unanswered Question* — trumpet question + woodwind answer (~90s) | From https://www.youtube.com/watch?v=vXD4tIp59L0 (Bernstein/NYP) |

## Station 03 — Relativity+Cubism / Stravinsky (red) ✅ DONE

Einstein 1921 | Picasso's *Guitar* (1912) | Stravinsky 1920s — with the full Rite audio.
**Optional upgrade:** Nicholas Roerich's actual 1913 set design for the Rite premiere,
https://upload.wikimedia.org/wikipedia/commons/6/62/Roerich_Rite_of_Spring.jpg — could replace
the Stravinsky portrait (`s03_music.jpg`) if you prefer the pagan landscape to a face.
**Audio note:** current file is the full 86 MB ballet; consider trimming to the "Sacrificial
Dance" finale (~90s).

## Station 04 — Electromagnetism / Theremin (violet)

**The wall:** the invisible field made visible → the inventor mid-gesture → the virtuosa.
Previously two theremin players flanked a circuit diagram; now the field itself opens the wall
and Theremin's demonstration (the moment physics became an instrument) takes the center.

| File | What to get | Source |
|---|---|---|
| `s04_physics.jpg` | **Iron filings tracing a magnetic field** (the invisible medium the instrument plays) | https://upload.wikimedia.org/wikipedia/commons/2/25/Iron-filings-around-magnet.jpg |
| `s04_center.jpg` | **Leon Theremin demonstrating the termenvox, c.1927** | https://upload.wikimedia.org/wikipedia/commons/d/d3/Termen_demonstrating_Termenvox.jpg (higher-res alt: https://upload.wikimedia.org/wikipedia/commons/7/74/Lev_Termen_playing_-_cropped.jpg) |
| `s04_music.jpg` | Clara Rockmore at her theremin — eyes closed, hands in the air | https://upload.wikimedia.org/wikipedia/commons/1/1a/Clara_Rockmore_%281911-1998%29_at_her_Theremin.jpg |
| `s04_audio.mp3` | Clara Rockmore, "The Swan" (~2min, use it all) | From https://www.youtube.com/watch?v=pSzTPGlNa5U |
| `s04_video.mp4` | (optional, HIGHLY recommended — hands playing the air IS the exhibit) | Same video |

## Station 05 — The Impossibility of Silence / Cage (white)

**The wall:** the room built to be silent → the score that says TACET → the composer.
This station has no audio by design, so the images do all the work: the chamber where Cage
heard his own nervous system, and the notated silence itself.

| File | What to get | Source |
|---|---|---|
| `s05_physics.jpg` | Anechoic chamber (wedged walls, engulfing) | https://upload.wikimedia.org/wikipedia/commons/5/52/Anechoic_chamber.jpg |
| `s05_center.jpg` | **4′33″ score page — "I. TACET / II. TACET / III. TACET"** | https://www.researchgate.net/profile/Rvp-Rvp/publication/304261080/figure/fig1/AS:669407978192897@1536610707138/The-Score-of-John-Cages-433.jpg (alt: https://termita.pt/wp-content/uploads/2026/06/433-Tacet-Version-%E2%80%93-John-Cage.png — convert to .jpg) |
| `s05_music.jpg` | John Cage portrait (1988) | https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Componist_John_Cage.jpg/960px-Componist_John_Cage.jpg |
| audio | **Deliberately none — the station instruction says listen to your own room.** | — |

## Station 06 — Statistical Mechanics / Xenakis (green)

**The wall:** Perrin's real Brownian-motion particle tracks → Xenakis's glissandi graph → the composer.
This is the strongest left↔center rhyme in the exhibition: Perrin's 1908 traced particle paths
and the Pithoprakta string glissandi are *visually the same picture*, fifty years apart.
(Replaces the Maxwell–Boltzmann curve, which was a single dull line.)

| File | What to get | Source |
|---|---|---|
| `s06_physics.jpg` | **Jean Perrin's Brownian-motion particle tracks (1908/1913, *Les Atomes*)** | https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/PerrinPlot2.svg/1280px-PerrinPlot2.svg.png (convert to .jpg; alt: the book plate https://commons.wikimedia.org/wiki/File:Perrin,_Jean_-_Les_Atomes,_F%C3%A9lix_Alcan,_1913_(page_280_crop).jpg) |
| `s06_center.jpg` | Xenakis's graphical score of *Pithoprakta* (mm. 52–59 — the particle cloud) | Search "Pithoprakta graphical score" (Xenakis Foundation) |
| `s06_music.jpg` | Xenakis portrait | Wikimedia "Iannis Xenakis" |
| `s06_audio.mp3` | *Pithoprakta* — the glissandi cloud section (~90s) | From https://www.youtube.com/watch?v=nvH2KYYJg-o |
| `s06_video.mp4` | (optional, recommended — animated score shows the cloud moving) | Same video |

## Station 07 — Nuclear / Penderecki (ash)

**The wall:** the cloud → the score that notates the scream → the composer. Unchanged in
structure — this wall already worked. Get a good-quality Penderecki portrait.

| File | What to get | Source |
|---|---|---|
| `s07_physics.jpg` | Hiroshima cloud (public domain, US gov) | https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Atomic_cloud_over_Hiroshima.jpg/1280px-Atomic_cloud_over_Hiroshima.jpg |
| `s07_center.jpg` | Penderecki's graphic notation page from *Threnody* | https://media2.wnyc.org/i/800/426/c/80/1/threnody-hiroshima-score.PNG (convert to .jpg) |
| `s07_music.jpg` | Penderecki portrait (good quality) | https://commons.wikimedia.org/wiki/File:Krzysztof_Penderecki_Polish_composer_1993.jpg (in Category:Krzysztof Penderecki) |
| `s07_audio.mp3` | *Threnody* opening scream (~60–90s) | From https://www.youtube.com/watch?v=Dp3BlFZWJNA (Wit/Polish RSO) |
| `s07_video.mp4` | (optional, HIGHLY recommended — gerubach animated graphic score) | https://www.youtube.com/watch?v=HilGthRhwP8 |

## Station 08 — Room Acoustics / Lucier (gold)

**The wall:** sand drawing the room's resonance → speech dissolving into pure tone → the man
whose stutter the room erased. Chladni figures replace the generic standing-wave diagram:
resonance made physically visible, in sand — the same phenomenon the tape process reveals in sound.

| File | What to get | Source |
|---|---|---|
| `s08_physics.jpg` | **Chladni figures — sand patterns on a vibrating plate** | https://upload.wikimedia.org/wikipedia/commons/4/43/Chladni_plate_10.jpg (more in Commons "Category:Chladni figures") |
| `s08_center.jpg` | Before/after spectrogram of the piece (speech → resonance bands) | Search "Lucier I Am Sitting in a Room spectrogram" (Trevor Cox) |
| `s08_music.jpg` | Alvin Lucier portrait | Wikimedia Commons "Alvin Lucier" |
| `s08_audio.mp3` | **Two excerpts spliced: iteration 1 (clear speech ~30s) + late iteration (pure tones ~45s)** | From https://www.youtube.com/watch?v=fAxHlLK3Oyk |

## Station 09 — Fourier / Grisey (ocean blue)

**The wall:** the mathematician → the spectrogram that became a score → the composer.
Deliberately mirrors Station 03 (Einstein | artwork | Stravinsky): two faces flanking the
central object. Replaces the redundant second spectrogram on the physics side.

| File | What to get | Source |
|---|---|---|
| `s09_physics.jpg` | **Joseph Fourier portrait (Boilly engraving, public domain)** | https://commons.wikimedia.org/wiki/Jean_Baptiste_Joseph_Fourier — download the engraved portrait |
| `s09_center.jpg` | The trombone-E spectrogram-to-score mapping | https://www.youtube.com/watch?v=mq74L2vVvsw (Bolanos analysis — screenshot) or search "Grisey Partiels spectral analysis diagram" |
| `s09_music.jpg` | Grisey portrait | Wikimedia Commons "Gérard Grisey" |
| `s09_audio.mp3` | *Partiels* opening — trombone E blooming into the ensemble (~2min) | From https://www.youtube.com/watch?v=4Db_uz1a2v8 (Dal Niente) |

## Station 10 — Quantum Computing / Miranda (magenta)

**The wall:** the golden cryostat (the cathedral object of our era) → the qubit's geometry →
the composer. The chandelier-like cryostat is far more compelling than a flat chip photo — it
answers the Great Door's golden arch across the room.

| File | What to get | Source |
|---|---|---|
| `s10_physics.jpg` | **IBM quantum computer cryostat — the "golden chandelier"** | IBM newsroom press images (search "IBM Quantum System One cryostat"); IBM Research Flickr (CC) https://www.flickr.com/photos/ibm_research_zurich/ (fallback: Eagle 127-qubit chip photo) |
| `s10_center.jpg` | Bloch sphere diagram, or Qubism album art | Wikipedia "Bloch sphere" / https://51beats.bandcamp.com/album/qubism |
| `s10_music.jpg` | Miranda performing | https://51beats.bandcamp.com/album/qubism or search "Eduardo Reck Miranda performing" |
| `s10_audio.mp3` | *Swirling Qubits* or *Qubism* track excerpt (~90s) | https://soundcloud.com/51beats/sets/51bts080-eduardo-reck-miranda-qubism or https://www.youtube.com/watch?v=5PilN5ynYv8 |
| `s10_video.mp4` | (optional) Swirling Qubits Bloch-sphere visualization | https://www.youtube.com/watch?v=5PilN5ynYv8 |

---

## Video priority (if you only prepare a few)
1. **s04** Theremin — seeing hands play the air IS the exhibit
2. **s07** Penderecki — the animated graphic score is unforgettable
3. **s06** Xenakis — animated score literally shows particles
4. **s03** Rite of Spring — visceral orchestra footage

## Testing
After adding files, reload the page — images appear in frames automatically,
and the Play buttons light up at each station.

## Note on captions
The 3D wall captions in `index.html` already match this revised list
(e.g. s01 center reads "Nijinsky as the Faun -- Bakst, 1912"). If you substitute a
different image at any slot, tell Claude to update that station's `phLabel`/`ctLabel`/`muLabel`.
