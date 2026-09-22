# Master Checklist — DISCE Website Revision

**Document type:** Consolidated implementation checklist. Consolidates the four baseline audits, the four deep dives, the locked founder decisions, and the already-implemented containment edits. It introduces **no new decisions**.
**Date:** 2026-09-21
**Authoritative inputs (priority order):** `founder-decisions-locked.md` → `sprint-0-triage-and-sprint-1-decision-pack.md` → `sprint-2-deep-dive-target-ia.md` → `sprint-3-deep-dive-a11y-performance-evidence.md` → `sprint-4-deep-dive-conversion-trust-legal.md` → baseline `sprint-1…sprint-4` → `Pre-Launch-Website-Exhaustive-Report.md`.

## 0. How to use this checklist

**Statuses:** `DONE` = already implemented and verified (listed once, never re-implemented). `OPEN-CODE` = an implementation task with a defined target. `OPEN-FOUNDER` = a decision or input only the founder can provide. `OPEN-LEGAL` = requires legal/external review. `DEFERRED` = "only after validated interest" (benchmark §12) — do last.
**Priorities:** `BLOCKER` = must close before any public + indexable launch. `P0` = required before launch. `P1` = before active acquisition. `P2` = after initial validated signals.
**Rules:** every item traces to a source document and, where applicable, a repo `file:line`. DONE items keep their `file:line` evidence as a regression reference. Where a deep dive left an option open, it appears as an `OPEN-FOUNDER` checklist item; this document does not choose for the founder. No new claims, wording, dates, or decisions are introduced. This is not legal advice.

---

## 1. Release gates (must close before public + indexable launch)

| ID | Prio | file:line | What is missing | Type | Depends on |
|---|---|---|---|---|---|
| GATE-01 | BLOCKER | `impressum.html:79` | Imprint — ladungsfähige Anschrift (street, house number) | OPEN-FOUNDER | — |
| GATE-02 | BLOCKER | `impressum.html:80` | Imprint — PLZ, Ort | OPEN-FOUNDER | — |
| GATE-03 | BLOCKER | `impressum.html:86` | Imprint — telephone number | OPEN-FOUNDER | — |
| GATE-04 | BLOCKER | `impressum.html:102` | Imprint — MStV address line | OPEN-FOUNDER | GATE-01/02 |
| GATE-05 | BLOCKER | `impressum.html:118` | Imprint — notice date ("Stand") | OPEN-FOUNDER | — |
| GATE-06 | BLOCKER | `datenschutz.html:80–81` | Privacy — controller address/PLZ | OPEN-FOUNDER | GATE-01/02 |
| GATE-07 | BLOCKER | `datenschutz.html:90` | Privacy — third-country transfer basis (hosting) | OPEN-LEGAL | — |
| GATE-08 | BLOCKER | `datenschutz.html:102` | Privacy — transfer basis + Art. 28 DPA status (Cloudflare/Airtable) | OPEN-LEGAL | — |
| GATE-09 | BLOCKER | `datenschutz.html:103` | Privacy — retention period | OPEN-FOUNDER | — |
| GATE-10 | P0 | `datenschutz.html:125` | Privacy — notice date ("Stand") | OPEN-FOUNDER | — |
| GATE-11 | BLOCKER | `impressum.html:87`; `datenschutz.html:82,131`; `waitlist.html:733,740` (+ `beta.html:97`, `index.html:309`, `kernel.html:80,496,527`, `philosophy.html:482`, `status.html:304`, `team.html:196`) | Mailbox verification — confirm `bjarne.dudzus@disce.de` exists and is monitored before public promotion | OPEN-FOUNDER | — |
| GATE-12 | BLOCKER | `impressum.html`; `datenschutz.html` | Legal review of imprint + privacy notice (both currently marked draft) | OPEN-LEGAL | GATE-01…10 |
| GATE-13 | P2 | `waitlist.html` form; CONV-05 | Final decision on internal field name `availability_june` / Airtable column (non-public) | **SUPERSEDED** — the public availability field and all code-level dependence on `availability_june` were removed in Batch D/CONV-05 (no markup, validation, error association, or payload key remains). No Airtable column was renamed or deleted; it is simply no longer written. | — |
| GATE-14 | BLOCKER | `robots.txt`; per-page `<meta name="robots">`; `sitemap.xml`; canonical/OG in page heads | Staging→production indexability decision + execution (robots allow, remove `noindex`, align canonical/OG/sitemap) | OPEN-FOUNDER + OPEN-CODE | GATE-01…12 |
| GATE-15 | P1 | — | BFSG/accessibility applicability review (Sprint 4 §4.9.5; deep-dive §6 item 15) | OPEN-LEGAL | GATE-12 |

**Gate rule:** GATE-01…12 must close before GATE-14 (indexability). Until then the site stays in its current non-indexable staging posture (`robots.txt` `Disallow: /`; `noindex` on every page).

**GATE-13 note:** closed as **SUPERSEDED** in Batch D/CONV-05 — the availability field and every code-level reference to `availability_june` (markup, validation, error association, payload key) are gone. The Airtable column was not renamed or deleted; it is simply no longer written.

---

## 2. Consolidated implementation backlog

### 2.1 Positioning & messaging (POS)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| POS-01 | P0 | DONE | Sprint 1 §1.5/§1.8; decision pack B.1; locked #2/#5 | Reframe homepage hero eyebrow/lede to the primary professional audience and the truthful planned status; no availability claim | Hero names the primary audience/context and a planned status; no "available/now" claim | `index.html:77` eyebrow → audience ("Für internationale Fachkräfte in Deutschland" / "For international professionals in Germany"); `index.html:79` lede → career context (job interview / day-to-day work / next career step) + system framing (diagnosis, targeted practice, feedback) + truthful status ("Proof of Principle (Cervus) abgeschlossen; nächster Prototyp in Entwicklung; Private Beta geplant"). Hero primary CTA "Interesse anmelden" unchanged (`:81`). **Manual visual review + founder sign-off required** | medium | — |
| — | — | — | **Batch D note** | Supersedes the Batch A overlap note: the IA-04 hero primary-CTA change (`index.html:81` → `waitlist.html`) was reviewed in Batch D and retained; POS-01 hero eyebrow/lede framing is completed. | — | — | — | — |
| POS-02 | P0 | DONE | locked #2; Sprint 1 §1.7; `index.html:90`; `status.html:78,82` | Make status labels consistent site-wide: "Cervus research completed" / "private beta planned" / "next research phase in preparation — recruitment not open" | Grep shows no conflicting present-tense study/availability labels on public pages; `beta.html` exempt as founder-deferred | Manual + grep; founder sign-off | low | — |
| POS-03 | P1 | DONE | Sprint 1 §1.14; decision pack B.3 | Apply codename policy: gloss "Kernel" at first contact; keep "Cervus" contextual; keep Midgard/Asgard deep-page only | No unexplained public codename at first contact | `kernel.html:81` hero lede now glosses Kernel plainly ("die Systemschicht hinter dem Coaching: das System, das Diagnose, gezieltes Üben und Rückmeldung verbindet") before the technical detail; `index.html:94` stat label `Pilotphase` → `Proof of Principle` with value "Cervus — abgeschlossen" (Cervus framed as completed research, not the product); Midgard/Asgard remain only in `status.html` roadmap cards (`:173`,`:188`, deep page). Nav label "Der Kernel" is a link label; the gloss lives at its destination. **Manual visual review required** | low | POS-02 |
| POS-04 | P1 | DONE | locked #8; founder-decisions-locked.md (a)#8; decision pack B.3 | Confirm "Proof of Principle" as the public research term and keep "Proof of Visibility" out of headline/marketing positions | No "Proof of Visibility" in public copy; PoP used for Cervus | Grep + founder sign-off | low | — |
| — | — | — | **Batch A note** | POS-04 closed per founder decision #8: "Proof of Principle public; Proof of Visibility internal-only." Grep confirms "Proof of Visibility" appears only in internal `.md` documents, not in any public HTML. | — | — | — | — |

### 2.2 Information architecture (IA)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| IA-01 | P1 | DONE | target IA §1; founder correction (this pass) | Execute page dispositions: keep `kernel.html` as mechanism, reframe `status.html` as canonical status, and **keep `philosophy.html` as a regular, publicly discoverable secondary page**. The former "deep-link-only" demotion is **superseded** by founder decision. | Nav and links reflect dispositions; `philosophy.html` present in header + footer nav on every public non-deferred page; no primary path orphaned | Visual review + grep | medium | POS-02 |
| — | — | — | **Founder correction (Philosophy restored)** | Founder overrides the former IA-01 interpretation: `philosophy.html` remains a regular, publicly discoverable secondary page, visually secondary to the primary CTA "Interesse anmelden / Register interest"; it is not removed, hidden, `noindex`ed or deferred, and its content/claims/status wording are unchanged. The "Philosophie / Philosophy" link was restored in the **header nav** at `index.html:47`, `kernel.html:42`, `philosophy.html:57`, `status.html:42`, `team.html:42`, `datenschutz.html:42`, `impressum.html:42`, and in the **footer "Seiten" nav** at `index.html:295`, `kernel.html:513`, `philosophy.html:468`, `status.html:291`, `team.html:182`, `datenschutz.html:154`, `impressum.html:134`. The pre-existing contextual homepage link (`index.html:78`) is preserved. `beta.html:42,83` was already correct and is unchanged. Valid Batch-A IA-01 outcomes retained: `kernel.html` stays the mechanism page, `status.html` is the canonical status page, and no page was removed/renamed/deleted. | — | — | — | — |
| IA-02 | P2 | DONE | target IA §1, §5; `beta.html`; founder decision #2 | Decide `beta.html` role (keep deferred/unlinked, repurpose as status deep-link, or remove from scope) | Decision recorded; page stays `noindex`/unlinked until then | Founder sign-off | low | GATE-14 |
| — | — | — | **Batch A note** | Closed by founder decision #2: `beta.html` remains deferred, unlinked, `noindex`, and outside the sitemap, reserved for a future real beta. Only the CONV-01 label change was applied (`beta.html:46,95`). | — | — | — | — |
| IA-03 | P1 | DONE | Sprint 4 §7; Sprint 3 §1.8; benchmark §3/§6; `waitlist.html` FAQ | Add a small FAQ module on `waitlist.html` using the existing (unused) accordion; answer the conversion-relevant questions | Module answers the defined questions; accordion keyboard-operable; no new page created | FAQ section added after the form/privacy area, before the footer; six Q&A on the six confirmed questions only, DE/EN via `data-lang`; native `<button>` + `aria-expanded`/`aria-controls`/`hidden`; links only to `datenschutz.html` and `mailto:bjarne.dudzus@disce.de`; **manual keyboard + content review required** | low–med | A11Y-09 |
| IA-04 | P1 | DONE | target IA §2; Sprint 4 §1.4 | Enforce one funnel per intent: one homepage-primary route (professionals), secondary intents by direct email | No competing primary CTAs on the homepage | Visual review | low | CONV-01 |
| — | — | — | **Batch A note** | Homepage hero primary CTA changed from `team.html` to `waitlist.html` with the interest-registration label (`index.html:77`), so the single lead-capture route is interest registration; team/about and partner/investor contexts remain as secondary nav/footer/mailto routes. | — | — | — | — |
| IA-05 | P1 | DONE | locked #7; target IA §5; `index.html:308` | Place the Substack development-updates link as a clearly labeled **external** deep link in Status/About/Contact, not as a homepage-primary CTA | Link present in Status/Contact; not a primary CTA; no consent mechanism added | Visual review | low | — |
| — | — | — | **Batch A note** | Verified founder-provided URL `https://disce.substack.com` exists in the repo. Added a clearly labeled external development-updates link in the canonical Status page (`status.html:277`: "Entwicklungs-Updates (Substack, extern)" / "development updates (Substack, external)"), `target="_blank" rel="noopener"`, not a primary CTA. Existing footer "Substack" links left unchanged (secondary). No subscription form or consent mechanism added. | — | — | — | — |
| IA-06 | P1 | OPEN-CODE | target IA §4; `sitemap.xml` | Update `sitemap.xml` to the real public set (include `kernel.html`, `status.html`, `waitlist.html`; exclude `beta.html` while deferred) | Sitemap matches the indexable public set | Manual check | low | GATE-14 |

### 2.3 Accessibility (A11Y)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| A11Y-01 | P0 | DONE | Sprint 3 §1.1; `waitlist.html` form | Add `aria-invalid` + `aria-describedby` linking fields to their `.form-error` elements; `role="alert"`/live region for the error summary | Screen reader announces each error tied to its field; axe reports no unassociated error | Structural (all `aria-describedby` IDs resolve; no duplicate IDs) + `node --check` of inline script + source review of invalid/clear paths passed; **keyboard + screen-reader test required** | medium | — |
| A11Y-02 | P0 | DONE | Sprint 3 §1.2; Sprint 4 §2.2; `waitlist.html` success state | Make `#successMsg` an `aria-live`/`role="status"` region and move focus to it after submit | Confirmation announced without navigation; no duplicate announcement | `#successMsg` now `role="status" tabindex="-1"`; **required a prerequisite structural fix** (feedback block moved outside `<form>`, which is hidden on success); source review passed; **screen-reader test required** | low | — |
| A11Y-03 | P1 | DONE | Sprint 3 §1.3; `waitlist.html` submit flow | Mirror the existing disabled/loading toggle with `aria-busy`; keep spinner decorative | Assistive tech exposes busy state; visible behavior unchanged | `aria-busy` set `false` at submit start, `true` while pending, `false` on success + API failure; spinner `aria-hidden="true"`; source review passed; **screen-reader test required** | low | — |
| A11Y-04 | P0 | DONE | Sprint 3 §1.4; all public pages | Wrap primary content of every page in one `<main>` landmark | Exactly one `<main>` per page; landmark navigation works | Structural: exactly one `<main id="main" tabindex="-1">` per page (9/9), header/main/footer order verified; **landmark SR test required** | low | — |
| A11Y-05 | P1 | DONE | Sprint 3 §1.5 | Add a visually-hidden-until-focused skip-to-content link targeting `<main>` | Tab on load reveals skip link; it moves focus to main content | Skip link is first focusable element after `<body>` on 9/9 pages, targets existing `#main`, bilingual DE/EN; CSS `.skip-link` + `main:focus`; **keyboard/visual-focus test required** | low | A11Y-04 |
| A11Y-06 | P0 | DONE | Sprint 3 §1.6; `css/experimental.css` ticker; `index.html` ticker; `js/site.js` | Add a keyboard-operable pause/stop control for the ticker, or make the logos a static row (content unchanged per locked #4) | Motion can be stopped or is absent; partner content unchanged; WCAG 2.2.2 met | **Option A (pause/resume)** implemented; native `<button>` with `aria-pressed` + DE/EN state label; `animation-play-state: paused`; reduced motion keeps `animation: none` and hides the control; partner markup/logos unchanged; **manual keyboard + reduced-motion test required** | low | — |
| A11Y-07 | P1 | DONE | Sprint 3 §1.10 | Verify heading order and `<title>`/OG alignment per page | No skipped heading levels; title/OG match page role | Within-main skips fixed (`team.html` founder `h3`→`h2`; `philosophy.html` TOC `h4`→`h2`) and site-wide footer column headings `h4`→`h2`; now strictly `h1→h2→h3` on all editable pages. Title/OG audited — 2 factual mismatches reported (not edited). `beta.html` heading `h4`s left unchanged (out of scope). **Visual check of heading styling required** | low | POS-02 |
| A11Y-08 | P1 | MEASURE-ONLY | Sprint 3 §1.13; benchmark §5 | Measure tap-target sizes and reflow at 320–430 px; fix only if a target is <24×24 or overflow occurs | No target <24×24; no horizontal scroll | **Measured** (headless Firefox 156 / WebDriver BiDi, localhost, 2026-09-21) at 320/375/430 px: index, waitlist, kernel, status, team = **0 px horizontal overflow**; **philosophy.html @320 px = 3 px overflow** (`.eyebrow` span; originally outside the Batch E permitted file set → corrected in the post-Batch-E reflow fix, see note). All undersized controls on index/waitlist pass the WCAG 2.5.8 **spacing exception** (0 without exception at every width). Retained MEASURE-ONLY. | low–med | CONV-01 |
| — | — | — | **A11Y-08 fix note (post-Batch-E reflow correction)** | **Root cause:** the `philosophy.html` hero eyebrow "Unternehmensphilosophie" is an `inline-flex` (7 px diamond + 40 px gap + one long unbreakable uppercase word ≈ 223 px); its min-content width (≈ 279 px) exceeded the `.wrap` content box (≈ 244 px) at 320 px, and `.page-hero--art` sets `overflow: visible`, so it added **3 px** to document scroll width. **Fix** (`css/experimental.css`, `.eyebrow`): added `max-width: 100%` and `overflow-wrap: anywhere` — a narrow, reusable guard; no content hidden/truncated/removed, no fixed widths, no copy/design change; wrapping only occurs when the label would otherwise exceed the container. **Re-measured** (headless Firefox 156 / BiDi, localhost, fresh profile, cache-busted, 2026-09-21): philosophy @320 **docSW 308 ≤ innerWidth 320, overflow 0** (eyebrow wraps to two lines, right edge 276, fully visible); philosophy @375 and @430 overflow 0; index/waitlist @320 overflow 0; all six public pages @320/375/430 overflow 0 (no regression). **Remaining manual check:** human mobile legibility of the two-line eyebrow at 320 px. | — | — | — | — |
| A11Y-09 | P1 | DONE | Sprint 3 §1.8; `js/site.js`; `css/experimental.css` | Dispose of the dead accordion: repurpose for IA-03 or remove | No unused code (or clearly documented as reserved) | **Replaced/removed** — dead `.accordion-*` JS (`js/site.js:54–76`) and CSS (`css/experimental.css:1670–1682`) removed; one new accessible FAQ accordion implemented in `waitlist.html`; `grep` confirms no `.accordion-*` remnants remain; code review done | low | IA-03 |
| A11Y-10 | P1 | DONE | Sprint 3 §1.9; `js/generative/registry.js` | Remove the dangling `kernel-loop` registry entry (or add the module if intended) | All registry keys resolve; no failed import | Stale `kernel-loop` entry removed; registry now resolves to existing `section-motif` + `dot-field` modules; page mounts use only `data-gen="dot-field"`; `node --check` passed; no-JS/reduced-motion untouched | low | — |

### 2.4 Performance (PERF)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| PERF-01 | P1 | DONE | Sprint 3 §1.7; `css/experimental.css:13`; `waitlist.html` | Add font `rel="preload"` for above-the-fold faces; dedup the duplicate `@font-face` declarations (without breaking the self-contained waitlist page) | No external font request; identical rendering; preload paths resolve | Preload added for the above-the-fold **headline** face only: `index.html:14` → `fonts/newsreader-roman-var.woff2` (matches `css/experimental.css:41`); `waitlist.html:16` → `fonts/noto-serif-var.woff2` (matches the inline `@font-face` at `:49`). Resource-timing check (BiDi) shows exactly **one** entry per face → no duplicate request; fonts stay self-hosted; `font-display: swap` and rendering unchanged. Declaration **dedup deferred** — coupled to DEF-03 (waitlist remains self-contained). No runtime LCP improvement was measured. | low–med | DEF-03 |
| PERF-02 | P1 | DONE | Sprint 3 §3; benchmark §5 | Measure LCP ≤ 2.5 s and CLS ≤ 0.1 (lab) | Report recorded; no claim without measurement | **Measured** (headless Firefox 156 / BiDi, local `python3 -m http.server` on `http://127.0.0.1:8300`, 2026-09-21; viewports 1280×900 and 375×812): index LCP 74 ms / 39 ms, waitlist LCP 59 ms / 22 ms; CLS 0 at both viewports for both pages. Both under the 2.5 s / 0.1 thresholds. **Limitation:** localhost + warm cache + no CPU/network throttling → not a production guarantee; re-measure with throttled Lighthouse/PageSpeed before launch. | low | GATE-14 |
| — | — | — | **Hero Performance Pass 1 (PageSpeed-driven, 2026-09-21)** | Deployed PSI established the hero `<img>` as the LCP element (≈240 ms resource load delay + ≈240 ms download + ≈80 ms render delay; ~670 KiB image-delivery savings) with oversized decorative assets. Implemented: (1) **one responsive AVIF hero preload** (`index.html:19–21`) mirroring the hero AVIF `<source>` exactly — cold-cache check: exactly one hero request at 320/375/390/430/1440 px, AVIF only, no WebP/PNG fallback fetch; (2) **partner logos** `loading="lazy" decoding="async"` + intrinsic `width`/`height` (`index.html:299–301`); (3) **decorative assets modernized** via the existing approved pipeline (`images/derived/goethe-{360,720}`, `wittgenstein-{360,720}`, `antlers-green-{28,56}`, AVIF+WebP, alpha preserved, masters untouched) wired via `<picture>` (`index.html:47–56`, `:62–66`) with one layout-preserving rule (`css/experimental.css:252`). Local cold 390 px eager image bytes **1,007,989 → 106,480** (≈ −880 KiB); partner logos no longer fetched before scroll. **Deployed LCP target not claimed** (local Firefox BiDi only). Detail: `hero-performance-diagnostic.md`. **Follow-up: re-run PageSpeed Insights on the deployed site after this commit before considering R5/R7/R8 or CSS/font architecture changes.** | — | — | — | — |
| PERF-03 | P1 | MEASURE-ONLY | Sprint 3 §3; benchmark §5 | Measure INP ≤ 200 ms (field once traffic exists) | Report recorded | **Retained MEASURE-ONLY.** Repository contains no `web-vitals`/field-measurement setup (grep for `web-vitals`/`gtag`/analytics code: none). **"Field data unavailable; evaluate only after public traffic exists."** INP ≤ 200 ms kept as a future validation target, not a present claim. No measurement script added (out of scope). | low | GATE-14 |
| PERF-04 | P1 | MEASURE-ONLY | Sprint 3 §3; benchmark §5 | Measure AA contrast on hero/dark bands/form/footer | 4.5:1 normal, 3:1 large | **Partial measurement** (live `getComputedStyle` + WCAG contrast formula, headless Firefox 156, 1280×900; 25 sampled pairings): all pass — lowest 6.44:1 (ticker label), form/trust/FAQ ≥ 10:1, hero h1 7.74:1, CTA 16.32:1, footer links 16.32:1, skip link 17.35:1. **Caveat:** backgrounds are computed-style ancestor colours, not pixel-sampled over the photographic hero; no dedicated contrast-checker tool exists locally → retained MEASURE-ONLY pending visual/pixel and focus-state confirmation. Manual procedure in §2.13. | low | — |
| PERF-05 | P1 | MEASURE-ONLY | Sprint 3 §3 | Run full keyboard-path measurement (nav, language switch, form, success/error) | All paths operable | **Partial rendered test** (headless Firefox 156 / BiDi `input.performActions`): first Tab focuses `.skip-link`, which becomes visible (settled transform none, top 8 px, height 46 px) on index/waitlist/philosophy; index order skip → brand → nav; waitlist order skip → language toggle → back-link → first_name. Full invalid/corrected/success/API-failure journey and a screen-reader pass were **not** run → retained MEASURE-ONLY until the founder confirms the manual sequence in §2.13. | low | A11Y-01…05 |
| PERF-06 | P1 | DONE | Sprint 3 §3 | Mobile viewport checks (320–430 px; hero/form/CTA readable) | No overflow; CTA obvious | **Measured** (headless Firefox 156 / BiDi, localhost, 2026-09-21) at 320/375/430 px for index + waitlist: **0 px horizontal overflow**; hero h1, primary CTA, ticker toggle, form label, trust block and FAQ trigger all present and within the viewport with sane font sizes (index h1 36 px / CTA 57 px tall / ticker toggle 35 px tall; waitlist h1 28 px / CTA 48 px tall / FAQ trigger 52 px tall). **Residual:** human legibility/visual check not performed. | low | CONV-01 |

### 2.5 Conversion (CONV)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| CONV-01 | P0 | DONE | Sprint 4 §1.2; locked #1/#2. Full list: `index.html:51,260,307`; `beta.html:46,95`; `datenschutz.html:46,166`; `impressum.html:46,146`; `kernel.html:46,525`; `philosophy.html:61,480`; `status.html:46,276,302`; `team.html:46,194` | Replace generic CTA labels with the recommended set: primary "Interesse anmelden / Register interest"; secondary variant "Interesse anmelden – Private Beta / Register interest – private beta" | Every listed CTA uses the label set; no "Auf die Warteliste/Join the Waitlist" remains | Grep + visual review | low–med | — |
| — | — | — | **Batch A closure note** | Applied on all eight pages. Final state: `index.html:50,259,306`; `beta.html:46,95`; `kernel.html:45,524`; `philosophy.html:60,479`; `status.html:45,275,302`; `team.html:45,193`; `datenschutz.html:46,166`; `impressum.html:46,146` all read "Interesse anmelden / Register interest". Grep for "Auf die Warteliste" / "Join the Waitlist" returns **zero HTML hits** (remaining occurrences are internal `.md` documents only). | — | — | — | — |
| CONV-02 | P0 | DONE | Sprint 4 §1.3; `index.html:256–257` | Replace "join the beta"/"first cohort" with target interest-registration wording (no cohort/access implication) | No cohort/access/availability implication in band | Founder sign-off + manual review | low | — |
| — | — | — | **Batch A note** | `index.html:255–256` now reads "Die Entwicklung verfolgen oder Interesse anmelden." / "…melden Sie unverbindlich Ihr Interesse an der geplanten Private Beta an." No cohort/access/date/response implication remains. | — | — | — | — |
| CONV-03 | P0 | DONE | Sprint 4 §2.2; Sprint 3 §1.2; `waitlist.html` success state | Complete thank-you state: accessible confirmation (A11Y-02), privacy deep link to `datenschutz.html`, correction/withdrawal note | Confirmation announced; privacy linked; withdrawal stated | `waitlist.html:745–746` success text now confirms receipt, restates the honest expectation (contact only when the planned beta/next research phase opens), states no queue position / automatic invitation / access guarantee / fixed date, links `datenschutz.html`, and gives the `mailto:bjarne.dudzus@disce.de` correction/withdrawal path. Batch-B mechanics preserved (`role="status" tabindex="-1"`, focus on success); `.submit-feedback a` styled (`:392`); no response-time target shown. **Manual screen-reader + link check required** | low | A11Y-02 |
| CONV-04 | P1 | OPEN-FOUNDER | Sprint 4 §2.3; locked #1; founder decision #3 | Finalize the follow-up runbook (who/trigger/medium/no-trigger message) | Runbook documented; mailbox confirmed | Founder sign-off | low | GATE-11 |
| — | — | — | **Founder decision (Batch A, later Batch D)** | Owner: Bjarne Dudzus. Trigger: a valid interest-registration submission. Internal service target: review/respond within five business days — **internal only, never displayed as a public response-time guarantee**. Medium: `bjarne.dudzus@disce.de`. Initial response: acknowledgement, honest status, no access promise, optional one relevant follow-up question. Spam/irrelevant may receive none/short neutral reply. List usable for narrowly related beta/next-study status communication (incl. delay notices), **not** a general newsletter; any future Substack/newsletter opt-in must be separate, voluntary, unchecked, distinct purpose, and legally reviewed. **Not implemented in Batch A; remains OPEN-FOUNDER for Batch D.** | — | — | — | — |
| — | — | — | **Batch D evidence note** | Operational follow-up runbook recorded here: owner Bjarne Dudzus; trigger a valid interest-registration submission; internal target review/respond within five business days (**internal only, never published**); medium `bjarne.dudzus@disce.de`; initial reply = acknowledgement + honest status + no access promise, optionally one relevant follow-up question; spam/irrelevant = none or short neutral reply; narrowly related beta/research status updates (incl. delay notices) permitted; **no** general-newsletter scope. Status deliberately left **OPEN-FOUNDER**: mailbox verification (GATE-11) and founder sign-off remain, and CONV-04 is outside Batch D scope. | — | — | — | — |
| CONV-05 | P0 | DONE | Sprint 4 §3; founder decision #4 | Form data minimization: drop/defer availability + microphone fields; simplify level; defer role/career data; adjust JS validation accordingly | Form fields reflect the decision; validation still blocks invalid submits | Removed the availability group and the microphone checkbox; `german_level` is now optional (no required star, no `aria-describedby`, no error element); the optional free-text `source_channel` input is relabelled "Kontext, Interesse oder Fragen" (same `name`/Airtable column); validation requires `first_name`, `email`, `consent_contact` only; payload no longer carries `availability_june`/`has_microphone` and sends `german_level`/`source_channel` only when provided; adjacent privacy summary (`waitlist.html:814` DE / `:821` EN) and `datenschutz.html:102` DE / `:138` EN updated; dead `.availability-grid` CSS removed. **Manual form test + founder sign-off required** | medium | — |
| — | — | — | **Founder decision (Batch A, later Batch D)** | Keep name + email; remove/defer availability field; remove/defer microphone field; keep language level only as a simplified, low-friction **optional** field; defer role/career/detailed qualification to a later actual beta invitation/application; keep free text optional. Once availability is removed in Batch D, **GATE-13 becomes obsolete/superseded**. **Not implemented in Batch A** (no form/JS/Airtable changes); remains OPEN-FOUNDER for Batch D. | — | — | — | — |
| — | — | — | **Batch D evidence note** | Implemented in Batch D/CONV-05. Kept: name, email, optional German level, optional free-text context. Removed/deferred: availability, microphone, and any study-scheduling/qualification/segmentation field. Airtable schema untouched (no column renamed or deleted); removed fields are simply no longer written. | — | — | — | — |
| CONV-06 | P2 | DEFERRED | Sprint 4 §4/§7; benchmark §7 | Introduce privacy-friendly, low-traffic measurement only after validated interest (no trackers now) | Measurement introduced with consent-free config | Post-launch review | medium | GATE-14 |

### 2.6 Trust & evidence (TRUST)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| TRUST-01 | P0 | DONE | Sprint 4 §5; target IA §5; `waitlist.html` form | Add a compact trust/status block near the form: status, data-use summary, privacy deep link, contact, completed-Cervus context | Block present; privacy linked; no security/availability overclaim | `waitlist.html:753–770` compact `.trust-block` added inside the form card, below the form: status (Cervus complete as Proof of Principle; next prototype in development; private beta planned), interest clarity (no queue position / fixed access date / access guarantee), data-use summary, `datenschutz.html` link, and `mailto:bjarne.dudzus@disce.de` contact/withdrawal. No security/availability claim; no new CTA. Styled subordinate (`.trust-block` `:420–431`). **Manual content + keyboard review required** | low–med | CONV-03 |
| TRUST-02 | P1 | DONE | Sprint 3 §2; founder decision #5; Batch E founder decision | Decide the product-evidence strategy: raise the Kernel architecture plate as labeled evidence and/or supply a real prototype artifact / anonymized output | Decision recorded; artifacts supplied (if any) | **Decision recorded (Batch E):** "Current evidence strategy: retain existing Kernel conceptual architecture; no additional public artifact is approved at this stage." No prototype screenshot, testimonial, anonymized Cervus output, evidence card or visual proof module is to be added; a future stable prototype screenshot may be considered only when a real, truthful, reviewable artifact exists; nothing may imply live access, public availability, validated efficacy, product readiness, or active beta participation. | low | — |
| — | — | — | **Founder decision (Batch A, confirmed Batch E)** | Retained: no new public product artifact at this stage; existing Kernel architecture communication remains the current conceptual mechanism representation; no testimonial approved; prototype screenshots only later when a stable, truthful artifact exists and is labeled "prototype in development"; no evidence asset may imply current access, public availability, validated efficacy, or product readiness. Confirmed as the Batch E evidence decision. | — | — | — | — |
| TRUST-03 | P1 | DEFERRED | Sprint 3 §2; target IA §3; `kernel.html:142–220,217–219`; founder decision #5 | Implement the chosen evidence placement (e.g., label the existing architecture plate as a figure with its textual equivalent) | Evidence artifact visible and truthful; no availability implication | **Deferred by the Batch E founder decision: no new public evidence placement.** `kernel.html` copy, product claims and visual evidence layout left unchanged. Reopens only when a stable, truthful founder-supplied artifact exists (with TRUST-02). | medium | TRUST-02 |
| TRUST-04 | P1 | DONE | Sprint 4 §4; `waitlist.html` consent/purpose surfaces | Final check that the single-purpose contact consent still suffices (no new scopes; no consent manager) | Consent text matches purpose; no new consent mechanism | Source-level consistency audit passed: the sole required consent (`waitlist.html:701–704`) is limited to being contacted when the planned private beta / next research phase opens, states no fixed commitment and no queue position; the trust block, success message, FAQ, privacy summary and `datenschutz.html:104` purpose all describe the same interest-registration purpose; **no** newsletter/marketing scope, recruitment claim, access/scheduling/selection promise, or consent manager was added. See the OPEN-LEGAL note below | low | GATE-12 |
| — | — | — | **OPEN-LEGAL (TRUST-04)** | This item confirms source-level consistency only and does **not** close legal review. Final legal review of the consent/privacy wording (GATE-12) and mailbox verification (GATE-11) remain open and are not resolved in code. | — | — | — | — |
| TRUST-05 | P2 | OPEN-CODE | Sprint 4 §8 | Use the claim register as a pre-publish verification reference | Each public claim type checked against its evidence pointer | Manual check | low | — |

### 2.7 Legal (LEGAL)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| LEGAL-01 | P1 | OPEN-LEGAL | Sprint 4 §6 item 15 | BFSG/accessibility applicability review | Review recorded | Legal/external review | low | GATE-12 |

### 2.8 Deferred — only after validated interest (DEFERRED)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| DEF-01 | P2 | DEFERRED | Sprint 2 §2.3; Sprint 4 §4.8 | Standalone security / AI-transparency page (substance already in `kernel.html:445–474`, `philosophy.html:264–269`) | Page created only after validated interest | Post-launch review | medium | — |
| DEF-02 | P2 | DEFERRED | Sprint 2 §2.3 | Use-case pages / role-specific landing pages | Created only after validated interest | Post-launch review | medium | — |
| DEF-03 | P2 | DEFERRED | Sprint 3 §1.7/§1.11; `waitlist.html:28–46` | Migrate `waitlist.html` to the shared design system (fonts/header/footer) — enables PERF-01 dedup | Rendering matches shared system; form behavior unchanged | Visual diff | medium–high | — |

---

## 2.9 Batch A execution log (before → after)

Batch A = CONV-01, CONV-02, POS-02, IA-01, IA-04, IA-05. All edits are German public copy matching the existing tone; English mirrors preserved. No design-system/layout/JS/form/consent/robots/sitemap/canonical changes.

| Item | file:line | Before | After |
|---|---|---|---|
| CONV-01 | `index.html:51,260,307` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 | `beta.html:46,95` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 | `kernel.html:46,525` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 | `philosophy.html:61,480` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 | `status.html:46,276,302` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 | `team.html:46,194` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` |
| CONV-01 (closure) | `datenschutz.html:46,166`; `impressum.html:46,146` | `Auf die Warteliste` / `Join the Waitlist` | `Interesse anmelden` / `Register interest` (nav + footer chrome only; no legal content touched) |
| CONV-02 | `index.html:255–256` | `Die Entwicklung verfolgen oder Teil der Beta werden.` / `…trägt Sie in die Warteliste ein, um zur ersten Kohorte zu gehören.` | `Die Entwicklung verfolgen oder Interesse anmelden.` / `…melden Sie unverbindlich Ihr Interesse an der geplanten Private Beta an.` (EN mirrored) |
| POS-02 | `index.html:90` | stat value `Abgeschlossen, Auswertung läuft` / `Completed, evaluation ongoing` (label `Pilotphase`) | stat value `Cervus — abgeschlossen` / `Cervus — completed` (label `Pilotphase` unchanged) |
| IA-01 | `index.html:47`, `kernel.html:42`, `philosophy.html:57`, `status.html:42`, `team.html:42` | `<a href="philosophy.html">…Philosophie…</a>` in header nav | removed in Batch A; **restored** by founder correction (see §2.9 founder correction) |
| IA-01 (closure) | `datenschutz.html:42`, `impressum.html:42` | `<a href="philosophy.html">…Philosophie…</a>` in header nav | removed in Batch A; **restored** by founder correction |
| IA-01 (closure) | footer nav on `index`, `kernel`, `philosophy`, `status`, `team`, `datenschutz`, `impressum` | `<a href="philosophy.html">…Philosophie…</a>` in footer | removed in Batch A; **restored** by founder correction |
| IA-01 (founder correction) | header + footer nav on `index`, `kernel`, `philosophy`, `status`, `team`, `datenschutz`, `impressum` | (Philosophy link absent) | `<a href="philosophy.html">Philosophie / Philosophy</a>` restored in both header and footer; `beta.html` unchanged |
| status lede | `status.html:274` | `Tragen Sie sich in die Warteliste ein, um direkt informiert zu werden.` / `Join the waitlist to be notified directly.` | `Melden Sie unverbindlich Ihr Interesse an – wir informieren Sie, sobald die geplante Private Beta startet.` / `Register your interest – we will inform you when the planned private beta starts.` |
| IA-04 | `index.html:77` | hero primary `<a href="team.html" class="btn-primary">Das Team</a>` | hero primary `<a href="waitlist.html" class="btn-primary">Interesse anmelden</a>` |
| IA-05 | `status.html:277` | (none) | added external link: `Entwicklungs-Updates erscheinen außerdem im externen Substack-Kanal: <a href="https://disce.substack.com" target="_blank" rel="noopener">Entwicklungs-Updates (Substack, extern)</a>` (EN mirrored) |
| POS-04 | (no code) | — | closed per founder decision #8 |

**Batch A verification (grep):** `Auf die Warteliste` / `Join the Waitlist` — **zero HTML hits** after the closure pass (remaining occurrences are internal `.md` documents only). `first cohort` / `erste Kohorte` / `earliest cohort` / `join the beta` — none. `Proof of Visibility` — internal `.md` documents only, not public HTML. `Geschlossene Beta` / `Prototyp in Arbeit` remain only in `beta.html:7,21,28,67,68` (founder-deferred page; intentionally preserved). Philosophy **deep-link-only demotion superseded** by founder correction: the "Philosophie / Philosophy" link is now present in **both header and footer nav** on `index.html`, `kernel.html`, `philosophy.html`, `status.html`, `team.html`, `datenschutz.html`, `impressum.html`, alongside the preserved contextual homepage link (`index.html:78`). `beta.html:42,83` was already correct and is unchanged.

**Pending manual verification (before Batch B):** a rendered **visual/mobile review** (homepage hero and primary CTA, homepage status/band copy, nav/footer CTA labels, `status.html`, `kernel.html`, `philosophy.html`, `beta.html`, and at least one mobile viewport) has **not** been performed — the agent has no browser. Markup/structure and anchor-balance checks were run instead. This review must be completed manually before Batch B begins.

---

## 2.10 Batch B execution log (before → after)

Batch B = A11Y-01, A11Y-02, A11Y-03, A11Y-04, A11Y-05, A11Y-06, A11Y-07, A11Y-10. Batch A routing, CTA labels, status wording, terminology and page dispositions are preserved. No third-party code, trackers, frameworks, build step or new pages. `beta.html` was touched only for `<main>` and skip-link scaffolding.

### 2.10.1 Waitlist form — A11Y-01 / A11Y-02 / A11Y-03

| Item | file:line | Before → After |
|---|---|---|
| A11Y-01 | `waitlist.html:590` | *(no summary)* → `<div id="formErrorSummary" role="alert" tabindex="-1">` at top of form |
| A11Y-01 | `waitlist.html:604,606` | first name: *(unassociated)* → `aria-describedby="first_name-error"`; error `<div id="first_name-error">` |
| A11Y-01 | `waitlist.html:621,623` | email: → `aria-describedby="email-error"`; `<div id="email-error">` |
| A11Y-01 | `waitlist.html:636,647` | level: → `aria-describedby="german_level-error"`; `<div id="german_level-error">` |
| A11Y-01 | `waitlist.html:662,669,676,683,690` | availability: → `aria-describedby="availability_june-error"` on all four checkboxes; `<div id="availability_june-error">` |
| A11Y-01 | `waitlist.html:716` | required pair uses existing `id="checkbox-error"`; both checkboxes now `aria-describedby="checkbox-error"` |
| A11Y-01 | `waitlist.html:826–890,960–978` | JS: `setError()` toggles `aria-invalid` per control; invalid submit shows + focuses the summary; the edit handler removes `aria-invalid` and retires the summary once no error group remains |
| A11Y-02 | `waitlist.html:752` | `<div id="successMsg">` → `role="status" tabindex="-1"`; success path moves focus to it (`:948`) |
| A11Y-02 | `waitlist.html:747–759` | **prerequisite fix:** feedback block moved outside `<form>`. The form is `display:none`d on success, so a confirmation nested inside it could never be shown, read, or focused |
| A11Y-02 | `waitlist.html:756` | `#errorMsg` → `role="alert"` |
| A11Y-03 | `waitlist.html:740` | spinner → `aria-hidden="true"` (decorative) |
| A11Y-03 | `waitlist.html:846,910,947,954` | `aria-busy="false"` at submit start, `"true"` while pending, `"false"` on success and on API failure |

### 2.10.2 Landmarks + skip link — A11Y-04 / A11Y-05

- `<main id="main" tabindex="-1">` added to every public page (`index`, `kernel`, `philosophy`, `status`, `team`, `datenschutz`, `impressum`, `beta`); `waitlist.html`'s existing `<main>` was given the id and `tabindex`.
- Skip link `<a class="skip-link" href="#main">Zum Inhalt springen / Skip to content</a>` added as the first focusable element after `<body>` on all nine pages.
- `css/experimental.css`: new `.skip-link` rule (hidden until focus via `translateY(-200%)`; ink chip, green border, parchment focus outline) plus `main:focus { outline: none; }`.
- `waitlist.html`: equivalent inline `.skip-link` / `main:focus` rules using its local tokens (it does not link the shared stylesheet).

### 2.10.3 Ticker — A11Y-06 (approach A: pause/resume control)

**Approach A chosen.** Reason: it removes the WCAG 2.2.2 failure with the smallest robust change, preserves the partner/ecosystem visual block and logo ordering exactly (locked #4), and avoids the layout churn of converting the duplicated track into a static row. Reduced-motion users already receive `animation: none`, and the control is hidden in that case so there is nothing to operate.

| Item | file:line | Before → After |
|---|---|---|
| A11Y-06 | `index.html:287–290` | *(no control)* → native `<button id="tickerToggle" aria-pressed="false">` inside `.ticker-section`, bilingual pause/play label |
| A11Y-06 | `css/experimental.css:1729–1753` | added `.ticker-toggle`, `.is-paused` label swap, `.ticker-section.is-paused .ticker-track { animation-play-state: paused; }`; the existing reduced-motion block now also hides the control |
| A11Y-06 | `js/site.js:42–53` | added click handler toggling `.is-paused` and `aria-pressed` |

### 2.10.4 Headings / titles / OG — A11Y-07 (audit report)

Audited pages: `index`, `kernel`, `philosophy`, `status`, `team`, `datenschutz`, `impressum`, `beta`, `waitlist`.

**Edits (mechanical heading-level fixes only):**

| Page | Before → After |
|---|---|
| `team.html:76,85,94,103,112,120` | six founder/seat headings `h3` → `h2` (removed `h1→h3` skip) |
| `philosophy.html:111` | TOC "Inhalt / Contents" `h4` → `h2` (removed `h1→h4` skip) |
| `index/kernel/philosophy/status/team/datenschutz/impressum` footer | column headings `h4` → `h2` (removed `h2→h4` skips) |
| `css/experimental.css` | `.team-card h2,.team-card h3`, `.philosophy-toc h2,.philosophy-toc h4`, `.footer-col h2,.footer-col h4` — selectors widened so computed styling is unchanged |

Result: `h1→h2→h3` strictly sequential on all editable pages.

**Reported, not edited (would need messaging/translation or touch OG/locked content):**
1. `waitlist.html:16–17` sets `og:locale="en_US"` with `og:locale:alternate="de_DE"`, while the site and the page copy are DE-primary (every other page uses `de_DE`/`en_US`). OG content is outside Batch B scope.
2. `datenschutz.html:8`, `impressum.html:8`, `waitlist.html:7`: `<title>` carries no `data-title-de`/`data-title-en` pair, so the shared `site.js` language switch does not update the tab title on those pages. Fixing needs new English title copy.
3. `beta.html:81,89,94`: footer column headings remain `h4` with no preceding `h3`; `beta.html` content/structure is out of scope for Batch B (main/skip-link only).

No title/OG mismatch caused by Batch A was found.

### 2.10.5 Registry — A11Y-10

| Item | file:line | Before → After |
|---|---|---|
| A11Y-10 | `js/generative/registry.js:4` | `'kernel-loop': () => import('./kernel-loop/index.js')` removed (no such module; no page mounts it). Registry now resolves to `section-motif` + `dot-field`, both present |

### 2.10.6 Batch B verification

Structural: exactly one `<main>` (and one `id="main"`) per public page (9/9); every skip link targets an existing `#main`; ticker control present and reachable; all `aria-describedby` IDs resolve; no duplicate IDs on any page; registry keys all resolve to existing modules; anchor balance OK on 9/9.

Source-level: waitlist invalid/clear paths reviewed (`aria-invalid` set then removed), busy state cleared on all four outcomes, success path clears busy then shows + focuses `#successMsg`; `node --check` passed for `js/site.js`, `js/generative/registry.js` and the extracted inline waitlist script.

**Manual verification still required (cannot be performed here):** keyboard traversal (skip link, ticker control, form); one screen-reader pass (error summary + field association, success announcement, busy state); visual focus/skip-link review; ticker pause control review; form invalid/success/failure/retry paths; mobile viewport check; confirmation that heading re-tagging did not shift rendered typography.

---

## 2.11 Batch C execution log (before → after)

Batch C = IA-03, A11Y-09. Batch A/B preserved. Files touched: `waitlist.html`, `js/site.js`, `css/experimental.css`, and this checklist only.

### Decision: option B — replaced/removed, not repurposed

The repo's only accordion was the dead `.accordion-*` code, mounted by no markup. Repurposing it would not have been a small change: it had **no** `aria-expanded`/`aria-controls`/ids/`hidden`; it used a single-open model; it animated `max-height` via inline styles; its collapsed panels (`max-height:0; overflow:hidden`) left links keyboard-focusable; and its styles lived only in `css/experimental.css`, which `waitlist.html` does not load. So the dead JS + CSS were removed and one small accessible FAQ accordion was implemented in `waitlist.html` (inline JS + CSS, matching that page's self-contained pattern). **Exactly one accordion implementation remains.**

### Edits

| Item | file:line | Before → After |
|---|---|---|
| A11Y-09 | `js/site.js:54–76` | dead `.accordion-trigger` handler (single-open, `max-height`, no ARIA) → removed |
| A11Y-09 | `css/experimental.css:1670–1682` | dead `FAQ / ACCORDION` block (`.accordion-item`, `.accordion-trigger`, `.plus`, `.accordion-panel`, `.accordion-panel-inner`) → removed |
| IA-03 | `waitlist.html:427–463` | *(none)* → inline `.faq-section` / `.faq-list` / `.faq-item` / `.faq-question` / `.faq-trigger` / `.faq-icon` / `.faq-panel` styles |
| IA-03 | `waitlist.html:832–942` | *(none)* → FAQ `<section class="faq-section" aria-labelledby="faq-title">` placed after the form + privacy area, before `</main>`/footer; `<h2 id="faq-title">`; six `<h3 class="faq-question"><button type="button" class="faq-trigger" aria-expanded="false" aria-controls="faq-aN">` + six `<div class="faq-panel" id="faq-aN" role="region" aria-labelledby="faq-qN" hidden>` |
| IA-03 | `waitlist.html:1130–1141` | *(none)* → inline accordion JS toggling `aria-expanded` and the panel's `hidden` state |

### Copy (the six confirmed questions only)

| # | DE / EN question | Answer content |
|---|---|---|
| 1 | Ist Disce schon nutzbar? / Is Disce available to use yet? | No; next product stage in development, private beta planned, no publicly available product |
| 2 | Was bedeutet „Interesse anmelden“? / What does “register interest” mean? | Records interest; not a queue position, not an automatic invitation, not a guarantee of access |
| 3 | Wann startet die Private Beta? / When will the private beta start? | No fixed public date; contact when the beta or a next research phase opens |
| 4 | Läuft gerade eine Studie? / Is a study currently recruiting? | No; Cervus completed; next phase in preparation; recruitment not currently open |
| 5 | Was passiert mit meinen Angaben? / What happens to my information? | Used to manage the interest registration; links to `datenschutz.html` |
| 6 | Kann ich mein Interesse zurückziehen? / Can I withdraw my interest? | Yes; email `bjarne.dudzus@disce.de` |

Links in the FAQ: `datenschutz.html` (×2, DE+EN) and `mailto:bjarne.dudzus@disce.de` (×2, DE+EN) only. No Substack/newsletter/pricing/feature/timeline/priority-access/“first cohort”/study-selection content.

### Verification

Structural: six native `<button type="button" class="faq-trigger">` (all inside `<h3>`); six `aria-controls` values each resolving to exactly one `faq-aN` id; all answer ids unique; six panels `hidden` by default; button `id`s (`faq-qN`) used by `aria-labelledby`. `grep -rIn accordion` returns no `.accordion-*` selectors or JS (only a prose comment in the new FAQ block). Anchor balance in `waitlist.html`: 10/10. No duplicate IDs. FAQ heading order: `h2` (Häufige Fragen) → `h3` (questions). `data-lang` DE/EN balanced 13/13 in the FAQ region.

Source-level: `node --check js/site.js` OK; extracted inline `waitlist.html` script OK. JS keeps `aria-expanded` and `hidden` in lock-step; collapsed answers are `hidden`, so no focusable content remains; native buttons give Enter/Space; no single-open restriction; no animation (reduced-motion safe).

**Manual verification still required:** keyboard operation with Enter and Space; focus visibility on the FAQ buttons; open/close behaviour (multi-open); screen-reader announcement of expanded/collapsed state; mobile readability; language switching (DE/EN); the privacy (`datenschutz.html`) and withdrawal (`mailto:`) links.

---

## 2.12 Batch D execution log (before → after)

Batch D = POS-01, POS-03, CONV-03, CONV-05, TRUST-01, TRUST-04. Files touched: `index.html`, `kernel.html`, `waitlist.html`, `datenschutz.html`, this checklist. Batch A/B/C behaviour preserved. No metadata/indexability/robots/OG/canonical changes.

> **Scope note.** The Batch D brief's general "do not edit" list names `index.html`, `kernel.html` and `datenschutz.html`, but the item specs (POS-01 → homepage hero; POS-03 → `index.html`/`kernel.html`; CONV-05 item 5 → `datenschutz.html` field enumeration) explicitly require them. Interpretation applied: those files were edited **only** for the scoped Batch D items; no indexability, metadata, legal-placeholder, transfer, retention, or provider text was changed.

### 2.12.1 Positioning and codenames — POS-01 / POS-03

| Item | file:line | Before → After |
|---|---|---|
| POS-01 | `index.html:77` | eyebrow "Vor der Gründung · Berlin / Potsdam" → "Für internationale Fachkräfte in Deutschland" / "For international professionals in Germany" |
| POS-01 | `index.html:79` | investor-facing lede → audience + career context + system framing (diagnosis / practice / feedback) + truthful status ("Proof of Principle (Cervus) abgeschlossen; nächster Prototyp in Entwicklung; Private Beta geplant") |
| POS-03 | `index.html:94` | stat label `Pilotphase` / `Pilot Phase` → `Proof of Principle` (value "Cervus — abgeschlossen" unchanged) |
| POS-03 | `kernel.html:81` | Kernel hero lede → plain gloss first ("die Systemschicht hinter dem Coaching: das System, das Diagnose, gezieltes Üben und Rückmeldung verbindet"), then the existing technical detail |
| POS-03 | *(no change)* | Midgard/Asgard remain only in `status.html:173,188` roadmap cards (deep page, with explanatory sentences) |

### 2.12.2 Form-data minimization — CONV-05 (before → after inventory)

| Field | Before | After |
|---|---|---|
| First name (`first_name`) | required | **required** (unchanged) |
| Email (`email`) | required | **required** (unchanged) |
| German level (`german_level`) | required select A1–C2 | **optional** select A1–C2 (no required star, no error element/`aria-describedby`) |
| Availability (`availability_june`) | required, 4 checkboxes | **removed** |
| Microphone (`has_microphone`) | required checkbox | **removed** |
| Contact consent (`consent_contact`) | required checkbox | **required** (unchanged; now the only checkbox) |
| Free text (`source_channel`) | optional "How did you hear about this?" | **optional** "Kontext, Interesse oder Fragen" (same `name`/Airtable column) |

Evidence: removed markup at old `waitlist.html:691–732` and `:739–745`; `german_level` block now `:674–690`; free-text label `:726`; validation now `first_name`+`email`+`consent_contact` (`:991,997,1006`); payload `:1035–1042` no longer carries `availability_june`/`has_microphone`; privacy summary `:814`/`:821`; `datenschutz.html:102` (DE) and `:138` (EN field list), `:124` ("Aufnahme in die Warteliste" → "Interessenbekundung"); dead `.availability-grid` CSS removed. Airtable schema unchanged — removed fields are simply no longer written.

### 2.12.3 Thank-you and trust — CONV-03 / TRUST-01

| Item | file:line | Before → After |
|---|---|---|
| CONV-03 | `waitlist.html:745–746` | one-line confirmation → confirmation + honest expectation + "keine Wartelistenposition, keine automatische Einladung, keine Zugangszusage und kein fester Termin" + `datenschutz.html` link + `mailto:bjarne.dudzus@disce.de` correction/withdrawal; `role="status" tabindex="-1"` and focus behaviour preserved; `.submit-feedback a` styled |
| TRUST-01 | `waitlist.html:753–770` | *(none)* → compact `.trust-block` inside the form card: status, interest clarity, data-use summary, privacy link, contact/withdrawal; subordinate styling `.trust-block` at `:420–431` |

### 2.12.4 Consent/purpose consistency — TRUST-04

Source-level audit only (no legal conclusion). The single required contact consent (`waitlist.html:701–704`) is limited to being contacted when the planned private beta / next research phase opens, with no fixed commitment and no queue position. Form intro (`:620–623`), info list (`:587`), success (`:745–746`), trust block (`:753–770`), FAQ (`:837–908`) and the privacy notice purpose (`datenschutz.html:104`; `waitlist.html:814`) all describe the same interest-registration purpose. No newsletter/marketing consent, recruitment claim, access/scheduling/selection promise, or consent manager was added. **OPEN-LEGAL:** GATE-12 (legal review) and GATE-11 (mailbox verification) remain open and are not resolved in code.

### 2.12.5 GATE-13

**SUPERSEDED.** The availability field and every code-level reference to `availability_june` (markup, validation, error association, payload key) are removed. No Airtable column was renamed or deleted.

### 2.12.6 Batch D verification

Form-data: 5 visible controls after (`first_name`, `email`, `german_level`, `consent_contact`, `source_channel`); no residue of availability/microphone (`grep` zero); all `aria-describedby` references resolve (`first_name-error`, `email-error`, `checkbox-error`); no duplicate IDs; retained optionals are not required (only `first_name`, `email`, `consent_contact` are required).

Consistency: `grep` of the public HTML + JS for the audit terms — "Warteliste/waitlist" occurrences are all negative/qualifying or technical page references; "Verfügbarkeit/availability/Mikrofon/microphone/erste Kohorte/first cohort/Studienteilnahme/study participation" **zero** in conversion surfaces; "Zugang/access" only in negations, technical hosting text, or out-of-scope philosophy/kernel prose.

Accessibility regression: labels intact; `node --check` OK for `js/site.js` and the inline `waitlist.html` script; invalid/success/failure/retry state transitions coherent source-level; trust/thank-you `datenschutz.html` and `mailto:` links are native anchors (keyboard-reachable); anchor balance 18/18.

Copy/status: no availability, open-recruitment, beta-admission, queue, first-cohort, fixed-date, or efficacy claim in edited surfaces; "Proof of Visibility" absent from public HTML; Kernel glossed at its page hero and Cervus framed as a completed Proof of Principle.

**Manual verification still required:** rendered browser/mobile review of the homepage hero and `kernel.html` hero; keyboard operation of the trimmed form; screen-reader check of success + error summary after field removal; actual form submission against the live worker/Airtable (payload acceptance of an omitted `german_level`/`source_channel` and of the removed fields); visual review of the trust block and heading re-tagging; legal review (GATE-12) and mailbox verification (GATE-11).

---

## 2.13 Batch E execution log (measurement & evidence)

Batch E = TRUST-02, TRUST-03, PERF-01, A11Y-08, PERF-02…06. Files touched: `index.html`, `waitlist.html`, this checklist.

### 2.13.1 PERF-01 — font preload (decision option A)

A safe, clearly local, above-the-fold headline-face preload is separable from the deferred DEF-03 design-system migration, so option A was implemented minimally:

- `index.html:14` → `<link rel="preload" href="fonts/newsreader-roman-var.woff2" as="font" type="font/woff2" crossorigin>` (hero headline face; exact URL of `css/experimental.css:41`).
- `waitlist.html:16` → `<link rel="preload" href="fonts/noto-serif-var.woff2" as="font" type="font/woff2" crossorigin>` (hero headline face; exact URL of the inline `@font-face` `:49`).
- **No duplicate request:** resource-timing check (`performance.getEntriesByType('resource')`) shows exactly one entry per face (`newsreader-roman-var.woff2`, `noto-serif-var.woff2`).
- Body/Inter and the other faces were deliberately **not** preloaded (heavier; no measured benefit). `@font-face` declaration **dedup** remains deferred under **DEF-03** (waitlist stays self-contained; its Inter weight range intentionally differs). No runtime LCP improvement is claimed.

### 2.13.2 Measurement environment (real, local, no installation)

- Headless **Firefox 156.0** (`firefox --headless --remote-debugging-port=9333`), WebDriver **BiDi** endpoint `ws://127.0.0.1:9333/session`, driven by a dependency-free Node 24 client using the built-in `WebSocket`.
- Local static server `python3 -m http.server 8300 --bind 127.0.0.1` from the repo root.
- Date: 2026-09-21. Scripts kept outside the repo (`/tmp/opencode`).
- **Not available locally:** Lighthouse, PageSpeed Insights, axe, pa11y, Puppeteer/Playwright, geckodriver. No package was installed.
- **Limitations:** localhost response times, warm cache, headless, and **no CPU/network throttling** → performance numbers are indicative, not production-representative.

### 2.13.3 A11Y-08 — reflow & tap targets (measured)

| Page | 320 px | 375 px | 430 px |
|---|---|---|---|
| index.html | overflow 0 | 0 | 0 |
| waitlist.html | 0 | 0 | 0 |
| kernel.html | 0 | 0 | 0 |
| status.html | 0 | 0 | 0 |
| team.html | 0 | 0 | 0 |
| philosophy.html | 0 (was **3 px**; fixed post-Batch-E) | 0 | 0 |

Undersized controls (index n=12, waitlist n=5–6) all pass the WCAG 2.5.8 spacing exception (0 without exception at every width). **Resolved post-Batch-E:** the `philosophy.html` 3 px overflow at 320 px was fixed in `.eyebrow` (`max-width: 100%` + `overflow-wrap: anywhere`) and re-measured to 0 px on all six pages (see the A11Y-08 fix note). Retained MEASURE-ONLY (strict "no target <24×24" is met only via the spacing exception).

### 2.13.4 PERF-02 — LCP & CLS (measured)

| Page | 1280×900 | 375×812 |
|---|---|---|
| index.html | LCP 74 ms · CLS 0 | LCP 39 ms · CLS 0 |
| waitlist.html | LCP 59 ms · CLS 0 | LCP 22 ms · CLS 0 |

Both pages are under LCP ≤ 2.5 s and CLS ≤ 0.1 in this local lab. **Follow-up:** re-measure with throttled Lighthouse/PageSpeed before launch, e.g. `npx lighthouse http://localhost:8000/index.html --only-categories=performance --preset=desktop` (run later; not installed in this batch).

### 2.13.5 PERF-03 — INP

Retained MEASURE-ONLY. No `web-vitals`/field setup exists in the repo. **Field data unavailable; evaluate only after public traffic exists.** INP ≤ 200 ms remains a future target.

### 2.13.6 PERF-04 — contrast (partial measurement)

Method: live `getComputedStyle` colour + WCAG relative-luminance formula in the rendered page (headless Firefox, 1280×900). 25 pairings sampled; all pass:

- lowest 6.44:1 — ticker label (green on ink); hero h1 7.74:1; hero lede 12.91:1; primary CTA 16.32:1; nav/footer links 16.32:1; form label 17.16:1; trust line 11.35:1; FAQ trigger 17.16:1; FAQ panel 10.25:1; privacy text 11.35:1; skip link 17.35:1.
- **Caveat:** backgrounds are computed-style ancestor colours, **not** pixel samples over the photographic hero, and focus/hover states were not measured. No dedicated contrast-checker tool exists locally → retained MEASURE-ONLY.
- **Manual procedure (founder):** open each page in a real browser; use DevTools/axe contrast tool or a pixel eyedropper on the hero over its scrim, dark bands, CTA, form error text, trust block, ticker toggle, FAQ, footer, and the focused skip link; confirm ≥ 4.5:1 normal / ≥ 3:1 large.

### 2.13.7 PERF-05 — keyboard (partial rendered test)

Measured with BiDi `input.performActions` (Tab): first Tab focuses `.skip-link`, which becomes visible when settled (transform none, top 8 px, height 46 px) on index/waitlist/philosophy; index order = skip → brand → nav; waitlist order = skip → language toggle → back-link → first_name. The full invalid/corrected/success/API-failure journey and a screen-reader pass were **not** run → retained MEASURE-ONLY.

**Final manual keyboard sequence (founder):** (1) first Tab reveals skip link, Enter moves focus to `<main>`; (2) header nav, language switch (DE/EN), homepage CTA; (3) ticker pause/resume control; (4) waitlist: submit empty → error summary announced + focus, each field reachable with its error; (5) correct fields → submit → success state announced + focused; (6) simulate API failure → error message + retry; (7) FAQ open/close with Enter and Space; (8) privacy + withdrawal links; (9) footer navigation.

### 2.13.8 PERF-06 — mobile viewports (measured)

index + waitlist at 320/375/430 px: **0 px horizontal overflow**; hero h1, primary CTA, ticker toggle, form label, trust block and FAQ trigger present and within the viewport with sane sizes (index h1 36 px, CTA 57 px tall, ticker toggle 35 px tall; waitlist h1 28 px, CTA 48 px tall, FAQ trigger 52 px tall). Residual: human legibility/visual confirmation.

### 2.13.9 TRUST-02 / TRUST-03

TRUST-02 DONE — founder evidence decision recorded (retain existing Kernel conceptual architecture; no additional public artifact approved). TRUST-03 set to **DEFERRED** — no new evidence placement; `kernel.html` copy, claims and layout unchanged. No release gate closed.

### 2.13.10 Residual manual verification

- Throttled Lighthouse/PageSpeed LCP/CLS/INP re-run (pre-launch).
- Pixel/visual contrast confirmation, including hero over imagery and focus states.
- Full keyboard journey + one screen-reader pass (PERF-05 sequence).
- Human mobile-legibility review of index/waitlist.
- `philosophy.html` 320 px overflow — **resolved** post-Batch-E via the `.eyebrow` reflow guard (re-measured 0 px).

### 2.13.11 Hero Performance Pass 2a — deferred decorative hero dot-field (post-Batch-E)

- **Target:** a main-thread / initial-paint mitigation for the hero — **not** a claimed deployed LCP fix.
- **Change:** `js/generative/loader.js` — `.dot-field--hero` mounts are deferred: wait for `window.load`, then `requestIdleCallback({ timeout: 1500 })`, with a `setTimeout(1500)` fallback; skipped at ≤768 px (matches the CSS `display:none`); `WeakSet` duplicate-mount guard; no hero mount scheduled when absent. Non-hero mounts, reduced-motion, no-JS fallback, registry semantics and error handling unchanged; no `hidden` added, so the static dot plate stays visible immediately.
- **Validation (local Firefox BiDi, cold profile; not deployed data):** desktop 1440 — hero canvas absent at DOMContentLoaded, exactly one after load+idle (~195 ms), CLS 0, no console errors; hero-only `datenschutz.html` 1440 — the module import itself is deferred (79 ms vs DOMContentLoaded at 54 ms); mobile 390 — no hero canvas, and on a hero-only page **no `dot-field` module import at all**; `?gen-motion=off` — no canvas, static preserved; `.dot-field--focal` mounts still operate; hero image request/preload unchanged (exactly one).
- **Local timing:** hero canvas is now created after load+idle instead of during the DOMContentLoaded pass (on `index.html` the module import remains early because the below-fold focal mount imports it, unchanged).
- **Follow-up:** re-run PageSpeed Insights on the deployed site after commit; manual device check of the static→canvas handoff. Detail: `hero-performance-diagnostic.md` (Pass 2a). No release/legal gate altered.

---

## 3. Implementation sequence

Batches are sized to one OpenCode session each. Founder gates (GATE-01…12) run **in parallel** and do not block the code batches unless marked. Each batch ends with its own verification step.

| Batch | Contains | Rationale | Verification |
|---|---|---|---|
| **A — Structure & CTA (IA/positioning)** | CONV-01, CONV-02, POS-02, IA-01, IA-04, IA-05 | Fix the shared structure and the uniform CTA/routing first so later accessibility and trust work attaches to stable markup | Grep for CTA labels; visual review; founder sign-off on POS-02/CONV-02 |
| **B — Accessibility** | A11Y-01, A11Y-02, A11Y-03, A11Y-04, A11Y-05, A11Y-06, A11Y-07, A11Y-10 | Build on the stable structure; a11y changes touch nav/form/scaffolding | Keyboard + screen reader + axe on the form and all pages |
| **C — Content module & dead code** | IA-03, A11Y-09 | FAQ module and dead-code disposition are coupled (accordion repurpose) | Keyboard test of FAQ; code review |
| **D — Conversion & trust** | CONV-03, CONV-05, TRUST-01, TRUST-04, POS-01, POS-03, POS-04 | Conversion/trust refinement after structure + a11y; data-minimization needs founder sign-off | Manual form journeys; content review; founder sign-off |
| **E — Evidence & performance** | TRUST-02, TRUST-03, PERF-01, A11Y-08, then PERF-02…06 | Evidence strategy is founder-gated; measurement last, on the near-final build | Founder sign-off; Lighthouse + CWV + contrast + keyboard + viewport reports |
| **Gates (parallel)** | GATE-01…15 | Legal/founder inputs are independent of code batches | Gate table closed; legal review signed off |
| **Deferred** | CONV-06, DEF-01…03 | Only after validated interest (benchmark §12) | Post-launch review |

---

## 4. Launch verification protocol

Run only when GATE-01…12 are closed and all `P0` items are `DONE`.

1. **Gates closed:** confirm GATE table has no open BLOCKER; legal review of imprint + privacy confirmed.
2. **P0 DONE:** verify every P0 item in §2 is `DONE` (spot-check file:line evidence for the DONE items below).
3. **User journeys:** first screen → CTA (uniform label) → interest form → success; test DE and EN, desktop and mobile.
4. **Form integrity:** labels, error announcement, success announcement, duplicate-submit, retry; withdrawal/privacy link present.
5. **CWV measured:** LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 reported (PERF-02/03); contrast (PERF-04), keyboard (PERF-05), mobile (PERF-06) reported.
6. **Indexability switch:** apply GATE-14 only after 1–5; verify `robots.txt`, per-page `noindex`, canonical/OG, `sitemap.xml`.
7. **Claim register spot-check:** sample the claim types in Sprint 4 §8 against their evidence pointers; no prohibited claim present.
8. **Regression DONE-list:** re-verify the already-implemented items below remain intact.

### Already implemented (DONE — regression reference; never re-implement)

| Area | Evidence (file:line) | Source |
|---|---|---|
| waitlist title/meta/OG/Twitter reframed to interest registration | `waitlist.html:7,8,18,25` | Phase 2/2b |
| waitlist hero h1/subtitle; info block rebuilt | `waitlist.html:474–534` | Phase 2 |
| waitlist form heading/intro/success message | `waitlist.html:543,547–548,704–708` | Phase 2 |
| availability field date-free with flexible options | `waitlist.html:610–650` | Phase 2b |
| consent checkbox aligned to beta-or-next-study contact | `waitlist.html:665–668` | Phase 2b |
| on-page privacy purpose aligned; controller = `bjarne.dudzus@disce.de` | `waitlist.html:730,733–734,737,740–741` | Phase 2/2b |
| datenschutz controller + placeholders; §4 purpose/retention; EN mirrors | `datenschutz.html:79–82,97–103,131,133,134,135` | Phase 2/2b |
| datenschutz false Google-Fonts statement corrected | `datenschutz.html:105–106` | Phase 2 |
| impressum responsible person; no legal-form claim; founder-input placeholders | `impressum.html:70,76,78,91,79–80,86,102,118` | Phase 2 |
| team legal-form string removed | `team.html:61` | Phase 2b |
| team N=150 RCT corrected to completed past tense (DE+EN) | `team.html:74` | Founder fix |

---

**Grounding:** repo anchors as cited per row; source sections as cited per row. Benchmark sections: §3, §5, §6, §7, §8, §10, §11, §12. This checklist adds no new claims, wording, dates, or decisions; open options are presented as `OPEN-FOUNDER` items for the founder to decide.
