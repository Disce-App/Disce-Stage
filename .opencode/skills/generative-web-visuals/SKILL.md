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
