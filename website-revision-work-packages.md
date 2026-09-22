# Website Revision — Work Packages

**Document type:** Structured planning companion to `master-checklist-website-revision.md`.
**Date:** 2026-09-22
**Status:** Planning only. No website code has been changed, and no task in this document has been executed.

## 0. Purpose and relationship to the master checklist

This document is a **companion** to `master-checklist-website-revision.md`. It is **not** a replacement for it.

- It **preserves every existing task** from the master checklist (all IDs and their meanings) and adds the newly requested tasks alongside them.
- It groups related existing and new tasks into **work packages** with concrete subtasks.
- Where the master checklist holds authoritative detail (acceptance criteria, validation, `file:line` evidence, batch execution logs, priorities, dependencies), **the master checklist remains authoritative**; this document only points to it.
- This document introduces **no new priorities, technical solutions, dependencies, scope decisions, or implementation details** beyond what is explicitly stated in the available inputs. Where information is missing, it is marked **Open question** or **To be clarified**.
- Existing tasks retain their `Status` and `Priority` exactly as recorded in the master checklist. New tasks carry no status or priority (none was given).

### Task markers

- `[EXISTING]` — comes from `master-checklist-website-revision.md`; the ID is preserved.
- `[NEW]` — one of the newly requested tasks.

### Existing status vocabulary (from the master checklist, §0)

`DONE` = already implemented and verified (listed once, never re-implemented). `OPEN-CODE` = implementation task with a defined target. `OPEN-FOUNDER` = decision or input only the founder can provide. `OPEN-LEGAL` = requires legal/external review. `DEFERRED` = "only after validated interest" (do last). `MEASURE-ONLY` / `SUPERSEDED` as recorded.

### Available inputs used for this document

- `master-checklist-website-revision.md` (all existing tasks).
- The nine newly requested tasks supplied in the task brief.
- Repository context already present: `DESIGN-BRIEF.md`, `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md`, `sprint-1-positioning-messaging.md`, `sprint-0-triage-and-sprint-1-decision-pack.md`, `sprint-3-deep-dive-a11y-performance-evidence.md`, `sprint-4-deep-dive-conversion-trust-legal.md`, `founder-decisions-locked.md`, `hero-performance-diagnostic.md`, and the current HTML/CSS/JS tree.

> **Scope guardrail.** Creating this document does not authorize any content, copy, legal, or structural change. Any subtask that would change product copy, claims, legal text, or routing still requires the approvals noted in the master checklist.

---

## 1. Newly added tasks → work-package map

| New ID | New task (as requested) | Work package |
|---|---|---|
| NEW-01 | Get the website performance under control. | WP-E — Performance |
| NEW-02 | Redesign the waitlist so that it matches the visual style of the rest of the website, including its own background image—ideally `1.png`. | WP-F — Conversion & Waitlist |
| NEW-03 | Animate the hero images. | WP-H — Visual System: Typography, Imagery & Motion |
| NEW-04 | Synthesize the strategy, positioning, and customer segment documents; add relevant content to the website and adapt existing content where necessary. | WP-B — Positioning, Messaging & Document Synthesis |
| NEW-05 | Revamp the team page. | WP-I — Team Page |
| NEW-06 | Rework the fonts so that the text is easier to read over the background images. | WP-H — Visual System: Typography, Imagery & Motion |
| NEW-07 | Load and display the research reports/results in the Research section. | WP-G — Trust, Evidence & Research Content |
| NEW-08 | Change the email addresses shown or used on the website. | WP-J — Contact & Email Addresses |
| NEW-09 | Consider integrating the newsletter or Substack as an RSS feed or live feed. | WP-K — Newsletter / Substack Feed |

---

## 2. Work packages

### WP-A — Legal & Release Gates `[EXISTING]`

**Purpose:** Close the founder/legal inputs that gate a public + indexable launch. Source: master checklist §1 and §2.7.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| GATE-01 | BLOCKER | OPEN-FOUNDER | Imprint — ladungsfähige Anschrift (street, house number) | §1 |
| GATE-02 | BLOCKER | OPEN-FOUNDER | Imprint — PLZ, Ort | §1 |
| GATE-03 | BLOCKER | OPEN-FOUNDER | Imprint — telephone number | §1 |
| GATE-04 | BLOCKER | OPEN-FOUNDER | Imprint — MStV address line | §1 |
| GATE-05 | BLOCKER | OPEN-FOUNDER | Imprint — notice date ("Stand") | §1 |
| GATE-06 | BLOCKER | OPEN-FOUNDER | Privacy — controller address/PLZ | §1 |
| GATE-07 | BLOCKER | OPEN-LEGAL | Privacy — third-country transfer basis (hosting) | §1 |
| GATE-08 | BLOCKER | OPEN-LEGAL | Privacy — transfer basis + Art. 28 DPA status (Cloudflare/Airtable) | §1 |
| GATE-09 | BLOCKER | OPEN-FOUNDER | Privacy — retention period | §1 |
| GATE-10 | P0 | OPEN-FOUNDER | Privacy — notice date ("Stand") | §1 |
| GATE-11 | BLOCKER | OPEN-FOUNDER | Mailbox verification — confirm `bjarne.dudzus@disce.de` exists and is monitored before public promotion | §1 |
| GATE-12 | BLOCKER | OPEN-LEGAL | Legal review of imprint + privacy notice (both currently marked draft) | §1 |
| GATE-13 | P2 | SUPERSEDED | Internal field-name decision; superseded in Batch D/CONV-05 | §1 |
| GATE-14 | BLOCKER | OPEN-FOUNDER + OPEN-CODE | Staging→production indexability decision + execution (robots allow, remove `noindex`, align canonical/OG/sitemap) | §1 |
| GATE-15 | P1 | OPEN-LEGAL | BFSG/accessibility applicability review | §1 |
| LEGAL-01 | P1 | OPEN-LEGAL | BFSG/accessibility applicability review (Sprint 4 §6 item 15) | §2.7 |

**Open questions / To be clarified**

- None introduced here. The master checklist's gate rule (§1) remains in force: GATE-01…12 before GATE-14.

---

### WP-B — Positioning, Messaging & Document Synthesis `[EXISTING + NEW]`

**Purpose:** Keep public positioning truthful and consistent, and (new) synthesize the existing strategy / positioning / customer-segment documents into the website content. Source: master checklist §2.1, plus the new task.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| POS-01 | P0 | DONE | Reframe homepage hero eyebrow/lede to the primary professional audience and the truthful planned status; no availability claim | §2.1 |
| POS-02 | P0 | DONE | Make status labels consistent site-wide ("Cervus research completed" / "private beta planned" / "next research phase in preparation — recruitment not open") | §2.1 |
| POS-03 | P1 | DONE | Apply codename policy: gloss "Kernel" at first contact; keep "Cervus" contextual; keep Midgard/Asgard deep-page only | §2.1 |
| POS-04 | P1 | DONE | Confirm "Proof of Principle" as the public research term; keep "Proof of Visibility" out of headline/marketing positions | §2.1 |

**Newly added work**

- `[NEW]` **NEW-04 — Synthesize strategy, positioning, and customer segment documents.**
  - Subtask 1: Gather the relevant strategy, positioning, and customer-segment documents. *(To be clarified: which exact documents. No document explicitly titled "customer segment" / "strategy" was found in the tracked tree; `sprint-1-positioning-messaging.md` and `sprint-0-triage-and-sprint-1-decision-pack.md` (Part B.1, B.2) contain positioning material.)*
  - Subtask 2: Identify, per document, what content is relevant to the website and where it would live (add to existing pages or adapt existing content).
  - Subtask 3: Define what must remain unchanged (product copy, headlines, CTAs, claims, translations, legal copy, content) versus what is explicitly approved for adaptation. *(Any copy/claim change remains subject to the master checklist's scope guardrail.)*
  - Subtask 4: Draft the resulting content changes for founder sign-off before any implementation.
  - Subtask 5: Reconcile the synthesized content with the locked positioning constraints in `sprint-0-triage-and-sprint-1-decision-pack.md` (audience = international professionals in Germany, B2–C1 plus role context; research-grounded but product relevance more prominent than academic framing).
  - **Open question:** Does "customer segment documents" refer to the primary-audience definition (international professionals in Germany) already captured in the locked decisions, or to separate, not-yet-in-repo documents?
  - **To be clarified:** Is there a single canonical source set, and who signs off the synthesized wording?

---

### WP-C — Information Architecture & Page Structure `[EXISTING]`

**Purpose:** Keep page roles, navigation, funnel routing, and the sitemap consistent. Source: master checklist §2.2.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| IA-01 | P1 | DONE | Execute page dispositions; keep `philosophy.html` a regular, publicly discoverable secondary page (founder correction) | §2.2 |
| IA-02 | P2 | DONE | Decide `beta.html` role; closed by founder decision #2 (deferred, unlinked, `noindex`, outside sitemap) | §2.2 |
| IA-03 | P1 | DONE | Add a small FAQ module on `waitlist.html` using the existing (unused) accordion; answer the conversion-relevant questions | §2.2 |
| IA-04 | P1 | DONE | Enforce one funnel per intent: one homepage-primary route (professionals), secondary intents by direct email | §2.2 |
| IA-05 | P1 | DONE | Place the Substack development-updates link as a clearly labeled external deep link in Status/About/Contact, not a homepage-primary CTA | §2.2 |
| IA-06 | P1 | OPEN-CODE | Update `sitemap.xml` to the real public set (include `kernel.html`, `status.html`, `waitlist.html`; exclude `beta.html` while deferred) | §2.2 |

**Open questions / To be clarified**

- GATE-14 (indexability) and the primary-domain question noted in `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md` §5 remain open in the master checklist; this document adds no decision.

---

### WP-D — Accessibility `[EXISTING]`

**Purpose:** Preserve and complete the accessibility work. Source: master checklist §2.3.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| A11Y-01 | P0 | DONE | Add `aria-invalid` + `aria-describedby` linking fields to their `.form-error` elements; live region for the error summary | §2.3 |
| A11Y-02 | P0 | DONE | Make `#successMsg` an `aria-live`/`role="status"` region and move focus to it after submit | §2.3 |
| A11Y-03 | P1 | DONE | Mirror the disabled/loading toggle with `aria-busy`; keep spinner decorative | §2.3 |
| A11Y-04 | P0 | DONE | Wrap primary content of every page in one `<main>` landmark | §2.3 |
| A11Y-05 | P1 | DONE | Add a visually-hidden-until-focused skip-to-content link targeting `<main>` | §2.3 |
| A11Y-06 | P0 | DONE | Add a keyboard-operable pause/stop control for the ticker, or make the logos a static row | §2.3 |
| A11Y-07 | P1 | DONE | Verify heading order and `<title>`/OG alignment per page | §2.3 |
| A11Y-08 | P1 | MEASURE-ONLY | Measure tap-target sizes and reflow at 320–430 px; fix only if a target is <24×24 or overflow occurs | §2.3 |
| A11Y-09 | P1 | DONE | Dispose of the dead accordion: repurpose for IA-03 or remove | §2.3 |
| A11Y-10 | P1 | DONE | Remove the dangling `kernel-loop` registry entry (or add the module if intended) | §2.3 |

**Cross-reference (not a stated dependency):** NEW-03 (animate hero images), NEW-06 (font readability), NEW-02 (waitlist redesign), and NEW-05 (team page) may touch accessible markup, focus visibility, motion, and contrast. Any such change must preserve the accessibility guardrail in `AGENTS.md` and the master checklist a11y results.

---

### WP-E — Performance `[EXISTING + NEW]`

**Purpose:** Measure and improve site performance. Source: master checklist §2.4, plus the new task.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| PERF-01 | P1 | DONE | Add font `rel="preload"` for above-the-fold faces; dedup duplicate `@font-face` declarations | §2.4 |
| PERF-02 | P1 | DONE | Measure LCP ≤ 2.5 s and CLS ≤ 0.1 (lab) | §2.4 |
| PERF-03 | P1 | MEASURE-ONLY | Measure INP ≤ 200 ms (field once traffic exists) | §2.4 |
| PERF-04 | P1 | MEASURE-ONLY | Measure AA contrast on hero/dark bands/form/footer | §2.4 |
| PERF-05 | P1 | MEASURE-ONLY | Run full keyboard-path measurement (nav, language switch, form, success/error) | §2.4 |
| PERF-06 | P1 | DONE | Mobile viewport checks (320–430 px; hero/form/CTA readable) | §2.4 |

**Also relevant (recorded in the master checklist, §2.4):** Hero Performance Pass 1 (responsive AVIF hero preload, lazy partner logos, modernized decorative assets) and Hero Performance Pass 2a (deferred decorative hero dot-field). Follow-up recorded: re-run PageSpeed Insights on the deployed site after commit. Detail file: `hero-performance-diagnostic.md`.

**Newly added work**

- `[NEW]` **NEW-01 — Get the website performance under control.**
  - Subtask 1: Establish what "under control" means here (target metrics/thresholds). *(To be clarified: no target beyond the existing PERF-02/03/04/05/06 thresholds has been stated for this new task.)*
  - Subtask 2: Re-run the recorded pre-launch follow-up: throttled PageSpeed Insights / Lighthouse on the deployed site (master checklist §2.13.10 and the Hero Performance Pass 1/2a follow-ups).
  - Subtask 3: Inventory current performance findings and any remaining open items across the repo (`hero-performance-diagnostic.md`, master checklist §2.4 and §2.13).
  - Subtask 4: Identify the concrete bottleneck(s) and the change(s) to address them. *(To be clarified: which changes are in scope.)*
  - Subtask 5: Re-measure after changes and record results, distinguishing local lab numbers from deployed/field numbers (as the master checklist does).
  - **Open question:** Does this task supersede, extend, or sit alongside the existing PERF-01…06 items? *(Not stated.)*
  - **Open question:** Are there defined budgets for total page weight, image delivery, or third-party impact? *(Not stated.)*
  - **To be clarified:** Which performance tooling may be used, given the dependency guardrail in `AGENTS.md`.

---

### WP-F — Conversion & Waitlist `[EXISTING + NEW]`

**Purpose:** Keep the single interest-registration funnel consistent and (new) redesign the waitlist page. Source: master checklist §2.5, plus the new task.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| CONV-01 | P0 | DONE | Replace generic CTA labels with the recommended interest-registration set | §2.5 |
| CONV-02 | P0 | DONE | Replace "join the beta"/"first cohort" with target interest-registration wording | §2.5 |
| CONV-03 | P0 | DONE | Complete thank-you state: accessible confirmation, privacy deep link, correction/withdrawal note | §2.5 |
| CONV-04 | P1 | OPEN-FOUNDER | Finalize the follow-up runbook (who/trigger/medium/no-trigger message) | §2.5 |
| CONV-05 | P0 | DONE | Form data minimization: drop/defer availability + microphone fields; simplify level; defer role/career data; adjust JS validation | §2.5 |
| CONV-06 | P2 | DEFERRED | Introduce privacy-friendly, low-traffic measurement only after validated interest (no trackers now) | §2.5 |

**Newly added work**

- `[NEW]` **NEW-02 — Redesign the waitlist so that it matches the visual style of the rest of the website, including its own background image—ideally `1.png`.**
  - Subtask 1: Define the visual target by matching the waitlist page to the shared design system / visual style of the other pages. *(Context: `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md` §4 already records that `waitlist.html` is "in the old blog layout", has its own stylesheet and its own language switcher, and is "the only page outside the design system"; master checklist DEF-03 also covers migration to the shared design system.)*
  - Subtask 2: Select and approve the background image. **Open question / To be clarified:** which `1.png`. Two files named `1.png` exist untracked in the tree — `Greenery/1.png` and `Kernel Background Images/1.png` — and neither is referenced by any HTML/CSS/JS today. Confirm the intended file.
  - Subtask 3: Process the chosen image through the approved image pipeline (`scripts/optimize_images.py`, per `AGENTS.md` image pipeline), without editing masters.
  - Subtask 4: Define how the background image interacts with text readability (background/scrim treatment), consistent with the font task NEW-06.
  - Subtask 5: Preserve existing waitlist behavior and content (form fields, consent, FAQ, trust block, success state) unless a change is explicitly approved.
  - Subtask 6: Re-check accessibility of the redesigned page (keyboard, focus, contrast, reflow) against the a11y guardrail and the A11Y-/PERF- items.
  - **To be clarified:** whether redesigning the waitlist includes migrating it off its self-contained stylesheet (DEF-03) or only restyling within the current structure. *(Not stated in the new task.)*
  - **Open question:** does the "own background image" apply only to the waitlist, or also to other pages that currently have none (`impressum.html`, `datenschutz.html`)? *(Not stated.)*

---

### WP-G — Trust, Evidence & Research Content `[EXISTING + NEW]`

**Purpose:** Keep public trust/evidence claims truthful and (new) expose the research reports/results in the Research section. Source: master checklist §2.6, plus the new task.

**Existing tasks**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| TRUST-01 | P0 | DONE | Add a compact trust/status block near the form | §2.6 |
| TRUST-02 | P1 | DONE | Decide the product-evidence strategy (Batch E decision: retain existing Kernel conceptual architecture; no additional public artifact approved) | §2.6 |
| TRUST-03 | P1 | DEFERRED | Implement the chosen evidence placement (deferred by the Batch E founder decision) | §2.6 |
| TRUST-04 | P1 | DONE | Final check that the single-purpose contact consent still suffices (source-level consistency only; legal review remains open) | §2.6 |
| TRUST-05 | P2 | OPEN-CODE | Use the claim register as a pre-publish verification reference | §2.6 |

**Newly added work**

- `[NEW]` **NEW-07 — Load and display the research reports/results in the Research section.**
  - Subtask 1: Identify the "Research section" (page and location). *(Context: `status.html` currently has no heading named "Research"/"Forschung"; research appears only inside copy — e.g. Cervus "Forschungssandbox zur abgeschlossenen Masterarbeit" at `status.html:133` and roadmap item III "Premium, KI & Forschung". Confirm where the Research section is / should be.)*
  - Subtask 2: Identify the actual report/result artifacts to load. *(To be clarified: no research-report or results artifact is present in the tracked tree. `Kernel Documents/` holds specs/protocols (`Disce_Evidenz_Validitaet_Unsicherheit_Protokoll_V0.1.md`, `Disce_Kernel_V0_Observatory_Spec_Canonical.md`, `Disce_Kernel_V0_PRD_Canonical_EN.md`, `Disce_Kernel_V0_Technical_Architecture_and_Stack_EN.md`), but no Cervus study report/results. The founder decisions state the report is completed but locate no report artifact in the repo.)*
  - Subtask 3: Confirm permission and scope for publishing/summarizing/linking the report(s). *(Source: `sprint-3-deep-dive-a11y-performance-evidence.md` and `sprint-0-triage-and-sprint-1-decision-pack.md` explicitly list "confirmation that the completed research report may be referenced/linked and what may be cited from it" as a founder input, and prohibit numeric effectiveness/accuracy claims without the report.)*
  - Subtask 4: Define the display format and placement. *(To be clarified.)*
  - Subtask 5: Reconcile with TRUST-02/TRUST-03 (the Batch E evidence decision currently approves no additional public artifact) and with the claim-register check TRUST-05. **This is a recorded inconsistency in the inputs: NEW-07 appears to require a public research artifact, while TRUST-02/TRUST-03 record that no additional public artifact is approved at this stage. Resolve with the founder before implementation.**
  - **Open question:** Are the report/results already approved for publication, and in what form (full document, executive summary, figures, or a plain link)?
  - **To be clarified:** language/translation and whether results may include metrics, given the "no numeric claims without the report" rule.

---

### WP-H — Visual System: Typography, Imagery & Motion `[NEW]`

**Purpose:** Address the two new visual-system tasks — font readability over background images and hero animation. Source: the two new tasks, plus repository design/motion guardrails.

**Newly added work**

- `[NEW]` **NEW-06 — Rework the fonts so that the text is easier to read over the background images.**
  - Subtask 1: Inventory the current typefaces and where text sits over background imagery. *(Context: `css/experimental.css` declares Archivo Black, Inter, Newsreader italic/roman; `waitlist.html` declares Inter and Noto Serif. Pages use photographic/AI background images and scrims, e.g. `index.html` hero, `philosophy.html`, `kernel.html`, `beta.html`, `status.html`.)*
  - Subtask 2: Identify the specific text/background combinations that are hard to read. *(To be clarified.)*
  - Subtask 3: Define the readability goal and how it will be verified (e.g. contrast and legibility review). *(To be clarified: target standard or method.)*
  - Subtask 4: Decide the change type — font choice, weight, size, letter-spacing, and/or background/scrim treatment. *(Not stated which; do not assume.)*
  - Subtask 5: Re-check that the change preserves the design reference `DESIGN-BRIEF.md` and WCAG AA contrast (accessibility guardrail).
  - Subtask 6: Account for both the shared stylesheet pages and the self-contained `waitlist.html` (see DEF-03).
  - **Open question:** Does "the background images" mean all imagery-bearing pages or a specific page/section?
  - **To be clarified:** Are fonts allowed to change, or is the intent to keep the current faces and adjust treatment only?
  - **To be clarified:** Does the change also cover headings vs body text differently?

- `[NEW]` **NEW-03 — Animate the hero images.**
  - Subtask 1: Identify which hero images/pages are meant. *(To be clarified: `index.html` hero already has a generative animated dot-field over the hero image; other pages have static hero imagery. "The hero images" scope is not stated.)*
  - Subtask 2: State the user/product purpose of the animation before any implementation. *(Required by the repo's generative-visuals guardrail in `AGENTS.md`: "State its user/product purpose first; if none exists, propose a static or CSS/SVG alternative.")*
  - Subtask 3: Read `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and `docs/generative-visuals/implementation-plan.md` before planning/implementing, as required by `AGENTS.md`, and use the `generative-web-visuals` skill.
  - Subtask 4: Ensure the animation is optional and deletable without losing page meaning, uses only existing CSS design tokens, and has a static/no-JS fallback equal to the current look (repo guardrail).
  - Subtask 5: Address motion accessibility (pause/reduced-motion) consistent with A11Y-06 and the accessibility guardrail.
  - Subtask 6: Evaluate performance impact and reconcile with the performance work package WP-E.
  - **Open question:** Does "animate the hero images" mean animating the photographic images themselves (e.g. motion effects) or adding an animated/generative layer over them?
  - **To be clarified:** Which pages and which hero images.
  - **To be clarified:** Whether the existing dot-field hero animation is considered sufficient or is to be changed.

- **Cross-reference:** `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md` records related, still-open image decisions (e.g. "at most one to two AI images per page", which homepage images stay, philosophy header images). These are not tasks supplied here, but they intersect NEW-02/NEW-03/NEW-06.

---

### WP-I — Team Page `[EXISTING + NEW]`

**Purpose:** Revamp the team page (new), while preserving the previously fixed team-page items. Source: the new task, plus master checklist records.

**Existing tasks affecting `team.html`**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| A11Y-07 | P1 | DONE | Heading-level fixes on `team.html` (six founder/seat headings `h3`→`h2`) | §2.3, §2.10.4 |
| CONV-01 | P0 | DONE | CTA labels on `team.html` updated to interest-registration wording | §2.5, §2.9 |

**Newly added work**

- `[NEW]` **NEW-05 — Revamp the team page.**
  - Subtask 1: Inventory the current page. *(Context: `team.html` has a `page-hero`, a `team-grid` with six cards — five founders plus an inline-styled "Der sechste Platz" CTO seat card — an advisor list, a full-width band picture, a dark "Offene Position — CTO" section, and footer. Portrait names are placeholder SVGs; Joscha is an explicit placeholder lacking role/surname/bio.)*
  - Subtask 2: Define what "revamp" covers — content, layout, imagery, structure, or all. *(To be clarified.)*
  - Subtask 3: Resolve the portrait-photo question already recorded in `docs/website-round2/…Notes_EN.md` §2/§3: collect portrait photos for all team members, or remove the image column entirely and switch cards to plain text (the notes state the goal is "information parity"). *(To be clarified: whether photos are available and who supplies them.)*
  - Subtask 4: Decide the disposition of the team band image, which the Round-2 notes §2 flag for removal under their image rule. *(To be clarified.)*
  - Subtask 5: Fill the open CTO seat / advisor content only with approved, factual information. *(Any copy change requires explicit approval.)*
  - Subtask 6: Preserve the DE/EN `data-lang` pairing, accessibility, CTA routing to the single funnel, and the existing DONE items (A11Y-07, CONV-01).
  - **Open question:** Does the revamp include the advisor list and the CTO open-position section, or the team grid only?
  - **To be clarified:** Is the N=150 RCT text (corrected to past tense on `team.html:74`) to be retained as-is?

---

### WP-J — Contact & Email Addresses `[EXISTING + NEW]`

**Purpose:** Change the email addresses shown/used on the website (new), coordinating with the existing mailbox-verification gate. Source: the new task, plus master checklist GATE-11/CONV-04.

**Existing related tasks / records**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| GATE-11 | BLOCKER | OPEN-FOUNDER | Mailbox verification — confirm `bjarne.dudzus@disce.de` exists and is monitored before public promotion | §1 |
| CONV-04 | P1 | OPEN-FOUNDER | Finalize the follow-up runbook (medium currently recorded as `bjarne.dudzus@disce.de`) | §2.5 |

**Newly added work**

- `[NEW]` **NEW-08 — Change the email addresses shown or used on the website.**
  - Subtask 1: Inventory every email address currently shown or used. *(Context: `bjarne.dudzus@disce.de` appears in imprint, privacy, waitlist, and possibly other contact/`mailto:` surfaces; the master checklist records the address locations in GATE-11.)*
  - Subtask 2: Confirm the new address(es) to use and where they apply (displayed contact, `mailto:` links, form/consent/withdrawal path, Airtable/follow-up runbook). *(To be clarified: the specific new addresses are not provided.)*
  - Subtask 3: Confirm the new mailbox(es) exist and are monitored — coordinated with GATE-11.
  - Subtask 4: Apply the change consistently across all surfaces (public pages, legal pages, form success/trust/FAQ withdrawal paths, follow-up runbook). *(Requires approval before editing legal/contact copy.)*
  - Subtask 5: Re-verify after the change that all displayed addresses and `mailto:` links resolve and match.
  - **Open question:** Which address(es) replace which, and is a role address (e.g. `info@`) intended versus a personal one?
  - **To be clarified:** Does the change affect legal pages (`impressum.html`, `datenschutz.html`) and therefore require the GATE-12 legal review to be re-run?

---

### WP-K — Newsletter / Substack Feed `[EXISTING + NEW]`

**Purpose:** Consider integrating the newsletter or Substack as an RSS feed or live feed (new), keeping it consistent with the existing Substack link and consent rules. Source: the new task, plus master checklist §2.2/§2.5/§2.6.

**Existing related tasks / records**

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| IA-05 | P1 | DONE | Place the Substack development-updates link as a clearly labeled external deep link in Status/About/Contact, not a homepage-primary CTA | §2.2 |
| CONV-04 | P1 | OPEN-FOUNDER | Follow-up runbook records that the interest list is **not** a general newsletter; any future Substack/newsletter opt-in must be separate, voluntary, unchecked, distinct purpose, and legally reviewed | §2.5 |
| TRUST-04 | P1 | DONE | Consent/purpose consistency verified; no newsletter/marketing scope added; legal review remains open | §2.6 |

**Newly added work**

- `[NEW]` **NEW-09 — Consider integrating the newsletter or Substack as an RSS feed or live feed.**
  - Subtask 1: Clarify what "consider" implies here — evaluate feasibility, or implement. *(To be clarified.)*
  - Subtask 2: Determine the desired integration: RSS/Atom feed, an embedded live feed, or both. *(To be clarified.)*
  - Subtask 3: Establish whether the existing Substack (`https://disce.substack.com`, referenced in footers and `status.html:281`) provides an RSS/feed endpoint, and what it returns. *(To be clarified: no RSS/Atom feed or "newsletter" reference currently exists in the repo.)*
  - Subtask 4: Reconcile with the dependency guardrail (`AGENTS.md`): no third-party services, CDNs, analytics, or scripts without explicit approval; assets/fonts stay self-hosted.
  - Subtask 5: Address privacy/consent implications, given the recorded rule that any newsletter opt-in must be separate, voluntary, unchecked, distinct purpose, and legally reviewed (CONV-04, TRUST-04, GATE-12).
  - Subtask 6: Preserve the DONE IA-05 decision (Substack stays an external, clearly labeled link, not a primary CTA) unless the founder explicitly changes it.
  - Subtask 7: Define the no-JS/fallback behavior and the placement on Status/About/Contact. *(To be clarified.)*
  - **Open question:** Is the intent a passive feed (read/subscribe externally) or an on-site subscribe flow? A subscribe flow would raise the consent questions above.
  - **To be clarified:** Whether a feed may be fetched client-side (third-party request) or must be generated/self-hosted to respect the dependency/privacy guardrails.

---

### WP-L — Deferred (only after validated interest) `[EXISTING]`

**Purpose:** Items intentionally deferred until validated interest. Source: master checklist §2.8.

| ID | Prio | Status | Preserved task | Master ref |
|---|---|---|---|---|
| DEF-01 | P2 | DEFERRED | Standalone security / AI-transparency page | §2.8 |
| DEF-02 | P2 | DEFERRED | Use-case pages / role-specific landing pages | §2.8 |
| DEF-03 | P2 | DEFERRED | Migrate `waitlist.html` to the shared design system (fonts/header/footer) — enables PERF-01 dedup | §2.8 |

**Cross-reference:** CONV-06 (deferred privacy-friendly measurement) is listed under WP-F. NEW-02 may relate to DEF-03; whether the waitlist redesign adopts the shared design system is **To be clarified** (see WP-F).

---

## 3. Complete task inventory (traceability)

Every existing task ID from the master checklist appears exactly once below, mapped to its work package. No existing ID was dropped.

| Work package | Existing task IDs |
|---|---|
| WP-A Legal & Release Gates | GATE-01…GATE-15, LEGAL-01 |
| WP-B Positioning, Messaging & Document Synthesis | POS-01, POS-02, POS-03, POS-04 |
| WP-C Information Architecture & Page Structure | IA-01, IA-02, IA-03, IA-04, IA-05, IA-06 |
| WP-D Accessibility | A11Y-01…A11Y-10 |
| WP-E Performance | PERF-01, PERF-02, PERF-03, PERF-04, PERF-05, PERF-06 |
| WP-F Conversion & Waitlist | CONV-01, CONV-02, CONV-03, CONV-04, CONV-05, CONV-06 |
| WP-G Trust, Evidence & Research Content | TRUST-01, TRUST-02, TRUST-03, TRUST-04, TRUST-05 |
| WP-H Visual System: Typography, Imagery & Motion | *(none — new tasks only)* |
| WP-I Team Page | *(cross-refs only: A11Y-07, CONV-01)* |
| WP-J Contact & Email Addresses | *(cross-refs only: GATE-11, CONV-04)* |
| WP-K Newsletter / Substack Feed | *(cross-refs only: IA-05, CONV-04, TRUST-04)* |
| WP-L Deferred | DEF-01, DEF-02, DEF-03 |

**Batch execution logs (Batch A–E) and the already-implemented DONE regression reference** remain in `master-checklist-website-revision.md` (§2.9–§2.13 and §4). They are evidence of completed work, not new tasks, and are not duplicated here.

---

## 4. Consolidated open questions / To be clarified

These are collected from the work packages above. None are decisions; each requires founder or source-document input.

| # | Open question / To be clarified | Work package |
|---|---|---|
| 1 | Which exact strategy, positioning, and customer-segment documents form the synthesis source set, and who signs off the wording? | WP-B |
| 2 | Does "customer segment documents" mean the locked audience definition or separate documents not found in the repo? | WP-B |
| 3 | Which `1.png` is intended — `Greenery/1.png` or `Kernel Background Images/1.png`? (Neither is referenced in code today.) | WP-F |
| 4 | Does the waitlist redesign migrate it to the shared design system (DEF-03) or restyle within its current structure? | WP-F, WP-L |
| 5 | Does the waitlist background image apply to other pages that currently have none (`impressum.html`, `datenschutz.html`)? | WP-F |
| 6 | What does "under control" mean for performance (targets), and does NEW-01 supersede or extend PERF-01…06? | WP-E |
| 7 | Which performance tooling may be used under the dependency guardrail? | WP-E |
| 8 | Where is the "Research section", and which report/result artifacts exist and may be published? | WP-G |
| 9 | How does NEW-07 reconcile with the TRUST-02/TRUST-03 decision that no additional public research artifact is approved at this stage? | WP-G |
| 10 | Does "the background images" for the font rework mean all imagery-bearing pages or specific ones? | WP-H |
| 11 | Is the font change a change of faces or an adjustment of treatment only? | WP-H |
| 12 | Which hero images are to be animated, and is it image motion or an animated/generative overlay? | WP-H |
| 13 | What is the user/product purpose of the hero animation (required before implementation)? | WP-H |
| 14 | What does "revamp" cover on the team page, and are portrait photos available? | WP-I |
| 15 | Which new email address(es) replace which, and does the change trigger a legal re-review? | WP-J |
| 16 | Is the Substack integration a passive feed or an on-site subscribe flow (consent implications)? | WP-K |
| 17 | May a feed be fetched from a third party, or must it be self-hosted, under the dependency/privacy guardrails? | WP-K |

---

## 5. Notes on what this document deliberately does not do

- It does not choose priorities, sequencing, dependencies, technical approaches, or scope for any new task.
- It does not add, alter, or remove existing tasks; existing IDs, priorities, and statuses are carried over unchanged.
- It does not execute any work package.
- It does not edit `master-checklist-website-revision.md`.
- It does not modify any website code, copy, legal text, or assets.