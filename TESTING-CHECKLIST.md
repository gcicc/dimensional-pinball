# Dimensional Pinball — Manual Testing Checklist

## Pre-Launch (Developer)

- [x] All 9 files created and committed
- [x] Git repo initialized and pushed to GitHub
- [x] GitHub Pages configured and deploying
- [x] Service worker registered
- [x] Icons generated (192x512)
- [x] Manifest.json valid
- [x] No console errors

## Game Launch

- [ ] **Onboarding:** Modal appears with instructions
- [ ] **Start Button:** "Start Game" button works, clears modal
- [ ] **HUD Renders:** Score, balls, dimension name visible at top
- [ ] **Canvas Loads:** Pinball table visible with walls, bumpers, portal

## Physics & Mechanics

- [ ] **Launcher:** Visible in bottom-right corner
- [ ] **Launcher Drag:** Touch/drag in launcher zone loads spring
- [ ] **Ball Launch:** Release launches ball upward with force
- [ ] **Gravity:** Ball falls and bounces realistically
- [ ] **Flipper Control:** Tap left screen half → left flipper activates
- [ ] **Flipper Control:** Tap right screen half → right flipper activates
- [ ] **Bumper Hit:** Ball bounces off 3 bumpers
- [ ] **Bumper Scoring:** +100 pts per bumper hit
- [ ] **Bump Sound:** Click/pop sound plays on bumper hit
- [ ] **Portal Hit:** Ball bounces off portal without teleporting
- [ ] **Portal Scoring:** +250 pts per portal hit
- [ ] **Portal Audio:** Ethereal shimmer sound on portal hit
- [ ] **Portal Counter:** "0/3", "1/3", "2/3" shown below portal

## Dimension Warping

- [ ] **Hit Portal 3x:** Portal hit counter reaches "3/3"
- [ ] **Warp Transition:** Screen flashes (black), dimension changes
- [ ] **Dimension Warp Audio:** Dramatic whoosh plays
- [ ] **Score Bonus:** +1000 pts on warp
- [ ] **New Dimension:** Visuals change (colors, particle effects, etc.)
- [ ] **New Dimension Name:** HUD shows new dimension (Space, Ocean, Storm)
- [ ] **Physics Changed:** Ball behavior changes per dimension:
  - Classic: normal speed
  - Space: slow fall (low gravity)
  - Ocean: sluggish movement (high viscosity)
  - Storm: wind gusts push ball sideways

## Dimension-Specific Features

### Classic
- [ ] Neon blue/pink wireframe aesthetic
- [ ] Dark background
- [ ] Standard pinball behavior

### Space
- [ ] Low gravity (ball floats)
- [ ] Star field background
- [ ] Purple/blue color palette
- [ ] Ball has glow trail

### Ocean
- [ ] High viscosity (ball slower)
- [ ] Blue-green tint
- [ ] Bubble particles rise from bottom
- [ ] Wavy distortion lines
- [ ] Coral-shaped bumpers

### Storm
- [ ] Dark gray/yellow colors
- [ ] Random wind gusts
- [ ] Lightning flashes on big hits
- [ ] Normal gravity

## Scoring & Game State

- [ ] **Score Display:** Updates in real-time
- [ ] **Ball Count:** Starts at 3, displays correctly
- [ ] **Ball Lost:** Ball disappears and resets when it hits drain
- [ ] **Ball Count Decrements:** -1 ball per drain
- [ ] **New Ball:** Ball resets to top center
- [ ] **Game Over:** After 3 drains, "Game Over" modal appears

## Game Over Screen

- [ ] **Modal Appears:** Centered on screen
- [ ] **Final Score:** Shows total score earned
- [ ] **Best Dimension:** Lists high scores per dimension
- [ ] **Play Again Button:** Reloads page and starts new game

## Audio

- [ ] **Flipper Click:** Short noise burst on flipper activation
- [ ] **Bumper Bounce:** Sine wave pop on bumper hit
- [ ] **Ball Launch:** Ascending tone when launching from spring
- [ ] **Ball Drain:** Sad descending tone sequence
- [ ] **Portal Hit:** Ethereal shimmer (multi-layer sine)
- [ ] **Dimension Warp:** Dramatic whoosh effect
- [ ] **Master Volume:** Audible but not too loud (0.3)

## UI/UX

- [ ] **Font:** Readable monospace for score/balls
- [ ] **Colors:** Dark theme with accent colors visible
- [ ] **Portrait Mode:** App fits portrait on phone without scrolling
- [ ] **Touch Targets:** Flipper zones are large enough to hit reliably
- [ ] **No Lag:** Rendering smooth, no jank

## PWA Installation

### iOS
- [ ] Open in Safari
- [ ] Tap Share → Add to Home Screen
- [ ] App installs with icon and name "Dimensional Pinball"
- [ ] App launches in full-screen mode
- [ ] Works offline (service worker cached)

### Android
- [ ] Open in Chrome
- [ ] Tap Menu → Install App (or Add to Home Screen)
- [ ] App installs with icon
- [ ] App launches in full-screen
- [ ] Works offline

## localStorage & Persistence

- [ ] **High Scores Saved:** Play in Classic, warp to Space, back to Classic
- [ ] **High Score Retained:** Classic dimension remembers previous high score
- [ ] **Per-Dimension:** Each dimension has independent high score
- [ ] **Survives Reload:** Close app, reopen, high scores intact

## Browser Console

- [ ] **No JavaScript Errors:** Console is clean
- [ ] **Service Worker Registered:** "SW registered" or no error message
- [ ] **No Network Errors:** All resources loaded (Matter.js CDN, etc.)

## Edge Cases

- [ ] **Rapid Flipper Taps:** Multiple flips in succession work
- [ ] **Ball Lost Immediately:** Launch ball, it goes straight to drain → reset
- [ ] **Exact Dimension Boundary:** Ball bounces correctly off walls
- [ ] **Portal Overlap:** Ball can't get stuck in portal

## Performance

- [ ] **Frame Rate:** Smooth 60 FPS (no stuttering)
- [ ] **Memory:** No obvious memory leaks (App stays responsive after 5+ warps)
- [ ] **CPU:** Reasonable battery drain (not overheating)

## Accessibility (Optional but recommended)

- [ ] [ ] Text contrast: readable in sunlight
- [ ] [ ] Touch targets: 44x44px minimum

---

## Sign-Off

Date tested: ___________
Tester: ___________
All tests passed: [ ] Yes [ ] No

### Issues Found (if any):
1. ________________________________________________________
2. ________________________________________________________
3. ________________________________________________________

### Recommended next features:
- Additional dimensions
- Leaderboard
- Sound toggle
- Haptic feedback
