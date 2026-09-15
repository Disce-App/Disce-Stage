# Implementation Plan — Generative Web Visuals

**Status:** approved 2026-09-15 as the working basis · Batch 0–1 cleared to proceed
**Date:** 2026-09-15
**Sources:** `GENERATIVE_WEB_VISUALS_COMPETENCY.md`, `LLM_Generative_Coding_Modern_Web_Design_EN.md`, `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md`, `DESIGN-BRIEF.md`, and the codebase.
**Binding design reference:** `DESIGN-BRIEF.md`. This plan does not override it.

---

## 0. Frame

Generative visuals are an **organic supplement**, not a rework. Every rule below follows from that:

- No page is redesigned, restructured, or re-templated.
- A visual replaces either (a) an asset round 2 already flagged for removal, or (b) nothing — a new, clearly bounded component inside an existing section.
- Its static / reduced-motion / no-JS fallback **is the current look** of that section; the visual is injected by JS and is deletable without the page losing meaning.
- All existing copy stays. Any user-facing string a visual needs (labels, description, pause control) is new copy and needs separate DE/EN sign-off, exactly as in previous batches.
- Palette comes only from existing CSS tokens. No new hues. No dependencies. No build step.

Two reconciliation points found during the audit, carried into §8:

1. The competency document's reference architecture assumes TypeScript, component folders, and a test runner. This repo has **no build system, no TypeScript, no test framework, no dependencies** (`AGENTS.md`). The plan maps its *principles* onto plain ES modules + a dev-only Node harness, not a React/TS-shaped port.
2. `DESIGN-BRIEF.md` currently contains **no generative, motion, or animation guidance**; it governs static raster imagery only. A generative visual is undefined territory relative to the binding brief, so a short brief addendum is an owner decision (§8).

---

## 1. Current-state audit

### 1.1 Visuals by page (codebase ground truth)

| Page | Section (class) | Visual today | Type |
|---|---|---|---|
| index | `.hero` | `picture.hero-bg` — `DISCE_C01_r1_arena-stag-bordeaux` (AI) | decorative key visual |
| index | `.corridor` | `picture.corridor-bg` — `DISCE_C02_r1_corridor-stag-threshold` (AI) | decorative interstitial |
| index | section under "A clear path" | 2× `.media-card` — `DISCE_B03_r3_canal-pavilions`, `DISCE_C07_r1_stag-path-bordeaux-city` (AI) | decorative (round 2 flagged removal) |
| index | `.bg-forest no-halftone` | none (halftone + grain only) | surface treatment |
| index | `.cta-band` | `picture.cta-band-bg` — `DISCE_B04_r4_causeway-palms` (AI) | decorative band |
| philosophy | `.band` (top) | `DISCE_C03_r1_zeppelin-forest` (AI) | decorative band |
| philosophy | `.tight` (TOC) | 2× `.media-card` — `DISCE_A01_r2_wall-aperture-shadow`, `DISCE_A09_r4_garden-wall-snow` (AI) | decorative |
| philosophy | `.tight` (essays) | 8 essays (DE) + 8 (EN) in `.prose`, **no images** | text only |
| philosophy | `.band` (bottom) | `DISCE_A08_r4_billboard-wrong-sea` (AI) | decorative band |
| team | section under hero | 5× `img.portrait` — SVG placeholders (non-AI) | placeholder |
| team | `.band` | `DISCE_C06_r1_stag-antlers-city` (AI) | decorative (round 2 flagged removal) |
| team | `.bg-forest no-halftone` | none | surface treatment |
| status | `.tight.status-strip` | ledger (no image) | informative (HTML) |
| status | `.status-projects` | 4 project cards (no image) | informative (HTML) |
| status | `.bg-forest.long-range` | DACH map mask `dach-map-mask-1600.webp` (non-AI) + halftone | informative |
| status | `.cta-band` | `DISCE_B04_r4_causeway-palms` (AI, shared template) | decorative band |
| beta | `.beta-hero` | `DISCE_C08_r1_sky-aperture-heron` (AI) | decorative (out of scope) |
| waitlist | own stylesheet | out of scope | — |

**Removed slot (status):** the former `.loop-card` (`DISCE_C04_r1_loop-train-violet`) sat in the "current phase" area above the long-range section. It was **decorative** (`alt=""`, the source comment literally said *"No copy is added"*), and it was removed with the funding-phase section. **No caption ever existed for it** — the "draft, test, keep or discard" wording is not in any commit or doc (verified across full history). Any caption for a replacement is new copy.

**AI-image count vs round-2 targets:** homepage 5 (target 1–2), philosophy 4, team 1 + 5 SVG placeholders (target 0), status 1 shared CTA band (target 0 AI images; the CTA band is the deliberately retained template).

### 1.2 Candidate slots and classification

| Slot | Category | Basis |
|---|---|---|
| **A. Status — kernel working-loop diagram** | **informative** | answers the removed decorative loop slot with a function: make the kernel's iterate/keep-or-discard method legible |
| **B. Homepage hero** | decorative | brand landscape; round-2 image decision still open |
| **C. Philosophy — essay header motifs** | decorative | owner's round-2 counter-proposal; thematic imagery is allowed on Philosophy |
| D. index "A clear path" media-cards | decorative → could become informative | flagged for removal; possible later replacement |
| E. team `.band` antlers-city | decorative | flagged for removal; **not planned** (team is out of scope) |
| F. shared CTA band | decorative | retained template; **not planned** |

Only A–C are planned this round.

---

## 2. Candidate visuals — the seven mandatory questions

### 2.1 Slot A — Development Status: kernel working-loop diagram *(pilot)*

A calm, bounded plate inside the existing `.status-projects` section, after the project cards. It shows the kernel's operating loop — **entwurf / draft → prüfen / test → entscheiden / decide → behalten oder verwerfen / keep or discard → back** — so the copy "V0 is a proving ground" is visible rather than asserted.

1. **Purpose.** Make the kernel's iterative working method legible: the reader understands that the kernel advances by drafting, testing, and consciously keeping or discarding, not by shipping a fixed plan. This is a genuine explanation, not atmosphere.
2. **Category.** **Informative.**
3. **Fallback.** With JS off, the figure is empty → the section is exactly as today. `prefers-reduced-motion: reduce` → the same static composition, token parked at a stage, no motion.
4. **Simplest renderer.** **Inline SVG + CSS.** It is a labelled diagram; the technology table's first choice for "diagram / accessible infographic" is SVG, and Canvas would push essential labels into pixels. No Canvas, no rAF, no dependency.
5. **Devices/input.** 375 / 768 / 1440 (the repo's existing breakpoints). No pointer-only interaction is required; the pause control is keyboard-operable. Touch has no special path because there is no interaction.
6. **Measurable criteria.** JS ≤ 8 kB gzip; zero new images; zero rAF; one CSS animation, cycle 18–30 s with a rest phase; ≤ 6 moving elements; no CLS (explicit aspect ratio); no long task > 50 ms; all labels ≥ 4.5:1; a DOM textual equivalent; a keyboard-reachable pause/play control.
7. **Seed / test.** Deterministic geometry, hand-authored; a `data-seed` controls only sub-pixel stroke jitter and the motion phase, from a curated set. `?gen-motion=off` freezes time; screenshots at t=0 and t=frozen-later for DE/EN at three widths.

**Approved caption (2026-09-15), rendered as visible text below the diagram:**
DE „Der Kernel wächst in Schleifen: entwerfen, prüfen, behalten oder verwerfen." · EN “The Kernel grows in loops: draft, test, keep or discard.”
The DOM textual equivalent describes the four stages; the caption is editorial, not the accessible description's only carrier.

**Recommendation: recommended — this is the pilot.** Lowest risk, clearest purpose, no image decision required, fully revertible.

### 2.2 Slot B — Homepage hero

1. **Purpose.** Currently: brand landscape / "invisible → visible" mood. As a *photograph replacement* a procedural layer would only be decorative, and it cannot render the stag — the brief's central identification motif ("never covered, never cut off").
2. **Category.** Decorative.
3. **Fallback.** The existing `arena-stag-bordeaux` picture is the current look; any generative layer must sit *behind* it and be deletable.
4. **Simplest renderer.** Canvas 2D (many dynamic 2D lines) — the only candidate that would plausibly need Canvas; otherwise CSS.
5. **Devices.** Hero is the LCP element. A generative layer must not enter the critical path: load after `load`, render behind content, DPR cap 1.5 (mobile) / 2 (desktop).
6. **Measurable criteria.** Lazy JS ≤ 20 kB gzip, loaded after LCP; 20–30 FPS; ≤ 150 mobile / ≤ 400 desktop primitives; pause offscreen + hidden tab; no CLS; copy contrast verified over the full cycle; `aria-hidden="true"`.
7. **Seed / test.** Fixed per deploy from a curated set; test seed via query; screenshots at t=0 and t=5 s; a trace under CPU throttling.

**Recommendation: not recommended as a photo replacement.** Replacing the arena photo would lose the stag totem, contradict `DESIGN-BRIEF §4/§7`, and put LCP at risk — it does **not** remove the "which image stays" decision so much as make it differently. If the owner wants exploration later, scope it as a **decorative ambient layer behind the existing photo**, which is a different project with a profiling gate. Keep the homepage image decision separate.

### 2.3 Slot C — Philosophy: seeded essay-header motifs

1. **Purpose.** Give each of the eight essays a quiet, heading-bound motif that aids orientation and scan. Thematic imagery is explicitly allowed on Philosophy by the round-2 image rule. The purpose is real but modest; it must not compete with the essay text.
2. **Category.** Decorative.
3. **Fallback.** No motif = current look. Reduced motion → static motif.
4. **Simplest renderer.** **One SVG system, eight instances** — a single module, seeded per heading id, not eight bespoke scenes. No Canvas, no rAF.
5. **Devices.** Inline SVG sized to a small header rule (~80–120 px); must not alter text layout or the TOC; must stay out of the copy-safe zone.
6. **Measurable criteria.** Shared JS ≤ 8 kB gzip total (one module, no per-instance code); static by default, at most a very slow drift; zero images; no CLS; decorative (`aria-hidden`); no contrast concern because motifs sit in whitespace.
7. **Seed / test.** Seed derived from the heading `id` (stable across deploys) within a curated range; screenshots per seed.

**Recommendation: recommended, but reduced scope** — one deterministic system across the eight headings, not eight illustrated scenes.
**Approved 2026-09-15:** the system **replaces** the current AI images once shipped, rather than being added beside them (do not silently drop assets — the existing `A01`/`A09` media-cards come out as the motifs go in). Batch 2 must end with a clear before/after so the "eight header images" question can be decided on seen static frames.

### 2.4 Additional candidates — noted, not planned

- **index "A clear path" 2× media-cards** (round 2: remove without replacement). A future informative replacement is plausible, but it changes a homepage section; defer.
- **team `.band` antlers-city** (round 2: remove). Team is out of scope this round.
- **shared CTA band.** Retained template; do not touch.

---

## 3. Technology proposal

Apply the competency renderer-selection table; choose the smallest surface.

| Slot | Renderer | Why not the alternatives |
|---|---|---|
| **A. Status loop** | **SVG + CSS animation** | Labelled diagram → SVG is the table's first choice. Canvas would put labels in pixels and break text accessibility. No rAF needed. |
| **C. Philosophy motif** | **SVG** (one module, N instances) | Small, addressable, scalable, no rAF. |
| **B. Hero** (if ever) | **Canvas 2D**, lazy | Only if many dynamic 2D primitives are genuinely needed; profile first. |

**Zero new dependencies.** No p5.js, PixiJS, Three.js, GSAP, D3, Rough.js. The landscape report's rule applies: do not add a library when ~50–150 lines of native code suffice for a single route. Expected effect sizes are far below that.

**Plain-ES-module architecture** (the vanilla equivalent of the competency's component layout; tokens separated from simulation and rendering):

```
js/generative/
  loader.js            # scans [data-gen] mounts, dynamic-imports the visual, checks reduced motion
  tokens.js            # reads frozen CSS custom-property values once, exposes { palette, motion }
  prng.js              # seeded PRNG (mulberry32) + derive(seed, id) helpers
  registry.js          # name -> dynamic import
  kernel-loop/
    index.js           # mount(el, { seed, motion, lang }) -> { destroy() }
    composition.js     # pure static-SVG geometry builder (unit-testable without a browser)
    motion.js          # CSS timing / phase logic (no rAF)
    README.md          # intent, parameters, ranges, trade-offs, fallback
```

- Mount contract: `<figure class="gen-visual" data-gen="kernel-loop" data-seed="…" hidden>`. `loader.js` reveals it only after mounting; `destroy()` removes listeners and injected nodes.
- Loaded per page with `<script type="module" src="js/generative/loader.js"></script>` **only on pages that use a visual**. `js/site.js` (classic, site-wide) stays untouched; module scripts are deferred, so ordering is safe.
- Seed and time are explicit: `data-seed` + `?gen-seed=`/`?gen-motion=off` for reproducible screenshots. No hidden globals.
- `composition.js` is pure (geometry in, SVG string/element out), so it can be checked without a browser.

**Testing without a framework.** The repo has no test runner and must not gain a project dependency. Proposal: keep the existing dev-only Node CDP harness (outside the tree) for screenshots at fixed seed/time and viewports, plus pure-function checks on `composition.js`/`prng.js` via `node`. This is dev tooling, not a repo dependency. **Approved 2026-09-15:** harness stays outside the tree; its location and output convention are recorded in Appendix B.

---

## 4. Design-token mapping

Use the tokens **as rendered today** (the brief's renamed tokens are noted where relevant). No new hues.

| Token | Value | Generative use |
|---|---|---|
| `--ochre` | `#E3AF50` | the single loud accent: the moving token / active stage |
| `--legacy-ink` | `#141414` | hairline strokes, primary labels on light |
| `--ink-soft` | `#2A2A28` | secondary text |
| `--muted` | `#5C5A52` | tertiary labels |
| `--line-soft` | `rgba(20,20,20,0.16)` | hairlines, dividers |
| `--legacy-paper` | `#FBF8EF` | plate surface (matches `.media-card`) |
| `--cream` / `--cream-dim` | `#F6F1E2` / `#EDE6D2` | light section surfaces |
| `--green-forest` | `#1E4B3A` | dark-band surface (rendered dark band) |
| `--green-dark` / `--green` | `#357435` / `#4FAC4E` | functional accents, sparingly |
| `--parchment` | `#D5C09D` | labels/linework on dark |
| `--font-display` / `--font-body` | Archivo Black / Inter | labels use `--font-body`, uppercase, tracking 0.08–0.18 em |
| `--fs-100/200` | 11px / 12px | label sizes |
| `--sp-*`, `--maxw` | 4px grid / 1200px | plate padding and width |
| `--ease`, `--dur-fast/base/slow` | one curve, 120/180/260 ms | micro transitions only (reveal, pause toggle) |

**Form language:** square corners, 1–2px hairlines, ochre **diamond** markers (`rotate(45deg)`, matching `.eyebrow::before`), controlled imperfection via seeded stroke jitter. Reuse the existing film-grain feTurbulence data-URI (~5%) and the halftone PNGs **only** where a band already uses them; add no new grain.

**Forbidden:** new hues; gradients/glassmorphism; rounded "friendly tech" cards; bordeaux behind text; gamification patterns (rings, stars, XP) — the product explicitly avoids overall verdicts.

**Motion — genuinely missing tokens (proposed, not added):**

| Proposed token | Intent | Candidate value |
|---|---|---|
| `--gen-cycle` | full loop period | 24 s |
| `--gen-rest` | idle pause fraction per cycle | 0.35 |
| `--gen-amplitude` | max displacement | 4 px |
| `--gen-fps` | ambient target (Canvas only) | 24 |
| `--gen-dpr-cap` | DPR cap | 1.5 mobile / 2 desktop |
| `--gen-density` | primitive count per LOD tier | 24 / 60 / 120 |

**Approved 2026-09-15** as the `--gen-*` set; final values ship with Batch 1 (only the tokens a batch consumes are added to `css/experimental.css`).

---

## 5. Performance & accessibility budgets (strict end)

These pages are calm and editorial, so budgets sit at the conservative end of the competency defaults.

| Visual | JS (gzip) | Renderer cost | Motion | Density | Pause | Reduced motion | Semantic layer |
|---|---|---|---|---|---|---|---|
| **A. Status loop** | ≤ 8 kB | SVG + CSS, **no rAF** | one 18–30 s loop, rest phase | ≤ 6 moving elements | keyboard pause/play control | static composition, token parked | SVG `aria-hidden`; DOM `<figcaption>`/`<ol>` describes the loop (DE/EN) |
| **C. Philo motif** | ≤ 8 kB shared | SVG, **no rAF** | static default; optional slow drift | per-heading, ≤ 12 marks | none (below threshold) | static motif | `aria-hidden` decorative |
| **B. Hero (if pursued)** | ≤ 20 kB, lazy post-LCP | Canvas 2D, one rAF | 20–30 FPS | ≤ 150 mobile / 400 desktop | click/keyboard pause | static frame or hidden | `aria-hidden`; photo stays the semantic layer |

**Global rules for every visual:** zero dependencies; no entry into the LCP path; explicit dimensions/aspect-ratio so CLS is 0; one `requestAnimationFrame` maximum (Canvas only); pause via `IntersectionObserver` offscreen and Page Visibility in hidden tabs; delta-time clamping; no per-frame allocations; full cleanup (RAF, listeners, observers) in `destroy()`; no scroll hijacking; no custom cursor; no flashing (>3 Hz) or large parallax; contrast ≥ 4.5:1 measured over the cycle; every pointer interaction has a keyboard equivalent; any persistent automatic motion gets a pause control with a DE/EN label.

---

## 6. Sequencing — rising risk, pilot first

Each batch is independently shippable, with its own acceptance criteria and the established screenshot routine (375/768/1440, DE/EN, closed + reduced-motion, console + no-overflow + no-failed-asset diagnostics).

**Batch 0 — Groundwork (0.5–1 day).** `js/generative/` skeleton (`loader`, `tokens`, `prng`, `registry`), the `data-gen` mount contract, the `?gen-seed`/`?gen-motion` test hooks, and the CDP screenshot harness extended for frozen time. Drafts the `DESIGN-BRIEF.md` addendum as a proposed diff (not applied silently). No visual on any page.
*Acceptance:* loader loads nothing on pages without `[data-gen]`; zero page impact; `composition.js` pure-function check runs under `node`; the addendum is presented as a diff for approval.

**Batch 1 — Status kernel-loop diagram (pilot, 2–4 days).** SVG + CSS, mounted inside `.status-projects`; final `--gen-*` values land in `css/experimental.css` here.
*Acceptance:* static composition approved before motion; budgets in §5 met (measured JS ≤ 8 kB gzip reported); DOM textual equivalent; DE/EN pause control; no CLS; reduced-motion static frame; no-JS render byte-identical to today; screenshots DE/EN at 375/768/1440; `destroy()` verified by navigating away.
*Text-node scope:* only the plate markup (`aria-hidden` where appropriate), its textual equivalent, the caption, the four stage labels, and the pause controls may change; nothing else.
*Stop:* if the purpose cannot be stated in one sentence, or any budget regresses → revert (the visual is deletable).

**Batch 2 — Philosophy motif system (3–5 days).** One seeded SVG module across eight headings; **replaces** the current AI images once shipped (not added beside them).
*Acceptance:* single module reused; seed from heading id; no layout change to prose/TOC; static by default; before/after frames across all eight headings; screenshots per seed.
*Gate:* owner confirms motifs answer the round-2 "eight header images" counter-proposal on the strength of the before/after.

**Batch 3 — Homepage hero ambient study (gated, 3–5 days).** Only if the owner resolves the homepage image decision and wants an additive layer behind the photo.
*Acceptance:* LCP not regressed; trace under CPU throttling; DPR/LOD caps; pause offscreen/hidden; reduced-motion static.

**Batch 4 — Deferred candidates (no estimate).** index media-card replacement, team band, CTA ambient — only with explicit approval, one at a time.

Effort is deliberately pessimistic; small and verifiable beats comprehensive.

---

## 7. AGENTS.md / skills proposal *(proposed text only — not created)*

### 7.1 Proposed `AGENTS.md` block

```md
## Generative web visuals

Before planning, implementing, refactoring, or reviewing any Canvas, SVG
motion, CSS animation, WebGL, shader, particle, procedural, or scroll-linked
visual, read `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and
`docs/generative-visuals/implementation-plan.md`.

A generative visual is an optional enhancement. It must be deletable without
the page losing meaning, its static/no-JS fallback is the current look of the
section, and it uses only existing CSS design tokens. State its user/product
purpose first; if none exists, propose a static or CSS/SVG alternative. Do not
add dependencies or a build step.
```

### 7.2 Proposed on-demand skill

Create `.opencode/skills/generative-web-visuals/SKILL.md` — loaded only when relevant, never in every session.

```md
---
name: generative-web-visuals
description: Plan, implement, review, or refactor production-safe generative web visuals (SVG, Canvas, CSS motion, procedural, scroll-linked) in this static, dependency-free site.
license: Proprietary
compatibility: OpenCode project skill
metadata:
  domain: frontend-creative-coding
  priority: production-quality
---

# Generative Web Visuals

Read `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and
`docs/generative-visuals/implementation-plan.md` before editing relevant code.

## Required workflow
1. State the user/product purpose and classify it decorative / informative / interactive.
2. Propose the simplest renderer (SVG → Canvas 2D → WebGL); justify any Canvas use.
3. Define the static fallback (the current look), reduced-motion behavior, the
   semantic/textual alternative, target viewports, and the budget.
4. Implement in slices: static composition → deterministic render → motion →
   interaction → responsive/LOD → tests.
5. Derive all variation from an explicit seed; make seed and time controllable.
6. Clean up RAF, listeners, observers, and injected nodes in `destroy()`.

## Repo non-negotiables
- No new dependencies, no build step; plain ES modules under `js/generative/`.
- Palette and form come only from existing CSS tokens; no new hues.
- Any user-facing string is bilingual and copy-frozen: add paired `data-lang`
  spans (or read `body.lang-en`) and get DE/EN sign-off.
- A visual is injected by JS and deletable; no-JS and reduced-motion fall back
  to the current look.
- Verify with the dev-only CDP harness: console clean, no horizontal overflow,
  no failed assets, fixed seed/time, 375/768/1440 in DE and EN.
- One bounded task per commit.

## Evidence
Report files changed, measured budgets, screenshots at fixed seed/viewport,
reduced-motion and keyboard findings, and residual risks. Never claim
performance or accessibility compliance without measurements.
```

**Permissions:** keep this skill and a future `motion-accessibility` skill available by default; no MCP servers are needed for the pilot (the built-in browser/CDP harness suffices). No `opencode.json` change is required for Batch 0–1.

---

## 8. Risks and owner decisions *(resolved 2026-09-15)*

The table records the state at planning time; §8.1 records the approvals.

| # | Decision | Recommendation |
|---|---|---|
| 1 | Does a code-rendered informative diagram conflict with status's "0 AI images" intent? | It is not an AI image and adds function; treat as compliant, but confirm. |
| 2 | Loop caption copy (DE/EN) — the cited "draft, test, keep or discard" text does not exist in history | Approve a short new caption, or keep the diagram self-labelling; either way it needs copy sign-off. |
| 3 | Homepage hero: procedural replacement? | Not recommended as a replacement (loses the stag totem, LCP risk); revisit only as an additive ambient layer, gated. |
| 4 | Philosophy scope: motifs vs. images; add to or replace `A01`/`A09`? | One seeded motif system; do not silently drop existing assets. |
| 5 | Add generative motion tokens (`--gen-*`) to the token set? | Approve names/values; needed because existing durations (120–260 ms) are UI-scale. |
| 6 | Pause control on the status loop | Approve a small keyboard-accessible DE/EN pause/play control. |
| 7 | New front-end structure: `js/generative/` + per-page module script | Approve; keeps `site.js` untouched and cost per page to one module. |
| 8 | `DESIGN-BRIEF.md` has no generative/motion section | Approve a short addendum (binding reference otherwise stays silent). |
| 9 | Dev-only Node/CDP test harness vs. zero-dependency manual checks | Keep the harness outside the tree; do not add a repo dependency. |
| 10 | Commit this plan? | Owner decides; it is currently untracked. |

### 8.1 Approvals (2026-09-15)

1. **Approved** — a code-rendered informative diagram is not an AI image under the round-2 rule.
2. **Approved** — caption copy as quoted in §2.1, rendered as visible text below the diagram; the DOM textual equivalent describes the four stages.
3. **Confirmed** — the hero is not a photo replacement and gets no ambient layer now; it stays out of every batch beyond the shared Batch 0 groundwork.
4. **Approved** — one motif system, reused, **replacing** the current AI images; Batch 2 ends with a clear before/after.
5. **Approved** — `--gen-*` motion tokens; final values ship with Batch 1.
6. **Approved** — DE/EN pause control on the status loop.
7. **Approved** — `js/generative/` + per-page module script; `site.js` untouched.
8. **Approved** — draft the `DESIGN-BRIEF.md` addendum in Batch 0 as a proposed diff, not applied silently.
9. **Approved** — dev-only harness stays outside the tree; convention in Appendix B.
10. **Approved** — the plan and the two source documents are committed together, followed by a separate commit for the `AGENTS.md` rule and the skill.

Commit policy: bounded commits on owner request only, except the two pre-authorized commits above.

---

## Appendix A — later / explicitly not planned

Waitlist redesign, `beta.html`, sitemap/domain questions, team portraits, team `.band` image, homepage "A clear path" media-cards, and the shared CTA band are **out of scope** this round. Recorded here so they are not lost.

## Appendix B — dev-only verification harness (approved 2026-09-15)

Kept **outside the repository** in `/tmp/opencode/`; never committed, never a project dependency.

- `lib.mjs` — static file server + `chrome-headless-shell` CDP driver (no Playwright/Selenium; Node's built-in `WebSocket`). Server-rendered fonts and `--blink-settings` force a hover-capable pointer for `@media (hover: hover)` checks.
- `shot.mjs <outdir> <page> <width> <de|en> [open] [reduced]` — full-page PNG via `captureBeyondViewport`, with per-shot diagnostics (`overflow`, `failedImages`, console errors). Sticky header is pinned static during capture. `settle()` scrolls to decode lazy images.
- `probe.mjs` — interaction/a11y assertions: `aria-controls` validity, toggle state, layout stability, hover path, reduced motion, contrast ratio.
- `extract_text.py <file>` — visible text nodes for copy-freeze diffs.
- `composition.js` / `prng.js` pure-function checks run under plain `node`.
- **Output convention:** rendered checks go to `_screenshots/<batch>/` (untracked, excluded via `.git/info/exclude`); JSON assertion results are written alongside.
- **Frozen time / seed:** pass `?gen-seed=<n>` and `?gen-motion=off`; capture at t=0 and one fixed later instant.
- **Chrome binary:** `~/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`.
