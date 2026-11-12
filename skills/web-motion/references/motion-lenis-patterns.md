# Motion (`motion/react`) + Lenis (`lenis/react`) Patterns

## 1. Installation & Imports

```bash
npm install motion lenis
```

```tsx
"use client";

import { useEffect, useRef } from "react";
import { ReactLenis, type LenisRef, useLenis } from "lenis/react";
import "lenis/dist/lenis.css";
import {
  motion,
  AnimatePresence,
  MotionConfig,
  frame,
  cancelFrame,
  useScroll,
  useTransform,
  useSpring,
} from "motion/react";
```

---

## 2. Unified Smooth Scroll + Motion Frame Loop

Prevent duplicate `requestAnimationFrame` loops by disabling Lenis's internal `autoRaf` and driving it through Motion's `frame.update`:

```tsx
"use client";

import { useEffect, useRef, type ReactNode } from "react";
import { ReactLenis, type LenisRef } from "lenis/react";
import { frame, cancelFrame, MotionConfig } from "motion/react";
import "lenis/dist/lenis.css";

export function SmoothMotionProvider({ children }: { children: ReactNode }) {
  const lenisRef = useRef<LenisRef | null>(null);

  useEffect(() => {
    function update(data: { timestamp: number }) {
      lenisRef.current?.lenis?.raf(data.timestamp);
    }

    frame.update(update, true);
    return () => cancelFrame(update);
  }, []);

  return (
    <MotionConfig reducedMotion="user">
      <ReactLenis
        root
        ref={lenisRef}
        options={{
          autoRaf: false,
          lerp: 0.1,
          smoothWheel: true,
          syncTouch: false, // Keep native momentum on touch devices
        }}
      >
        {children}
      </ReactLenis>
    </MotionConfig>
  );
}
```

### Lenis Guardrails
- Keep `syncTouch: false` unless building a custom WebGL touch-scrub canvas — hijacking native iOS/Android touch scroll hurts UX.
- For nested scrollable modals or drawers inside a Lenis page, add `data-lenis-prevent` on the scrollable container so wheel events stay inside the modal.
- Stop/resume page scroll when opening overlays: `const lenis = useLenis(); lenis?.stop();` / `lenis?.start();`.

---

## 3. Core `motion/react` Patterns

### A. Staggered Entrance (Viewport-Triggered)

```tsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.07, delayChildren: 0.1 },
  },
};

const item = {
  hidden: { opacity: 0, y: 18 },
  show: {
    opacity: 1,
    y: 0,
    transition: { type: "spring", stiffness: 320, damping: 28 },
  },
};

export function StaggerReveal({ items }: { items: string[] }) {
  return (
    <motion.ul
      variants={container}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, amount: 0.2 }}
    >
      {items.map((label) => (
        <motion.li key={label} variants={item}>
          {label}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

### B. Shared Layout Morphing (`layoutId`) & Exit (`AnimatePresence`)

- Always give `AnimatePresence` children a stable `key`.
- Use `layout="position"` on text nodes inside morphing containers so font glyphs don't stretch/distort during scale changes.

```tsx
<AnimatePresence mode="popLayout">
  {activeTab && (
    <motion.div
      layoutId="active-pill"
      transition={{ type: "spring", stiffness: 450, damping: 34 }}
    />
  )}
</AnimatePresence>
```

### C. Scroll-Linked Parallax (`useScroll` + `useTransform`)

Read `scrollYProgress` as a `MotionValue` — it updates outside React state without triggering component re-renders:

```tsx
const targetRef = useRef<HTMLElement | null>(null);
const { scrollYProgress } = useScroll({
  target: targetRef,
  offset: ["start end", "end start"],
});
const smoothProgress = useSpring(scrollYProgress, { stiffness: 140, damping: 24 });
const y = useTransform(smoothProgress, [0, 1], [60, -60]);
```
