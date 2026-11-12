# React Bits, Animated Registries & Shadcn Preset Reference

## 1. Multi-Registry `components.json` Setup (shadcn CLI v3+)

Register third-party namespaces once inside `components.json` so components can be installed cleanly by short handle:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json",
    "@magicui": "https://magicui.design/r/{name}.json",
    "@skiper-ui": "https://skiper-ui.com/registry/{name}.json"
  }
}
```

---

## 2. React Bits (`reactbits.dev`) — Deep Reference

### A. 4-Flavor Suffix Convention (CRITICAL)

Every React Bits component requires a suffix matching the project's language and styling engine:

| Project Stack | Required Suffix | Example Registry Target |
|---|---|---|
| TypeScript + Tailwind CSS *(Recommended)* | `-TS-TW` | `@react-bits/SplitText-TS-TW` |
| TypeScript + Plain CSS | `-TS-CSS` | `@react-bits/SplitText-TS-CSS` |
| JavaScript + Tailwind CSS | `-JS-TW` | `@react-bits/SplitText-JS-TW` |
| JavaScript + Plain CSS | `-JS-CSS` | `@react-bits/SplitText-JS-CSS` |

### B. CLI Commands

```bash
# Via shadcn CLI (with @react-bits configured in components.json)
npx shadcn@latest add @react-bits/SplitText-TS-TW

# Direct URL (no components.json namespace needed)
npx shadcn@latest add "https://reactbits.dev/r/SplitText-TS-TW.json"

# Via jsrepo (works cleanly in non-shadcn React projects too)
npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW
```

### C. High-Value React Bits Catalog

- **Text Animations**:
  - `SplitText` — Per-char/per-word staggered entrance (GSAP/Motion powered; ideal for hero headlines)
  - `BlurText` — Soft optical blur-to-crisp reveal by word or letter
  - `DecryptedText` — Cipher/matrix character scramble reveal on hover or view (great for technical/cyber/brutalist vibes)
  - `ShinyText` / `GradientText` — Subtle metallic sweep on badges or CTAs
  - `CountUp` / `ScrollVelocity` — Numeric counters and scroll-speed-reactive marquee strips
- **Interactive Components & Micro-interactions**:
  - `TiltedCard` / `SpotlightCard` / `PixelCard` — Tactile 3D tilt or cursor-tracked illumination
  - `Magnet` — Physical magnetic pull on primary CTA buttons
  - `SplashCursor` / `Crosshair` / `BlobCursor` — Custom cursor physics (disable automatically on coarse/touch pointers: `(pointer: coarse)`)
  - `Dock` / `FlowingMenu` / `InfiniteMenu` — Non-standard navigation topologies
- **Backgrounds (Use max 1 per viewport)**:
  - `Aurora` / `Silk` / `Iridescence` / `LiquidChrome` — WebGL/OGL fluid shaders (customize RGB stops to avoid default AI purple!)
  - `Threads` / `Waves` / `Squares` / `DotGrid` / `Particles` — Geometric & technical canvas backgrounds (`ogl` / `three` / 2D canvas)

---

## 3. Magic UI (`magicui.design`)

```bash
# Direct URL or @magicui namespace
npx shadcn@latest add "https://magicui.design/r/animated-theme-toggler"
npx shadcn@latest add "https://magicui.design/r/marquee"
npx shadcn@latest add "https://magicui.design/r/animated-beam"
npx shadcn@latest add "https://magicui.design/r/number-ticker"
```

- Best used selectively for functional motion blocks (`AnimatedThemeToggler`, `AnimatedBeam` architecture diagrams, `Terminal` CLI demos, `NumberTicker`).
- Avoid dropping unmodified `BentoGrid` + purple `BorderBeam` onto every landing page.

---

## 4. Skiper UI (`skiper-ui.com`), OriginKit (`originkit.dev`) & Animmaster (`animmasterlib.dev`)

- **Skiper UI**:
  ```bash
  npx shadcn@latest add @skiper-ui/<component-name>
  ```
  Great when the brief calls for **editorial / studio / Awwwards** layouts (stacked scroll cards, image trail cursors, expandable dynamic island navs, text mask reveals).
- **OriginKit & Animmaster Lib**:
  - Use for specialized hero centerpieces (3D perspective carousels, WebGL image distortion on scroll, shader page transitions).
  - Always audit bundle weight (`three` / `ogl` / `gsap`) and lazy-load heavy WebGL canvases with `next/dynamic(..., { ssr: false })`.

---

## 5. Shadcn Preset (`shadcnpreset.com`)

Instead of accepting default `zinc`/`slate` + `Inter` + `0.5rem` radius on `shadcn/ui` apps:
- Use `shadcnpreset.com` presets (or `npx shadcn@latest init` preset codes) to configure cohesive **OKLCH CSS custom properties** (`--background`, `--foreground`, `--primary`, `--border`, `--radius`) paired with intentional display + body + mono fonts in `globals.css`.

---

## 6. Optional Live Discovery via MCP

If the user wants live component search/installation via MCP in `mcp_config.json`:
- **shadcn Official MCP** (works across `@shadcn`, `@react-bits`, `@magicui`, `@skiper-ui` once listed in `components.json`):
  ```json
  {
    "mcpServers": {
      "shadcn": {
        "command": "npx",
        "args": ["shadcn@latest", "mcp"]
      }
    }
  }
  ```
