# Website Content Strategy & Revision Plan

**Document type:** Planning and analysis only. No website code, copy, styles, routes, assets, configuration, or existing planning document has been changed.
**Date:** 2026-09-22
**Status:** Planning only. No task described here has been executed.
**Strategic source of truth:** `Disce — Making Expertise Visible.md` (repository root), subject to legal/evidence review where applicable.
**Companion documents (not modified):** `master-checklist-website-revision.md` (authoritative task detail), `website-revision-work-packages.md` (WP A–L structure), `DESIGN-BRIEF.md` (binding visual/copy claim guardrails), `founder-decisions-locked.md`, the `sprint-*` audits, and `Pre-Launch-Website-Exhaustive-Report.md`.

---

## 1. Purpose and Scope

This document translates `Disce — Making Expertise Visible.md` (hereafter "the Strategy") into a page-aware, website-wide **content revision plan**. It bridges four inputs:

1. the Strategy's narrative, positioning, and claims;
2. the current state of the website's copy and structure;
3. the existing master checklist (`master-checklist-website-revision.md`) and work packages (`website-revision-work-packages.md`, WP A–L);
4. concrete page-level content decisions for a later implementation phase.

It is explicitly **not**:

- a replacement for `master-checklist-website-revision.md` (which remains authoritative for task IDs, acceptance criteria, priorities, dependencies, and `file:line` evidence);
- an alteration of `website-revision-work-packages.md` or any sprint/decision document;
- an authorization to change copy, claims, routing, legal text, or assets. Every copy/claim change remains subject to the master-checklist scope guardrail and `AGENTS.md`;
- a source of new priorities, deadlines, or decisions. Where this document recommends, it explains its reasoning and marks the recommendation as such. Where information is missing, it records an open question instead of inventing an answer.

**Relationship to WP B.** WP B ("Positioning, Messaging & Document Synthesis") is the primary strategic anchor. NEW-04's subtask 1 asks *which* strategy/positioning/customer-segment documents form the synthesis source set; this document answers that by naming the Strategy as the new primary source and reconciling it against the previously locked positioning decisions, without overwriting those locks.

**Relationship to the other work packages.** Content decisions here create handoffs and dependencies to WP A (legal/release gates and public-claim safety), WP C (information architecture and page structure), WP F (conversion and waitlist), WP G (trust, evidence, and research content), WP H (visual system where it affects messaging hierarchy), WP I (team page), WP J (contact/email addresses), and WP K (newsletter/Substack). These are flagged per section and consolidated in §7–§9.

**Two guardrails carried from the inputs:**

- **Copy guardrail** (`DESIGN-BRIEF.md:10`): the brief governs design, not copy; existing copy stays as-is and headline/body/CTA/claim changes require explicit approval. `DESIGN-BRIEF.md:22` fixes the claim **"Sag, was du meinst." / "Say what you mean."** and states it must not be rewritten or translated inside the DE context.
- **Claim guardrail** (master checklist §0, §2.6 TRUST-05; `sprint-4-deep-dive-conversion-trust-legal.md` §8): public claims must be matched against the claim register and evidence pointers; no numeric effectiveness/accuracy claims without the research report.

---

## 2. Strategic Messaging Foundation

This section extracts the Strategy into a usable messaging foundation. Each item separates **recommended public-facing messaging** (candidate direction, not production copy), the **supporting rationale** in the Strategy, and any **qualification or validation** required before publication.

> **Reading note.** The Strategy is described as public-release-safe, but "safe to read" is not the same as "safe to publish as website copy." A large share of the Strategy is investor/partnership/recruiting/product/research material, not website material. §5 and §6 draw that line explicitly.

### 2.1 One-sentence category definition

- **Recommended public direction:** Disce is an AI-supported system for *professional* German (advanced level, B2–C2 range) that prepares internationally trained professionals for the specific high-stakes moments where their career is decided in German.
- **Rationale:** Strategy §1 Executive Summary ("an AI-powered learning system for advanced professional German (B2–C2)… a **professional performance layer**") and the "What Disce is — and is not" box (§3, lines 84–93).
- **Qualification required:**
  - The Strategy says **B2–C2**; the locked positioning in `sprint-0-triage-and-sprint-1-decision-pack.md` B.1 and `website-revision-work-packages.md:105` say **B2–C1 plus role context**; `DESIGN-BRIEF.md:16` says B2–C2. **This is a live conflict** — resolve before publishing any level range (see §8 Q1).
  - "Performance layer" is a strong, category-making phrase but is not yet on the website except implicitly. Whether to adopt it as public vocabulary is a WP B decision (see §3.1, §6 row "Category").

### 2.2 Core brand promise

- **Recommended public direction:** Disce makes expertise visible by giving professionals the German they need to perform in the moments that determine their career. (Strategy §6 closing promise, lines 201–203.)
- **Rationale:** The Strategy's central construct — "I am competent — but I cannot show it when it matters" (line 13) — and the vision "makes the expertise of international professionals visible" (line 25). `DESIGN-BRIEF.md:17` already encodes this as "professional visibility through language."
- **Qualification required:** The **fixed public claim remains "Sag, was du meinst."** (`DESIGN-BRIEF.md:22`). "Expertise visible" is compatible as a *supporting* formulation (eyebrow, section framing, meta description) but must **not** overwrite the headline claim without explicit founder approval. This is a WP B decision, not a silent substitution.

### 2.3 Problem statement

- **Recommended public direction:** Internationally trained professionals are already competent; their barrier is not knowledge but the situational performance of it in German at decisive moments. The failure point for advanced learners is usually **register**, not grammar.
- **Rationale:** Strategy §1, §3 Principle 2 (lines 45–47): "Good language does not rescue a missed task." The current homepage problem section (`index.html:144–163`: "Sie haben B2 oder C1, und trotzdem fehlt etwas.") is already close to this and rated strong by `sprint-1-positioning-messaging.md` §1.6.
- **Qualification required:** The Strategy's market-sizing and "career ceiling" narratives (lines 11–13, 150) are audience/positioning input, not proof. Avoid presenting the problem as a statistic unless sourced (see §6 "Problem severity/statistics").

### 2.4 Primary transformation/outcome

- **Recommended public direction:** From "competent but unable to show it" to "able to perform the decisive German moment" — passing the exam, completing recognition, or clearing the career ceiling — measured in real-world readiness rather than points or badges.
- **Rationale:** Strategy §3 Principle 1 ("think backwards from the goal"), Principle 5 ("evidence over engagement"), §5 scorecard ("measurable performance change… demonstrated communicative capability… verified at objective milestone checkpoints").
- **Qualification required:** The outcome vocabulary is aspirational and must not become an outcome *claim*. The master checklist claim register and `sprint-4-deep-dive-conversion-trust-legal.md` §8 prohibit numeric effectiveness, pass-rate, recognition-timeline, or career-outcome claims without the research report. Publicly available evidence does not currently exist in the repository (see §6).

### 2.5 Primary audience

- **Recommended public direction:** Internationally trained professionals in Germany who already hold real expertise and need to perform it in German — starting with professionals preparing for regulated or career-decisive German contexts.
- **Rationale:** Strategy §1 and §5 audience table (lines 146–151): physicians, nursing professionals, white-collar professionals, academics.
- **Qualification required — major conflict:** The locked founder decision #5 (`founder-decisions-locked.md`) fixes the **primary homepage audience** as international professionals in Germany (engineering/tech, consulting, comparable white-collar) in a job-search/interview/advancement context, with doctors/the *Fachsprachprüfung* as a **valid sub-context but not the lead identity**. `sprint-0-triage-and-sprint-1-decision-pack.md` B.1 reinforces B2–C1 plus role context. The Strategy leads with physicians and names four audiences plus an institutional buying audience. **The Strategy does not by itself overturn locked decision #5.** The current homepage (`index.html:192–206`) already names two groups (physicians + professionals) and should not silently expand or reorder. Resolve in §8 Q2.

### 2.6 Institutional audience

- **Recommended public direction:** For hospitals, employers, universities, and professional bodies, Disce turns language from an unmanaged risk into a measurable asset, with auditable progress data and a defensible answer to "does the investment work?"
- **Rationale:** Strategy §4 value proposition for institutions (line 117) and Principle 7 ("trust is built through institutions", lines 79–81).
- **Qualification required:** This is currently a **forward-looking, largely unproven** value proposition. The repository contains **no institutional page, no pilot case study, no named institutional partner in the confirmed partner block, and no outcome data**. Master checklist DEF-02 defers use-case/role pages "only after validated interest." The Strategy's "complete our first institutional pilots" (line 195) is a forward plan, not a current fact. Institutional messaging must therefore be **held or framed as intended scope, not current capability**, until evidence exists (see §5.4, §6 row "Institutional adoption/partnerships").

### 2.7 Differentiation statement

- **Recommended public direction (safe version):** *One engine, many professional contexts* — a learning architecture built for situational, register-aware professional German, configured per professional world rather than broadened across languages.
- **Rationale:** Strategy §3 Principle 3 ("vertical depth over horizontal breadth"), §5 "One engine, many contexts" (lines 155–157).
- **Qualification required — significance:** The Strategy's stronger differentiation material is **investor-facing competitive logic**, not website copy:
  - "the intersection… is unoccupied. Disce is there" (line 109);
  - "the architecture is the moat" (line 51);
  - "no other platform offers" scenario depth (line 15) and "cannot be crawled… or synthesized" (line 126);
  - "taken successful replicators four to seven years to approach" (line 126);
  - "last mover in our category" (line 173);
  - "a market small enough that giants rationally ignore it" (line 131).
  None of these are substantiated in the repository and several are comparative/superiority claims. They are **strategic input, not automatic website copy** (per the task brief). Public differentiation should rest on *what Disce does differently* (goal-first, register-aware, evidence-over-engagement) rather than on *what competitors cannot do* (see §6 row "Unoccupied category / competitive comparison").

### 2.8 Evidence/trust posture

- **Recommended public direction:** "We are building the evidence system that can produce certainty — rather than claiming certainty we do not yet have." Honesty about what is complete (Cervus as a completed Proof of Principle) and what remains open.
- **Rationale:** Strategy §3 Principle 5 (line 71) and Principle 4 (line 61, "defend the causal theory; iterate the delivery mechanism"). This posture is already the site's strongest existing trait (`status.html` "Wo Disce heute steht."; `waitlist.html` trust block `:758–775`; FAQ `:821–915`).
- **Qualification required:** The website may describe *method* (research-grounded, multidimensional measurement) but must not convert method into *result*. `TRUST-02`/`TRUST-03` (Batch E founder decision) currently approve **no additional public evidence artifact**; `NEW-07` appears to contradict this (see §6 row "Research report / results" and §8 Q4). Specific soft claims already live on the site are unsupported and should be reviewed: `index.html:217` ("auf gesicherter Lernpsychologie"), `philosophy.html:234` ("das GER-Niveau zuverlässig vorhersagt"), `philosophy.html:197` (unnamed "Studien zeigen").

### 2.9 Privacy/compliance posture

- **Recommended public direction:** Privacy and compliance are treated as product properties, not obligations — GDPR-native, European hosting, and learner data never used for third-party commercial model training.
- **Rationale:** Strategy §3 Principle 6 (lines 73–77).
- **Qualification required — major conflict:** The Strategy claims a GDPR-native, EU-hosted architecture "from the ground up" and "learner interaction data is never exposed to third-party commercial model training pipelines." The repository's actual, current data-processing description names **GitHub Pages (USA)** for hosting/logs (`datenschutz.html:90–95`), **Cloudflare proxy** and **Airtable (USA)** for the waitlist (`datenschutz.html:103`; worker endpoint `waitlist.html:1051`), and leaves the **third-country transfer basis and Art. 28 DPA status as open legal placeholders** (GATE-07/GATE-08, `datenschutz.html:94,106`). `kernel.html:238–239` currently asserts "Anbieterneutral und EU-gehostet" / "Betrieb in einer kontrollierten EU-Region" in the present tense for a V0-in-development system. Therefore:
  - the Strategy's privacy language **cannot be published as-is today**;
  - any EU-hosting claim must be reconciled against the real tool stack and legal review (GATE-07/08/12);
  - the "no third-party commercial model training" commitment is currently a **governance intent**, not a documented contractual fact in the repository, and needs substantiation before it becomes a public commitment (see §6 row "Data / AI / training pipeline").

### 2.10 Messaging principles (3–5) governing all public copy

Derived from the Strategy and existing guardrails:

1. **Outcome before language.** Lead with the decisive professional moment, not with vocabulary, grammar, or streaks. (Strategy Principle 1.)
2. **Register over grammar.** Name the real failure mode — the ability to move between *Fachsprache* and *Umgangssprache* under pressure. (Strategy Principle 2.)
3. **Honest status, dated and qualified.** Present tense only for what exists; planned/aspirational states must be labeled as such. (Master checklist §0; `sprint-0` B.5.5/B.5.8.)
4. **Evidence over engagement — including about ourselves.** No engagement metrics as proof; no outcome claim without evidence. (Strategy Principle 5; claim register.)
5. **Vertical, not generic.** Every page should read as professional-German-specific, never as "learn a language." (Strategy Principle 3; `DESIGN-BRIEF.md:16`.)

### 2.11 "What Disce is / is not" — adapted for website use

Adapted from the Strategy's detail box (§3, lines 84–93), with claim-safety notes:

| Disce is… | Disce is not… | Website treatment |
|---|---|---|
| A professional performance layer for advanced German. | A general language-learning app. | Safe to use; already echoed in `index.html:194` ("Disce ist kein allgemeines Deutsch"). Recommend strengthening the category frame in the hero/meta. |
| A goal-first system that starts from the professional outcome. | An exam-prep course. | Safe, but avoid implying exam-outcome results. CEFR is a milestone, not a guarantee. |
| An active, adaptive, feedback-driven system. | A passive content platform. | Safe; supported by the Kernel/mechanism page. |
| A category of its own (professional certification/performance layer). | "A better version" of an existing language product. | **Use the positive clause only.** The comparative clause ("no language-learning platform has ever built") is a superiority claim — hold or qualify (§6). |

---

## 3. Messaging Hierarchy

A hierarchy from homepage-level language to deeper pages. Final production copy is deliberately **not** written here; limited example formulations are included only where needed to remove ambiguity.

### 3.1 Hero-level message (layer 1)

- **Job:** category + primary audience + stakes + truthful status, above the fold.
- **Current state:** `index.html:117–119` — eyebrow "Für internationale Fachkräfte in Deutschland"; h1 "Sag, was Du meinst."; lede already carries diagnosis/practice/feedback + status. This is already aligned with locked #5 and POS-01 (`master-checklist-website-revision.md` §2.1).
- **Recommended direction:** Keep the fixed claim as the h1; let the eyebrow name the audience/context and the lede carry category + mechanism + status (as it does). The open question is whether the *category* phrase ("professional German / professional performance layer") should be more explicit in the eyebrow or a kicker, given the benchmark's "headline should not be a poetic slogan without a product category" (`Pre-Launch-Website-Exhaustive-Report.md` §4, `sprint-1-positioning-messaging.md` §1.5).
- **Example formulation (illustrative only):** eyebrow/label = "Berufliches Deutsch für internationale Fachkräfte" — but note this collides with the footer's generic "KI-gestütztes Deutschlernen" (`index.html:340`), which should be reconciled (§4).

### 3.2 Supporting explanation (layer 2)

- **Job:** the problem and the transformation — "competent but invisible"; register as the real gap.
- **Current state:** `index.html:144–163` (problem, strong) and `index.html:215–240` (how it works). `DESIGN-BRIEF.md:17–20` supplies the core construct.
- **Recommended direction:** Preserve the problem section; ensure it names *register* and the *decisive moment*, and does not present statistics without a source.

### 3.3 Audience-specific proof/value messages (layer 3)

- **Job:** make the abstract promise concrete for each audience.
- **Current state:** `index.html:192–206` names two groups (physicians preparing for the *Fachsprachprüfung*; professionals who need German that carries at work).
- **Recommended direction:** This is the layer where locked #5 (white-collar primary, physicians as sub-context) and the Strategy (physicians-led, four audiences) **conflict**. Recommendation: hold the current two-group framing as the homepage's public scope until the audience-breadth decision (§8 Q2) is made; do **not** expand to nursing/academics/institutions on the homepage without that decision. Institutional and additional-audience messaging belongs on candidate deeper pages (§5.3, §5.4).

### 3.4 Product/approach explanation (layer 4)

- **Job:** explain the mechanism — goal-backwards, adaptive diagnostics, register-aware feedback, task-based scenarios.
- **Current state:** `kernel.html` (mechanism, technical), `index.html:215–240` (user-level "how it works"), `philosophy.html` chapters (learning philosophy/measurement).
- **Recommended direction:** Keep the two registers separate: `index.html` for the user-level approach; `kernel.html` for the architectural mechanism. Caution: `kernel.html` currently describes V0 architecture in the present tense while labeling it "in Entwicklung" (`kernel.html:496–497`); the mechanism page should distinguish *design intent* from *shipped capability* (see §6 row "Product/AI capability and architecture").

### 3.5 Trust, evidence, privacy, and institutional credibility layer (layer 5)

- **Job:** make honesty and data responsibility visible; provide the evidence/limitations posture.
- **Current state:** `status.html` (canonical status/roadmap), `waitlist.html:758–775` trust block, `philosophy.html:265–273` (technology/governance), `kernel.html:456–477` (explicit limits/non-claims). Privacy lives in `datenschutz.html`.
- **Recommended direction:** Consolidate a *public* evidence posture from the Strategy's Principle 5 ("building the evidence system…"), while keeping the actual legal/data facts in `datenschutz.html`. Institutional credibility messaging should **not** be added until evidence exists (§6, §8 Q5).

### 3.6 Conversion message and CTA logic (layer 6)

- **Job:** one funnel per intent — "Interesse anmelden / Register interest" as the single primary route for professionals; secondary intents by direct email.
- **Current state:** Uniform CTA already applied (`master-checklist-website-revision.md` §2.9 Batch A); homepage routes to `waitlist.html`; `kernel.html` routes to status/email; `philosophy.html` has **no in-content CTA** (only nav/footer).
- **Recommended direction:** Preserve locked #1/#6 (interest registration, no queue/date/guarantee) and the IA-04/IA-05 routing. Any new CTA introduced by the content revision must reuse the existing label set and the single funnel; do not introduce a competing primary CTA (WP C/WP F).

---

## 4. Current Website: Gaps, Misalignments, and Opportunities

Assessment is grounded in the current files. "Alignment" is judged against the Strategy plus the locked decisions. Where the Strategy and locked decisions conflict, the row notes the conflict rather than resolving it.

| Page / file | Current purpose/message | Alignment | Specific issue or opportunity | Recommended content direction | Work package(s) | Dependencies / open questions |
|---|---|---|---|---|---|---|
| `index.html` hero (`:117–119`) | Audience + fixed claim + mechanism/status | **Aligned** | Category phrase still implicit; footer elsewhere says "KI-gestütztes Deutschlernen" | Keep fixed claim; make professional-German category explicit in a kicker/eyebrow or lede; reconcile footer tag | WP B, WP H | Category vocabulary decision; tagline lock (`DESIGN-BRIEF.md:22`) |
| `index.html` problem (`:144–163`) | "B2/C1 yet something is missing"; register gap | **Aligned**, partly **unsupported** | `:162` ("Die meisten Lernenden, die B2 erreichen, bleiben dort stehen…") is a statistic-like claim with no source | Keep structure; either source the claim or reframe as qualitative | WP B, WP G | Evidence/claim review |
| `index.html` audience (`:192–206`) | Two groups: *Fachsprachprüfung* doctors + professionals needing work German | **Partially aligned / conflicted** | Strategy leads physicians; locked #5 makes white-collar primary and doctors sub-context; `:200` asserts exam format and "klinisches Wissen ist selten das Hindernis" unsourced | Hold current two-group scope until audience decision; qualify exam/format statements | WP B, WP C | §8 Q2 audience breadth; §8 Q1 level range |
| `index.html` how-it-works (`:215–240`) | Goal → benchmark → daily coaching | **Aligned** | `:217` "auf gesicherter Lernpsychologie" unsupported as stated | Reframe to "research-grounded approach" without implying validated efficacy | WP B, WP G | Claim review |
| `index.html` pull-quote (`:125`, `:179`, `:270`) | Same quote 3× verbatim | **Misaligned (quality)** | Repetition dilutes hierarchy; flagged by `sprint-1-positioning-messaging.md` §1.6 | Replace at least one repetition with substantive outcome/approach content | WP B, WP C | Copy approval |
| `index.html` outcome section (`:269–272`) | Quote repeated, no distinct outcome content | **Misaligned** | No dedicated transformation/outcome content; benchmark wants outcome clarity | Add a distinct outcome/transformation block (non-numeric) | WP B | Claim review |
| `index.html` team teaser (`:280–284`) | 5 founders + advisors, Berlin scene/Uni Potsdam | **Partially aligned** | "Strategische Partner & Ökosystem" ticker (`:313–330`) carries relationship claim and 7 empty placeholder tiles | Keep confirmed ticker per locked #4; label relationship type; remove empty tiles or leave as-is per founder | WP I, WP G | Locked #4; Round-2 notes §3 |
| `index.html` footer tag (`:340`) | "KI-gestütztes Deutschlernen… Berlin/Potsdam" | **Misaligned (category)** | Generic "German learning" contradicts the Strategy's category distinction | Update footer tag to professional-German framing | WP B, WP C | Copy approval; tagline lock |
| `philosophy.html` (essay) | Long-form manifesto: philosophy, psycholinguistics, measurement, AI/governance | **Partially aligned / strategically outdated** | Audience list `:254` is far broader than locked positioning; present-tense platform claims for unbuilt product `:252–253, :235–236`; unsourced science `:197, :234`; internal spec/monetization detail `:270–273`; grand "Institution der Sprache" `:254` | Keep as deliberate long-form; tighten audience scope, convert product claims to intent, source or soften science, review privacy/monetization candor | WP B, WP H, WP G | §8 Q2; claim review; founder approval (philosophy copy is founder-authored) |
| `status.html` (canonical status) | "Where Disce stands today" + project ledger + long-range roadmap | **Aligned** | Hidden HTML comments expose internal process (`:71–73, :106–110, :139–144, :158–163, :199–211, :264–267`); "Gründung Geplant · Q4 2026" reads as a committed date; "interne Roadmap" phrasing | Keep sober status; remove/neutralize internal comments; ensure planned dates are clearly directional | WP B, WP C, WP G | Date policy; copy approval |
| `kernel.html` (mechanism) | System layer, cycle, layers, compounds, limits | **Partially aligned** | Present-tense architecture/EU-hosting claims (`:238–239`), competitive "surface around a model" (`:412–413`), "prüfbar" data trace for unbuilt V0; meta description claims triangulation/calibration | Keep mechanism page but distinguish design intent from shipped capability; align hosting language with `datenschutz.html`; move competitive framing out of public copy | WP B, WP G, WP H | §6 rows; GATE-07/08 |
| `team.html` (team) | 5 founders + open CTO seat + advisors | **Partially aligned** | **N=150 RCT claim** (`:74, :78`); Joscha full placeholder (`:110–114`); portraits are placeholder SVGs; band image flagged by Round-2 notes; CTO section says "Link unten" but has no CTA | Verify/qualify N=150 and completed-study framing; resolve placeholders; align with WP I revamp | WP I, WP G | §8 Q6; locked decision on research wording |
| `waitlist.html` (conversion) | Interest registration + trust + FAQ | **Aligned** | Outside the design system (DEF-03); `og:locale` mismatch `:20`; privacy note says "nicht an Dritte weitergegeben" `:792` vs named Cloudflare/Airtable processors; 4-week deletion `:792` vs placeholder `datenschutz.html:107`; footer "Ein Forschungsprojekt der BSP Berlin" `:924–925` differs from other pages | Preserve behavior/content; WP F redesign; reconcile data statements with legal page | WP F, WP D, WP G, WP A | GATE-07/08/12; DEF-03; NEW-02 |
| `impressum.html` (imprint) | Legal notice (draft) | **Blocked** | Address/PLZ/phone/MStV/date placeholders; draft banner `:72–75` | No content revision beyond closing gates | WP A | GATE-01…05, GATE-12 |
| `datenschutz.html` (privacy) | Privacy notice (draft) | **Blocked / conflicted** | Controller address, transfer basis, Art. 28 DPA, retention, date placeholders `:84, :94, :106, :107, :129`; naming GitHub Pages/Cloudflare/Airtable (USA) conflicts with Strategy's EU-hosting claim | No content revision beyond closing gates; reconcile any public EU-hosting claim with actual stack | WP A, WP G | GATE-06…10, GATE-12; §6 |
| `beta.html` (deferred) | "Prototyp in Arbeit." | **Aligned (intentionally deferred)** | Unlinked, `noindex`, outside sitemap (locked #2) | Leave deferred; do not link | WP C (IA-02) | Locked #2 |
| `sitemap.xml` | Lists 5 pages; omits `kernel.html`, `impressum.html`, `datenschutz.html` | **Misaligned** | Mismatch with the real public set; all pages are `noindex` | Fix in IA-06; include imprint/privacy; keep beta excluded | WP C | GATE-14 |
| `robots.txt` | `Disallow: /` staging posture | **Aligned (staging)** | Must be lifted deliberately before launch | Keep until GATE-01…12 close | WP A | GATE-14 |

**Cross-cutting findings**

1. **Category language is inconsistent.** The Strategy defines Disce against "German learning"; the footer tag (`index.html:340` et al.) still uses "KI-gestütztes Deutschlernen." This is the single most repeated generic phrase across pages.
2. **Present tense leaks into unbuilt capability.** `philosophy.html:235–236, 252–253`, `kernel.html:238–239, 412–413`, and `status.html:90` all describe unbuilt or aspirational states in ways that read as current. This directly conflicts with `sprint-0` B.5.5.
3. **No public evidence layer exists.** There is no research page, no report artifact in the tree, and no measured outcome. `status.html` says validation is coming; it states no results. This is honest but leaves the Strategy's evidence narrative without a public home (see §5.5).
4. **No institutional/employer surface exists.** The Strategy's institutional value proposition has no page and no evidence; DEF-02 defers use-case pages.
5. **Internal-strategy material is visible in source comments** (`status.html`) and in body copy (`philosophy.html` monetization, taxonomy, "intern" phrasing). This is a leakage risk, not just a messaging risk.
6. **Legal facts and marketing claims are not yet reconciled** (EU hosting, processor list, retention). This must close before any privacy-forward marketing claim is published.

---

## 5. Proposed Website-Wide Content Architecture

This section recommends how the Strategy's narrative should be distributed. It labels **existing pages to revise**, **candidate new pages/sections**, and **items that depend on decisions rather than being immediate recommendations**.

### 5.1 Homepage sections and their narrative role

Existing page to revise (`index.html`). Recommended section roles, mapped to the Strategy:

1. **Hero (layer 1):** category + primary audience + stakes + truthful status. Already aligned; refine category explicitness only.
2. **Problem / register gap (layer 2):** "competent but invisible"; register not grammar. Keep; source or soften statistics.
3. **Transformation/outcome (layer 2):** currently missing as a distinct block (the quote is repeated instead). Add a non-numeric outcome block describing the shift from "following the conversation" to "leading it."
4. **How it works (layer 4):** goal → diagnostics → targeted practice → feedback. Keep.
5. **Who it's for (layer 3):** keep the two current groups pending the audience decision (§8 Q2). Do not expand to institutions here.
6. **Evidence/trust teaser (layer 5):** short, honest posture ("completed research; no public product yet; evidence built in the open"), linking to `status.html`.
7. **Team teaser:** keep; align with WP I outcome.
8. **CTA band + ticker:** keep single funnel and confirmed partner block.

### 5.2 Role of product/approach content

Existing pages (`kernel.html`, `index.html:215–240`, `philosophy.html`). Recommendation: preserve the two-level separation — user-level approach on the homepage; architectural mechanism on `kernel.html`. The content revision should add an explicit **"design intent vs. shipped capability"** distinction on `kernel.html` and on the homepage method block, so that describing the architecture does not read as describing a live product. This is a WP B/WP G copy decision with WP H hierarchy implications.

### 5.3 Audience or use-case pages

**Dependent on a decision.** The Strategy names four audiences (physicians, nursing, white-collar, academics) plus institutions; locked #5 narrows the homepage primary audience. Master checklist **DEF-02 defers** use-case/role-specific landing pages "only after validated interest." Recommendation: **do not create audience pages in this revision.** If audience-specific content is wanted, the least-risky interim is a single "Who it's for / berufliche Kontexte" section on the homepage or `status.html`, held within the current locked audience scope. Creating per-role pages without evidence of demand risks the "too narrow / premature" failure mode the benchmark warns about (`Pre-Launch-Website-Exhaustive-Report.md` §2).

### 5.4 Placement of institutional/employer messaging

**Dependent on a decision, and on evidence.** The Strategy gives institutions a full value proposition, but the repository has no institutional page, no pilot case, and no outcome data; DEF-02 defers such pages. Recommendation: **hold institutional/employer messaging off the public site** for this revision, except possibly:
- a single neutral line on `status.html` or a future "Für Institutionen" page stub **only if** the founder wants to signal institutional intent; and
- the existing confirmed partner ticker kept as-is (locked #4).

Any "auditable progress data / measurable asset" language is unproven and should not be published until a pilot and metric definitions exist (§6, §8 Q5).

### 5.5 Placement of evidence, learning-science, privacy, and compliance messaging

- **Evidence/research:** There is no public evidence layer today. `status.html` is the closest and should remain the canonical home for *status*, not for *results*. Candidate new section (not a new page): a short, clearly labeled **"Research & evidence"** block on `status.html` describing method and limitations, **only if** the founder approves publication of the research report summary. This directly intersects the `NEW-07` vs `TRUST-02/TRUST-03` conflict (§6, §8 Q4). Recommendation: hold until the report's publication scope is decided.
- **Learning science:** belongs as *method* on `philosophy.html` and `kernel.html`, framed as approach, not as validated effect. Review present-tense and unsourced statements (`philosophy.html:197, 234`).
- **Privacy/compliance:** belongs primarily in `datenschutz.html` (facts) and secondarily as a short trust statement near the waitlist form (`waitlist.html:758–775`, already present). Any EU-hosting/data-governance *marketing* claim must be reconciled with the actual processor list and legal review first (§2.9, §6).

### 5.6 Role of team, newsletter, waitlist, and contact pages

- **Team (`team.html`):** revise per WP I. Ensure the N=150 claim is verified/qualified, placeholders removed, and imagery parity resolved (Round-2 notes §2). Institutional/advisor representation is factual and may stay.
- **Waitlist (`waitlist.html`):** revise per WP F (visual redesign) while preserving content/behavior. Reconcile data statements with `datenschutz.html`.
- **Newsletter/Substack (WP K):** the Strategy does not require on-site subscription. Keep the existing external, clearly labeled Substack deep link (locked #7/IA-05). Any on-site feed/subscribe flow raises consent and dependency-guardrail questions and should remain a separate decision.
- **Contact/email (WP J):** the Strategy does not change contact requirements. Keep the coordinated mailbox decision (GATE-11) authoritative.

### 5.7 Content that should explicitly NOT be placed on the public website

Even though it appears in the Strategy, the following should not become public copy in this revision:

1. **Moat/defensibility arguments:** architecture-as-moat, four-to-seven-year replication claims, "last mover," "unoccupied category," "giants rationally ignore it."
2. **Competitive comparisons** naming or implying inferiority of Duolingo/Babbel/Goethe-Institut/AI-native startups (Strategy lines 105–109).
3. **Market-entry/expansion narrative:** B2C → B2C2B → B2B sequencing, beachhead doctrine, "before the space becomes crowded."
4. **Internal scorecard metrics** and the "data flywheel"/"diagnostic precision with every session" mechanism as a public promise.
5. **Unproven institutional claims** (auditable data, faster time-to-effectiveness, workflow integration).
6. **Specific outcome promises** (pass rates, recognition timelines, promotions, tenure).
7. **Proprietary scenario-depth and behavioral-validation claims** as proof, absent published evidence.
8. **Roadmap dates** presented as commitments (including "Gründung Q4 2026" as a hard date).
9. **Investor-facing framing** ("for partnership, investment…") beyond the existing neutral deep-page invitation.
10. **Privacy-forward marketing claims not backed by the live stack** (EU-hosted "from the ground up," no-third-party-training) until substantiated and legally reviewed.

**Existing pages to revise:** `index.html`, `philosophy.html`, `status.html`, `kernel.html`, `team.html`, `waitlist.html` (light content), plus footer tags across pages.
**Candidate new pages/sections:** a "Research & evidence" section (decision-dependent, likely `status.html`); optionally a single "Für Institutionen" line/section (decision-dependent). No new standalone pages are recommended in this round.
**Decision-dependent items (not immediate recommendations):** audience expansion; institutional page; research report publication; level-range wording; tagline relationship; on-site newsletter.

---

## 6. Claim-Safety and Evidence Review

A claim-review register for the material claims implied by the Strategy and (in some cases) already present on the site. **Strategic desirability is not proof.** "Repository evidence?" asks whether the repository currently contains something that substantiates the claim for a public audience.

| # | Claim family / proposed public claim | Why it matters | Evidence required | Repository evidence? | Recommended treatment |
|---|---|---|---|---|---|
| 1 | **Unoccupied category / "no other player"** — "the intersection is unoccupied; Disce is there" (Strategy §4) | Defines positioning; high legal/reputational risk if wrong; requires current market data | Dated, scoped competitive analysis; methodology; legal review | **No** — the Strategy asserts it; no market study in the repo | **Hold.** Do not publish comparative market claims. Use positive self-definition instead. |
| 2 | **Competitive comparison** — naming/implying competitors cannot do X (Strategy lines 105–109; `kernel.html:412–413`) | Comparative advertising risk; unverifiable | Verifiable, like-for-like evidence; legal review | **No** | **Remove/hold** from public copy. |
| 3 | **Learning-effectiveness claims** — "measurable performance change," "register coaching that fixes causes," "phoneme-accurate feedback" (Strategy §3/§4) | Core value prop; outcome claims are the most regulated | Validated outcome study with source, scope, limitations; or method-only framing | **No validated outcome**; Cervus is described as completed Proof of Principle only (`status.html:133`) | **Use only with qualified wording** (method/approach) or **hold** until the report is approved. No efficacy numbers. |
| 4 | **Exam pass rates / recognition timeline / career outcomes** (Strategy §5 scorecard, lines 180–184) | Strongest but most legally sensitive claims | Longitudinal outcome data; sourcing; consent for testimonials | **No** | **Hold.** Not publishable. |
| 5 | **Institutional adoption/partnerships** — "partners with hospitals/employers/universities," "first institutional pilots," workflow integration (Strategy §4/§5/§6) | Trust signal; false partnership claims are high risk | Named, permission-cleared partners; pilot status | **Confirmed partner block only** (locked #4): StromGold, Potsdam Transfer, Gründen in Brandenburg; **no hospital/employer pilots** | **Hold** any institutional adoption claim. Keep only the confirmed ticker as-is. |
| 6 | **Data / AI / GDPR / EU-hosting** — "GDPR-native, EU-hosted from the ground up," "never exposed to third-party commercial model training" (Strategy Principle 6) | Legal compliance and credibility; directly contradicted by live stack | Documented hosting/processing architecture; DPAs; transfer basis; legal review | **Partially** — `datenschutz.html` names GitHub Pages/Cloudflare/Airtable (USA) and leaves transfer basis/DPAs open (GATE-07/08) | **Hold/qualify.** Publish only post-legal-review and only what the live stack supports. Reconcile `kernel.html:238–239`. |
| 7 | **Proprietary scenario depth / defensibility** — "deep library no other platform offers," "cannot be crawled or synthesized," "4–7 years to replicate" (Strategy §3/§4) | Differentiation; unverifiable superiority | Auditable scenario inventory; independent comparison | **No** | **Hold.** Not public copy. |
| 8 | **Guarantees / exclusivity / superiority** — "last mover," "define the standard," "durable position" (Strategy §4/§5) | Framing claims; no place on a customer-facing site | — | **No** | **Remove from public messaging.** Investor/strategy register only. |
| 9 | **Research report / results** — "the completed research report," "reduction in bias," any results | Could substantiate rows 3/4; but publication scope is undecided | The actual report; permission; defined citation scope | **Report artifact not located in the tree**; `Kernel Documents/` holds specs/protocols only | **Hold** pending founder decision (§8 Q4). Reconciles `NEW-07` vs `TRUST-02/TRUST-03`. |
| 10 | **N=150 RCT (team.html:74, :78)** | Founder credibility claim; must be accurate and past-tense | Study documentation; correct framing (completed pilot; co-founder led it) | **Claim exists on the site**; verification not evidenced in repo | **Verify and qualify.** Ensure completed/past tense and accurate attribution; otherwise hold. |
| 11 | **"Proof of Principle"/"Proof of Visibility"** terms | Terminology lock | Founder decision #8 | **Yes** — locked: PoP public; Proof of Visibility internal-only | **Safe to use** PoP; never surface Proof of Visibility. |
| 12 | **Status/availability** — "Cervus completed / private beta planned / recruitment not open" | Truthfulness; release-critical | Founder decision #2/#6 | **Yes** — locked and implemented (POS-02) | **Safe to use.** Keep uniform and dated. |
| 13 | **Product/AI capability & architecture** (`kernel.html` present tense; meta description) | Describes an unbuilt V0 as if live | Stable, truthful artifact; design-intent labeling | **Partial** — V0 is "in Entwicklung" (`kernel.html:496`) | **Use only with qualified wording.** Label design intent; avoid capability claims. |
| 14 | **Problem severity/statistics** — "most learners who reach B2 stop there" (`index.html:162`), unnamed "Studien zeigen" (`philosophy.html:197, 234`) | Credibility; unsourced stats undermine trust | Citations, scope, limitations | **No** | **Qualify or remove.** Reframe qualitatively or source properly. |
| 15 | **"Research-grounded / methodologically rigorous"** (Strategy; `index.html:217`) | Legitimate method claim if accurate | Documented methodology | **Partial** — methodology exists as intent; no published validation | **Qualify.** Safe as approach framing; not as proven efficacy. |
| 16 | **Direct contact / response** | Conversion trust | Founder runbook | **Partial** — internal target only | **Safe** to offer contact; never publish response-time promises (CONV-04). |
| 17 | **Development updates / Substack** | Channel claim | Locked #7 | **Yes** — external deep link only | **Safe**, as external link; no on-site subscription promise. |

**Summary of strongest claim-safety risks**

1. The Strategy's **market/moat/competitive superiority** narrative (rows 1, 2, 7, 8) is investor material and must not become website copy.
2. The **EU-hosting / no-third-party-training** privacy claim (row 6) is contradicted by the repository's own privacy notice and open legal gates.
3. **Outcome/efficacy numbers** (rows 3, 4) have no supporting evidence in the repository and are prohibited by the existing claim register.
4. **Institutional adoption** (row 5) is unproven and would be a false-partnership risk.
5. **Present-tense architecture capability** (row 13) and **unsourced science/statistics** (row 14) are already live and should be corrected proactively.

---

## 7. Recommended Sequencing

Recommendations only; no deadlines are invented. Sequencing follows the existing batch/gate logic in `master-checklist-website-revision.md` §3 and WP structure.

### 7.1 Decisions and evidence needed before copywriting (gate the content work)

1. **Resolve the audience conflict** (Strategy's four audiences + institutions vs locked #5 white-collar primary). — §8 Q2. Blocks homepage audience section, philosophy audience list, and any use-case page.
2. **Resolve the level range** (B2–C1 locked vs B2–C2 strategy/design brief/site). — §8 Q1.
3. **Decide the research-report publication scope** and reconcile `NEW-07` with `TRUST-02/TRUST-03`. — §8 Q4. Blocks any evidence/research section.
4. **Decide the privacy/EU-hosting public claim** against the real stack. — §8 Q3. Blocks any privacy-forward marketing.
5. **Decide the tagline/category relationship** (fixed "Sag, was du meinst." vs "expertise visible" vs explicit "professional German" category). — §8 Q7.
6. **Confirm the confirmed-partner block and relationship labeling** (locked #4 permits keeping it as-is; do not change without founder). — §8 Q6.
7. **Close legal gates** GATE-01…12 before any indexable launch; legal review (GATE-12) covers outward claims touching privacy/consent. — WP A. These run in parallel but gate publication.

### 7.2 Homepage/content work that can begin once those are resolved

- WP B copy pass across `index.html`, footer tags, `philosophy.html` audience/product-claim review, `kernel.html` design-intent labeling, `status.html` internal-comment cleanup.
- WP C: reconcile sitemap, page dispositions, and any new sections.
- WP G: evidence posture wording (method vs result), N=150 verification.
- WP F: waitlist content/data-statement reconciliation during the WP F redesign.
- WP H: messaging-hierarchy implications for typography/hero.

### 7.3 Later page-level work

- WP I team-page revamp (portraits/placeholders/CTO section) once WP I decisions are made.
- WP J email-address change once addresses and GATE-11 are settled.
- WP K Substack feed decision (separate consent/dependency analysis).
- Deeper audience/use-case content only after evidenced demand and the audience decision.

### 7.4 Deferred

- DEF-01 (security/AI-transparency page), DEF-02 (use-case/role pages), DEF-03 (waitlist design-system migration — though NEW-02 may pull this forward), CONV-06 (measurement), and any institutional page.

### 7.5 Mapping to work packages

| Sequencing stage | Work packages |
|---|---|
| Decisions/evidence gates | WP-B (lead), WP-A, WP-G |
| Homepage/content revision | WP-B, WP-C, WP-G |
| Visual/hierarchy consequences | WP-H |
| Conversion/content reconciliation | WP-F |
| Later page-level | WP-I, WP-J, WP-K |
| Deferred | WP-L (DEF-01/02/03, CONV-06) |

---

## 8. Open Questions and Decisions Required

Only questions that materially block sound public messaging or implementation are listed. "Can proceed without it?" indicates whether content work is blocked or can continue partially.

| # | Question/decision | Why it matters | Affected pages / WPs | Recommended owner/type | Can proceed without it? |
|---|---|---|---|---|---|
| Q1 | **Level range: B2–C1 (locked) or B2–C2 (Strategy, design brief, current site)?** | Level range is the audience contract; inconsistency across sources and the live site | `index.html:130`, `philosophy.html`, meta; WP B/C | Founder (locked-decision amendment) | Partially — wording must be frozen before copy goes live |
| Q2 | **Audience breadth:** locked #5 (white-collar primary, physicians sub-context) vs Strategy (physicians-led + nursing + academics + institutions) | Determines homepage audience section, philosophy audience list, candidate pages, institutional messaging | `index.html:192–206`, `philosophy.html:254`, WP B/C | Founder | Homepage can hold current two-group scope; no expansion without decision |
| Q3 | **Privacy/EU-hosting public claim:** what may be said given GitHub Pages/Cloudflare/Airtable and open GATE-07/08? | Public privacy-forward marketing currently conflicts with the privacy notice | `kernel.html:238–239`, `philosophy.html:269–273`, `datenschutz.html`, WP A/G | Founder + legal (OPEN-LEGAL) | No — hold until legal review |
| Q4 | **Research report publication:** does it exist, may it be published, in what form (full/summary/figures/link), and does it reconcile `NEW-07` with `TRUST-02/TRUST-03`? | Blocks any evidence/research content; substantiates or withholds outcome claims | `status.html`, team N=150, WP G | Founder (evidence content decision) | Yes for non-evidence content; blocks evidence sections |
| Q5 | **Institutional/employer messaging:** signal intent on-site now, defer, or create a page? | Strategy emphasizes institutions; no evidence exists; DEF-02 defers pages | Candidate new section; WP B/C/L | Founder | Yes — hold off by default |
| Q6 | **Partner block and relationship labeling:** keep as-is (locked #4) or add explicit relationship types? | Avoids "unsubstantiated relationship" risk identified in `sprint-4-conversion-trust-legal.md` §4.7 | `index.html:313–330`; WP I/G | Founder | Keep as-is; labeling optional |
| Q7 | **Tagline/category relationship:** how do the fixed claim, "expertise visible," and "professional German" coexist? | Determines hero/meta/footer wording | All pages; WP B/H | Founder (copy approval per `DESIGN-BRIEF.md:10`) | No — needed before hero copy changes |
| Q8 | **Footer tag and category vocabulary:** replace "KI-gestütztes Deutschlernen" site-wide? | Currently contradicts the category distinction | Footer of all pages; WP B/C | Founder | No, but low-risk once Q7 resolved |
| Q9 | **Internal-strategy leakage:** remove internal HTML comments and marketing/monetization candor from `status.html`/`philosophy.html`? | Public source comments reveal internal process; monetization detail is strategically sensitive | `status.html`, `philosophy.html`; WP B/C | Founder | Yes (cleanup is low-risk) |
| Q10 | **Status date commitments:** is "Gründung Geplant · Q4 2026" published as a directional target? | Reads as a committed date despite the disclaimer | `status.html:90`; WP B | Founder | Yes, with qualified wording |
| Q11 | **N=150 RCT wording/verification on `team.html`** | Founder credibility; accuracy risk | `team.html:74, :78`; WP I/G | Founder + evidence | Blocked for this claim |
| Q12 | **Source set and sign-off owner for NEW-04** (`website-revision-work-packages.md` open Q1/Q2) | Determines whether the Strategy is the canonical source and who approves wording | WP B | Founder | No — this document proposes the Strategy as primary source, to be confirmed |

> Q12 is the direct answer this document offers to the prior planning round's outstanding WP B question: the Strategy (`Disce — Making Expertise Visible.md`) is proposed as the canonical strategic source for this revision, with the locked decisions and `DESIGN-BRIEF.md` as binding constraints. Confirmation and wording sign-off remain the founder's.

---

## 9. WP B Completion Proposal

A proposed definition of done for WP B ("Positioning, Messaging & Document Synthesis"), incorporating NEW-04. This is a proposal, not a decision.

### 9.1 Strategy/messaging decisions

- [ ] The Strategy is formally accepted as the revision's strategic source, and the source set/sign-off owner (Q12) is recorded.
- [ ] Audience breadth (Q2) and level range (Q1) are decided and dated.
- [ ] Tagline/category relationship (Q7) and site-wide category vocabulary (Q8) are decided.
- [ ] The public messaging foundation (§2) is approved as the governing reference, with the qualification notes preserved.

### 9.2 Copy and page-architecture deliverables

- [ ] A page-by-page copy change list for `index.html`, `philosophy.html`, `status.html`, `kernel.html`, `team.html`, `waitlist.html` (content-only), and shared footer tags.
- [ ] Each change labeled: revise / add / hold / remove, with the responsible work package.
- [ ] Confirmation that no product copy, headline, CTA, claim, translation, or legal copy is changed without explicit approval (`DESIGN-BRIEF.md:10`; `AGENTS.md` scope guardrail).
- [ ] Internal-strategy leakage (Q9) and roadmap-date wording (Q10) resolved.

### 9.3 Claim/evidence review deliverables

- [ ] The claim register (§6) reviewed against every public claim, with treatment decisions recorded (safe / qualified / hold / remove).
- [ ] Explicit confirmation that no market-gap, competitive, efficacy, outcome, institutional-partnership, EU-hosting, or data-training claim is published without evidence and legal review.
- [ ] N=150 wording verified or held (Q11).
- [ ] Reconciliation recorded between `NEW-07` and `TRUST-02/TRUST-03` (Q4).

### 9.4 Cross-package handoffs

- [ ] **WP A:** every claim touching privacy, consent, or data handling routed through GATE-07/08/12 before publication; indexability (GATE-14) still gated.
- [ ] **WP C:** information-architecture changes (sitemap, new sections) agreed and reflected in page dispositions.
- [ ] **WP F:** waitlist content/data-statement reconciliation agreed with the WP F redesign.
- [ ] **WP G:** evidence/trust wording and the research-report decision handed over.
- [ ] **WP H:** messaging hierarchy and hero/footer wording handed to the visual system work.
- [ ] **WP I/J/K:** team-page content, email-address change, and Substack decision dependencies recorded.

### 9.5 Explicit non-goals

- No new standalone pages (audience/use-case/institutional) — deferred under DEF-02.
- No implementation, no copy edits, no legal-text edits, no routing/robots/sitemap changes authored within WP B.
- No adoption of the Strategy's investor/moat/market-expansion language as public copy.
- No claims of validated efficacy, outcomes, institutional adoption, or EU-hosting beyond what is evidenced and legally reviewed.

---

## Appendix A — Files reviewed for this plan (repository-grounded)

- `Disce — Making Expertise Visible.md` (strategic source)
- `website-revision-work-packages.md` (WP A–L, open questions)
- `master-checklist-website-revision.md` (tasks, gates, claim register reference, batch logs)
- `founder-decisions-locked.md` (locked decisions #1–#8)
- `sprint-0-triage-and-sprint-1-decision-pack.md` (positioning B.1, status truth B.2, terminology B.3, guardrails B.5)
- `sprint-1-positioning-messaging.md`
- `sprint-4-deep-dive-conversion-trust-legal.md` (§8 claim register)
- `sprint-4-conversion-trust-legal.md`
- `Pre-Launch-Website-Exhaustive-Report.md` (benchmark anti-patterns)
- `DESIGN-BRIEF.md` (copy guardrail, fixed claim, product reality)
- `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md`
- Public pages: `index.html`, `kernel.html`, `philosophy.html`, `status.html`, `team.html`, `waitlist.html`, `impressum.html`, `datenschutz.html`, `beta.html`
- `sitemap.xml`, `robots.txt`, `CNAME`, `README.md`, `Kernel Documents/`

## Appendix B — Deliberate limitations of this plan

- It does not write final production copy.
- It does not modify any existing file.
- It does not resolve the audience, level-range, tagline, research-publication, or privacy-claim questions; it records them.
- It does not assert that the Strategy's market, moat, outcome, or institutional claims are true; it treats them as strategic input requiring evidence.
- It does not re-prioritize or re-status any master-checklist task.