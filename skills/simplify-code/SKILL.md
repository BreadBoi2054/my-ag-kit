---
name: simplify-code
description: Reduce complexity of over-engineered code and enforce "Lazy Senior Dev" (Ponytail / YAGNI) minimalism — prefer platform-native APIs and standard libraries before writing new abstractions or adding packages.
when_to_use: "When code is over-engineered, overly abstract, or bloated, or when the user says 'simplify', 'clean up', 'reduce complexity', 'ponytail', 'be lazy', 'yagni', or 'simplest solution'."
allowed-tools: Read, Write, Edit, Grep, Glob
version: 1.1.0
effort: medium
---

# Simplify Code — Lazy Senior Minimalism & Anti-Bloat

> The best code is the code you never wrote. The second best is plain, platform-native code anyone can read in 30 seconds.

## Core Principle

```
Complexity is a liability. Every wrapper, helper, config layer, and npm package
is future maintenance debt. Solve 100% of the real problem with the smallest
possible surface area.
```

---

## 0. The Ponytail Priority Ladder (Before Writing Any New Code)

Adapted from `DietrichGebert/ponytail` — climb down this ladder strictly in order and stop at the highest rung that solves the problem completely:

| Rung | First Choice | Examples |
|---|---|---|
| **1. YAGNI (Delete / Skip)** | Don't build speculative hooks, plugin systems, or config flags nobody asked for | Skip multi-provider adapters when only 1 provider exists |
| **2. Platform / Runtime Native** | Use built-in HTML, CSS, Web APIs, or language standard library | `<dialog>`, `<details>`, native `<form>` validation, CSS `:has()` / `@starting-style` / scroll-driven animations, `fetch`, `Intl`, `URL`, `crypto.randomUUID()`, Node `fs/promises` & `node:test` |
| **3. Existing Project Dependencies** | Reuse utilities already in `package.json` / `pyproject.toml` / `Cargo.toml` | Don't add `lodash` or `axios` when native JS or an already-installed helper covers it |
| **4. Minimal Plain Code** | Write flat, direct functions inline where used (Rule of Three before abstracting) | 10 lines of clear TypeScript beats a 120-line generic factory |
| **5. New Third-Party Package** | **Last resort only** — must justify bundle weight, maintenance, and lock-in | Complex crypto, battle-tested parsers, accessibility primitives, or heavy physics/WebGL engines |

---

## Simplification Checklist

### 1. Unnecessary Abstractions
| Smell | Simplification |
|---|---|
| Wrapper class that just delegates | Remove wrapper, use the inner class directly |
| Factory that creates only one type | Replace with direct constructor |
| Strategy pattern with one strategy | Replace with simple function |
| Interface with one implementation | Remove interface, use the class |
| Abstract class with one child | Merge into the child class |
| Config object for 2 values | Use function parameters |

### 2. Dead Code
| Smell | Action |
|---|---|
| Unused imports | Remove |
| Unreachable branches | Remove (check tests first) |
| Commented-out code | Remove (it's in git history) |
| Unused variables/functions | Remove |
| TODO comments older than 6 months | Remove or create issue |
| Feature flags for launched features | Remove flag, keep the code |

### 3. Deep Nesting
```javascript
// ❌ Before: 4 levels deep
function process(data) {
  if (data) {
    if (data.items) {
      for (const item of data.items) {
        if (item.active) {
          doSomething(item)
        }
      }
    }
  }
}

// ✅ After: Early returns + filter
function process(data) {
  if (!data?.items) return

  data.items
    .filter(item => item.active)
    .forEach(doSomething)
}
```

### 4. Over-Parameterized Functions
```typescript
// ❌ Before: 8 parameters
function createUser(name, email, age, role, dept, active, verified, avatar) { }

// ✅ After: Object parameter
function createUser(opts: CreateUserOpts) { }
```

### 5. Premature Optimization
| Smell | Simplification |
|---|---|
| Custom cache for <100 items | Remove cache, measure first |
| Memoization on cheap functions | Remove memo |
| Lazy loading for small modules | Use direct import |
| Complex state machine for 3 states | Use simple if/else or switch |

---

## Simplification Protocol

### Step 1: Identify Complexity
```
- Count nesting levels (target: ≤3)
- Count function parameters (target: ≤4)
- Count lines per function (target: ≤30)
- Count abstractions per feature (target: ≤2)
- Check for dead code (target: 0)
```

### Step 2: Verify Understanding
Before simplifying, ensure you understand:
- What the code does (not what it looks like it does)
- Why it was written this way (maybe there's a reason)
- What tests cover it (simplification must not break tests)

### Step 3: Simplify Incrementally
```
1. Remove dead code first (safest)
2. Flatten nesting with early returns
3. Inline trivial abstractions
4. Merge related functions
5. Simplify data structures
```

### Step 4: Verify Behavior Preserved
```bash
npm run test    # All existing tests still pass
npm run build   # Still compiles
```

---

## When NOT to Simplify

| Situation | Why Keep Complexity |
|---|---|
| Performance-critical hot path | Optimization may look complex but is necessary |
| Required by framework/library | External constraints |
| Explicitly requested pattern | User chose this architecture |
| Will need extension soon | Abstraction prepares for known growth |

> **Ask first:** "This pattern seems over-engineered. Should I simplify it, or is there a reason for the abstraction?"

---

## Ponytail Closing Note (When Applying Aggressive Minimalism)

When intentionally skipping speculative abstractions or dependencies, finish concisely with:
- **Skipped intentionally**: Which unnecessary layers/packages were omitted (and which native/existing feature replaced them).
- **Residual risk / When to revisit**: The concrete trigger condition (e.g., *"3+ callers"* or *"measured >10k rows"*) that would justify adding complexity later.
