# Website Accessibility — WP D Implementation Log

**Document type:** Implementation record for work package **WP D — Accessibility** (task **A11Y-08**, reflow & tap targets).
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Basis:** `master-checklist-website-revision.md` §2.3 / §2.13.3 (A11Y-08), `website-revision-work-packages.md` WP D, WCAG 2.2 SC 2.5.8 (Target Size, Minimum) and SC 1.4.10 (Reflow), `AGENTS.md` accessibility guardrail.

> This log records the WP D close-out. It does not replace the changes themselves. The authoritative master checklist was not modified; A11Y-08 can be updated by the owner on the evidence below.

---

## 1. Scope of this round

Every WP D task except **A11Y-08** was already `DONE` (A11Y-01…07, A11Y-09, A11Y-10). A11Y-08 is `MEASURE-ONLY`: *measure tap-target sizes and reflow at 320–430 px; fix only if a target is <24×24 or overflow occurs.*

The prior A11Y-08 measurement (headless Firefox 156 / BiDi, 2026-09-21) predated this round's work — the shared three-column grid, Blocksatz, larger section headings, the reading field, the team-page revamp and the waitlist migration all changed layout and text metrics. This round therefore **re-measured the current build** and closed the remaining gaps.

---

## 2. Method

- **Tooling:** headless Firefox 156 via the built-in **WebDriver BiDi** endpoint (`ws://127.0.0.1:9222/session`), driven by a Node 24 script using the global `WebSocket`. Local `python3 -m http.server` on the repo root.
- **Pages:** all six public pages — `index`, `philosophy`, `kernel`, `team`, `status`, `waitlist`.
- **Widths:** 320, 375, 430 px (the A11Y-08 range).
- **Cache-busting:** every navigation carried a `?t=<timestamp>` query string, because Firefox heuristic caching served stale HTML/CSS across runs (this initially masked the checkbox fix).
- **Reflow/overflow:** `max(documentElement.scrollWidth, body.scrollWidth) − innerWidth`. A negative value is the 12 px scrollbar difference; **≤ 0 means no horizontal scroll**.
- **Target size (WCAG 2.5.8):** every `a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button]` was measured; a target is undersized if width < 24 or height < 24.
- **Spacing exception:** for each undersized non-inline target, a 24 px-diameter circle centred on it must not intersect another target's rect (or another undersized target's circle).
- **Inline exception:** targets whose computed `display` is `inline` are treated as exempt (SC 2.5.8 Inline exception).

---

## 3. Result before fixes

- **Horizontal overflow: 0 px on all six pages at 320 / 375 / 430 px.** The post-Batch-E `philosophy.html` fix holds; the layout/readability work introduced **no reflow regression**. (Elements reported "beyond the viewport" — the partner ticker track, kernel diagram, etc. — are inside `overflow: hidden` containers and do not add document scroll width.)
- **Undersized targets:** 12 per page on the shared-chrome pages, all passing the spacing exception. Three controls were under 24 px **by size**:
  - `.footer-col a` — 22 px tall (10 links per page).
  - `.lang-switch button` — 23 px tall.
  - waitlist consent `#consent_contact` — 20 × 20 px.
- **Spacing failures: 0** anywhere.

The prior measurement accepted these via the spacing exception. Because the WP D acceptance is *"no target <24×24"*, this round met the **size** criterion instead of relying on the exception.

---

## 4. Fixes applied

| File | Change | Effect |
|---|---|---|
| `css/experimental.css` | `.footer-col a` → added `min-height: 24px` | footer links 22 → 24 px tall |
| `css/experimental.css` | `.lang-switch button` → added `min-height: 24px` | language buttons 23 → 24 px tall |
| `css/experimental.min.css` | the two rules above, kept in sync | linked stylesheet matches source |
| `waitlist.html` | `.checkbox-label input[type="checkbox"]` → `width/height: 24px`, `margin-top: 0` | consent checkbox 20 → 24 px |

No HTML structure, copy, behaviour, or images changed. The footer/lang-switch changes add ≤ 2 px per control; the footer columns grow by roughly 20 px in total.

---

## 5. Result after fixes (re-measured, cache-busted)

| Page | 320 px | 375 px | 430 px |
|---|---|---|---|
| index.html | overflow 0 · undersized 0 | 0 · 0 | 0 · 0 |
| philosophy.html | 0 · 0 non-inline (5 inline-exempt) | 0 · 0 (5 inline) | 0 · 0 (6 inline) |
| kernel.html | 0 · 0 | 0 · 0 | 0 · 0 |
| team.html | 0 · 0 | 0 · 0 | 0 · 0 |
| status.html | 0 · 0 | 0 · 0 | 0 · 0 (1 inline) |
| waitlist.html | 0 · 0 (3 inline-exempt) | 0 · 0 (3 inline) | 0 · 0 (3 inline) |

- **No horizontal overflow** on any page at any width.
- **Zero undersized non-inline targets.** The only remaining sub-24 px targets are **inline links inside body text** (privacy link and `mailto:` links on the waitlist; prose links on philosophy; one on status) — these conform via the SC 2.5.8 **Inline exception** and cannot be enlarged without breaking the text flow.
- **Zero spacing failures.**

**A11Y-08 acceptance:** no horizontal scroll ✔; no non-inline target below 24 × 24 ✔ (inline links exempt under WCAG 2.5.8).

---

## 6. Intentionally not changed

- **Inline text links** remain at line-height size — the WCAG Inline exception applies and enlarging them would disrupt reading.
- **No layout or copy changes** beyond the four size declarations.
- **Kernel's own section system** is untouched.

---

## 7. Residual / notes

- **Human mobile legibility** of the wrapped philosophy eyebrow at 320 px remains the only non-automated residual (unchanged from the prior measurement).
- **Tooling note (this session):** full-page headless screenshots are large PNGs (9–11 MB); they must be cropped and downscaled to small JPEGs before being read, to stay under the harness image-size cap.
- **Nothing committed.** A11Y-08 can move from `MEASURE-ONLY` to `DONE` on the evidence above.
