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
| GATE-13 | P2 | `waitlist.html:610,618,625,632,639`; JS `:829,:862` | Final decision on internal field name `availability_june` / Airtable column (non-public) | OPEN-FOUNDER | — |
| GATE-14 | BLOCKER | `robots.txt`; per-page `<meta name="robots">`; `sitemap.xml`; canonical/OG in page heads | Staging→production indexability decision + execution (robots allow, remove `noindex`, align canonical/OG/sitemap) | OPEN-FOUNDER + OPEN-CODE | GATE-01…12 |
| GATE-15 | P1 | — | BFSG/accessibility applicability review (Sprint 4 §4.9.5; deep-dive §6 item 15) | OPEN-LEGAL | GATE-12 |

**Gate rule:** GATE-01…12 must close before GATE-14 (indexability). Until then the site stays in its current non-indexable staging posture (`robots.txt` `Disallow: /`; `noindex` on every page).

**GATE-13 note:** founder decision #4 — once the availability field is removed in Batch D/CONV-05, GATE-13 becomes obsolete and may be closed as superseded.

---

## 2. Consolidated implementation backlog

### 2.1 Positioning & messaging (POS)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| POS-01 | P0 | OPEN-CODE | Sprint 1 §1.5/§1.8; decision pack B.1; locked #2/#5; `index.html:73–75` | Reframe homepage hero eyebrow/lede to the primary professional audience and the truthful planned status; no availability claim | Hero names the primary audience/context and a planned status; no "available/now" claim | Founder sign-off; manual review | medium | — |
| — | — | — | **Overlap note (Batch A closure)** | The homepage hero **primary CTA** was changed for IA-04 (`index.html:77` → `waitlist.html` "Interesse anmelden"). This touches the hero but is IA-04 work; POS-01 (hero eyebrow/lede framing) remains OPEN-CODE and the hero CTA change must be **reviewed in Batch D**, not treated as POS-01 completion. | — | — | — | — |
| POS-02 | P0 | DONE | locked #2; Sprint 1 §1.7; `index.html:90`; `status.html:78,82` | Make status labels consistent site-wide: "Cervus research completed" / "private beta planned" / "next research phase in preparation — recruitment not open" | Grep shows no conflicting present-tense study/availability labels on public pages; `beta.html` exempt as founder-deferred | Manual + grep; founder sign-off | low | — |
| POS-03 | P1 | OPEN-CODE | Sprint 1 §1.14; decision pack B.3; `index.html:48`; `kernel.html:76–77` | Apply codename policy: gloss "Kernel" at first contact; keep "Cervus" contextual; keep Midgard/Asgard deep-page only | No unexplained public codename at first contact | Visual review | low | POS-02 |
| POS-04 | P1 | DONE | locked #8; founder-decisions-locked.md (a)#8; decision pack B.3 | Confirm "Proof of Principle" as the public research term and keep "Proof of Visibility" out of headline/marketing positions | No "Proof of Visibility" in public copy; PoP used for Cervus | Grep + founder sign-off | low | — |
| — | — | — | **Batch A note** | POS-04 closed per founder decision #8: "Proof of Principle public; Proof of Visibility internal-only." Grep confirms "Proof of Visibility" appears only in internal `.md` documents, not in any public HTML. | — | — | — | — |

### 2.2 Information architecture (IA)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| IA-01 | P1 | DONE | target IA §1; founder correction (this pass) | Execute page dispositions: keep `kernel.html` as mechanism, reframe `status.html` as canonical status, and **keep `philosophy.html` as a regular, publicly discoverable secondary page**. The former "deep-link-only" demotion is **superseded** by founder decision. | Nav and links reflect dispositions; `philosophy.html` present in header + footer nav on every public non-deferred page; no primary path orphaned | Visual review + grep | medium | POS-02 |
| — | — | — | **Founder correction (Philosophy restored)** | Founder overrides the former IA-01 interpretation: `philosophy.html` remains a regular, publicly discoverable secondary page, visually secondary to the primary CTA "Interesse anmelden / Register interest"; it is not removed, hidden, `noindex`ed or deferred, and its content/claims/status wording are unchanged. The "Philosophie / Philosophy" link was restored in the **header nav** at `index.html:47`, `kernel.html:42`, `philosophy.html:57`, `status.html:42`, `team.html:42`, `datenschutz.html:42`, `impressum.html:42`, and in the **footer "Seiten" nav** at `index.html:295`, `kernel.html:513`, `philosophy.html:468`, `status.html:291`, `team.html:182`, `datenschutz.html:154`, `impressum.html:134`. The pre-existing contextual homepage link (`index.html:78`) is preserved. `beta.html:42,83` was already correct and is unchanged. Valid Batch-A IA-01 outcomes retained: `kernel.html` stays the mechanism page, `status.html` is the canonical status page, and no page was removed/renamed/deleted. | — | — | — | — |
| IA-02 | P2 | DONE | target IA §1, §5; `beta.html`; founder decision #2 | Decide `beta.html` role (keep deferred/unlinked, repurpose as status deep-link, or remove from scope) | Decision recorded; page stays `noindex`/unlinked until then | Founder sign-off | low | GATE-14 |
| — | — | — | **Batch A note** | Closed by founder decision #2: `beta.html` remains deferred, unlinked, `noindex`, and outside the sitemap, reserved for a future real beta. Only the CONV-01 label change was applied (`beta.html:46,95`). | — | — | — | — |
| IA-03 | P1 | OPEN-CODE | Sprint 4 §7; Sprint 3 §1.8; benchmark §3/§6; `js/site.js:42–64`; `css/experimental.css:1673–1682` | Add a small FAQ module on `waitlist.html` using the existing (unused) accordion; answer the conversion-relevant questions | Module answers the defined questions; accordion keyboard-operable; no new page created | Keyboard/manual; content review | low–med | A11Y-09 |
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
| A11Y-10 | P1 | DONE | Sprint 3 §1.9; `js/generative/registry.js` | Remove the dangling `kernel-loop` registry entry (or add the module if intended) | All registry keys resolve; no failed import | Stale `kernel-loop` entry removed; registry now resolves to existing `section-motif` + `dot-field` modules; page mounts use only `data-gen="dot-field"`; `node --check` passed; no-JS/reduced-motion untouched | low | — |

### 2.4 Performance (PERF)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| PERF-01 | P1 | OPEN-CODE | Sprint 3 §1.7; `css/experimental.css:13`; `waitlist.html:33,40` | Add font `rel="preload"` for above-the-fold faces; dedup the duplicate `@font-face` declarations (without breaking the self-contained waitlist page) | No external font request; identical rendering; preload paths resolve | Lighthouse + visual diff | low–med | DEF-03 |
| PERF-02 | P1 | MEASURE-ONLY | Sprint 3 §3; benchmark §5 | Measure LCP ≤ 2.5 s and CLS ≤ 0.1 (lab) | Report recorded; no claim without measurement | Lighthouse / PageSpeed Insights | low | GATE-14 |
| PERF-03 | P1 | MEASURE-ONLY | Sprint 3 §3; benchmark §5 | Measure INP ≤ 200 ms (field once traffic exists) | Report recorded | web-vitals / CrUX | low | GATE-14 |
| PERF-04 | P1 | MEASURE-ONLY | Sprint 3 §3; benchmark §5 | Measure AA contrast on hero/dark bands/form/footer | 4.5:1 normal, 3:1 large | axe / contrast checker | low | — |
| PERF-05 | P1 | MEASURE-ONLY | Sprint 3 §3 | Run full keyboard-path measurement (nav, language switch, form, success/error) | All paths operable | Manual keyboard + SR | low | A11Y-01…05 |
| PERF-06 | P1 | MEASURE-ONLY | Sprint 3 §3 | Mobile viewport checks (320–430 px; hero/form/CTA readable) | No overflow; CTA obvious | DevTools + one real device | low | CONV-01 |

### 2.5 Conversion (CONV)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| CONV-01 | P0 | DONE | Sprint 4 §1.2; locked #1/#2. Full list: `index.html:51,260,307`; `beta.html:46,95`; `datenschutz.html:46,166`; `impressum.html:46,146`; `kernel.html:46,525`; `philosophy.html:61,480`; `status.html:46,276,302`; `team.html:46,194` | Replace generic CTA labels with the recommended set: primary "Interesse anmelden / Register interest"; secondary variant "Interesse anmelden – Private Beta / Register interest – private beta" | Every listed CTA uses the label set; no "Auf die Warteliste/Join the Waitlist" remains | Grep + visual review | low–med | — |
| — | — | — | **Batch A closure note** | Applied on all eight pages. Final state: `index.html:50,259,306`; `beta.html:46,95`; `kernel.html:45,524`; `philosophy.html:60,479`; `status.html:45,275,302`; `team.html:45,193`; `datenschutz.html:46,166`; `impressum.html:46,146` all read "Interesse anmelden / Register interest". Grep for "Auf die Warteliste" / "Join the Waitlist" returns **zero HTML hits** (remaining occurrences are internal `.md` documents only). | — | — | — | — |
| CONV-02 | P0 | DONE | Sprint 4 §1.3; `index.html:256–257` | Replace "join the beta"/"first cohort" with target interest-registration wording (no cohort/access implication) | No cohort/access/availability implication in band | Founder sign-off + manual review | low | — |
| — | — | — | **Batch A note** | `index.html:255–256` now reads "Die Entwicklung verfolgen oder Interesse anmelden." / "…melden Sie unverbindlich Ihr Interesse an der geplanten Private Beta an." No cohort/access/date/response implication remains. | — | — | — | — |
| CONV-03 | P0 | OPEN-CODE | Sprint 4 §2.2; Sprint 3 §1.2; `waitlist.html:704–708,728–743` | Complete thank-you state: accessible confirmation (A11Y-02), privacy deep link to `datenschutz.html`, correction/withdrawal note | Confirmation announced; privacy linked; withdrawal stated | Screen reader + link check | low | A11Y-02 |
| CONV-04 | P1 | OPEN-FOUNDER | Sprint 4 §2.3; locked #1; founder decision #3 | Finalize the follow-up runbook (who/trigger/medium/no-trigger message) | Runbook documented; mailbox confirmed | Founder sign-off | low | GATE-11 |
| — | — | — | **Founder decision (Batch A, later Batch D)** | Owner: Bjarne Dudzus. Trigger: a valid interest-registration submission. Internal service target: review/respond within five business days — **internal only, never displayed as a public response-time guarantee**. Medium: `bjarne.dudzus@disce.de`. Initial response: acknowledgement, honest status, no access promise, optional one relevant follow-up question. Spam/irrelevant may receive none/short neutral reply. List usable for narrowly related beta/next-study status communication (incl. delay notices), **not** a general newsletter; any future Substack/newsletter opt-in must be separate, voluntary, unchecked, distinct purpose, and legally reviewed. **Not implemented in Batch A; remains OPEN-FOUNDER for Batch D.** | — | — | — | — |
| CONV-05 | P0 | OPEN-FOUNDER | Sprint 4 §3; founder decision #4 | Form data minimization: drop/defer availability + microphone fields; simplify level; defer role/career data; adjust JS validation accordingly | Form fields reflect the decision; validation still blocks invalid submits | Founder sign-off + manual form test | medium | — |
| — | — | — | **Founder decision (Batch A, later Batch D)** | Keep name + email; remove/defer availability field; remove/defer microphone field; keep language level only as a simplified, low-friction **optional** field; defer role/career/detailed qualification to a later actual beta invitation/application; keep free text optional. Once availability is removed in Batch D, **GATE-13 becomes obsolete/superseded**. **Not implemented in Batch A** (no form/JS/Airtable changes); remains OPEN-FOUNDER for Batch D. | — | — | — | — |
| CONV-06 | P2 | DEFERRED | Sprint 4 §4/§7; benchmark §7 | Introduce privacy-friendly, low-traffic measurement only after validated interest (no trackers now) | Measurement introduced with consent-free config | Post-launch review | medium | GATE-14 |

### 2.6 Trust & evidence (TRUST)

| ID | Prio | Status | Source | Action | Acceptance | Validation | Effort | Depends |
|---|---|---|---|---|---|---|---|---|
| TRUST-01 | P0 | OPEN-CODE | Sprint 4 §5; target IA §5; `waitlist.html:728–743` | Add a compact trust/status block near the form: status, data-use summary, privacy deep link, contact, completed-Cervus context | Block present; privacy linked; no security/availability overclaim | Content review | low–med | CONV-03 |
| TRUST-02 | P1 | OPEN-FOUNDER | Sprint 3 §2; founder decision #5 | Decide the product-evidence strategy: raise the Kernel architecture plate as labeled evidence and/or supply a real prototype artifact / anonymized output | Decision recorded; artifacts supplied (if any) | Founder sign-off | low | — |
| — | — | — | **Founder decision (Batch A, later Batch E)** | No new public product artifact at this stage; existing Kernel architecture communication remains the current conceptual mechanism representation; no testimonial approved; prototype screenshots only later when a stable, truthful artifact exists and is labeled "prototype in development"; no evidence asset may imply current access, public availability, validated efficacy, or product readiness. **Not implemented in Batch A.** | — | — | — | — |
| TRUST-03 | P1 | OPEN-CODE | Sprint 3 §2; target IA §3; `kernel.html:142–220,217–219`; founder decision #5 | Implement the chosen evidence placement (e.g., label the existing architecture plate as a figure with its textual equivalent) | Evidence artifact visible and truthful; no availability implication | Founder sign-off + visual review | medium | TRUST-02 |
| TRUST-04 | P1 | OPEN-CODE | Sprint 4 §4; `waitlist.html:665–668,730,737` | Final check that the single-purpose contact consent still suffices (no new scopes; no consent manager) | Consent text matches purpose; no new consent mechanism | Legal review (GATE-12) | low | GATE-12 |
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
