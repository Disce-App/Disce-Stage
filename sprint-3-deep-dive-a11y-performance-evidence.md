# Sprint 3 Deep Dive — Accessibility, Performance & Evidence

**Document type:** Specification for a later implementation step (document-only; no code changed by this document).
**Status:** Target spec. Not a master checklist.
**Date:** 2026-09-21
**Inputs:** baseline `sprint-3-ui-ux-accessibility-performance.md`; `founder-decisions-locked.md`; `sprint-0-triage-and-sprint-1-decision-pack.md`; `sprint-2-deep-dive-target-ia.md`; tracked repository; benchmark `Pre-Launch-Website-Exhaustive-Report.md`; repo rules `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and `docs/generative-visuals/implementation-plan.md`.
**Locked decisions honored:** #2 (truthful interest registration, consistent status labels), #6 (planned beta only, no apply mechanic), #7 (Substack external deep link; no homepage-primary CTA; no new consent mechanism).

No production copy is written below. Effort classes are coarse relative sizing (low / med / high) and are not estimates of calendar time. "Dependency on Sprint 2 IA" refers to `sprint-2-deep-dive-target-ia.md`.

---

## 1. Actionable item register

Each item: exact target fix · acceptance criterion · benchmark/WCAG reference · effort · Sprint 2 IA dependency.

### 1.1 Interest form — programmatic error identification (`aria-invalid` / `aria-describedby`)

- **Current state (repo):** waitlist form uses `novalidate` and JS validation (`waitlist.html:789–890`); errors are textual and field-adjacent (`:570–573`, `:586–589`, `:610–613`, `:646–649`, `:672–675`) but no field carries `aria-invalid`, no error element is referenced via `aria-describedby`, and no `role="alert"`/`aria-live` exists (verified by repo-wide search — Sprint 3 §3.8).
- **Target fix:** on validation failure, set `aria-invalid="true"` on the offending input/select and `aria-describedby` to the corresponding `.form-error` id; give each error element a stable `id`; use `role="alert"` (or an `aria-live="polite"` region) for the error summary. On success/clear, remove `aria-invalid` and restore `aria-describedby`. Do not change validation logic, fields, or endpoints.
- **Acceptance criterion:** with a screen reader (NVDA/VoiceOver) and with a keyboard, submitting an empty form announces each error and associates it with its field; correcting a field clears the invalid state; automated axe/Lighthouse audit reports no "form field has no accessible name/description" error on the page.
- **Benchmark/WCAG:** benchmark §5 "Accessibility minimum" ("Textual, field-adjacent, and programmatically announced errors with guidance for correction"; "Announce form and status messages for screen readers"); WCAG 2.2 SC 3.3.1 (Error Identification), SC 3.3.3 (Error Suggestion), SC 4.1.3 (Status Messages).
- **Effort:** med.
- **Sprint 2 IA dependency:** none (form stays the Route A destination). Should not be done before the residual waitlist wording items in §1.12 are decided, to avoid touching the same block twice.

### 1.2 Interest form — announce success/status

- **Current state (repo):** success banner `#successMsg` (`waitlist.html:705–708`) is toggled with `.show` via JS (`:882–883`); no `aria-live`/`role="status"`.
- **Target fix:** make `#successMsg` an `aria-live="polite"` (or `role="status"`) region and move focus to it (or to a heading) after a successful submit; keep the existing visible confirmation.
- **Acceptance criterion:** after a successful submit a screen reader announces the confirmation without the user having to navigate to it; keyboard focus lands on/near the confirmation; no duplicate announcement on subsequent interactions.
- **Benchmark/WCAG:** benchmark §5 "Announce form and status messages"; §7 "Thank-you flow" (visible confirmation not solely email-dependent — already met); WCAG 2.2 SC 4.1.3.
- **Effort:** low.
- **Sprint 2 IA dependency:** post-submit expectation wording is fixed by locked #1/#2 (already reflected in `waitlist.html`).

### 1.3 Submit button busy state

- **Current state (repo):** button is disabled and gets `.loading` during submit (`waitlist.html:843–844`, `:692–701`); no `aria-busy`.
- **Target fix:** add `aria-busy="true"`/`false` in parallel with the existing disabled/loading toggle; keep the spinner decorative (`aria-hidden`).
- **Acceptance criterion:** assistive tech exposes a busy state during the request; no change to the visible loading behavior.
- **Benchmark/WCAG:** benchmark §5 "Accessible states and forms"; WCAG 2.2 SC 4.1.3.
- **Effort:** low.
- **Sprint 2 IA dependency:** none.

### 1.4 `<main>` landmark on all pages

- **Current state (repo):** only `waitlist.html:485` has `<main>`; the other eight pages have no `<main>` (content sections are direct children of `<body>`; Sprint 3 §3.8/§3.11).
- **Target fix:** wrap the primary content of each page in a single `<main>` landmark; keep header/footer outside.
- **Acceptance criterion:** every page has exactly one `<main>`; screen-reader landmark navigation lists "main"; no visual/layout change.
- **Benchmark/WCAG:** benchmark §5 "Semantic landmarks and a sensible heading hierarchy"; WCAG 2.2 SC 1.3.1, SC 2.4.1 (Bypass Blocks, with §1.5).
- **Effort:** low.
- **Sprint 2 IA dependency:** low; apply after the target-IA page roles are settled so the landmark wrapping is done once.

### 1.5 Skip-to-content link

- **Current state (repo):** no skip link on any page (verified; Sprint 3 §3.8).
- **Target fix:** add one visually-hidden-until-focused skip link as the first focusable element on each page, targeting the `<main>` id (depends on §1.4).
- **Acceptance criterion:** pressing Tab on page load reveals the skip link; activating it moves keyboard focus to the main content; it is not visible until focused.
- **Benchmark/WCAG:** benchmark §5 "Full keyboard operability"; WCAG 2.2 SC 2.4.1 (Bypass Blocks).
- **Effort:** low.
- **Sprint 2 IA dependency:** requires §1.4 (`<main>` id/target).

### 1.6 Infinite logo ticker — pause/stop or removal

- **Current state (repo):** CSS `animation: ticker-scroll 34s linear infinite` (`css/experimental.css:1712`), duplicated by JS (`js/site.js:27–40`), markup `index.html:267–283`; reduced-motion disables it (`css/experimental.css:1727`) but there is **no pause control**. Repo rule (`docs/generative-visuals/implementation-plan.md` §5) states "any persistent automatic motion gets a pause control with a DE/EN label".
- **Target fix (two acceptable options; founder/owner chooses):** (a) add a visible, keyboard-operable pause/play control with a bilingual label that stops the CSS animation (and pauses the JS duplication is unnecessary since duplication is static); or (b) remove the animation and render the partner/ecosystem logos as a static row (the block's content itself is fixed by locked #4 and must not change). Either option must preserve the logos/names/framing exactly.
- **Acceptance criterion:** a user can stop the motion (option a) or there is no automatic motion (option b); the partner/ecosystem content is unchanged; no layout overflow introduced; control is keyboard-reachable and labeled.
- **Benchmark/WCAG:** benchmark §5 "Endless logo marquees" and "Motion"; §5 "Avoid or use carefully"; WCAG 2.2 SC 2.2.2 (Pause, Stop, Hide).
- **Effort:** low (option a control) / low–med (option b static layout).
- **Sprint 2 IA dependency:** none for placement; locked #4 fixes content.

### 1.7 Font delivery — preload + duplicate declaration dedup

- **Current state (repo):** four `@font-face` families live in `css/experimental.css:13–41` (archivo-black, inter-var, newsreader-italic-var, newsreader-roman-var) with `font-display: swap`; **no `rel="preload"`** anywhere (verified; Sprint 3 §3.9). `waitlist.html:33–46` re-declares Inter and Noto Serif inline (`waitlist.html:38`, `:45`) using the same `fonts/` files.
- **Target fix:** (a) add `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the font(s) used above the fold, with the correct files; (b) remove the duplicated `@font-face` declarations from `waitlist.html` and rely on the shared stylesheet — but only if `waitlist.html` is given a link to `css/experimental.css`; note that the waitlist page is currently **self-contained with its own inline stylesheet and does not link the shared CSS**, so dedup must not break its rendering. If linking the shared stylesheet is out of scope, an alternative is to keep the local declarations but ensure they match the shared files/weights exactly (no functional duplication).
- **Acceptance criterion:** no external font request; no 404; hero text renders with the intended face without invisible-text flash; the waitlist page renders identically before/after; preload hints resolve to existing files under `fonts/`.
- **Benchmark/WCAG:** benchmark §5 "Reduce and subset fonts and preload them sensibly"; §5 "Performance minimum".
- **Effort:** low–med (dedup path is med because of the waitlist page's self-contained styling).
- **Sprint 2 IA dependency:** depends on whether `waitlist.html` is later unified with the shared design system; if it stays self-contained, take the matching-declaration route.

### 1.8 Dead accordion code

- **Current state (repo):** `js/site.js:42–64` implements an accordion; `css/experimental.css:1673–1682` styles it; **no page mounts `.accordion-trigger`** (Sprint 3 §3.11, Sprint 1 §1.12).
- **Target fix:** either remove the dead JS/CSS, or (if a FAQ module is decided in a later IA step) keep it as the intended implementation. Do not create a FAQ now.
- **Acceptance criterion:** no console errors; no unused code if removal is chosen; if kept, it is clearly documented as reserved for a future FAQ.
- **Benchmark/WCAG:** benchmark §5 "Remove unnecessary JavaScript"; §3 FAQ (P0 module) is a content/IA decision, not this item.
- **Effort:** low.
- **Sprint 2 IA dependency:** depends on the FAQ decision in `sprint-2-deep-dive-target-ia.md` §5 item 4.

### 1.9 Dangling `kernel-loop` registry entry

- **Current state (repo):** `js/generative/registry.js:3` registers `'kernel-loop': () => import('./kernel-loop/index.js')`, but `js/generative/kernel-loop/` does not exist (only `dot-field/` and `section-motif/` exist). No page mounts `data-gen="kernel-loop"`, so there is no runtime error today (Sprint 3 §3.11).
- **Target fix:** remove the dangling registry entry, or add the module if it is intended for a later phase (not in current scope).
- **Acceptance criterion:** registry keys all resolve to existing modules; loader logs no failed import when a real regression harness mounts all `[data-gen]` values.
- **Benchmark/WCAG:** benchmark §5 "Remove unnecessary JavaScript"; repo `GENERATIVE_WEB_VISUALS_COMPETENCY.md` (no broken modules).
- **Effort:** low.
- **Sprint 2 IA dependency:** none.

### 1.10 Heading structure and page `<title>` consistency

- **Current state (repo):** one `<h1>` per page (verified); `waitlist.html` had English-first `<title>`/OG while the site is DE-primary — the Phase 2 containment changed these to German. Remaining minor: `waitlist.html:6` still inherits inline styling separate from the shared system.
- **Target fix:** verify heading order (`h1` → `h2` → `h3`) per page after any content edits; keep `<title>` and OG aligned with page role.
- **Acceptance criterion:** no skipped heading levels; `<title>`/OG describe the actual page role; DE/EN `<title>` data attributes where the shared system expects them.
- **Benchmark/WCAG:** benchmark §5 "Semantic landmarks and a sensible heading hierarchy"; WCAG 2.2 SC 1.3.1, SC 2.4.2.
- **Effort:** low.
- **Sprint 2 IA dependency:** after target-IA page roles are final.

### 1.11 Waitlist page visual/structural detachment (design system)

- **Current state (repo):** `waitlist.html` uses its own inline `<style>` (`:28–450`), its own token values (e.g. `--color-primary: #4FAC4E`, `:52`), its own fonts (`:33–46`), and no shared header/footer (Sprint 3 §3.0/§3.11).
- **Target fix:** decide whether to migrate the page to the shared stylesheet/header/footer. This is a **design-system decision** dependent on Sprint 2; no change implied now.
- **Acceptance criterion:** if migrated, the page matches the shared header/footer and tokens without changing the form behavior; if not, the divergence is explicitly accepted.
- **Benchmark/WCAG:** benchmark §5 "Consistent grid"/"Distinct but restrained brand system"; consistency is a comprehension aid (Sprint 1 §1.13).
- **Effort:** med–high (only if migration is chosen).
- **Sprint 2 IA dependency:** yes — depends on the decision to unify the conversion page with the shared system (§1.7 above is coupled).

### 1.12 Residual waitlist wording (form controls, consent, privacy)

- **Current state (repo):** after Phase 2/2b, the remaining study/date references are confined to the privacy notice controller line and the form's internal `availability_june` name; the visible availability label/options, consent text, and privacy purpose were aligned in Phase 2b (see the run report). The privacy notice still names `bjarne.dudzus@student.businessschool-berlin.de` and "BSP Business & Law School Berlin" (`waitlist.html:733–734`, `:740–741`), which differs from `impressum.html:87` / `datenschutz.html:82` (`bjarne.dudzus@disce.de`).
- **Target fix:** founder decision on the authoritative controller contact for the waitlist page; then a one-line alignment. Also decide whether the internal field name `availability_june` (and Airtable column) should be renamed (non-public, optional).
- **Acceptance criterion:** a single consistent controller contact across `waitlist.html`, `impressum.html`, `datenschutz.html`; no date-bearing public token.
- **Benchmark/WCAG:** benchmark §8 "Form transparency" and "Privacy policy reflect the actual stack".
- **Effort:** low.
- **Sprint 2 IA dependency:** none; it is a founder fact, not an IA decision.

### 1.13 Mobile tap targets and viewport checks

- **Current state (repo):** waitlist form inputs are 16 px with `autocomplete` and 48 px submit button (`waitlist.html:250`, `:338`, `:568`, `:584`); site-wide nav/ticker link target sizes were not measured (Sprint 3 §3.7).
- **Target fix:** ensure interactive targets meet WCAG 2.2 SC 2.5.8 minimum (24×24 CSS px) with comfortable spacing; verify no horizontal overflow at 320 px.
- **Acceptance criterion:** no target below 24×24; no horizontal scroll at 320/375 px; nav/CTA usable one-handed.
- **Benchmark/WCAG:** benchmark §5 "Mobile blind spots" and "Tap targets"; WCAG 2.2 SC 2.5.8, SC 1.4.10 (Reflow).
- **Effort:** low–med.
- **Sprint 2 IA dependency:** depends on any nav/CTA label changes (target-IA §5 item 8).

---

## 2. Product-evidence decision

Context: locked decisions #1/#2/#6 and the status matrix require "no active availability claim"; Cervus is a **dormant, completed** proof-of-principle; the next prototype is in development; the Kernel architecture is already the chosen mechanism presentation (`DESIGN-BRIEF.md` Kernel choices are not re-litigated).

### Candidate public artifacts (from the repo, or requiring founder supply)

| Candidate | Exists in repo? | Where / note | Evidence value | Risk if used |
|---|---|---|---|---|
| **Kernel runtime architecture plate** (annotated SVG) | **Yes** | `kernel.html:142–220` (inline SVG + bilingual `<figcaption>` `:217–219`); currently `aria-hidden="true"` (`:144`) and treated as a decorative plate | High: shows a real, deliberate system (four layers, provider boundary, persistence); the closest thing to a product/mechanism artifact | Must not imply the system is publicly usable or that V0 is a live product |
| **Kernel cycle / data-advantage text flow** | Yes (text) | `kernel.html:307–363`, `:404–442` | Medium: explains mechanism and governance | Text-only; no visual proof |
| **Cervus completed proof-of-principle** | Repo context only | `status.html:78` "Cervus — Abgeschlossen · Mai – August 2026"; `index.html:90`; research report/thesis **not in the repo** | Medium: completed research is a legitimate proof type (benchmark §8 "Research validation") | Must not be shown as active/recruiting; no results/figures until the report is supplied |
| **Anonymized example output / feedback report** | **No** | Not present; would require founder supply | High if it exists | Must be genuinely anonymized and representative; must not imply a released feature |
| **Prototype screenshot / screen recording** | **No real artifact in repo** | All `images/` assets are editorial art; `images/team/*.svg` are placeholders; `disce-kernel-architecture.html` / `.json` are **untracked** dev artifacts (`git status`) | High if a real, non-misleading artifact exists | A mockup must not suggest functions not planned (benchmark §4 "Visual hero choice") |
| **Editorial/abstract imagery** | Yes | Hero and section art (`index.html:63–69`, etc.) | Brand only | Already the only depiction; benchmark "abstract as sole product depiction" warning |

### Recommended primary evidence strategy

**Use the existing Kernel runtime architecture plate as the primary public mechanism/evidence artifact**, surfaced on `kernel.html` (and, if the homepage narrative needs it, as a deep link from the mechanism section — dependent on Sprint 2), with its existing bilingual textual equivalent. Reinforce with the **Cervus completed proof-of-principle as text/status context** (not as an interactive demo). Do **not** fabricate or import a product screenshot; the benchmark prefers real artifacts and warns against mockups that imply unplanned functions.

### What it must not imply (locked #2/#6)

- That a public product is available, or that the Kernel V0 is a live/released product.
- That Cervus is active, recruiting, or publicly interactive (it is dormant/completed).
- That the private beta is open or that evidence implies access.
- Any performance/accuracy/AI-capability claim not established in `kernel.html:445–474` or `philosophy.html:264–269`.

### What the founder must supply before a stronger evidence strategy

1. Decision to raise the architecture plate from decorative (`aria-hidden`) to a labeled evidence figure (or a duplicate), if desired.
2. Any **real** prototype artifact (screenshot/recording) that is truthful and non-misleading — or an explicit decision to remain text/diagram-only.
3. Any **anonymized** example output/report from Cervus, with its scope and limitations (benchmark §8 "source, scope, and limitations").
4. Confirmation that the completed research report may be referenced/linked and what may be cited from it.

---

## 3. Measurement protocol (for later)

No measurement was performed in this deep dive. The following is the protocol to run before/after the indexable launch.

| Dimension | Target / threshold | Tool(s) | Who | When |
|---|---|---|---|---|
| **LCP** | ≤ 2.5 s (good) | Lighthouse / PageSpeed Insights (lab); field data once traffic exists | implementer/founder | lab: before indexable launch; field: after traffic builds |
| **INP** | ≤ 200 ms (good) | Chrome DevTools Performance + `web-vitals` local capture; CrUX/field once available | implementer | lab: pre-launch; field: post-launch |
| **CLS** | ≤ 0.1 (good); repo brief target ≤ 0.05 (`DESIGN-BRIEF.md:143`) | Lighthouse; layout-shift observation on hero/media | implementer | pre-launch |
| **Contrast** | AA: 4.5:1 normal, 3:1 large | axe DevTools / WCAG contrast checker over hero, dark bands, form, footer | implementer | pre-launch and after any palette/scrim change |
| **Keyboard path** | Full traversal of nav, language switch, form, success/error | manual Tab/Shift-Tab/Enter/Escape + NVDA or VoiceOver | implementer | pre-launch; after §1.1–§1.6 |
| **Mobile viewports** | No horizontal scroll, readable hero/form/CTA at 320–430 px | DevTools device emulation + one real iOS/Android device | implementer | pre-launch |
| **Reduced motion** | Static/meaningful state, ticker stopped, generative frozen | DevTools rendering emulation + `?gen-motion=off` harness hook (`js/generative/loader.js`) | implementer | pre-launch and after §1.6 |

**Evidence rule:** per `GENERATIVE_WEB_VISUALS_COMPETENCY.md`, never claim performance/accessibility compliance without measurement. Automated checks supplement, not replace, manual keyboard/screen-reader/zoom testing (benchmark §5 "Accessibility minimum", "Pre-launch QA").

---

## 4. Classification table

| Item | Class | Notes |
|---|---|---|
| §1.1 `aria-invalid`/`aria-describedby` on form errors | **A11Y-GAP (fix)** | Visual errors exist; programmatic association missing |
| §1.2 `aria-live` success/status | **A11Y-GAP (fix)** | Visible confirmation exists; not announced |
| §1.3 `aria-busy` on submit | **A11Y-GAP (fix)** | Low effort |
| §1.4 `<main>` landmarks | **A11Y-GAP (fix)** | Structural |
| §1.5 Skip-to-content link | **A11Y-GAP (fix)** | Depends on §1.4 |
| §1.6 Infinite ticker pause/stop | **BUG (fix)** | Violates repo's own "pause control" rule and WCAG 2.2.2; content must stay per locked #4 |
| §1.7 Font preload + dedup | **BUG (fix)** | No preload; duplicate declarations; dedup is coupled to waitlist self-containment |
| §1.8 Dead accordion code | **BUG (fix)** | Dead code; remedy depends on FAQ decision |
| §1.9 Dangling `kernel-loop` registry entry | **BUG (fix)** | Broken reference |
| §1.10 Heading/`<title>` consistency | **A11Y-GAP (fix)** | Mostly satisfied; verify |
| §1.11 Waitlist page design-system detachment | **MEASURE-ONLY / deferred** | Only if migration decided |
| §1.12 Residual waitlist controller email | **BUG (fix)** | One-line alignment after founder decision; inconsistent contacts across pages |
| §1.13 Mobile tap targets/reflow | **MEASURE-ONLY** | No failure asserted until measured; fix only if < 24×24 or overflow found |
| §2 No real product screenshot/mockup | **MEASURE-ONLY** | Strategy decision, not a mechanical bug; no false artifact to invent |
| §3 CWV / contrast / keyboard results | **MEASURE-ONLY** | Unmeasured; no failure asserted |
| Sprint 3 §3.9 no measured CWV | **MEASURE-ONLY** | Targets exist; evidence absent |

---

**Grounding summary.** Repo anchors: `waitlist.html:6/28–450/33–46/250/338/485/570–675/692–708/789–890`; `index.html:267–283`; `kernel.html:142–220/144/217–219/307–363/404–442/445–474`; `status.html:78`; `team.html:61/74`; `impressum.html:82/87`; `datenschutz.html:82`; `css/experimental.css:13–41/1673–1682/1712/1727`; `js/site.js:27–40/42–64`; `js/generative/registry.js:3`; `js/generative/loader.js`; `docs/generative-visuals/implementation-plan.md` §5; `GENERATIVE_WEB_VISUALS_COMPETENCY.md`; `DESIGN-BRIEF.md:143`. Benchmark sections: §4 (Landing-Page Dramaturgy), §5 (UI/UX State of the Art), §7 (Conversion/Thank-you), §8 (Trust/Transparency/Legal), §11 (Master Checklist). WCAG 2.2 SCs: 1.3.1, 1.4.10, 2.2.2, 2.4.1, 2.4.2, 2.5.8, 3.3.1, 3.3.3, 4.1.3.
