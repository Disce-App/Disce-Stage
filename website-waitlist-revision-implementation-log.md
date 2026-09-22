# Website Waitlist Revision — WP F Implementation Log

**Document type:** Implementation record for work package **WP F — Conversion & Waitlist** (task `NEW-02`).
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Basis:** `website-revision-work-packages.md` WP F, `master-checklist-website-revision.md` §2.5 / DEF-03, `DESIGN-BRIEF.md`, `AGENTS.md` (image pipeline), and the founder's image decision: **`Greenery/1.png`**.

> This log records WP F. It does not replace the changes themselves. The master checklist and work-package documents were not modified; the owner can flip `NEW-02`/`DEF-03` to DONE on the evidence below.

---

## 1. Scope decision (recorded)

`NEW-02` asked for a waitlist redesign that "matches the visual style of the rest of the website, including its own background image." The prior planning round had left one open question: migrate the page off its self-contained stylesheet (DEF-03) or only restyle within it.

**Decision taken:** migrate `waitlist.html` into the **shared design system**. This is the only interpretation that actually satisfies "matches the visual style", and it resolves the previously flagged DEF-03 blocker as a byproduct. Every form control, consent text, FAQ, trust block, success/error state and the Airtable submission path are preserved.

---

## 2. Background image

- **Source:** `Greenery/1.png` (1122×1402, portrait), as instructed.
- **Content:** a dark green herbarium-cabinet archway opening onto a bright glasshouse, with stag hoof-prints leading through the doorway — a "threshold / next step" motif that fits the interest-registration narrative and the existing Greenery brand layer.
- **Pipeline:** copied to `images/greenery-herbarium-archway.png` (new master, `Greenery/1.png` untouched) and processed with `scripts/optimize_images.py --kind hero --widths 768,1122`. Only the width actually used is retained: `images/derived/greenery-herbarium-archway-1122.webp`. No upscaling.
- **Usage (corrected):** the image is the page's **baked-in background layer**, applied directly to `body.page-waitlist::after` at the site's standard **0.25 opacity** — the same fixed/cover layer and opacity as the homepage and other subpages. It is set on the pseudo-element (rather than through the shared `--botanical-image` custom property) because a relative URL declared in the document's inline style would otherwise be resolved against `css/experimental.min.css`, where the shared rule consumes it, producing a 404. There is **no hero band**; the page title is a plain intro on the paper background.

---

## 3. Files changed

| File | Change |
|---|---|
| `waitlist.html` | Migrated to the shared design system: links `css/experimental.min.css`; shared site header/nav/lang-switch and site footer; `js/site.js`; plain intro (no hero); scoped style block for form/error/trust/privacy/FAQ; page background set via `body.page-waitlist` |
| `images/greenery-herbarium-archway.png` | New image master (copy of `Greenery/1.png`) |
| `images/derived/greenery-herbarium-archway-1122.webp` | Generated background derivative (committed per the image pipeline) |

No change to `sitemap.xml` (the waitlist was already listed), no change to legal pages, no new routes, no new dependencies.

---

## 4. What was preserved (behaviour and content)

- **Form fields, ids, names, required/optional logic unchanged:** `first_name` (required), `email` (required), `german_level` (optional, A1–C2), `consent_contact` (required), `source_channel` (optional).
- **Validation, error summary, `aria-invalid`, `aria-describedby`, clear-on-edit** — logic unchanged.
- **Submission path unchanged:** `POST https://waitlist-proxy.bjarne-dudzus.workers.dev`; payload keys `first_name`, `email`, `consent_contact`, `language_pref`, plus optional `german_level`/`source_channel`. Airtable schema untouched.
- **Success/error states** unchanged, including feedback blocks outside the form (`role="status"`/`role="alert"`, focus on success).
- **All copy unchanged:** info block, details list, consent text, trust block, privacy summary, six FAQ Q&A, success/error messages, `mailto:` and `datenschutz.html` links. Only the B2–C2 level range (from the earlier messaging revision) is retained.
- **Accessibility:** skip link, one `<main>`, native FAQ buttons with `aria-expanded`/`aria-controls`/`hidden`, focus behaviour, reduced-motion safety.

---

## 5. Language switching

- Replaced the page's own `#langToggle` / `body.lang-en` implementation with the shared `.lang-switch` + `js/site.js` mechanism, so the waitlist now uses the same language component as every other page.
- Added `data-title-de`/`data-title-en` to `<title>` (previously the title did not switch; a known gap recorded during the accessibility audit).
- The one page-specific need — the empty first `<option>` of the level `<select>`, which cannot carry a `data-lang` span — is handled by a small script that sets it after `site.js` applies the stored language and on each language switch.
- **Fixed in passing:** the page's `og:locale` is now `de_DE` (was `en_US` on a DE-primary page), matching the rest of the site.

---

## 6. Verification performed

- **Structure:** tag-balance parser — **0 errors, 0 unclosed tags, 0 duplicate IDs, exactly one `<main>`**.
- **Required hooks present:** `#main`, `#site-nav`, `#waitlistForm`, `#formErrorSummary`, `#first_name`, `#email`, `#german_level`, `#consent_contact`, `#source_channel`, group ids, `#submitBtn`, `#spinner`, `#successMsg`, `#errorMsg`, `#faq-q1..q6`/`#faq-a1..a6`.
- **Scripts:** `node --check` passes for `js/site.js` and both inline scripts.
- **ARIA:** every `aria-describedby` and `aria-controls` target resolves.
- **Language parity:** `data-lang="de"` / `data-lang="en"` counts balanced (64/64).
- **Assets over HTTP** (local server, all `200`): `waitlist.html`, `css/experimental.min.css`, `js/site.js`, the background `greenery-herbarium-archway-1122.webp`, `images/antlers-green.png`, `fonts/newsreader-roman-var.subset.woff2`.
- **Semantic fix:** the loading spinner inside the submit `<button>` changed from `<div>` to `<span>` (a `<div>` is not valid phrasing content for a button).
- **Rendered check:** headless Firefox at 1440×900 confirms the background image renders behind the content at the intended opacity, with the shared nav and paper content column.
- Preview server stopped; ports free.

**Not verifiable without a browser:** rendered visual result, focus visibility, and the live form submission against the Cloudflare Worker/Airtable. A manual browser/mobile pass remains.

---

## 7. Remaining blockers / open questions

1. **Live form test** — submit a real test registration against the Worker/Airtable to confirm the (unchanged) payload still lands; no code path changed, but it is the one behaviour that cannot be checked statically.
2. **On-page privacy summary vs. `datenschutz.html`** — the summary says data is "nicht an Dritte weitergegeben" while the legal page names Cloudflare/Airtable processors. Left unchanged (legal copy); needs the WP A legal review (GATE-07/08/12).
3. **DEF-03** — the code migration is now done; the master checklist item can be closed.
4. **PERF-01 font dedup** — the waitlist no longer declares its own `@font-face`/Noto Serif; the shared font declaration is now the single source, so the deferred PERF-01 dedup is effectively enabled.
5. **GATE-14 indexability** — unchanged; the page remains `noindex`.

---

## 8. Recommended next step

A quick **manual browser + mobile pass** of the redesigned waitlist (hero readability, form, FAQ, DE/EN switch) and one **live test submission**, then proceed to **WP I (Team Page)**. WP A legal gates continue in parallel.
