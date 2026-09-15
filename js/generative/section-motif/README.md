# section-motif

Decorative section motif for the Philosophy essay headings. One generator,
eight instances — section identity comes from the seed plus its placement, not
from bespoke scenes.

## Purpose

Give each essay a quiet, heading-anchored mark that aids orientation and scan.
It is decorative-adjacent: `aria-hidden`, no text, no semantics.

## Architecture

- `composition.js` — pure geometry (`buildMotif`, `motifSvgMarkup`); a seeded
  bandwidth of contour hairlines. Importable under `node`, no DOM.
- `index.js` — `mount(el, { seed })` reads `data-section`, injects the SVG, and
  returns `{ destroy() }`.

Colors come from CSS classes that reference existing tokens (`--muted`,
`--ochre`); nothing is hard-coded in JS.

## Parameters

| Parameter | Source | Default | Effect |
|---|---|---|---|
| base `seed` | `data-seed` / `?gen-seed` | `motif` | shifts every instance together |
| `section` | `data-section` | `''` | derives the per-section variation |
| derived seed | `${seed}:${section}` | — | line count (6–9), amplitude, frequency, phase, ochre accent line |

## Status

**Static stills only (Batch 2).** Motion is deliberately not implemented yet;
the owner picks the stills first. When/if motion is added, it must follow the
plan's budget (CSS-only, calm loop, rest phase, reduced-motion static) and get
its own copy/seed sign-off.

## Fallback

No JS → the plate stays `hidden`; the page is exactly as before.

## Budget

No rAF; no images; shared module; CLS 0.
