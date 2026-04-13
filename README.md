# Dimensional Pinball

A physics-based pinball game across alternate dimensions. Hit bumpers, warp between worlds with unique physics themes. Built with vanilla HTML/CSS/JS and Matter.js physics engine.

**Play it live:** https://gcicc.github.io/dimensional-pinball/

## Features

### Core Mechanics
- **Portrait-mode pinball** with left/right flipper controls (tap left/right half of screen)
- **Matter.js physics** for realistic ball dynamics
- **Ball launcher** with spring — drag to load, release to fire
- **Bumpers** that bounce the ball and award points
- **Portal warp target** — hit it 3 times to shift to a new dimension
- **3 balls per game** with drain detection

### 4 Unique Dimensions
Each with distinct physics and visual theme:

1. **Classic** — Standard pinball. Normal gravity. Neon wireframe aesthetic (blue/pink on dark).
2. **Space** — Low gravity (0.3x). Star field background. Purple/blue theme. Glowing ball trails.
3. **Ocean** — High viscosity (ball moves slower, underwater feel). Bubble particles, wavy distortion, blue-green theme.
4. **Storm** — Wind gusts push ball randomly. Lightning flash effects on impacts. Dark gray/yellow theme.

### Scoring
- **Bumper hit:** 100 pts
- **Lane completion:** 500 pts
- **Portal hit:** 250 pts
- **Dimension warp:** 1000 pts bonus
- **High scores saved per dimension** (localStorage)

### Audio
Web Audio API generates dynamic sounds:
- Flipper clicks (noise bursts)
- Bumper bounces (varied sine waves)
- Ball launch (ascending tones)
- Drain (descending sad tone)
- Portal hits (ethereal shimmer)
- Dimension warps (dramatic whoosh)

## Controls

### Mobile
- **Left half of screen:** Left flipper
- **Right half of screen:** Right flipper
- **Launcher zone (bottom-right):** Drag down to load spring, release to launch

### Keyboard (desktop)
- **← (Arrow Left) or A:** Left flipper
- **→ (Arrow Right) or D:** Right flipper
- Mouse/touch in launcher area to load and fire

## Technical Details

- **Single-file PWA:** All HTML, CSS, and JS in `index.html`
- **Dependencies:** Only Matter.js (CDN)
- **Physics engine:** Matter.js 0.20.0
- **Offline support:** Service worker with cache-first strategy
- **No tracking, no accounts, no data collection**

## Project Files

- `index.html` — Complete single-page application
- `manifest.json` — PWA manifest (name, icons, metadata)
- `sw.js` — Service worker for offline support and caching
- `generate-icons.py` — Pillow script to generate pinball-themed icons
- `icon-192.png`, `icon-512.png` — App icons

## Installation

### Install as PWA
1. Open https://gcicc.github.io/dimensional-pinball/ on your phone
2. iOS: Tap **Share → Add to Home Screen**
3. Android: Tap **Menu → Install App** or **Add to Home Screen**

## Development

To test locally:
```bash
python -m http.server 8000
# Open http://localhost:8000 in browser
```

To regenerate icons:
```bash
python generate-icons.py
```

## Deploy

Push to GitHub and enable Pages in repo settings (already done):
```bash
git add -A && git commit -m "feat: ..."
git push origin master
```

App is live at: https://gcicc.github.io/dimensional-pinball/

## Future Enhancements
- Leaderboards (per dimension)
- Sound toggle
- Accessibility improvements (screen reader support)
- Additional dimensions (more themes)
- Ramps and mini-goals
- Combo scoring
- Multiplayer (turn-based on same device)

## License

Personal portfolio project. See parent MobileTapper for licensing.
