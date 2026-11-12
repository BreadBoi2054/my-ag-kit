---
name: animated-ui-registries
description: Curated workflow for sourcing, installing, and customizing animated web components and design-system presets from React Bits, Magic UI, Skiper UI, OriginKit, Animmaster Lib, and Shadcn Preset.
when_to_use: "When the user wants high-craft animated React/Tailwind/shadcn components (text reveals, shader backgrounds, micro-interactions, dynamic islands, theme toggles) or custom shadcn/ui presets — instead of coding complex visual effects from scratch. NOT for mobile apps or pure backend projects."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
version: 1.0.0
effort: medium
---

# Animated UI Registries & Shadcn Presets

> Own the source code: pull focused animated primitives via `shadcn` registries, customize tokens to match the project's brand, and avoid stacking visual clichés.

| Reference File | When to Read |
|---|---|
| [references/react-bits-and-registries.md](references/react-bits-and-registries.md) | Exact `components.json` namespaces, **React Bits** (`@react-bits` 4-flavor suffixes), **Magic UI** (`@magicui`), **Skiper UI** (`@skiper-ui`), **OriginKit**, **Animmaster Lib**, **Shadcn Preset**, and MCP setup |

---

## 1. Registry Selection Matrix (Right Source for Each Component)

| Need / Component Type | Best Registry | Signature Strengths |
|---|---|---|
| **Kinetic Text, Shader/Canvas Backgrounds, Cursor & Card Micro-interactions** | **React Bits** (`reactbits.dev` / `@react-bits`) | `SplitText`, `BlurText`, `DecryptedText`, `ShinyText`, `Aurora`, `Threads`, `Silk`, `SplashCursor`, `TiltedCard`, `Magnet` — ships in 4 variants (`TS/JS` × `TW/CSS`) |
| **Product / Marketing Blocks & Utility Transitions** | **Magic UI** (`magicui.design` / `@magicui`) | `AnimatedThemeToggler`, `AnimatedBeam`, `BorderBeam`, `Marquee`, `NumberTicker`, `Terminal`, `InteractiveHoverButton` |
| **Editorial, Agency & Uncommon Interactive Blocks** | **Skiper UI** (`skiper-ui.com` / `@skiper-ui`) | Dynamic islands, cursor image trails, stacked scroll cards, kinetic hero reveals built on Tailwind + Motion |
| **3D / WebGL / Scroll-Choreographed Showpieces** | **OriginKit** (`originkit.dev`) & **Animmaster Lib** (`animmasterlib.dev`) | High-end scroll shaders, 3D carousels, magnetic galleries, Framer/React motion primitives |
| **Whole-System Theme, Typography, Radius & Density Tokens** | **Shadcn Preset** (`shadcnpreset.com`) | Full design-system presets (OKLCH palettes, font pairings, border radii, icon sets) beyond basic color swaps |

---

## 2. Integration Protocol

### Step 1: Respect Project Stack & User UI Choice
- Check `package.json` and `components.json` first.
- If the project does **not** use `shadcn/ui` or Tailwind (e.g., plain React + CSS), either ask before initializing `shadcn` or pull **React Bits `-TS-CSS` / `-JS-CSS`** variants via `jsrepo` so you never force unwanted UI dependencies.

### Step 2: Pull Source, Then Adapt Tokens (Anti-Slop Customization)
Registry components ship with demo defaults (often indigo/purple glows, generic slate cards, or `rounded-xl` everywhere). Immediately after adding a component:
1. **Enforce Brand Palette & Purple Ban**: Replace hardcoded `#8b5cf6` / `indigo-*` / `purple-*` demo colors with project CSS variables (`var(--primary)`, `var(--accent)`) or the agreed non-purple brand palette from `DESIGN.md` / `frontend-design`.
2. **Match Geometry**: Align border-radius (`0px–2px` crisp vs `16px–28px` expressive) with the rest of the page.
3. **Motion Restraint Budget**:
   - Maximum **1 continuous WebGL / Canvas shader** visible in the viewport at one time (pause offscreen canvases via `IntersectionObserver`).
   - Never combine a shader background + marquee + particles + 3 looping beams in the same fold. Let one focal interaction breathe.

### Step 3: Verify Build, Types & Reduced Motion
- Inspect newly added files under `components/ui/` or `src/components/` for missing peer packages (`motion`, `gsap`, `ogl`, `three`, `lucide-react`) and mismatched import aliases (`@/`).
- Confirm `npm run build` / `npx tsc --noEmit` passes and `prefers-reduced-motion` does not trap hidden elements at `opacity: 0`.
