# Website Readability over Background Images — WP H / NEW-06 Implementation Log

**Document type:** Implementation record for work package **WP H — Visual System**, task **NEW-06** (rework fonts/legibility over background images).
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Basis:** `website-revision-work-packages.md` WP H (NEW-06, NEW-03), `DESIGN-BRIEF.md` §5/§6/§8/§10, `AGENTS.md` accessibility guardrail, and web research on text-over-image legibility (sources listed in §2).

> This log records NEW-06. It does not replace the changes themselves. The authoritative master checklist and work-package documents were not modified.

---

## 1. Problem

Nearly all body text set on the transparent (light) sections sits directly on the **botanical paper wash** (`body::after`, a fixed Greenery image at `--botanical-opacity: 0.25`). The headings (Archivo Black, near-black) hold up, but the grey reading text (`--muted` on `.lede`, `.process-item p`, `.team-member-body p`, `.advisor-row .advisor-role`) loses legibility against the wash's texture. The homepage below the hero is the most visible case (e.g. "Ein klarer Weg, keine Vokabelliste.").

Founder constraints recorded: **keep the background images; no boxes or flat panels behind text; a creative, layered solution like the homepage hero; apply it website-wide.**

---

## 2. Research (web) — techniques considered

Ranked shortlist from the research pass, with sources at the end:

1. **Eased/feathered gradient scrim** anchored to the text zone — box-free, cheap, robust. *Chosen (as the reading field).*
2. **Art-directed crop into copy space** — best aesthetics; already partly present (per-page `--botanical-position`). *Kept.*
3. **Source-level grading / duotone** — robust but changes the asset look. *Not used; the images are to stay as-is.*
4. **Radial vignette / `mask-image` soft shape** — surgical, edgeless. *Used (radial field).*
5. **`text-shadow` halo + type scale/weight/colour** — supporting layer. *Partly used (darker reading ink); halo held in reserve.*
6. **Feathered region blur** — optional; perf/forced-colors caveats. *Held in reserve.*

Anti-patterns explicitly avoided: opaque "safety" boxes, relying on shadow alone, testing only the best pixel.

Sources: NN/g `text-over-images`; Smashing Magazine "Designing accessible text over images" Part 1/2; CSS-Tricks "Design considerations: text on images"; Ahmad Shadeed "Handling text over image in CSS"; MDN `mask-image`, `backdrop-filter`, `@media (prefers-contrast)`, `@media (forced-colors)`; WebAIM contrast; WCAG 2.2 SC 1.4.3 / 1.4.11; WCAG.com "content over images".

---

## 3. Implemented system — "Reading field"

A three-layer system, layered like the hero (image → field → type), with no box anywhere:

1. **Image (unchanged):** the botanical wash stays exactly as it was (`body::after`, 0.25, per-page position).
2. **Reading field (new):** one feathered paper radial painted by `html::after` — the only layer that paints *after* the wash at the same negative z-index. It has no border and no flat edge; it dissolves into the image, calming the reading column while the image stays visible at the page's outer field and on the right.
   - `html::after` was chosen because `body::before` was already the left green rule and `body::after` is the wash itself.
   - Hidden below 1024 px, like the wash.
   - On Philosophy it is masked off the right-hand arches pane, mirroring the wash mask, so the two never overlap.
3. **Reading ink (new):** a `--reading-ink` token (`--ink-soft`) applied to the text most often set directly on the wash — `.lede`, `.process-item p`, `.team-member-body p`, `.advisor-row .advisor-role`. Dark sections (`.hero`, `.bg-forest`, `.bg-ink`, `.cta-band`) already override these, so the dark surfaces are untouched.
4. **`prefers-contrast: more`:** deepens both the field and the reading ink.

Deletable: removing the block returns the page to its previous rendering.

---

## 3b. Layout pass (A + B) — light sections

After the readability fix landed, the light sections still read as "plain": the copy occupied only the left part of the grid and the section headings were small. Two changes (both scoped to `body:not(.page-kernel)`, so the Kernel keeps its own section system):

**A — stronger section headings.** `.section-head h2` raised from `--fs-900` (30px) to `--fs-1000` (36px); reduced back to 30px at ≤640px so phones don't get a five-line hyphenated heading. Kernel keeps its `--k-fs-section` override.

**B — one shared three-column grid.** The section head and the process rows now use the same geometry — `100px | 1fr | 1.4fr` with a 40px gap — so each light section has two clean vertical lines: the wrap edge (eyebrow, heading, numbers) and the third column (lede, descriptions).
- **Section head:** eyebrow and heading span the left two columns; the lede sits in the third column, **top-aligned with the heading** (`grid-template-areas: "eyebrow eyebrow ." / "title title lede"`). Heads without a lede span the full width. Collapses to one column at ≤900px.
- **Process rows:** `number | title | description`. `display: contents` promotes the h3 and p out of their wrapper so they land in columns 2 and 3 without a markup change. Collapses to one column at ≤760px. Applies to the homepage "approach" list and the status long-range list; Kernel is excluded.

**C — Blocksatz.** Justified reading text with hyphenation on (so justified lines don't open rivers): `.lede`, `.prose p`, `.process-item p`, `.problem-card p`, `.persona-card p`, `.team-member-body p`. The hero lede stays left-aligned and the centred closing band stays centred.

---

## 4. Files changed

| File | Change |
|---|---|
| `css/experimental.css` | New "READING FIELD" block (`:root` tokens, `html::after`, mobile hide, Philosophy mask, `prefers-contrast: more`); `.lede`, `.process-item p`, `.team-member-body p`, `.advisor-row .advisor-role` switched to `var(--reading-ink, var(--muted))`; layout pass A + B + Blocksatz C (§3b). |
| `css/experimental.min.css` | The same four colour swaps and the `.section-head h2` size change (targeted in-place edits) plus the minified field/mask and layout blocks appended. |

No HTML, JS, image, or content files were changed. The homepage's inline critical CSS was left as-is: the reading field is below the fold, and the async minified sheet re-applies every rule.

---

## 5. Verification performed

- **CSS integrity:** brace counts balanced in both files; `--reading-ink` present in both (6 refs in the min).
- **Rendered (headless Firefox, 1440 px):** homepage (hero unchanged; problem / "Ein klarer Weg" / team-teaser sections use the shared grid; section lede and process descriptions share one vertical line; image visible again), Philosophy (prose legible; arches pane intact), Team (roster bios justified; founders head spans full width; open-role head uses the grid), Status (projects and dark long-range both use the grid), Waitlist (intro legible; form/FAQ cards unaffected), Kernel (unchanged — section system and process list intact).
- **Mobile (390 px):** section heads and process rows collapse to a single column with no overflow; section heading returns to 30px.
- **Blocksatz:** justified with hyphenation on the lede, process, prose and card paragraphs; hero and closing band exempt.
- **No layout shift from the field:** it is fixed and adds no flow.

---

## 6. Intentionally not changed / deferred

- **NEW-03 — animate the hero images:** deferred by founder decision (budget). Not started; still requires a stated user/product purpose and the generative-visuals guardrail before any work.
- **Hero:** untouched — it is the reference standard.
- **Background images:** kept; no master or derivative was edited.
- **Inline critical CSS (`index.html`):** unchanged (above-the-fold only).

---

## 7. Tuning knobs / open questions

- **Field strength:** `--reading-field` alpha stops (currently 0.34 centre, after the first pass at 0.62 proved too flat — it erased the image and read as "plain"). Lower it if the image should read more strongly behind the text; raise it for more separation. The darker reading ink now carries most of the legibility, so the field can stay light.
- **Reading ink:** `--reading-ink` (currently `--ink-soft`). Can be darkened to `--legacy-ink` or softened back toward `--muted`.
- **Optional extras held in reserve:** a subtle paper `text-shadow` halo on reading text; a mild wash grade or slight blur; a vertical component in the field so text near the viewport top/bottom gets equal protection.
- **Confirmation wanted:** whether the current balance (image visible on the right / calm reading column on the left) matches the intended look, or should be dialled toward more image / more calm.
