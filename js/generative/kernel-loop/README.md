# kernel-loop

Informative visual for the Development Status page: the kernel's working loop —
**Entwurf → Prüfung → Entscheidung → Behalten oder verwerfen → repeat**.

## Purpose

Make the kernel's iterative method legible: it advances by drafting, testing,
and consciously keeping or discarding, not by shipping a fixed plan. It is
informative, not decoration.

## Architecture

- `composition.js` — pure geometry (`buildLoop`, `loopSvgMarkup`); importable
  under `node`, no DOM.
- `motion.js` — the deterministic frozen dash offset only. Motion itself is CSS.
- `index.js` — `mount(el, { seed, motion, phase })` injects the SVG, wires the
  pause control, and returns `{ destroy() }`.

The semantic text (stage labels, caption, description, pause control) is static
markup in `status.html`; only the `aria-hidden` graphic is injected.

## Renderer

Inline SVG + one CSS `stroke-dashoffset` animation over a path normalised with
`pathLength="100"`. No `requestAnimationFrame`, no Canvas, no dependency.

## Parameters

| Parameter | Source | Default | Range | Effect |
|---|---|---|---|---|
| `seed` | `data-seed` / `?gen-seed` | `kernel-loop` | any string | sub-pixel jitter of the four loop corners |
| `motion` | reduced-motion / `?gen-motion` | on | on/off | off = frozen frame, pause control hidden |
| `phase` | `?gen-phase` | 0 | 0–1 | position of the frozen frame |
| `--gen-jitter` | `css/experimental.css` | `0.75` | 0–3 | jitter amplitude in viewBox units |
| `--gen-cycle` | `css/experimental.css` | `24s` | 18–30s | loop period, with a 35% rest phase |

## Fallback

- No JS → the plate stays `hidden`; the page is exactly as before.
- Import/error → the plate stays hidden.
- `prefers-reduced-motion: reduce` or `?gen-motion=off` → static frame, no
  animation, pause control hidden.

## Accessibility

- The graphic is `aria-hidden="true"`.
- The four stage labels are a real `<ol>`; the sr-only description explains the
  loop; the caption is visible editorial text. All bilingual via `data-lang`.
- The pause control is a real `<button>` with `aria-pressed`, keyboard-operable.

## Budget

JS ≤ 8 kB gzip; zero images; no rAF; CLS 0; no task > 50 ms. Verify with the
dev-only CDP harness (see the plan's Appendix B).
