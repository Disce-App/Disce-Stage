# Sprint 1 — Positioning, Messaging & Content

**Assessment / situation report (diagnostic only). No fixes, no rewrites, no prioritisation.**

- **Subject:** Disce website, repository `weltvorstellung`, staging host `stage.weltvorstellung.de` (`CNAME`), canonical `weltvorstellung.de`.
- **Benchmark:** `Pre-Launch-Website-Exhaustive-Report.md` (cited by section name/number).
- **Method:** full read of the benchmark plus direct inspection of the tracked site (`index.html`, `philosophy.html`, `kernel.html`, `team.html`, `status.html`, `beta.html`, `waitlist.html`, `impressum.html`, `datenschutz.html`, `js/site.js`, `js/generative/*`, `css/experimental.css`). Every finding below cites an actual file and line or a benchmark section.
- **Interview date:** 2026-09-21.

## 0. Scope note that conditions everything below

The benchmark is written for a **product pre-launch website** whose job is to make *a product* legible and to qualify *its future users*. The Disce site is not that unambiguously. Its homepage hero explicitly frames the site as a **founding-team introduction to investors, university partners, and the Berlin founder scene before incorporation**:

> "Disce ist ein Gründungsteam, das den Fall für KI-gestütztes Deutschlernen auf fortgeschrittenem Niveau (B2–C2) aufbaut. Wir stellen uns Investorinnen und Investoren, Hochschulpartnern und der Berliner Gründungsszene vor, bevor die Gesellschaft eingetragen wird." — `index.html:75`

At the same time, the same homepage carries product-learner messaging (problem, personas, "how it works"), and the only conversion form (`waitlist.html`) recruits **study participants / learners** (German B2–C1 speakers), not investors. The site therefore currently serves **two audiences with two different jobs at once** (venture/stakeholder communication and learner/study recruitment). This dual identity is the single most important context for Sprint 1: several "gaps" below are not simply missing copy but unresolved audience positioning.

Where the benchmark recommendation is context-dependent (`[K]`) or expert judgment (`[X]`), that is preserved in the Gap.

---

## 1.1 Primary website job per maturity phase

**Benchmark expectation** (§1 Executive Summary point 1; §2 "Maturity phases" table): the site must have **one defined primary job matching the current maturity phase**. For problem/MVP validation the best CTA is an interview/design-partner inquiry; for closed/private beta a **qualified beta application**; for an open waitlist, an email signup **with a value exchange**. Conversion *quality* matters more than volume.

**Current state on the website**

- Homepage stage signals: `index.html:89` "Phase — Validierung / Pre-Seed"; `index.html:90` "Pilotphase — Abgeschlossen, Auswertung läuft" (pilot completed, evaluation running); `status.html:72–86` "Kernel v0 — in Entwicklung", "Gründung — Geplant · Q4 2026".
- Primary homepage CTA is **not** product/validation-facing: `index.html:77` primary button = "Das Team", `index.html:78` secondary = "Unsere Philosophie". The learner/product conversion path is only in the nav (`index.html:51`) and the final band (`index.html:260–261`).
- The only actual conversion artifact is `waitlist.html`, which is a **pilot-study recruitment form** ("Sei dabei – Pilotstudie", `waitlist.html:475`), not a product beta application.
- The Kernel page argues the product in depth (`kernel.html:76–77`) and closes on an investor/partner CTA ("Für Partnerschaft, Investment oder ein Gespräch…", `kernel.html:493`).

**Gap / blind spot:** The site does not commit to a single primary job for the current phase. It is simultaneously (a) an investor/stakeholder introduction, (b) a learner-facing product narrative, and (c) a study-participant recruitment funnel. The benchmark's phase table anticipates exactly one dominant conversion per phase; here the dominant hero conversion ("Meet the Team") does not match the only functioning conversion mechanism (study signup). The mismatch between the maturity phase the homepage claims ("Pilotphase abgeschlossen") and the study the waitlist page is still recruiting for (§1.8) means the "primary job" is also internally inconsistent.

**Critical flag:** ⚠️ **CRITICAL** — see §1.8: the study/waitlist call-to-action promises a **future event dated in the past**, and the homepage declares the pilot phase already completed. A visitor who follows the stated primary conversion path is promised a study "starting mid-June 2026" while the site elsewhere says it is finished. That is a false/deceptive availability claim with direct trust and (for a research-recruitment consent context) functional risk, not ordinary polish.

---

## 1.2 Value-proposition logic

**Benchmark expectation** (§6 "Value-proposition logic"): a viable proposition combines **For [audience] who need [job/context], [product] is a [category] that enables [outcome] by [mechanism]. Unlike [status quo], it relies on [differentiation].** Category, audience, outcome, and mechanism should be reconstructible on the first screen or immediately after.

**Current state on the website**

- Category: present, in the homepage lede — "KI-gestütztes Deutschlernen auf fortgeschrittenem Niveau (B2–C2)" (`index.html:75`), and in the meta description (`index.html:7`).
- Audience: present, but as **investors/university partners/founder scene** (`index.html:75`). The learner ICP appears later (`index.html:148–162`).
- Outcome: the hero has no user outcome; it states what the team is doing. A user-outcome-shaped statement exists only as an aspiration quote ("Weniger Zeit dafür, einen Satz vorher im Kopf zu proben…", `index.html:81`) and in the persona section.
- Mechanism: absent from the hero. It lives at `index.html:175–197` ("Ein Ziel wählen / Standortbestimmung / Tägliches Coaching") and, at a different level, throughout `kernel.html`.
- Differentiation ("unlike the status quo"): implied in the problem section ("Kursfortschritt ≠ Fortschritt im Leben", `index.html:117`) and in `philosophy.html:247` ("Disce ist das bewusste Gegenmodell zu Sprach-Apps…"), but not stated as a single contrasting proposition on the homepage.

**Gap / blind spot:** The components are all present somewhere, but on the first screen they resolve to *"a founding team is building a case for AI German learning for investors"*, not *"for [learner] who need [job], Disce is [category] that gives [outcome] by [mechanism]"*. The benchmark permits not every component in the hero but requires category, audience, outcome and mechanism to be **reconstructible in the first screen or immediately after**. Outcome and mechanism are not immediately reconstructible for a learner; they arrive after two dark editorial bands and a persona section.

---

## 1.3 Category framing

**Benchmark expectation** (§6 "Category framing for AI and SaaS"): name a familiar category and explain the differentiator; avoid generic labels such as "AI platform", "agentic workspace", "intelligent automation" without grounding in an observable workflow. Granola ("AI notepad for people in back-to-back meetings") and Descript ("edit video by editing text") are the reference patterns. Also §6 "Precise pre-launch copy": name the category unless the product creates a new, explainable one.

**Current state on the website**

- Two category frames coexist, neither of them a single named category:
  1. Homepage/description: "**KI-gestütztes Deutschlernen**" / "AI-powered German learning" (`index.html:7`, `index.html:75`, footer `index.html:290`).
  2. Product-system frame on `kernel.html:77`: "**ein mehrschichtiges, longitudinales Betriebssystem für KI-gestütztes Sprachcoaching**" ("a multilayered, longitudinal operating system for AI-supported language coaching").
- `philosophy.html:250` rejects the app category outright: "Disce ist kurz gesagt nicht einfach eine weitere Sprachlernanwendung. Es ist eine lebendige Plattform und Institution der Sprache…".
- The first product scenario is defined in the design brief, not on the site: `DESIGN-BRIEF.md:19` "the German job interview („Bewerbungsgespräch · DACH") — this is where the Kernel beta on the website leads." The homepage personas do mention the Fachsprachprüfung and workplace scenarios (`index.html:156`, `161`), but the *job-interview V0* framing is not surfaced as the category anchor.

**Gap / blind spot:** For a visitor, "KI-gestütztes Deutschlernen" collides with the benchmark's "borrowed generic label" risk, because the differentiating mechanism ("register/prosody feedback on high-stakes professional scenarios", "not certificates, not streaks, not vocabulary") is only visible after the problem and persona sections. The site is trying to either create a new category ("Sprachcoaching-Betriebssystem", "Institution der Sprache") or reject the app category, but it does not perform the benchmark's required move: **anchor in a known category, then explain the differentiator in observable-workflow terms**. The most concrete, benchmark-aligned category grounding the project already owns — the job interview / Fachsprachprüfung scenario `DESIGN-BRIEF.md:19` — is not used as the homepage category frame.

---

## 1.4 Target audience / ICP

**Benchmark expectation** (§2 "Core tasks", §6; Master Checklist "Strategy — Is a primary ICP or a primary usage context named?"): name a specific primary audience/entry context. Benchmark weak pattern: "For teams of all sizes".

**Current state on the website**

- Homepage hero addresses investors and university partners (`index.html:75`).
- Homepage persona section names two learner groups: "Ärztinnen und Ärzte in Vorbereitung auf die Fachsprachprüfung" (`index.html:155`) and "Fachkräfte, die Deutsch brauchen, das im Beruf trägt" (`index.html:160`).
- `DESIGN-BRIEF.md:16–17` narrows this to "international professionals and graduate students in the DACH region who already have B2–C2 German" — a definition considerably tighter than the site copy.
- `waitlist.html:506–507` names a different, broader audience for the study: "Alle, die Deutsch als Fremdsprache sprechen (Niveau B2–C1)".

**Gap / blind spot:** At least three audience definitions are in play (investor/stakeholder; B2–C2 DACH professionals per the brief; B2–C1 "anyone" per the study form). The homepage does name two learner contexts, which satisfies the literal checklist item, but the audience named in the **hero** (investors) is not the audience of the **conversion mechanism** (learners). The study-level "Anyone who speaks German as a foreign language (B2–C1)" is precisely the broad-audience phrasing the benchmark warns against, though it is defensible as a research-screening criterion rather than an ICP. The site does not state which of these is the primary (commercial) ICP outside the non-public `DESIGN-BRIEF.md`.

---

## 1.5 Hero copy

**Benchmark expectation** (§4 "Hero requirements"): above the fold, recognize **category frame, target audience, outcome, mechanism, status label, one dominant CTA, and evidence** (product interface/workflow/prototype). Headline should not be a poetic slogan without a product category.

**Current state on the website** (`index.html:62–94`)

- Eyebrow: "Vor der Gründung · Berlin / Potsdam" (`:73`) — company status, not product status.
- H1: "Sag, was Du meinst." / "Say what you mean." (`:74`).
- Lede: the founding-team/investor paragraph (`:75`).
- CTAs: "Das Team" (primary), "Unsere Philosophie" (secondary) (`:77–78`).
- Right column: a stat panel — Fokus / Ansatz / Bereiche / Phase / Pilotphase / Team (`:86–91`).
- Evidence: an abstract full-bleed artwork (`DISCE_C01_r1_arena-stag-bordeaux`, `:63–69`); no product interface.

**Gap / blind spot:**

- **Category in hero:** present in body text only; the H1 itself carries no category.
- **Outcome:** absent. The H1 is the benchmark's "poetic slogan" pattern; the outcome exists only in the later testimonial-style quote.
- **Mechanism:** absent above the fold.
- **Status:** present, but it describes the *company's* incorporation stage, not the product/beta availability the benchmark's status label targets ("Private Beta", "Applications Open").
- **Next step:** present but misaligned — the dominant CTA routes to the team page, not to the product or the study.
- **Evidence:** absent; there is no product depiction in the hero (all hero media is decorative art, `alt=""`, `:68`).
- **Second CTA intent level:** the two hero CTAs ("Team" / "Philosophy") are both *learning-atmosphere* intents, not differentiated toward conversion, so the benchmark's "different intent level" rationale does not apply; simultaneously the actual conversion path (waitlist) is not in the hero at all.

This hero is a close match to the benchmark's **"Beautiful, empty hero"** anti-pattern (§10): strong visual identity, weak product explanation, no product artifact, CTA not tied to a product decision. The mitigation is that the page intentionally speaks to investors, for whom "meet the team" is a legitimate next step — but the hero then does not do the learner-facing pre-launch job the rest of the page attempts.

---

## 1.6 Three language layers (problem / outcome / mechanism)

**Benchmark expectation** (§6 "Three language layers"): strong early copy combines **problem language** (what is broken), **outcome language** (what the user can do), and **mechanism language** (how the product creates the change). Feature-only or outcome-only language is insufficient.

**Current state on the website**

- **Problem language** — strong and concrete: `index.html:101` "Sie haben B2 oder C1, und trotzdem fehlt etwas."; three problem cards at `:105–119` ("Verstehen, ohne zu sagen" / "Unsicherheit im Ton" / "Kursfortschritt ≠ Fortschritt im Leben"). This matches the benchmark's "precise problem language" bar well.
- **Outcome language** — present as a single repeated aspiration quote (`index.html:81`, `:135`, `:226`) and in persona narratives ("die Entscheidungen fallen ohne Sie", `:161`). It is stated once, verbatim, three times.
- **Mechanism language** — present and comparatively good at `index.html:175–197` (goal → 12–15-minute benchmark → daily structured coaching) and deeply at `kernel.html:307–356` (six-step cycle).

**Gap / blind spot:** All three layers exist, but they are **sequenced so that problem dominates and mechanism arrives late**, and the *outcome* layer is not independently articulated — it exists only as one verbatim quote. The benchmark's "repetition should restate at different levels of detail" principle (§4 "Narrative flow") is not met because the outcome is restated identically rather than progressively (see also Sprint 2, repetition). There is no single sentence on the homepage that combines problem → mechanism → outcome in the benchmark's causal form.

---

## 1.7 Outcome & mechanism precision, and status precision

**Benchmark expectation** (§6 "Language levels (weak vs. precise)" table): problem, feature, outcome, mechanism, status and CTA each have weak vs. precise forms. Examples of weak: "Knowledge work is broken", "AI-powered insights", "Work smarter", "Coming soon", "Join us". Also §6 "Precise pre-launch copy": use verbs and objects; show the causal mechanism; mark uncertainty ("planned", "being tested").

**Current state on the website**

- Problem precision: high ("Register, not vocabulary, is where advanced learners stall", `index.html:113`).
- Mechanism precision: high in isolation ("Kurze Schreib- und Sprecheinheiten mit Rückmeldung zu Ton, üblichen Formulierungen und kommunikativer Wirkung", `:194`); the Kernel's bounded-claim language (`kernel.html:115`, `:339`, `:360`) is unusually disciplined and matches the benchmark's "frame limitations as product logic" recommendation (`§6`).
- Status precision: mixed. `status.html:61` dates the page ("Stand: September 2026") and separates "Abgeschlossen / In Entwicklung / Geplant" (`status.html:125`, `:144`, `:171`, `:186`). But the homepage stats (`index.html:86–91`) and the waitlist copy (`waitlist.html:513–514`) conflict (see §1.8).
- "Coming soon"-type weakness: `beta.html:69` "Diese Seite entsteht gerade. Weitere Details folgen in Kürze." is the benchmark's weak "coming soon" form, but it is on an unlinked placeholder page (`beta.html`, noindex, not in nav).

**Gap / blind spot:** Mechanism and limitation language is a genuine strength relative to the benchmark. The weakness is **status precision across pages**: three different statements of project state coexist and are not reconciled. The benchmark requires vision, capability and planned functionality to be separated (Master Checklist "Strategy — Are vision, current capability, and planned functionality separated?"); the site does separate them on `status.html` and `kernel.html`, but the homepage stat panel ("Pilotphase Abgeschlossen, Auswertung läuft") and the waitlist page ("Die Studie startet Mitte Juni 2026") contradict each other.

---

## 1.8 Beta / status communication

**Benchmark expectation** (§6 "Beta status module"; §10 "Missing beta transparency"; §1 point 7): a trust-building status box distinguishes **Already testable / Still in development / Suitable for / Participation / Expectation / Not promised**, avoids apologetic tone and a vague permanent beta, avoids fixed roadmap dates without planning certainty, and must **state status in the hero and before the CTA** so the product never appears available and then ends in a waitlist.

**Current state on the website**

- `status.html` is the closest thing to a status module: a status ledger (`status.html:70–89`), project spine with done/in-progress/planned tags (`:119–194`), and a directional four-epoch roadmap explicitly flagged "keine verbindlichen Termine" (`:224`). This is a strong match for the benchmark's "direction, not binding dates" guidance.
- `kernel.html:445–474` "Die Grenzen" and `:473` ("V0 beansprucht keine validierte Langzeitwirkung, keinen realen Transfer und keine objektive CEFR-Einstufung") is an unusually explicit "Not promised" block — benchmark-aligned.
- **Conflicting status facts across pages:**
  - Homepage: "Pilotphase — Abgeschlossen, Auswertung läuft" (`index.html:90`).
  - Status page: "Cervus — Abgeschlossen · Mai – August 2026" (`status.html:78`), "Kernel v0 — in Entwicklung · seit September 2026" (`:82`).
  - Waitlist/study page: "Die Studie startet Mitte Juni 2026. Du setzt dich jetzt auf die Warteliste und wir melden uns bei dir." (`waitlist.html:513`), repeated in the form intro "wir melden uns im Juni zur Terminbestätigung" (`:555`) and the success message "Wir melden uns im Juni" (`:712`).
  - The waitlist page `<title>` and OG metadata still read "CERVUS Study — Join the Waitlist" (`waitlist.html:7`, `:18`, `:25`), and the study is described in the present/future tense throughout (`:498`).

**Gap / blind spot:** As of the assessment date (September 2026), the study page advertises a study that starts in **mid-June 2026** and promises contact "in June", while the homepage and status page state the Cervus phase is **complete (May–August 2026)**. The waitlist page has no visible "as of" date, unlike `status.html:61`. A visitor arriving through the primary CTA is therefore given a status that is both stale and contradicted by the rest of the site. The waitlist page also never states who is selected, in what waves, or what participants receive during any waiting period (benchmark §2 "Waitlist decision" three questions; see Sprint 4). The homepage's own status label ("Vor der Gründung", `index.html:73`) describes incorporation, not product/beta availability, so the benchmark's "state status before the CTA" is only partially met on the homepage.

**Critical flag:** ⚠️ **CRITICAL** — conflicting/stale availability and timing claims ("study starts mid-June 2026", "we'll reach out in June") versus "Cervus — Abgeschlossen · Mai–August 2026" and "Pilotphase abgeschlossen". This is the benchmark's "bait-and-switch / deceptive availability" risk, not polish.

---

## 1.9 AI communication

**Benchmark expectation** (§1 point 8; §6 "AI communication"; §8 "Trust modules and AI trust"; Master Checklist "Trust / legal — Are AI data usage, human control, and limits explained?"): an AI product page should, depending on risk, cover what task AI takes on; what stays human; what data forms the context; whether customer data trains the model; which models/subprocessors are involved; where data is stored; whether outputs can be checked/corrected/deleted; which actions AI performs autonomously; error classes/limits; sensitive-input handling; logging. NIST/NN-g fundamentals: transparency, control, consistency, support-when-the-system-fails. EU AI Act transparency obligations may apply.

**Current state on the website**

- Substantial AI-transparency content exists, but it is **distributed across a long philosophical essay**:
  - `philosophy.html:264–269` ("Technologie im Dienst der Souveränität"): open EU models (Teuken-7B/OpenGPT-X), EU/EEA cloud for MVP, own GPU resources as target state, data categories (core product data, "sparsame Produktanalytik … ohne dienstübergreifendes Tracking", quality/moderation signals, explicit opt-ins), bounded/explainable intelligent systems ("Warum sehe ich das?", human-decided edge cases), DSGVO + EU AI Act orientation, commitments ("Kennzeichnung KI-generierter Inhalte", no black-box decisions), and explicit "what we will not do" ("keine Zertifizierungsversprechen", no GER certificates, no pay-to-win, no black-box).
  - `kernel.html:105–116`, `:307–363`, `:445–474`: model-as-operator-not-final-decision, consent before evaluation, triangulation, logged rationale, no invisible LLM fallback, no psychological user model, "no invented precision", and the non-claims.
- There is **no dedicated `/ai-transparency` or `/responsible-ai` page**; the content is buried at philosophy chapter 7 and kernel sections. There is no explicit statement of *whether customer data is used for model training* in plain operational terms (only "ausdrückliche Einwilligungen für … später, gezieltes Fine-Tuning") and no model/subprocessor list on a trust page.

**Gap / blind spot:** The depth of AI transparency likely **exceeds** the benchmark's minimum, which is a strength. The gap is **discoverability and structure**: the benchmark treats AI transparency as a P0/P1 page (`§3 Page decisions`) and as a trust module reachable from the conversion path. Here it is only reachable by reading an 8-chapter essay or the Kernel page; neither the waitlist form nor the footer links to it, and there is no short plain-language AI summary near the form. `datenschutz.html` (the only "trust" document linked from the footer) does not mention AI processing, model use, or output handling at all.

**Critical flag:** None. Where AI is described, the claims are bounded and conservative; the gap is structural, not a false claim.

---

## 1.10 Weak-pattern language audit

**Benchmark expectation** (§6 "Weak patterns" table; §10 anti-pattern catalogue): avoid "The future of work", "Revolutionary AI platform", "Unlock your potential", "One platform for everything", "10x productivity", "Seamless", "Secure by design", "Trusted by …" with weak proof, "Limited spots", "Coming soon", "Join the waitlist", "For teams of all sizes".

**Current state on the website — item-by-item**

| Weak pattern | Present? | Evidence |
|---|---|---|
| "The future of work" | No | — |
| "Revolutionary AI platform" | No | — |
| "Unlock your potential" | Not on marketing pages; adjacent | `philosophy.html:126` uses "Ausdruckssouveränität" (expressiveness sovereignty), which is specific |
| "One platform for everything" | Close | `philosophy.html:248–250` explicitly aspires to a broad platform/institution ("Disce ist … eine lebendige Plattform und Institution der Sprache"), and `:250` enumerates a very wide audience ("Lernende … Lehrkräfte … Kultur- und Kreativszene … Forschende … Arbeitgeber … Diaspora … Vertriebs- und Technologiepartner"). This is the benchmark's "overly broad promise" / "For teams of all sizes" family, even if deliberately framed as vision. |
| "10x productivity" | No | Mechanism copy is qualitative (register/prosody), which is disciplined |
| "Seamless" | No | — |
| "Secure by design" | Not verbatim; adjacent | `philosophy.html:268` "Privacy by Design nach der DSGVO" is a named principle with listed governance measures, so it is closer to the "concrete measure" side than the empty "secure by design" side |
| "Trusted by …" / logo proof | **Yes, risk** | `index.html:269` heading "Strategische Partner &amp; Ökosystem" over partner logos (`:272–274`) — relationship type is not explained (see Sprint 4, §4.7) |
| "Limited spots" | No | The waitlist is not framed as scarce |
| "Coming soon" | Yes, but contained | `beta.html:69` "Weitere Details folgen in Kürze" (unlinked placeholder page) |
| "Join the waitlist" | **Yes** | Nav and CTAs "Auf die Warteliste" (`index.html:51`, `:260`; `status.html:276`; footer all pages) — benchmark calls this weak without value exchange; the value exchange is partly specified on `waitlist.html:502–538` (compensation, effort) but not in the CTA itself |
| "For teams of all sizes" | No | — |

**Gap / blind spot:** The site avoids most of the benchmark's weak-language table — notably no "future of work", no "10x", no "seamless", no fake scarcity. Two residual families remain: (a) the **broad-platform/institution ambition** in `philosophy.html` (context-dependent `[K]` as a long-term vision statement, but it sits inside a page that is linked from the primary nav and framed as company philosophy), and (b) the **generic "Join the waitlist" CTA** and **unexplained partner-logo claim**. The benchmark's own "weak patterns" verdict on "Join the waitlist" is "no value exchange"; here the value exchange exists one page deeper but is not carried by the label.

---

## 1.11 Verifiable numbers, logos, testimonials

**Benchmark expectation** (§6 "Precise pre-launch copy": "Back up concrete numbers: no time savings, accuracy, or user count without a verifiable basis"; §8 "Problematic trust claims"; §8 "Legitimate pre-launch proof").

**Current state on the website**

- Concrete numbers are mostly **procedural, not performance claims**: "12 bis 15 Minuten" benchmark (`index.html:187`), "sechzig Minuten" exam (`:156`), "N fünfzig" pilot (`team.html:74`), "fünf Gründer" (`team.html:60`, `index.html:91`), study effort "25–30 Minuten" and "7–10 €" voucher (`waitlist.html:527`, `:534`). These are concrete and attributable, which matches the benchmark's "mark uncertainty"/"concrete" guidance.
- `team.html:74` states an ongoing RCT "(N=150) zur Wirksamkeit KI-generierten Feedbacks" as the CEO's current role, while the homepage/status describe the pilot as completed/evaluation-running and the status page calls Cervus "die abgeschlossene Masterarbeit" (`status.html:129`). Whether N=150 is the completed or the follow-up study is not resolvable from the site.
- Partner logos (`index.html:272–274`): StromGold, "University of Potsdam, Potsdam Transfer Startup Service", "Gründen in Brandenburg, WFBB". `team.html:92` lists a co-founder as "Junior Associate bei StromGold AB". The "Strategische Partner" label is not substantiated anywhere on the site with a relationship description.
- Portraits: `team.html:70–110` uses placeholder SVGs with `alt="Portrait placeholder: …"` and a placeholder team entry (`:108–110` "Rolle, Nachname und Kurzbiografie von Joscha liegen … nicht vor").

**Gap / blind spot:** No unverifiable performance metrics ("10x", accuracy claims) were found — a strength. The open concerns are relational/attributional: the N=150 attribution is ambiguous against the completed-study framing, and the "Strategic Partners & Ecosystem" heading asserts a relationship type the site does not define. The placeholder portraits are honestly labelled, so they are a maturity gap rather than a trust violation.

---

## 1.12 FAQ content

**Benchmark expectation** (§3 Page decisions "FAQ — Reduce remaining uncertainty … P0 as a module"; §6 "Pre-launch FAQ"): a FAQ is a **P0 module** and should answer at minimum: what already works today; who can participate; how participants are selected; when a response/access can be expected; which platforms/integrations are supported; whether there are costs; what data is processed for sign-up and use; whether content is used for training; how data can be deleted; how feedback is used; what support participants receive; how participation can be ended; where security/technical questions can be clarified.

**Current state on the website**

- **There is no FAQ section or page anywhere in the tracked site.** A search for `accordion|faq|häufige` returns only the unused CSS/JS implementation (`css/experimental.css:1673–1682`, `js/site.js:42–64`) — i.e. an accordion component exists but is mounted on no page.
- Partial answers are scattered: study participation/compensation/effort (`waitlist.html:502–538`), data handling for sign-up (`waitlist.html:735–750`), AI limits (`kernel.html:445–474`), roadmap direction (`status.html:218–258`).

**Gap / blind spot:** This is a direct, unambiguous miss of a P0 benchmark item. The accordion infrastructure is even present but unused, which suggests the gap is content/structure, not capability. None of the benchmark's minimum FAQ questions (selection, response window, costs, deletion, training, participation end, support) is answered in one place.

---

## 1.13 Bilingual integrity and language-level consistency

**Benchmark expectation** (not a named section, but "clarity" and master-checklist "Can a person correctly restate the product, target audience, and next step?" apply in both languages; the repo's own `DESIGN-BRIEF.md:11` requires every decision to work in both languages).

**Current state on the website**

- Six pages use a shared `data-lang` DE/EN system driven by `js/site.js:66–91`; both languages are present in the markup.
- `waitlist.html` implements a **separate** inline language toggle (`waitlist.html:761–793`) and its `<title>`/description/OG tags are **English-only** (`waitlist.html:7`, `:8`, `:18`, `:25`) while the visible page defaults to German.
- Legal pages intentionally note DE-only authoritative text (`impressum.html:62`, `datenschutz.html:63`).

**Gap / blind spot:** The bilingual system works on the main pages, but the **conversion page is an outlier**: different language mechanism, English-first metadata, and no DE/EN `<title>` data attributes. For a German-primary site whose SEO/metadata is otherwise DE-first, the study page's English metadata is inconsistent and would be the page a German visitor lands on via the primary CTA. Not a legal or trust violation; a consistency and comprehension risk.

---

## 1.14 Naming and internal vocabulary

**Benchmark expectation** (§6 "Category framing"; §10 "Unclear product category", "AI buzzwords"): avoid internal jargon as public-facing category language; the visitor must understand what the product is.

**Current state on the website**

- Public-facing proper nouns: "Cervus" (`waitlist.html:7`, `status.html:78`, `:123`), "Kernel v0" (`status.html:82`, `:142`), "Midgard" (`status.html:169`), "Asgard" (`status.html:184`), plus "Der Kernel" as a top-level nav item (`index.html:48`).
- "Kernel" is explained on its dedicated page (`kernel.html:76–77`), but the homepage nav presents "Der Kernel" as a peer of "Team" and "Entwicklungsstand" without any explanation of what it is. "Cervus"/"Midgard"/"Asgard" are Norse/Latin internal project names, explained only inside `status.html` project cards.

**Gap / blind spot:** "Kernel" is a familiar technical word repurposed here for a proprietary system layer; it is defined on its own page but not at the point of first contact. "Cervus", "Midgard" and "Asgard" are internal codenames surfaced publicly without a plain-language gloss in the nav or headings (the status page does provide a summary sentence per project, `status.html:129`, `:149`, `:174`, `:189`). This is close to the benchmark's "AI buzzwords"/internal-jargon anti-pattern at the label level; the explanatory copy exists but the labels themselves are not self-explanatory.

---

## 1.15 Content items the benchmark lists but the site does not address

| Benchmark content item | Site status |
|---|---|
| FAQ (P0 module) | Absent (component exists, unused) |
| Dedicated AI transparency page | Absent; content embedded in philosophy/kernel |
| Security page (P0 for sensitive B2B data) | Absent; governance content in kernel/philosophy |
| Explicit "not yet" statements | Present and strong (`kernel.html:473`) |
| Team availability/roles | Present, includes honest placeholder (`team.html:108–110`) + open CTO (`:162–170`) |
| Selection criteria for access | Absent on the waitlist page (see Sprint 4) |
| Pricing/cost statement | Absent |
| Supported platforms/integrations | Absent |
| Data deletion path on the conversion page | Partly: `waitlist.html:738` ("jederzeit widerrufen … E-Mail") |

---

## 1.16 Sprint 1 summary of notable findings

**Strengths (explicitly matching or exceeding the benchmark):** problem-language precision (`index.html:101–119`); a disciplined, bounded-claim and "not promised" vocabulary (`kernel.html:445–474`); explicit separation of done/in-progress/planned with a directional (non-binding) roadmap (`status.html`); no "10x"/"seamless"/"future of work" hype; AI-governance content that is deeper than the benchmark minimum.

**Principal gaps:** (1) dual, unreconciled audience positioning (investor hero vs learner conversion); (2) hero lacks outcome, mechanism and product evidence and routes its dominant CTA away from conversion; (3) category framing is generic ("AI German learning") without the concrete scenario anchor the project already owns; (4) no FAQ module at all; (5) AI-transparency content is structurally buried and absent from the privacy/trust surface; (6) internal codenames ("Kernel", "Cervus", "Midgard", "Asgard") are surfaced without on-label explanation.

**Critical flags:** ⚠️ **CRITICAL** — §1.8: the waitlist/study page advertises a study "starting mid-June 2026" and contact "in June" while `index.html:90` and `status.html:78` state the pilot/Cervus phase is already completed (May–August 2026). Conflicting, stale, and deceptive availability/timing claims on the primary conversion path.
