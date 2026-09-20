# dot-field

Animated halftone-dot fields for the page-hero panel (`bloom`) and a section
focal (`arena`). One primitive, two fields.

## Purpose

Carry the print-editorial dot language already used across the site, with a
slow ambient life. Decorative only: `aria-hidden`, `pointer-events: none`, and
deletable — removing the mount leaves the static still (the page's base look).

## Architecture

- `composition.js` — pure field maths (`bloom`, `arena`, `current`).
  `forEachDot(field, opts, cb)` walks the lattice; no DOM, no canvas, safe to
  import for checks. Time enters only as `phase` 0..1 through `sin`/`cos`, so one
  cycle returns to the start: the loop is seamless.
- `index.js` — `mount(el, { motion, phase })`: injects a canvas, reads geometry
  from CSS custom properties, drives one `requestAnimationFrame`, and returns
  `{ destroy() }`.

The static assets in `images/derived/` (`dot-bloom-green.png`,
`dot-arena-green.png`) are generated from the **same maths** by
`scripts/generate_dot_patterns.py`, so the still and the animation match.

## Mount contract

```html
<div class="dot-field dot-field--hero"
     data-gen="dot-field" data-field="bloom" data-seed="dot-bloom"
     aria-hidden="true"></div>
```

`js/generative/loader.js` finds `[data-gen]` and calls `mount`. The element's
CSS background is the matching still; on a successful mount the module adds
`.is-gen-active` (which drops the still) and draws the canvas on top, so the two
never double up.

## Parameters

| Parameter | Source | Default | Effect |
|---|---|---|---|
| `field` | `data-field` | `bloom` | which field maths to run |
| `motion` | loader / reduced-motion / `?gen-motion=off` | on | `off` leaves the static still |
| `phase` | `?gen-phase=0..1` | 0 | frozen frame for screenshots |
| pitch / radius / min | CSS `--dot-pitch` / `--dot-radius` / `--dot-min` | 17 / 6 / 0.06 | dot lattice |
| cycle | `--gen-cycle` | 26 s | loop period |

Per-motif tuning lives in `FIELD_DEFAULTS` (`composition.js`) and is mirrored by
`scripts/generate_dot_patterns.py --params` for the still:

- `arena` — `ring` (ring wavelength, px), `waves` (whole wavelengths travelled
  per cycle; integer keeps the loop seamless), `reach` (field radius as a
  fraction of the short side), `breathe` (whole-field expansion/contraction:
  the calm pulse). Current: `ring 40`, `waves 3`, `reach 0.6`, `breathe 0.08`
  → a ring opens and settles roughly every 8.7 s.

Per-mount colour override: `--dot-color-a` / `--dot-color-b` on the mount replace
the global `--green` / `--green-dark`. The dark homepage hero uses this to render
the bloom in `--ochre` / `--parchment` (DESIGN-BRIEF §5: the bright green is for
light surfaces only, ochre/parchment on dark).

## Pointer reaction

`reactive.js` clears the dots under the cursor with a soft radial mask on the
mount. Because the mask sits on the mount it covers the animated canvas and the
static background image alike, so the still plate reacts too (including under
`prefers-reduced-motion` and `?gen-motion=off`). One shared passive
`pointermove` listener drives every field; the `is-reactive` class is present
only while the pointer is near, and a field opts out with
`data-gen-hover="off"`. There is no reaction on coarse pointers (touch), where
there is no hover. It is decorative and pointer-initiated — no meaning is gated
behind it and it is not autonomous motion.

## Fallback / accessibility

- No JS, failed import, or `prefers-reduced-motion: reduce` → the static PNG,
  i.e. the current look. `mount` returns a no-op when motion is off.
- Decorative: `aria-hidden`, never carries meaning; sits behind the copy.
- Contrast is untouched (dots are background; the copy stays on the paper tone).

## Performance

One rAF per mount, DPR capped at 2, pause via `IntersectionObserver` offscreen
and Page Visibility in hidden tabs, resize-aware, full cleanup in `destroy()`.
No dependencies.

## Status

Integrated for `bloom` (page-hero panel, team/status/legal) and `arena`
(homepage audience section focal; team page advisor block). Extended fields
(`current`) exist in `composition.js` but are not mounted yet.
