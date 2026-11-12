# Anime.js v4 & Browser View Transitions API

## 1. Anime.js v4 Modular Patterns (`animejs`)

Anime.js v4 uses **named modular exports** (`animate`, `createTimeline`, `stagger`, `createScope`, `svg`, `createDraggable`). Never use the legacy v3 `anime({...})` default call.

```bash
npm install animejs
```

### A. Scoped React Integration (`createScope` + `revert`)

Always scope DOM queries to a container ref and revert on unmount:

```tsx
"use client";

import { useEffect, useRef } from "react";
import { animate, createScope, createTimeline, stagger, type Scope } from "animejs";

export function KineticHeadline() {
  const rootRef = useRef<HTMLDivElement | null>(null);
  const scopeRef = useRef<Scope | null>(null);

  useEffect(() => {
    if (!rootRef.current) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    scopeRef.current = createScope({ root: rootRef }).add(() => {
      const tl = createTimeline({ defaults: { ease: "out(4)", duration: 750 } });

      tl.add(".char", {
        y: ["110%", "0%"],
        opacity: [0, 1],
        delay: stagger(35, { from: "first" }),
      }).add(
        ".underline-rule",
        { scaleX: [0, 1], duration: 500 },
        "-=400"
      );
    });

    return () => scopeRef.current?.revert();
  }, []);

  return (
    <div ref={rootRef}>
      {/* Scoped targets (.char, .underline-rule) */}
    </div>
  );
}
```

### B. SVG Line Drawing & Morphing (`svg`)

```tsx
import { animate, stagger, svg } from "animejs";

// 1. Stroke line-drawing (replaces manual strokeDashoffset math)
animate(svg.createDrawable(".blueprint-path"), {
  draw: ["0 0", "0 1"],
  ease: "inOut(2)",
  duration: 1400,
  delay: stagger(120),
});

// 2. Smooth SVG path morphing
animate("#shape-primary", {
  d: svg.morphTo("#shape-target"),
  ease: "outElastic(1, .6)",
  duration: 900,
});
```

---

## 2. View Transitions API (`clip-path` Theme Toggler Pattern)

Inspired by Magic UI's `AnimatedThemeToggler`: transition Light/Dark themes from the exact click coordinates using `document.startViewTransition` + `clip-path`, with an instant fallback for unsupported browsers or `prefers-reduced-motion`.

### Required Global CSS

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation: none;
  mix-blend-mode: normal;
}
```

### React Handler Pattern

```tsx
import { flushSync } from "react-dom";

export async function toggleThemeWithReveal(
  buttonEl: HTMLElement | null,
  applyTheme: () => void,
  duration = 500
) {
  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!buttonEl || !("startViewTransition" in document) || prefersReduced) {
    applyTheme();
    return;
  }

  const { top, left, width, height } = buttonEl.getBoundingClientRect();
  const x = left + width / 2;
  const y = top + height / 2;
  const maxRadius = Math.hypot(
    Math.max(left, window.innerWidth - left),
    Math.max(top, window.innerHeight - top)
  );

  const transition = document.startViewTransition(() => {
    flushSync(() => {
      applyTheme();
    });
  });

  await transition.ready;

  document.documentElement.animate(
    {
      clipPath: [
        `circle(0px at ${x}px ${y}px)`,
        `circle(${maxRadius}px at ${x}px ${y}px)`,
      ],
    },
    {
      duration,
      easing: "cubic-bezier(0.22, 1, 0.36, 1)",
      pseudoElement: "::view-transition-new(root)",
    }
  );
}
```
