---
name: web-motion
description: Creative web animation, smooth scrolling, SVG choreography, and View Transitions using Motion (motion/react), Lenis (lenis/react), Anime.js v4, GSAP, and native browser APIs.
when_to_use: "When building animated web UI, smooth scrolling pages, page/theme transitions, scroll-linked parallax, kinetic typography, or SVG morphing/line-drawing in React, Next.js, Vite, or vanilla JS. NOT for mobile native apps (use mobile-design)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
version: 1.0.0
effort: medium
---

# Web Motion — Creative Animation & Smooth Scroll

> Choreograph purposeful 60fps motion using the right engine for each job, one unified render loop, and strict accessibility fallbacks.

| Reference File | When to Read |
|---|---|
| [references/motion-lenis-patterns.md](references/motion-lenis-patterns.md) | React component transitions (`motion/react`), `AnimatePresence`, scroll-linked transforms, and `<ReactLenis>` ticker synchronization |
| [references/animejs-v4-and-view-transitions.md](references/animejs-v4-and-view-transitions.md) | **Anime.js v4** modular timelines/SVG morphing/line-drawing, and native **View Transitions API** (`clip-path` theme toggles & route transitions) |

---

## 1. Engine Selection Matrix (Pick the Simplest Fit)

Never install three animation libraries for one effect. Select the lowest tier that cleanly solves the requirement:

| Requirement | Primary Tool | Why |
|---|---|---|
| Hover, focus, simple enter (`@starting-style`), accordion height | **Native CSS Transitions / Keyframes** | Zero JS bundle cost, compositor-accelerated |
| Full-page theme reveal (Light/Dark) or DOM state morph | **View Transitions API** (`document.startViewTransition`) | Browser-native snapshot crossfade + custom `clip-path` geometry |
| React mount/unmount, shared `layoutId`, gestures, spring UI | **Motion** (`motion/react`) | Declarative React lifecycle awareness; replaces legacy `framer-motion` |
| Inertia smooth scrolling across the page | **Lenis** (`lenis/react` or `lenis`) | Lightweight, preserves native scroll position/accessibility & `position: sticky` |
| Multi-step timelines, stagger grids, SVG `morphTo` / `createDrawable` | **Anime.js v4** (`animejs`) | Tree-shakable modular v4 API (`animate`, `createTimeline`, `createScope`, `svg`) |
| Complex scroll-pinned scrubbing storytelling (Awwwards scrollytelling) | **GSAP + ScrollTrigger** | Industry standard for pinned multi-scene scrub timelines |

---

## 2. Critical Package & Import Rules (Avoid Legacy Traps)

1. **Motion (`motion`, NOT `framer-motion`)**:
   - Install `motion` and import from `"motion/react"` (or `"motion/react-client"` inside Next.js App Router RSC files when needed).
2. **Anime.js v4 (`animejs` v4+, NOT v3 default export)**:
   - Use named tree-shakable imports: `import { animate, stagger, createTimeline, createScope, svg } from "animejs";`
   - Never use the legacy v3 `import anime from "animejs"; anime({...})` syntax on v4 projects.
   - In React, wrap imperative animations inside `createScope({ root: containerRef })` and call `scope.current?.revert()` on cleanup.
3. **Lenis (`lenis`, NOT deprecated `@studio-freight/lenis`)**:
   - Install `lenis`, import `<ReactLenis>` / `useLenis` from `"lenis/react"`, and import `"lenis/dist/lenis.css"`.

---

## 3. Unified Render Loop (No Competing `requestAnimationFrame`)

When combining **Lenis** with **Motion**, **Anime.js**, or **GSAP**, never let two independent `rAF` loops fight for the main thread:
- Pass `options={{ autoRaf: false }}` to `<ReactLenis>` and drive `lenisRef.current?.lenis?.raf(timestamp)` from **Motion's `frame.update`** (or GSAP's `gsap.ticker`), cancelling cleanly on unmount.
- Read [references/motion-lenis-patterns.md](references/motion-lenis-patterns.md) for the exact copy-ready hook.

---

## 4. 60fps Performance & Accessibility Checklist (Mandatory)

- **GPU-Only Properties**: Animate `transform` (`x`, `y`, `scale`, `rotate`) and `opacity` (plus `clip-path` / `filter` sparingly). Never animate `top`, `left`, `width`, `height`, or `margin` continuously on scroll.
- **Reduced Motion**: Respect `prefers-reduced-motion: reduce`:
  - In Motion: wrap app in `<MotionConfig reducedMotion="user">`.
  - In Lenis / View Transitions / Anime.js: check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` and bypass heavy motion or fall back to instant state updates.
- **SSR & Hydration Safety**: Mark interactive animated components with `"use client"` in Next.js App Router; avoid reading `window` during initial render.
- **Strict Cleanup**: Every `createScope`, `ScrollTrigger`, `frame.update`, or event listener created in `useEffect` must be reverted/disposed on unmount.
