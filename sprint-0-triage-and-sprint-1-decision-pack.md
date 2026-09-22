# Sprint 0 — Critical Triage Revalidation & Sprint 1 Decision Pack

**Document type:** Decision document (prepares Sprint 2, Sprint 3, Sprint 4 and the final master checklist). **Not** the final implementation checklist. **No website changes are made or proposed as edits here.**

- **Subject:** DISCE website, repository `weltvorstellung` (tracked files), staging host `stage.weltvorstellung.de`.
- **Baseline used:** the four existing audit documents `sprint-1-positioning-messaging.md`, `sprint-2-information-architecture.md`, `sprint-3-ui-ux-accessibility-performance.md`, `sprint-4-conversion-trust-legal.md`; the benchmark `Pre-Launch-Website-Exhaustive-Report.md`; the tracked repository; and the founder decisions supplied in the task.
- **Date:** 2026-09-21.
- **Legal disclaimer:** This document is not legal advice. It does not invent company, address, provider, privacy, subprocessor, consent, or transfer information. Where such information is absent, it is marked as an open dependency.

## Evidence conventions used throughout

- **[FACT — repo]** directly observable in a tracked file (file:line).
- **[FOUNDER DECISION]** explicitly supplied in the task input.
- **[RECOMMENDATION]** this document's proposal; requires founder approval.
- **[UNRESOLVED ASSUMPTION]** not yet established by repo or founder input.
- **[BENCHMARK]** `Pre-Launch-Website-Exhaustive-Report.md` section citation.
- **[SPRINT n §x]** reference to an existing audit document.

**Founder-decision constraints that govern Part A and Part B (verbatim-intent, not verbatim quotes):** DISCE is a venture/project in development and not yet formally incorporated; the site may present DISCE as a project/company in development but must not claim a legal form or provider identity that does not exist; the responsible provider/imprint solution is currently unresolved; the site is intended to be public, visible, shareable, and commercially useful; it is not currently a customer-acquisition site for an available SaaS product; Cervus is completed (research report and Master's thesis work completed), technically dormant, and contextual background research rather than the primary public conversion frame; the next prototype is in development; a private beta and a next research phase are planned but not currently open; direct email can receive an individual response; research-grounded and methodologically rigorous should be a visible differentiator while concrete product relevance stays more prominent than academic framing.

---

# Part A — Critical Triage Revalidation

Revalidation scope: only the four previously flagged CRITICAL findings. Each was re-checked against the current tracked repository. The blocked/unblocked judgment refers to a **public, commercial, indexable release**. The site is currently in a non-indexable staging posture (`robots.txt` = `Disallow: /`; every page carries `noindex, nofollow`; see Sprint 2 §2.12), which affects containment options but not the underlying finding.

---

## A.1 — Stale / contradictory Cervus-study, availability, and contact-timing claims

**Classification:** `VERIFIED RELEASE BLOCKER`

**Exact repository evidence**
- `waitlist.html:7` — `<title>CERVUS Study — Join the Waitlist | Disce</title>`; same in `og:title` `waitlist.html:18` and `twitter:title` `waitlist.html:25`.
- `waitlist.html:475–476` — `<h1>` "Sei dabei – Pilotstudie" / "Join us – Pilot Study".
- `waitlist.html:479–480` — "Melde dich unverbindlich für unsere Studie an." (present-tense recruitment).
- `waitlist.html:498–499` — study described as ongoing research.
- `waitlist.html:506–507` — "Alle, die Deutsch als Fremdsprache sprechen (Niveau B2–C1)." (open recruitment criterion).
- `waitlist.html:513–514` — "**Wann?** Die Studie startet Mitte Juni 2026. Du setzt dich jetzt auf die Warteliste und wir melden uns bei dir." / "The study starts mid-June 2026. Sign up for the waitlist now and we'll contact you."
- `waitlist.html:554–555` — form intro "wir melden uns im Juni zur Terminbestätigung" / "we'll reach out in June to confirm your slot."
- `waitlist.html:711–714` — success message "Wir melden uns im Juni." / "We'll be in touch in June."
- Contradiction within the same tree: `index.html:90` — "Pilotphase — Abgeschlossen, Auswertung läuft" / "Pilot Phase — Completed, evaluation ongoing"; `status.html:78` — "Cervus — Abgeschlossen · Mai – August 2026" / "Complete · May – August 2026".
- The active study is also referenced in the privacy notice: `datenschutz.html:97–103` (section 4 "Anmeldung zur Warteliste und Studienteilnahme", retention "Löschung nach Abschluss der Studie").

**Sprint-document reference**
- Sprint 1 §1.8 (⚠️ CRITICAL); carried in Sprint 2 §2.14 and Sprint 4 §4.1/§4.3/§4.5/§4.12.

**Why it matters**
A visitor who follows the site's only conversion route is told a study starts in a month that is already in the past (relative to the site's own "Stand: September 2026", `status.html:61`) and is promised contact "in June". The rest of the site states the same phase is complete. This is the benchmark's "bait-and-switch / deceptive availability" risk (benchmark §10 "Missing beta transparency"; §6 "Beta status module": avoid fixed dates without certainty and avoid hidden constraints) and it is the page carrying the personal-data consent flow.

**Founder decision affecting it**
- Cervus is completed, not active; the research report and Master's thesis work are completed; Cervus is technically dormant with keys removed and no currently available public interaction. **[FOUNDER DECISION]**
- Recruitment for the next research phase is not currently open; a private beta is planned but scope, timing, selection criteria, and test conditions are not final. **[FOUNDER DECISION]**
- No fixed participation, access, or response promise may be made that DISCE cannot reliably fulfil. **[FOUNDER DECISION]**
- The site may use a truthful waitlist / interest-registration concept, but "waitlist" must be operationally defined. **[FOUNDER DECISION]**

**Decision required before implementation**
1. What "waitlist" means in the current pre-access state (what it registers, what it is not), per founder decision.
2. Whether the study-recruitment page is (a) repurposed into a truthful interest/waitlist page, (b) reduced to a completed-research/background context page, or (c) withdrawn from the public conversion path.
3. Whether the current Cervus page remains reachable at all before the provider/imprint question is resolved.

**Narrowly scoped safe temporary containment (option to be decided, not executed here)**
- Keep the site's existing non-indexable staging posture (`robots.txt` disallow + per-page `noindex`), and ensure the page does not present itself as *currently recruiting* or promise a response month. The smallest truthful state is a clearly-closed/complete context statement plus a non-promising interest registration. This still requires founder-approved wording and is therefore gated on the decision above.

**Blocks a public, commercial, indexable release?**
**Yes.** The page makes a present/future recruitment claim and a contact promise that the founder decisions prohibit and that the rest of the site contradicts. It cannot ship publicly as-is.

---

## A.2 — Draft / incomplete imprint and provider-identification status

**Classification:** `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED`

**Exact repository evidence**
- `impressum.html:70` — public banner "**Entwurf, nicht freigegeben.** … Sämtliche in eckigen Klammern gesetzten Felder sind vor Go-live zu vervollständigen."
- Provider identity is placeholder-only: `impressum.html:78–82` `[VOLLSTÄNDIGER NAME DER VERANTWORTLICHEN NATÜRLICHEN PERSON]`, `[LADUNGSFÄHIGE ANSCHRIFT …]`, `[PLZ, Ort]`.
- Contact placeholders: `impressum.html:86–87` `[TELEFONNUMMER]`, `[E-MAIL-ADRESSE]`.
- `impressum.html:91` `[NAME]` responsible natural person.
- Content-responsibility placeholders: `impressum.html:100–103`.
- Undated: `impressum.html:118` `Stand: [DATUM EINSETZEN]`.
- The page is linked from every page's footer, e.g. `index.html:302` (footer column "Rechtliches").
- The page correctly states pre-registration law literacy: `impressum.html:76` (until registration the responsible natural person must be named; "UG (haftungsbeschränkt)"/"i. Gr." may not be used before registration).

**Sprint-document reference**
- Sprint 4 §4.9.1 (⚠️ CRITICAL), §4.12.

**Why it matters**
The imprint is publicly reachable from every page but contains no provider identification. The benchmark marks provider identification as P0 ("Imprint … provider identification must be easily recognizable, directly accessible, and permanently available"; benchmark §8 Germany/EU; Master Checklist IA "Are legal, privacy, and contact information permanently findable?").

**Founder decision affecting it**
- The responsible provider/imprint solution is currently unresolved. **[FOUNDER DECISION]**
- The site may present DISCE as a project/company in development but must not claim a legal form or provider identity that does not exist. **[FOUNDER DECISION]**
- The site is intended to be public, visible, shareable, and commercially useful. **[FOUNDER DECISION]**

**Decision required before implementation**
1. The provider/controller solution for a not-yet-incorporated project (which natural person or entity is named, and in what form). This is a founder + legal decision; no information may be invented here.
2. Whether the imprint remains publicly reachable while in staging (it currently is, via the footer of every page).

**Narrowly scoped safe temporary containment (option to be decided, not executed here)**
- Maintain the non-indexable staging posture and the explicit draft-safety banner so the page is not presented as a final legal notice during pre-launch. No placeholder may be replaced with invented data.

**Blocks a public, commercial, indexable release?**
**Yes — conditionally and by definition:** a publicly promoted commercial site cannot ship an incomplete provider identification. It is classified strategic rather than a pure blocker because the founder has explicitly designated the provider solution as unresolved, so resolution is a strategic/legal decision rather than a wording fix.

---

## A.3 — Draft, placeholder-based, or technically inaccurate privacy-notice status

This previously-flagged finding is **composite**. It is revalidated here as two independently-classified sub-findings because one part is an unambiguous factual defect and the other depends on unresolved legal/provider facts.

### A.3a — Factual mismatch: the privacy notice states Google Fonts are loaded, but the code self-hosts fonts

**Classification:** `VERIFIED RELEASE BLOCKER`

**Exact repository evidence**
- `datenschutz.html:105–107` — "Auf der Warteliste-Seite werden derzeit Schriftarten von Google Fonts (Google Ireland Limited …) beim Seitenaufruf nachgeladen. Dabei wird die IP-Adresse an Google übermittelt." plus a note that a switch to locally delivered fonts is "vorgesehen".
- Contrary to that statement, `waitlist.html:33–46` declares local `@font-face` rules for `Inter` and `Noto Serif` loaded from `fonts/` (`waitlist.html:38`, `:45`), and no Google Fonts request exists anywhere in the tracked tree (verified by repository search across HTML/JS/CSS).
- `datenschutz.html:71` also states the notice "spiegelt den technischen Stand der Staging-Website" — which this paragraph does not.

**Sprint-document reference**
- Sprint 4 §4.9.2 (⚠️ CRITICAL), §4.12.

**Why it matters**
The benchmark requires the privacy policy to "reflect the forms, newsletter, hosting, analytics, video, calendar, and CRM services actually used" (benchmark §8 Germany/EU; Master Checklist "Does the privacy policy describe the actual tool stack?"). A privacy notice that misstates the actual processing is a transparency defect and, because it is publicly linked (`index.html:303`), a live statement.

**Founder decision affecting it**
- No founder decision resolves the wording; the repository already establishes the fact (fonts are self-hosted). **[FACT — repo]**

**Decision required before implementation**
- Confirm the final font-delivery approach is and remains self-hosted (no external font request). If confirmed, the privacy statement must match the code. No privacy/legal facts are to be invented.

**Narrowly scoped safe temporary containment**
- Keep the non-indexable staging posture. The specific remedy (removing/correcting the fonts paragraph) requires the founder/legal wording decision below and must not be inferred here; it is a factual correction, not a legal judgment call.

**Blocks a public, commercial, indexable release?**
**Yes.** A privacy notice containing a demonstrably false processing statement cannot be part of a public release.

### A.3b — Placeholder controller/transfer/retention fields and unapproved draft status

**Classification:** `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED`

**Exact repository evidence**
- `datenschutz.html:71` — public banner "**Entwurf, nicht freigegeben.** … anwaltlich zu prüfen."
- Controller placeholders: `datenschutz.html:79–83` `[VOLLSTÄNDIGER NAME]`, `[LADUNGSFÄHIGE ANSCHRIFT]`, `[PLZ, Ort]`, `[E-MAIL-ADRESSE]`.
- Third-country transfer basis unresolved for hosting: `datenschutz.html:90` `[ZU PRÜFEN: Angemessenheitsbeschluss EU-US Data Privacy Framework bzw. Standardvertragsklauseln …]`.
- Waitlist processing named (Cloudflare proxy; Airtable storage) but DPA status open: `datenschutz.html:99–102` ("Auftragsverarbeitungsverträge nach Art. 28 DSGVO sind mit beiden Anbietern abzuschließen und vor Go-live zu dokumentieren").
- Retention undefined: `datenschutz.html:103` `[FRIST FESTLEGEN]`.
- Undated: `datenschutz.html:126` `Stand: [DATUM EINSETZEN]`.
- The notice is footer-linked on every page, e.g. `index.html:303`.
- Positive facts already present and usable: named host (GitHub Pages, USA) `datenschutz.html:87`; named domain/DNS/email provider (STRATO AG, Berlin) `datenschutz.html:94`; data categories for the form `datenschutz.html:98`; rights and Berlin supervisory authority `datenschutz.html:117–118`; device-storage justification `datenschutz.html:109–111`; no automated decision-making `datenschutz.html:123–124`.

**Sprint-document reference**
- Sprint 4 §4.9.2 (⚠️ CRITICAL), §4.12.

**Why it matters**
The public privacy notice cannot identify the controller, cannot state a retention period, and leaves the transfer basis "to be checked". The benchmark marks the privacy policy P0 and requires purpose, recipients/services, retention, and withdrawal to be understandable (benchmark §8 Germany/EU).

**Founder decision affecting it**
- Provider/controller solution unresolved. **[FOUNDER DECISION]**
- No privacy/provider/transfer facts may be invented. **[TASK CONSTRAINT]**
- The privacy notice must match the actual tool stack (which changes if the waitlist page changes per A.1). **[FOUNDER DECISION + FACT]**

**Decision required before implementation**
1. Controller identity (same unresolved question as A.2).
2. Retention period for the interest/waitlist data (once "waitlist" is defined, A.1).
3. Confirmation that the Cloudflare/Airtable arrangements are the actual and final processing routes (or their replacement).
4. Legal review of third-country transfer bases and the final wording.

**Narrowly scoped safe temporary containment**
- Retain the non-indexable staging posture and the explicit draft banner; do not publish a commercial release until the controller, retention, transfer, and tool-stack facts are approved. No placeholders are to be filled with invented values.

**Blocks a public, commercial, indexable release?**
**Yes** (in combination with A.3a and A.2). Classified strategic because its resolution is a founder/legal fact-finding and review, not a copy fix.

---

## A.4 — Unsupported partner / ecosystem / logo relationship claims

**Classification:** `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED`

**Exact repository evidence**
- `index.html:269` — section label "Strategische Partner &amp; Ökosystem" / "Strategic Partners &amp; Ecosystem".
- `index.html:272–274` — three logo items: `images/partners/stromgold-logo.png` (alt "StromGold"), `images/partners/potsdam-startup-service.jpg` (alt "University of Potsdam, Potsdam Transfer Startup Service"), `images/partners/gruenden-in-brandenburg.jpg` (alt "Gründen in Brandenburg, WFBB").
- `index.html:275–281` — seven empty `ticker-logo` slots (hidden by CSS `:empty`, per Sprint 3 §3.5/§3.11).
- No relationship description accompanies the label on the page; no partner agreement, attribution note, or permission record was found in the tracked repository (search for partner-named documents returned none outside `images/partners/`).
- Counter-evidence about at least one relationship: `team.html:92` — co-founder Samuel Ingold is "Junior Associate bei StromGold AB." (translated: "Junior Associate at StromGold AB"), i.e. an employment/engagement relationship, not necessarily a "strategic partner" relationship.
- The remaining two logos correspond to startup-support/ecosystem programs (University of Potsdam Potsdam Transfer Startup Service; Gründen in Brandenburg / WFBB) whose exact relationship to DISCE is not stated in the repository.

**Sprint-document reference**
- Sprint 4 §4.7 (⚠️ CRITICAL), §4.12; Sprint 3 §3.5 (logo marquee anti-pattern).

**Why it matters**
The benchmark treats "logos without a clear relationship type" as a credibility risk and lists "Trusted by …" with weak proof and "premature social proof" as anti-patterns (benchmark §10; §8 "Problematic trust claims"). The founder's public-claim policy explicitly prohibits "any unsupported customer, partner, security, legal, performance, or AI capability claim". The finding is about the **relationship language and its evidence**, not the mere visual presence of the logos: the task explicitly instructs not to assume all logos are invalid.

**Founder decision affecting it**
- Any unsupported partner claim is prohibited now. **[FOUNDER DECISION]**
- Partners/organizations/tutors/schools are legitimate secondary audiences and may have their own contact route. **[FOUNDER DECISION]**
- Logos must not be assumed invalid; the relationship type must be audited. **[TASK CONSTRAINT]**

**Decision required before implementation**
1. For each of the three logos, the true relationship type (e.g. ecosystem/program affiliation, employer, accelerator, partner) and whether DISCE has the right to display the mark.
2. Whether the heading "Strategische Partner" is supportable for any or all of them, or must be replaced by accurate framing (e.g. ecosystem/program context) or removed.
3. What evidence must exist in the repository to substantiate any retained claim (per the founder's "subject to exact repository evidence and truthful wording").

**Narrowly scoped safe temporary containment**
- Maintain the non-indexable staging posture. Because the heading asserts an unsupported relationship, the safest temporary state is to not present the logos under a "Strategic Partners" claim until each relationship is confirmed; however, the choice between relabeling and removal is a founder decision and is not executed here.

**Blocks a public, commercial, indexable release?**
**Yes, in its current wording.** An unsupported "Strategic Partners" claim cannot ship under the founder's own public-claim policy. It is classified strategic because the correct resolution depends on founder-supplied relationship facts; the logos themselves are not presumed invalid.

---

## Part A summary

| # | Finding | Classification | Blocks public commercial indexable release? |
|---|---|---|---|
| A.1 | Stale/contradictory Cervus-study, availability, contact-timing claims | `VERIFIED RELEASE BLOCKER` | Yes |
| A.2 | Draft/incomplete imprint & provider identification | `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED` | Yes (resolution is a founder/legal decision) |
| A.3a | Privacy notice states Google Fonts loaded; code self-hosts them | `VERIFIED RELEASE BLOCKER` | Yes |
| A.3b | Privacy notice controller/transfer/retention placeholders, unapproved draft | `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED` | Yes (resolution is founder/legal fact-finding) |
| A.4 | Unsupported "Strategische Partner & Ökosystem" relationship claim | `VERIFIED BUT STRATEGIC / FOUNDER DECISION REQUIRED` | Yes, in current wording |

**Unresolved VERIFIED RELEASE BLOCKERS (as of this triage):** A.1 (stale recruitment/timing/promise on the only conversion page) and A.3a (privacy notice with a false tool-stack statement). No finding was classified `NOT VERIFIED / EVIDENCE INSUFFICIENT` or `SUPERSEDED BY FOUNDER DECISION`; however, the founder decisions do **supersede the premise** that the Cervus page is an active study, which is why A.1 is a blocker rather than a mere inconsistency.

---

# Part B — Sprint 1 Decision Pack

This pack transforms the Sprint 1 findings plus the founder decisions into decisions for positioning, status truthfulness, terminology, routing, and messaging guardrails. It contains **no final production copy**. Structured formulas and candidate status vocabulary are marked as requiring founder sign-off.

## B.1 Canonical public positioning

**Purpose:** one recommended canonical architecture (not a menu of generic alternatives), built from the founder decisions and the Sprint 1 gaps. Exact production sentences remain placeholders.

### Positioning architecture

**[PRIMARY FUTURE USER]**
International B2–C1 professionals in Germany, with initial focus on technology, engineering, and white-collar/knowledge-work profiles including comparable roles such as consultants. *(Source: founder decisions. Note: the current site persona `index.html:155` leads with doctors preparing for the Fachsprachprüfung; that remains a valid sub-context but is not the founder-stated initial focus, so it must not be the sole or lead identity.)*

**[SECONDARY PUBLIC AUDIENCES — explicit, downstream]**
Investors, companies, tutors, schools, strategic partners, and potential technical collaborators; plus future research participants as a distinct secondary interest. Founder decision: these must **not displace the primary professional-user story on the public homepage**.

**[CONCRETE CAREER CONTEXT]**
The job-search pipeline, job interviews, professional visibility, career transition, and career advancement/promotion. *(Founder decision.)* The design brief already identifies the German job interview (Bewerbungsgespräch · DACH) as the first V0 scenario (`DESIGN-BRIEF.md:19`); this is the concrete anchor the Sprint 1 audit found missing from the homepage category frame.

**[PRODUCT CATEGORY FRAME]**
A specialized additional qualification / capability system for ambitious professionals in high-stakes German career situations — explicitly **not** a substitute for general language instruction. *(Founder decision.)* This is the frame that reconciles the Sprint 1 tension between "AI German learning" (generic) and "institution of language" (over-broad).

**[HIGH-LEVEL MECHANISM]**
AI-supported, data-oriented training of high-stakes professional language situations, with feedback on register and communicative effect, built on the existing Kernel system layer. *(The Kernel and product-artifact architecture are already chosen and are not re-litigated here per the task; mechanism messaging may reference the existing `kernel.html` presentation.)*

**[RESEARCH / METHODOLOGICAL DIFFERENTIATOR]**
Research-grounded and methodologically rigorous development, substantiated by the completed Cervus proof-of-principle and the completed research report. Visible as a differentiator, but **concrete product relevance must remain more prominent than academic framing**. *(Founder decision.)*

**[TRUTHFUL CURRENT STATUS]**
A venture/project in development, not yet formally incorporated; next, more concrete prototype in development; private beta planned; next research phase planned; recruitment not currently open; no currently available external product interaction; direct email inquiries can receive an individual response; development/build updates are a legitimate future channel. *(Founder decision.)*

**[EXPLICITLY NON-CURRENT CAPABILITIES]**
No usable public product; no open beta; no open study recruitment; no immediate access; no "try now"; no fixed participation/access/response promise; no unsupported customer/partner/security/legal/performance/AI claims. *(Founder decision.)*

### Recommended message spine (formula, not production copy)

> For **[international B2–C1 professionals in Germany]** who face **[high-stakes German career situations — job interviews, transitions, advancement]**, DISCE is a **[specialized additional qualification / capability system]** that helps **[professional visibility through language]** — developed **[research-grounded and methodologically rigorous, currently building the next prototype]**. DISCE is **[a project in development, not yet incorporated; a private beta is planned]**; **[no product is currently publicly available]**.

This spine intentionally places the professional-user story and the category frame before the research differentiator and before the secondary audiences, per the founder decision.

---

## B.2 Public-status truth matrix

Columns: **Statement/claim · Allowed now · Allowed only with evidence/additional decision · Prohibited now · Exact evidence/rationale · Recommended status language.** "Recommended status language" is candidate status vocabulary for internal alignment and later founder approval — **not approved production copy**.

| Statement / claim | Allowed now | Allowed only with evidence / decision | Prohibited now | Exact evidence / rationale | Recommended status language (candidate, needs sign-off) |
|---|---|---|---|---|---|
| **Cervus** | Yes — as completed research/proof-of-principle context | Any expansion into "active", "ongoing", "now recruiting" requires a new founder decision | "Current study", "running study", "sign up to participate" | `status.html:78` "Cervus — Abgeschlossen · Mai – August 2026"; `index.html:90` "Pilotphase — Abgeschlossen"; contrast with `waitlist.html:513` "startet Mitte Juni 2026" | "Completed research / proof-of-principle context" |
| **Completed research report** | Yes | Linking/summarizing results requires the actual report and its scope/limitations (benchmark §8 "Research validation": source, scope, limitations) | Numeric effectiveness/accuracy claims without the report | Founder decision: report completed; no report artifact or figures located in the tracked tree | "Research report completed" (no metrics unless sourced) |
| **New prototype** | Yes — as in development | Naming/demoing it publicly requires a stable artifact and a decision about what may be shown | Presenting it as usable, available, or "try now" | `status.html:82` "Kernel v0 — in Entwicklung · seit September 2026"; `index.html:89` "Validierung / Pre-Seed" | "Next prototype in development" |
| **Private beta** | Yes — as **planned** | Timing, scope, selection criteria, test conditions, and any signup mechanics require founder decisions | "Open beta", "join the beta now", promised access or dates | Founder decision: beta planned but not final; `status.html:195–207` beta project is commented out; `index.html:256–257` currently says "join the beta … earliest cohort" | "A private beta is planned; details are not yet final" |
| **Next research phase** | Yes — as **planned** | Recruitment mechanics require a separate founder decision; if opened, benchmark §2 waitlist questions and §6 beta-status module apply | "Recruitment open", "apply now", any open-study framing | Founder decision: planned, recruitment not currently open; current `waitlist.html:506–507` recruitment criteria are open | "A next research phase is planned; recruitment is not currently open" |
| **Waitlist** | Yes — as interest registration, **only once operationally defined** | Must define what it registers and what it does not imply; if it implies access/queue position, that requires a real mechanism (benchmark §2 "Waitlist decision"; §7 "Gamification") | "Join the waitlist" implying guaranteed access, queue order, or beta entry; current page implies study contact in June | `waitlist.html:550–555`, `:705–713`; benchmark §6 weak pattern "Join the waitlist"; §7 CTA principles | "Register interest for future updates" (and, separately, future beta interest) — exact wording pending |
| **Active study** | No | — | Any present-tense study/recruitment claim | Founder decision: Cervus dormant, recruitment not open; `waitlist.html:479`, `:498`, `:513` currently contradict this | Not permitted in any current surface |
| **Product accessibility** | No | — | "Available now", "sign up and use", "try DISCE" | Founder decision: no currently available external product interaction | "No public product is available yet" |
| **Direct contact** | Yes — email can receive an individual response | Any stated response-time promise requires a founder decision | Invented response times, guaranteed reply windows | Founder decision: direct email can receive an individual response; no response-time promise present anywhere | "You can reach us by email" (no time promise) |
| **Development updates** | Yes — as a legitimate future channel | The channel mechanism, consent basis, and frequency require decisions; benchmark §7 follow-up sequence | Promising a frequency or content that is not operationally real; treating an external Substack as the site's owned list | Founder decision: updates are a legitimate future channel; current site only links `https://disce.substack.com` (`index.html:308`) with no consent linkage | "Development updates are planned" |

**Benchmark anchors used:** benchmark §6 "Beta status module" and "Pre-launch FAQ"; §7 "CTA principles", "Three conversion models", "Thank-you flow"; §8 "Problematic trust claims"; §2 "Waitlist decision"; §10 "Missing beta transparency".

---

## B.3 Terminology and codename policy

Scope is **public comprehensibility, status truthfulness, and claim discipline only**. The already-chosen Kernel/product-artifact architecture is not re-litigated.

| Term | Recommended classification | Rule / rationale |
|---|---|---|
| **DISCE** | Public and self-explanatory | Public brand spelling is DISCE. Never present a legal form (e.g. "UG", "GmbH", "i. Gr.") that does not exist; `impressum.html:76` already states this constraint. |
| **Kernel** | Public but immediately explained | Already a top-level nav item (`index.html:48`). Keep the existing chosen presentation, but ensure it is glossed as DISCE's own system layer at first contact; it is a repurposed technical word (`kernel.html:76–77`). |
| **Cervus** | Public but immediately explained — or contextual/deep-page only | Completed research/proof-of-principle context (founder decision). It must not be used as the primary public conversion frame. Currently appears in `<title>`/OG of the conversion page (`waitlist.html:7`, `:18`, `:25`) and in status cards (`status.html:78`, `:123`). |
| **Midgard** | Contextual/deep-page only | Internal-stage project name presented publicly in the status roadmap (`status.html:169`). Keep in the roadmap context with its explanatory sentence; do not surface as a standalone product/feature promise. |
| **Asgard** | Contextual/deep-page only | Same as Midgard (`status.html:184`); keep inside the directional roadmap with its "planned" status. |
| **proof of principle** | Public but immediately explained | Preferred framing for Cervus per founder decision ("completed research / proof-of-principle context"). Distinguish clearly from *product capability*. |
| **proof of visibility** | Internal-only / not surfaced without explanation; **[UNRESOLVED ASSUMPTION]** | Not present in the tracked site. If it is an internal construct, do not use it publicly until defined in the repo. |
| **research pilot** | Public but immediately explained, and only in the completed/contextual sense | "Pilot" must not imply an active or recruiting pilot. Tie to Cervus's completed status. |
| **prototype** | Public and self-explanatory | The founder-approved status is "next, more concrete prototype in development" (`status.html:82`). Never present the prototype as a usable product. |
| **private beta** | Public but immediately explained | Always with "planned" and "details not final" (founder decision; benchmark §6 Beta status module). |
| **waitlist** | Public but immediately explained — **and only after operational definition** | Must state what it registers and what it does not imply (see B.2). Must not imply guaranteed access, queue position, or beta entry. |
| **study** | Contextual/deep-page only | Because no study is currently recruiting, "study" must not appear as a present-tense public invitation. Use "completed research" for Cervus. |
| **development updates** | Public and self-explanatory | Legitimate future channel (founder decision). Must not promise frequency/content, and must not be conflated with an owned consent list until that is decided. |

---

## B.4 Audience and CTA routing model

Requirements: multiple funnels are allowed, but **one clear funnel per contact intent** rather than one misleading universal funnel (founder decision). No universal CTA is forced. Post-submit expectations must be truthful and must not promise response times not present in founder input.

### Route 1 — Future professionals / future users (PRIMARY homepage route)

- **Intended visitor:** international B2–C1 professionals in Germany; tech, engineering, white-collar/knowledge-work profiles incl. consultants.
- **Legitimate current value exchange:** registering interest in a future capability, and optionally receiving development/build updates; no product access.
- **What the CTA may say semantically:** "register interest", "join the interest list", "get development updates". (Semantics only; exact wording pending.)
- **What it must not imply:** available product, immediate access, beta entry, queue position, fixed timing, guaranteed response.
- **Priority:** **Primary** on the homepage.
- **Mechanism:** a truthful interest-registration form (repurposed from the current waitlist mechanism) or direct email; benchmark §7 Model A/B applies and the field set should be defined per intent.
- **Post-submit expectation:** confirmation on-page; state that this is interest registration only and that no access is currently available; do not promise a response month.

**Why this is the recommended primary route and why it avoids misleading availability claims:** it matches the founder-stated primary future audience and the site's core future use context (career/job-search language capability), and it names the only thing that is true in the pre-access state — interest can be registered. It does **not** assert that a product is available, that recruitment is open, or that a slot exists, so it satisfies the founder's prohibition on "immediate product access" and fixed promises while still giving the visitor a concrete next step (benchmark §7: action + value exchange + commitment + expectation; §6 weak pattern "Join the waitlist" is avoided only if the value exchange is explicit).

### Route 2 — Future research interest

- **Intended visitor:** people who want to participate in future research.
- **Legitimate value exchange:** being informed if/when a next research phase opens; contribution to research interest.
- **CTA may say semantically:** "register interest in future research" / "research interest".
- **Must not imply:** recruitment is open, selection, timing, eligibility, compensation.
- **Priority:** Secondary (deep-link or routed form option).
- **Mechanism:** a routed interest option (separate intent selector) or a dedicated email; best as a distinct funnel so it is not conflated with product waitlist.
- **Post-submit expectation:** state that recruitment is not currently open and no response window is promised.

### Route 3 — Future private-beta interest

- **Intended visitor:** professionals who might want private-beta access later (overlaps with Route 1 but is a distinct consent/intent).
- **Legitimate value exchange:** registering interest in a planned private beta.
- **CTA may say semantically:** "register interest in the planned private beta".
- **Must not imply:** beta is open, access is guaranteed, timing/selection exists.
- **Priority:** Secondary; may be merged into Route 1 with an explicit intent option (founder allows routed form options).
- **Mechanism:** routed form option or direct email.
- **Post-submit expectation:** state that the beta is planned, scope/timing/selection are not final, and no access is promised.

### Route 4 — Partners / organizations / tutors / schools

- **Intended visitor:** organizations, tutors, schools, and potential integration/ecosystem partners.
- **Legitimate value exchange:** a conversation about collaboration and the current development stage.
- **CTA may say semantically:** "contact us about collaboration" / "partner inquiry".
- **Must not imply:** an existing partnership, endorsement, or product capability; must not reuse the "Strategic Partners" wording unless substantiated.
- **Priority:** Secondary / deep-link-only.
- **Mechanism:** direct email is currently best (individual response per founder decision); a routed form option may be added later.
- **Post-submit expectation:** confirmation of receipt only; no response-time promise.

### Route 5 — Investors / strategic contacts / potential technical collaborators

- **Intended visitor:** investors, strategic contacts, potential CTO/technical co-founders and collaborators.
- **Legitimate value exchange:** a direct conversation about the venture and its current stage.
- **CTA may say semantically:** "contact us" / "start a conversation" (the existing `mailto:` pattern).
- **Must not imply:** a described investment round, valuation, or availability of the product.
- **Priority:** Secondary / deep-link-only (currently already served by `mailto:bjarne.dudzus@disce.de`, `kernel.html:496`).
- **Mechanism:** direct email; optionally a routed form option later.
- **Post-submit expectation:** confirmation only; no response-time promise.

**Routing rules:** each intent gets its own funnel with its own truthful post-submit expectation; the homepage's dominant CTA must be Route 1; other routes must not use equal visual emphasis on the homepage (benchmark §7 one/two CTAs; §10 "Conflicting CTAs").

---

## B.5 Messaging guardrails

Enforceable rules (all derived from founder decisions, Sprint 1 findings, and benchmark sections noted).

1. **Claims to avoid (prohibited now).** No usable public product; no open beta; no open study recruitment; no immediate/guaranteed access; no "try DISCE now"; no fixed participation/access/timing/response promise; no unsupported customer, partner, security, legal, performance, or AI capability claim. *(benchmark §6 weak patterns; §8 problematic trust claims; §10 anti-patterns.)*
2. **Distinctions that must remain visible.** (a) completed research vs. current prototype; (b) interest registration vs. access; (c) planned beta vs. open beta; (d) research/proof-of-principle vs. product capability. These four distinctions must never collapse into a single "available/coming" message.
3. **Research vs. product balance.** Research-grounded and methodologically rigorous may be a prominent differentiator, but concrete product relevance must lead: the career context and professional-user story come first; academic framing follows. *(Founder decision; consistent with Sprint 1 §1.2–§1.3.)*
4. **Evidence, numbers, logos, partners, quotes.** Every number, logo, partner name, and quote must be supported by repository evidence or a founder decision. Logos may remain where the relationship is accurately labeled; they must not be presented under "Strategic Partners" without a substantiated relationship type. Tests and pilots must be described with scope and status, not as product proof. *(benchmark §8 "Legitimate pre-launch proof"; founder public-claim policy.)*
5. **Current vs. future tense.** Present tense is reserved for what exists now (completed Cervus research, the research report, the project's existence, direct email). Everything else — next prototype, private beta, next research phase, updates — is future/planned tense and must say so. *(founder decision; benchmark §1 point 7, §6 precise copy.)*
6. **High-achievement / ambitious-professional positioning without elitism.** Describe the user by context and stakes (high-stakes German career situations, ambitious professionals), not by status markers, prestige adjectives, or claims of superiority. Avoid exclusionary or unsupported "top %, best, elite" claims; the audience definition is B2–C1 plus role context. *(founder decision; benchmark §2 "narrow but not exclusionary" trade-off; §6 weak patterns.)*
7. **AI, data, human review, product limits.** Describe AI's role as bounded and reviewable: what AI does, what the human decides, what data is used, what is not claimed. Preserve the existing conservative, bounded-claim language already present (`kernel.html:445–474`, `philosophy.html:264–269`) and do not let marketing surfaces assert capabilities the product has not established. *(benchmark §6 "AI communication"; §8 "AI trust"; Sprint 1 §1.9.)*
8. **Status wording must be dated and reconciliable.** Any status statement should carry an "as of" frame or be structurally true (e.g. "planned", "completed"), so the site cannot drift back into the current contradiction (A.1). *(benchmark §6 beta status module; Sprint 1 §1.7–§1.8.)*

---

## B.6 Decision dependencies for later sprints

Only decisions/unresolved facts that Sprint 2, Sprint 3, Sprint 4, and the final master checklist depend on. No implementation steps are given.

### Must be answered by founder
1. **Waitlist definition.** What "waitlist"/interest registration means operationally in the pre-access state, and what it must not imply (drives A.1, B.2, B.4; Sprint 4 §4.1/§4.3).
2. **Cervus page disposition.** Repurpose, reduce to background research context, or withdraw from the public conversion path (A.1; Sprint 2 §2.3/§2.14).
3. **Provider/imprint solution.** Who/what is named while unincorporated (A.2; Sprint 4 §4.9.1).
4. **Partner-logo relationships.** True relationship type and display permission for each logo, and the correct heading wording (A.4; Sprint 4 §4.7).
5. **Homepage primary route approval.** Confirm Route 1 (future professionals) as the dominant homepage conversion intent (B.4; Sprint 2 §2.4/§2.9).
6. **Private-beta and next-research-phase scope.** Whether any signup mechanic is offered now, and with what exact language (B.2/B.4; Sprint 4 §4.3–§4.5).
7. **Development-updates channel.** Owned vs. external (Substack), consent basis, and whether frequency is stated (B.2/B.4; Sprint 4 §4.10).
8. **“Proof of visibility” definition** (if it is intended as a public term) (B.3).

### Must be verified from repository/operations
1. **Final font-delivery reality** for the waitlist page to correct A.3a (already self-hosted per `waitlist.html:33–46`; confirm no external font request remains).
2. **Actual waitlist processing path and retention** (Cloudflare Worker → Airtable per `waitlist.html:871–878` and `datenschutz.html:99–103`), once the waitlist meaning is defined.
3. **Existence and location of the completed research report** and what, if anything, may be cited from it (B.2).
4. **Whether any fixed CTA/promise strings remain** across pages after the Sprint 1 baseline (Sprint 1 §1.8; `index.html:256–257`, `waitlist.html:513–555`).
5. **Analytics/measurement intent** (currently none; Sprint 4 §4.10) — whether any privacy-friendly measurement will be introduced.

### Requires legal or external review
1. Imprint/provider-identification wording for an unincorporated project (A.2).
2. Privacy-notice controller, retention, and third-country transfer wording, including the Cloudflare/Airtable arrangements (A.3b).
3. Correction of the Google-Fonts statement against the actual tool stack (A.3a).
4. BFSG/accessibility applicability review (Sprint 4 §4.9.5).
5. Any logo/mark usage rights and partner-relationship disclosures (A.4).

### Can be safely deferred (not blocking the first truthful public release, provided the blockers above are resolved)
1. FAQ module content (Sprint 1 §1.12) — benchmark P0 as a module, but can follow the status/route decisions.
2. Dedicated AI-transparency / security page structure (Sprint 2 §2.3; Sprint 4 §4.8) — the substance exists in `kernel.html`/`philosophy.html`; surfacing it can be sequenced.
3. Programmatic form error/status announcement (`aria-live`/`aria-invalid`; Sprint 3 §3.8) — accessibility improvement, not a release gate.
4. Logo-ticker pause control and ticker re-evaluation (Sprint 3 §3.6) — deferred pending A.4.
5. Core Web Vitals / contrast / keyboard measurement program (Sprint 3 §3.9) — deferred measurement.
6. Removal of dead accordion code and the dangling `kernel-loop` registry entry (Sprint 3 §3.11) — code hygiene.
7. `<main>` landmark additions and `<title>` consistency on the conversion page (Sprint 1 §1.13, Sprint 3 §3.11).

---

## Cross-references to the established baseline

- **A.1** ← Sprint 1 §1.8; Sprint 2 §2.14; Sprint 4 §4.1/§4.3/§4.5.
- **A.2** ← Sprint 4 §4.9.1.
- **A.3** ← Sprint 4 §4.9.2.
- **A.4** ← Sprint 4 §4.7; Sprint 3 §3.5.
- **B.1/B.2/B.3** ← Sprint 1 §1.1–§1.9, §1.14.
- **B.4** ← Sprint 4 §4.1–§4.5; Sprint 2 §2.2/§2.4.
- **B.5** ← Sprint 1 §1.7/§1.10/§1.11; benchmark §6/§8/§10.
- **B.6** ← all four audits' open dependencies.

**Benchmark sections referenced:** §1 (Executive Summary), §2 (Roles/Goals, Maturity phases, Waitlist decision), §3 (Information Architecture), §4 (Landing-Page Dramaturgy), §6 (Content/Messaging/Beta communication), §7 (Conversion and Waitlist Strategy), §8 (Trust/Transparency/Legal UX), §10 (Anti-Pattern Catalog), §11 (Master Checklist).

**Confirmed facts** are marked **[FACT — repo]** or cited by file:line; **founder decisions** are marked **[FOUNDER DECISION]**; **recommendations** are marked **[RECOMMENDATION]**; anything not yet established is marked **[UNRESOLVED ASSUMPTION]**. No founder aspiration has been converted into an implemented product capability, and planned beta/research/interest registration is treated throughout as **not currently open access**.
