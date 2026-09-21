# Sprint 4 — Conversion, Waitlist Strategy & Trust/Legal/Transparency

**Assessment / situation report (diagnostic only). No fixes, no rewrites, no prioritisation.**

- **Subject:** Disce website, repository `weltvorstellung`, staging host `stage.weltvorstellung.de`.
- **Benchmark:** `Pre-Launch-Website-Exhaustive-Report.md` §6 "Beta status module", §7 "Conversion and Waitlist Strategy", §8 "Trust, Transparency, and Legal UX", §2 "Waitlist decision", §11 Master Checklist.
- **Method:** direct inspection of `waitlist.html` (the only form), all CTA instances, the footer/contact surfaces, `impressum.html`, `datenschutz.html`, and the trust-claim surfaces (`index.html` ticker, `team.html`). Repo-internal constraints (`AGENTS.md`, `DESIGN-BRIEF.md`) are referenced where relevant.
- **Interview date:** 2026-09-21.

## 0. The conversion and trust surfaces as they actually exist

- **Only conversion form:** `waitlist.html` (`<form id="waitlistForm" novalidate>`, `:558`), a **pilot-study recruitment** form, posting JSON to `https://waitlist-proxy.bjarne-dudzus.workers.dev` (`:871–878`), which stores in Airtable per `datenschutz.html:99`.
- **CTA instances pointing at it:** nav CTA on every page (`index.html:51` and mirrored), homepage final CTA band (`index.html:260`), status-page CTA (`status.html:276`), footer "Kontakt" column (`index.html:307`).
- **Contact surfaces:** `mailto:bjarne.dudzus@disce.de` (footer, `kernel.html:496`), Substack external link (`index.html:308`).
- **Legal surfaces:** `impressum.html` and `datenschutz.html`, both marked **"Entwurf, nicht freigegeben"** (`impressum.html:70`; `datenschutz.html:71`).
- **Trust-claim surfaces:** homepage partner ticker (`index.html:267–283`); team/advisors (`team.html:67–143`); development status (`status.html`); AI governance in `philosophy.html:264–269` and `kernel.html:445–474`.
- **Tracking/consent:** none. No analytics, no cookies beyond a `localStorage` language preference (`js/site.js:68–90`; `waitlist.html:782–787`); `datenschutz.html:110` states "Cookies zu Analyse- oder Marketingzwecken werden nicht gesetzt … kein Tracking".

---

## 4.1 Conversion model

**Benchmark expectation** (§7 "Three conversion models"): choose **Model A — broad waitlist** (email/frictionless), **Model B — qualified beta** (work email, role, workflow, problem, willingness), or **Model C — design partner** (company, role, problem, urgency, capacity). "The mistake is treating all three as equivalent or placing them side by side with equal visual emphasis." Model fit should follow the product type (§2 "Business-model dependency": "Data-sensitive AI product → qualified beta or accompanied pilot project").

**Current state on the website**

- The form is functionally closest to a **hybrid Model A/B study screener**: it asks first name, email, self-assessed German level, availability in June, microphone availability, contact consent, optional referral source (`waitlist.html:558–699`). It does **not** ask work email, role, team size, current workflow, or main problem (Model B fields), nor company/urgency/sponsor (Model C).
- The page frames the exchange as a paid research study: four 60–90 s monologues, ~25–30 min, Amazon voucher €7–10 (`waitlist.html:498`, `:527`, `:534`).
- Meanwhile the homepage CTA band promises something different: "tragen Sie sich in die Warteliste ein, um zur ersten Kohorte zu gehören" (`index.html:257`) and "Teil der Beta werden" (`:256`); `status.html` says beta is a *later* stage after the evidence base (`status.html:191`, `:195–207` commented out).

**Gap / blind spot:** The site presents three different offers through one destination: a **study** (Model A/B screener), a **beta cohort** (`index.html:256–257`, `status.html` CTA at `:276` and hidden "Beta" project at `:198–207`), and generically a **waitlist** (nav/footer labels). The benchmark requires one chosen model and warns against advertising a beta for a product whose beta is not operational. For a data-sensitive AI product the benchmark's suggested model is B or C, but the built form is the low-friction A/B screener with a study incentive, and its destination copy is not reflected in the CTA labels. This is a direct match to the anti-pattern "Conflicting CTAs" / "Worthless waitlist" (§10) at the *offering* level rather than the button level.

---

## 4.2 CTA principles and count

**Benchmark expectation** (§7 "CTA principles"): a pre-launch CTA conveys **action, value exchange, commitment, expectation**. Better CTA concepts name the exchange ("Apply for the research beta", "Get monthly build updates"). §7 "one or two CTAs": one primary CTA when a single ICP and low-friction conversion; two differentiated CTAs when intent levels differ, and the secondary must be visually weaker and semantically different.

**Current state on the website — CTA inventory**

| Location | Label | Destination | Conveys action | value | commitment | expectation |
|---|---|---|---|---|---|---|
| Nav (all pages) | "Auf die Warteliste" | `waitlist.html` | "join a list" | no | no | no |
| Homepage hero | "Das Team" (primary) | `team.html` | yes | no | no | no |
| Homepage hero | "Unsere Philosophie" (secondary) | `philosophy.html` | yes | no | no | no |
| Homepage final band | "Auf die Warteliste" (primary) | `waitlist.html` | yes | no | no | no |
| Homepage final band | "Entwicklungsstand ansehen" (secondary) | `status.html` | yes | no | no | no |
| Homepage team teaser | "Das Team →" | `team.html` | yes | no | no | no |
| Kernel hero | "Entwicklungsstand ansehen" (primary) | `status.html` | yes | no | no | no |
| Kernel hero | "Kontakt aufnehmen" (secondary) | `mailto:` | yes | no | no | no |
| Status page | "Auf die Warteliste" | `waitlist.html` | yes | no | no | no |
| Footer | "Auf die Warteliste" | `waitlist.html` | yes | no | no | no |
| Waitlist page submit | "Auf die Warteliste →" | POST | yes | no | no | no |

- The only place the value exchange and effort are stated is the study info card on the destination page (`waitlist.html:502–538`), not in any CTA label.
- **Four distinct primary-looking CTAs compete across the site** (Team, Waitlist, Status, Contact), and the homepage hero's dominant CTA ("Das Team") is unrelated to conversion.

**Gap / blind spot:** No CTA on the site carries the benchmark's four elements simultaneously; the primary conversion label ("Join the waitlist") is the benchmark's named weak pattern (no value exchange). On the homepage, the conversion path is not the dominant action, and there are multiple co-equal "primary" buttons across pages. The benchmark permits two differentiated CTAs; here the differentiation is by *destination topic*, not by intent level, so it produces routing rather than commitment.

---

## 4.3 Waitlist strategy

**Benchmark expectation** (§2 "Waitlist decision"): a waitlist is only a product mechanism when three questions are answered — (1) Why can't everyone access it yet? (2) According to what criteria / in what waves are invitations sent? (3) What does the person receive during the waiting period? Without them it is "a contact form with low informational value". §7 "Gamification" table likewise warns against selection criteria that remain hidden and artificial scarcity.

**Current state on the website**

- The waitlist page states a start date and a compensation, but answers **none** of the three questions:
  - Why access is limited: not stated.
  - Selection criteria/waves: not stated (the form asks availability, implying scheduling, but no selection logic).
  - What participants receive while waiting: only "wir melden uns im Juni zur Terminbestätigung" (`waitlist.html:555`).
- The form does ask a genuine qualification signal (self-assessed level B2–C2, `:599–609`) and a capacity signal (microphone, quiet space, `:665–668`), and the page states who can participate (`:506–507`), effort (`:534`) and compensation (`:527`). That is more than a bare email field.
- The word "Warteliste" is used throughout (`:550–551`, `:705–706`, `:712–713`) while the page's `<title>`/OG metadata call it "CERVUS Study" (`:7`, `:18`, `:25`), and `datenschutz.html:100` calls it "Verwaltung der Warteliste sowie Organisation und Durchführung der Studienteilnahme".

**Gap / blind spot:** The mechanism is internally coherent as **study recruitment** (purpose, level screen, scheduling availability, compensation) but is not a *waitlist* in the benchmark's sense: it has no access constraint, no selection explanation, and no waiting-period value. Labeling it "Warteliste" sets an expectation (product early access) the page does not fulfil; conversely, the study framing (€7–10 voucher, one-time session) is never surfaced in the CTA labels. The three benchmark questions are unanswered, and the benchmark's explicit "Justify the exclusion" test (§2 Trade-offs: "Limited spots are plausible when support, infrastructure, or research capacity is limited") has no corresponding statement.

---

## 4.4 Form design and friction

**Benchmark expectation** (§7 Model A/B details; §2 "Conversion vs. lead quality"; §5 EAS/form guidance via NN/g and UK GDS "one thing per page"): remove non-essential fields; use conditional questions rather than a uniformly long form; explain requirements/effort in advance; break large forms into logical steps, especially on mobile; metrics for Model B include qualified applications, ICP fit, interview rate.

**Current state on the website** (`waitlist.html`)

- Fields: first name (required), email (required), self-assessed German level (required), availability in June 2026 multi-select (required), "I have a working microphone and a quiet space" (required checkbox), "I agree to be contacted" (required checkbox), referral source (optional) (`:560–699`).
- Required fields are marked with `*` (`:565`, `:581`, `:597`, `:621`, `:667`, `:675`); the form is `novalidate` and validates in JS (`:805–843`).
- Effort and compensation are explained **before** the form in the info card (`:502–538`), matching the benchmark's "explain requirements and approximate effort in advance".
- The form is a **single long card** with an internal divider rather than the benchmark/GDS multi-step or conditional pattern; on mobile it collapses but remains one page (`waitlist.html:429–437`).
- There is no work-email requirement, no role/company/team-size field, and no "main problem" field — the qualification is limited to language level and logistics.

**Gap / blind spot:** Field economy is reasonable and every required field has a stated rationale, so the EAS "remove first" step is largely respected. Two benchmark-relevant gaps: (a) the form asks **availability for a specific month ("Juni 2026")** and a **language level as self-assessment** but does not screen for the product's actual ICP (B2–C2 professionals in DACH) as tightly as `DESIGN-BRIEF.md:16` defines it — anyone B2–C1 can apply (`:507`); (b) as a study screener for a data-sensitive voice-data product, the form collects personally identifying contact data plus voice-adjacent usage context without any question about the participant's consent to future product use or data-processing nuance beyond the single contact-consent checkbox. The single-step layout is acceptable for the field count; the "one thing per page" guidance is context-dependent (`[K]`) at this size.

---

## 4.5 Thank-you flow and follow-up

**Benchmark expectation** (§7 "Thank-you flow and follow-up"; §6 "Beta status module"): after submit, the page should provide visible confirmation **not solely dependent on email**, a summary of the next step and realistic response/invitation logic, a link to privacy information, the ability to correct information or withdraw, and optionally a booking/relevant question — but no second mandatory form. Follow-up sequence: immediate confirmation → qualification/scheduling → substantive updates at an announced frequency → invitation with onboarding → a message if access is not possible/delayed. A weak thank-you page "wastes intent".

**Current state on the website** (`waitlist.html`)

- On success, the form is hidden and a success banner is shown: "✓ Du bist auf der Liste! Wir melden uns im Juni. Danke!" (`:711–714`, JS `:887–888`). It is a visible on-page confirmation, not dependent on email delivery — a partial match.
- On error, an error banner appears with fallback advice ("Bitte versuche es erneut oder schreib uns direkt", `:715–718`), and the button is re-enabled (`:892–894`).
- There is **no link to `datenschutz.html`** in the success state or the form; the privacy notice is a separate card below the form (`:727–753`) that names the controller and a mailto but does not deep-link the privacy policy or offer a correction/withdrawal mechanism beyond "schreib uns eine E-Mail" (`:738`).
- There is **no stated response window, selection process, next step, or frequency of updates** beyond "we'll be in touch in June".
- The success message and error message are not announced programmatically (Sprint 3 §3.8).

**Gap / blind spot:** The confirmation is visible and the error state is handled, but the benchmark's checklist for the post-submit experience is largely unmet: no response window, no selection logic, no privacy deep link, no self-service correction/withdrawal, no follow-up sequence. For a study that offers compensation, the absence of a clear scheduling/timing expectation beyond a possibly-past month is both a conversion-quality and a participant-trust problem. "We'll be in touch in June" combined with a status page saying Cervus completed in May–August 2026 (Sprint 1 §1.8) means the post-submit promise is itself unreliable.

---

## 4.6 Gamification

**Benchmark expectation** (§7 "Gamification" table): referral only with genuine network effect; invite system only when capacity increases in waves; queue position only when order matters; progress bars only for multiple necessary steps; quiz only to improve routing/eligibility; application only when lead quality is needed and criteria are visible; limited spots only with a real limit.

**Current state on the website**

- No referral mechanic, no invite system, no queue position, no progress bar, no quiz, no countdown, no "limited spots" language. The form collects availability (a capacity signal) but displays no scarcity.
- `philosophy.html:269` explicitly rejects manipulation ("keine Pay-to-win-Mechaniken") and `:249` describes a long-term "Animal-Crossing-Paradigma" for productive gamification inside the product (not the website).

**Gap / blind spot:** This item **meets** the benchmark; the site is free of gamification anti-patterns and artificial scarcity. The only nuance is that the page uses "Warteliste" (a queue metaphor) without a queue mechanic or ordering logic, which is a terminology mismatch rather than a manipulative mechanic.

---

## 4.7 Social proof and trust claims

**Benchmark expectation** (§8 "Legitimate pre-launch proof" and "Problematic trust claims"; §6 weak pattern "Trusted by … with weak proof"; §10 "Premature social proof"): proof must be **specific and proximate**; logos/testimonials without a clear relationship type create credibility risk; problem phrases: "Trusted by" for mere conversations, customer numbers mixing list/test/active usage, logos without approval, testimonials from people without product experience.

**Current state on the website**

1. **Partner ticker.** `index.html:268–283`: label "Strategische Partner &amp; Ökosystem" over `stromgold-logo.png` (StromGold), `potsdam-startup-service.jpg` (alt "University of Potsdam, Potsdam Transfer Startup Service"), `gruenden-in-brandenburg.jpg` (alt "Gründen in Brandenburg, WFBB"), followed by seven empty slots. The relationship type is not described anywhere on the page. `team.html:92` lists a co-founder as "Junior Associate bei StromGold AB", so at least one "strategic partner" is the employer of a team member; "University of Potsdam, Potsdam Transfer Startup Service" and "Gründen in Brandenburg, WFBB" are recognized startup-support programs, not necessarily partners. `_screenshots` and the untracked assets suggest these logos were sourced from the open web (jpg/png), and the round-2 notes (untracked `docs/website-round2/…`) describe the ticker as "honest but thin" with usage rights still to be cleared (per the explore summary of that doc). No consent/relationship documentation is in the tracked tree.
2. **Testimonial-styled card.** `index.html:80–83` uses `<figure class="glass-card glass-testimonial"><blockquote>…</blockquote>` styled as a testimonial, attributed to "Was wir mit Disce verändern wollen" (an aspiration, not a person). The class name and pattern read as social proof though the attribution makes clear it is not. The same quote is repeated at `:135` and `:226`.
3. **Team credibility.** `team.html:67–143` presents real names, degrees, roles and named advisors (Julian Kaulitzki, Maja Perković & Alexei Konstantinov, Aljoscha Heiland, Dr. Nikolas Höhnke) with concrete relationship labels ("Technische Beratung", "Accelerator-Mentoring", "Mentor"). This **meets** the benchmark's "explicit relationship type" requirement. Placeholder portraits (`alt="Portrait placeholder: …"`) and a placeholder team card are honest but incomplete.
4. **Research validation.** The pilot is described as a completed/ongoing RCT (`team.html:74`, N=150) and as "die abgeschlossene Masterarbeit" (`status.html:129`); no source, report, or result is linked. The benchmark's "Research validation" proof type requires "source, scope, and limitations".
5. **No customer count, no "trusted by", no user testimonials, no fake logos of non-consenting companies** were found beyond the ticker issue.

**Gap / blind spot:** The team/advisors surface is benchmark-aligned. The **partner ticker is the clearest trust-claim risk**: it asserts "Strategische Partner" as fact without disclosing relationship types, while at least one entity is a team member's employer and others are ecosystem programs. Combined with the benchmark's "endless logo marquee" anti-pattern and the absence of documented logo permissions, this is precisely the benchmark's "logos without relationship type"/"premature social proof" warning. The aspirational "testimonial" card is a lesser concern because its caption disclaims attribution.

**Critical flag:** ⚠️ **CRITICAL** — the homepage presents "Strategische Partner &amp; Ökosystem" logos as fact (`index.html:268–274`) with no relationship disclosure and at least one demonstrably different relationship (co-founder's employer, `team.html:92`). This is an unverifiable relationship claim presented as established fact, which is the benchmark's named trust-debt/credibility risk with potential brand-usage/legal exposure. Unlike ordinary polish, it is a live claim on a deployed page.

---

## 4.8 Trust modules and AI trust

**Benchmark expectation** (§8 "Trust modules and AI trust"): for an early AI/B2B product, a compact trust page is often sufficient — responsible company and security contact; data categories and purposes; data flow and storage region; subprocessors; deletion/retention; encryption/access control as implemented; training policy; incident contact; status of audits/certifications **without faking them**; clear "not yet" statements. A full trust center only becomes necessary once buyers run security reviews. NN/g/NIST: transparency, control, consistency, support-when-the-system-fails.

**Current state on the website**

- There is **no `/security`, `/trust` or `/ai-transparency` page**. The nearest equivalents:
  - `kernel.html:445–474` ("Die Grenzen"): explicit non-claims, no suitability/person assessment, no selection use, no invented precision, and "V0 does not claim validated long-term effectiveness…".
  - `kernel.html:404–442` ("Der Datenvorteil"): versioned state, calibratable parameters, provenance manifests, governance as governed objects.
  - `kernel.html:234–235`: "Anbieterneutral und EU-gehostet … Betrieb in einer kontrollierten EU-Region".
  - `philosophy.html:264–269`: model choices, EU hosting intent, data categories, training/consent policy, DSGVO + EU AI Act orientation, content-labeling and appeal paths, explicit "what we will not do".
  - `datenschutz.html`: hosting (GitHub Pages, USA), DNS/email (STRATO, Berlin), waitlist processing (Cloudflare + Airtable, USA) — but this is a data-protection notice, not a security page, and it contains no encryption/access-control or incident-contact information.
- **Data-flow specificity is strong**: `datenschutz.html:87–103` names host, registrars and the form subprocessors; the Kernel names the app stack (Next.js, FastAPI, PostgreSQL) and the provider boundary (`kernel.html:162–178`).

**Gap / blind spot:** The substance exists but has no trust surface and no proximity to conversion. Nothing in the conversion path (form or its vicinity) links to the Kernel's governance content or the philosophy's AI section, and `datenschutz.html` — the only trust document in the footer — omits AI processing, model/subprocessor list for the product (as opposed to the form), encryption/access control, training policy in operational terms, and security/incident contact. The benchmark marks Security as **P0 for sensitive B2B data**; this is a clear structural miss, with the mitigating fact that the site's public claims are conservative rather than overclaiming.

---

## 4.9 Legal & privacy UX (Germany/EU)

**Benchmark expectation** (§8 "Germany and the EU"): non-legal-advice; imprint under § 5 DDG easily recognizable, directly accessible, permanently available; privacy policy reflecting the actual tool stack; data minimization and retention; form transparency (purpose, recipients/services, follow-up type); newsletter separation; consent freely given/specific/informed/unambiguous and non-essential tracking only after opt-in; easy withdrawal; third-party embeds in the inventory; BFSG applicability review.

### 4.9.1 Impressum

**Current state** (`impressum.html`): the page carries a prominent **"Entwurf, nicht freigegeben"** banner (`:68–71`), and the provider identification is **unfilled placeholders**: `[VOLLSTÄNDIGER NAME DER VERANTWORTLICHEN NATÜRLICHEN PERSON]`, `[LADUNGSFÄHIGE ANSCHRIFT …]`, `[PLZ, Ort]`, `[TELEFONNUMMER]`, `[E-MAIL-ADRESSE]`, `[NAME]`, `[ANSCHRIFT WIE OBEN]`, and `Stand: [DATUM EINSETZEN]` (`:78–88`, `:91`, `:100–103`, `:118`). The page correctly states that pre-registration the responsible natural person must be named, and that "UG (haftungsbeschränkt)"/"i. Gr." may not yet be used (`:76`), which is legally literate.

**Gap:** The imprint is **linked publicly from the footer on every page** (`index.html:302`) but contains no actual provider identification. A visitor who needs to identify the operator — or an authority — finds a draft. The benchmark's P0 requirement ("provider identification easily recognizable, directly accessible, permanently available") is unmet by content.

**Critical flag:** ⚠️ **CRITICAL** — missing provider identification (name, address, contact, responsible person) under § 5 DDG on a publicly reachable, footer-linked page. This is a gross legal/trust violation regardless of the pre-incorporation stage.

### 4.9.2 Datenschutzerklärung

**Current state** (`datenschutz.html`): also bears the **"Entwurf, nicht freigegeben"** banner (`:69–72`) and contains:
- Placeholder controller (`[VOLLSTÄNDIGER NAME]`, `[LADUNGSFÄHIGE ANSCHRIFT]`, `[PLZ, Ort]`, `[E-MAIL-ADRESSE]`, `:79–82`).
- An unresolved third-country transfer basis for GitHub Pages: `[ZU PRÜFEN: Angemessenheitsbeschluss EU-US Data Privacy Framework bzw. Standardvertragsklauseln …]` (`:90`).
- For the waitlist: Cloudflare Worker + Airtable (USA) with `[ZU PRÜFEN: …]` and the statement that DPAs **must still be concluded and documented before go-live** (`:99–103`).
- An **outdated and now inaccurate statement about fonts**: "Auf der Warteliste-Seite werden derzeit Schriftarten von Google Fonts … beim Seitenaufruf nachgeladen. Dabei wird die IP-Adresse an Google übermittelt." (`:105–107`). In the current code, `waitlist.html` self-hosts Inter and Noto Serif (`waitlist.html:29–46`) and there is no Google Fonts request anywhere in the tracked tree. The policy therefore **does not reflect the actual tool stack**, which is the benchmark's explicit privacy requirement.
- Retention deadline left as `[FRIST FESTLEGEN]` (`:103`) and `Stand: [DATUM EINSETZEN]` (`:126`).
- Correct and useful features: named hosting/DNS/email providers, purpose + legal basis per processing, data-subject rights with the Berlin supervisory authority named (`:116–118`), necessity statement (`:120–121`), no automated decision-making (`:123–124`), and a courtesy English summary (`:130–139`). Device storage is correctly justified under § 25(2)(2) TDDDG and no analytics/tracking is declared (`:109–111`).

**Gap:** The privacy notice is substantively well-drafted but incomplete (placeholders, unconfirmed transfer basis, retention TBD) and **factually wrong about fonts**. It is publicly linked from every page footer.

**Critical flag:** ⚠️ **CRITICAL** — publicly linked privacy notice containing unfilled placeholders (`[VOLLSTÄNDIGER NAME]`, `[FRIST FESTLEGEN]`), an unconfirmed third-country transfer basis (`[ZU PRÜFEN]`), and a statement about Google Fonts that contradicts the deployed code. A privacy notice that misstates the actual processing is a GDPR transparency failure with real legal risk.

### 4.9.3 Consent, cookie banner, tracking

**Current state:** No consent banner, because there are no non-essential trackers (verified: no analytics/cookie scripts anywhere in the tracked tree). Language preference is stored in `localStorage` (`js/site.js:88`; `waitlist.html:787`), justified as strictly necessary in `datenschutz.html:109–111`. The form requires an explicit contact-consent checkbox (`waitlist.html:671–677`) with legal basis stated (`:739`).

**Gap / blind spot:** The *absence* of a banner is consistent with the benchmark's "consent only where required" posture and the privacy-friendly-analytics guidance (`§8`), so this item **meets** the benchmark — provided no tracker is added later without consent logic. There is **no newsletter/marketing consent** at all: the form's consent is scoped to "contacted for this study" (`:674`), and updates are offered only via an external Substack link (`index.html:308`), which is not an embedded signup and is not covered by the site's privacy logic. This correctly respects the benchmark's "newsletter separation" rule (nothing merged), but it means there is **no owned follow-up channel** (see §4.10).

### 4.9.4 Form transparency and withdrawal

**Current state:** The form's purpose and the services used are disclosed in the adjacent privacy card (Airtable, purpose, retention, withdrawal by email; `waitlist.html:735–750`) and in `datenschutz.html:97–103`. The benchmark requires the form's purpose, recipients, and follow-up type to be understandable; recipients and purpose are present, but the **follow-up type is not** ("we'll be in touch in June" only). Withdrawal is offered only by email (`:738`), with no settings link or self-service. There is **no deep link from the waitlist page to `datenschutz.html`**.

**Gap / blind spot:** Purpose is clear; withdrawal is technically available but not "easily accessible and practically usable" in the benchmark sense; the missing privacy link on the conversion page itself is a proximity failure the benchmark calls out ("privacy reassurance belongs near forms", §8).

### 4.9.5 BFSG / accessibility reinforcement

**Benchmark expectation** (§8): since 28 June 2025 the BFSG covers certain consumer-facing products/services; applicability to a pre-launch or purely B2B page must be reviewed separately.

**Current state:** No BFSG statement or assessment exists anywhere in the tracked tree. `AGENTS.md` has an accessibility guardrail, but no legal applicability review is documented.

**Gap / blind spot:** Not assessed. Given the site targets consumers (learners) as well as B2B/investors, the benchmark's "review separately" caveat applies; absence of any recorded review is a documentation gap rather than a proven violation.

---

## 4.10 Analytics, measurement and follow-up with low traffic

**Benchmark expectation** (§7 "Measurement with low traffic"; §11 Master Checklist "Are funnel and lead quality tracked by source?"): define the hypothesis and signal before launch; report absolute funnel steps; track by source; use qualitative follow-ups; sequential messaging tests rather than underpowered A/B; track invite acceptance/usage. Also a defined operational follow-up process ("a website should not collect leads that the team can neither answer nor activate", §12).

**Current state on the website**

- **No analytics of any kind** (privacy-friendly or otherwise). `datenschutz.html:110` confirms no reachweitenmessung/tracking. The `source_channel` field (`waitlist.html:688–699`) is the only self-reported acquisition signal; the form's language preference is also captured (`:855–865`).
- The conversion endpoint is a Cloudflare Worker → Airtable (`:871–878`); no funnel instrumentation, no event tracking, no confirmation email logic is visible in the repo.
- There is no owned follow-up channel: updates go through an external Substack (`index.html:308`) whose audience is not connected to the site's consent record; the only email path is `mailto:bjarne.dudzus@disce.de`.

**Gap / blind spot:** With zero tracking, the site cannot answer any of the benchmark's low-traffic measurement questions (funnel steps, source, ICP fit, drop-off) from its own data — only from Airtable tables and manual conversation. This is a legitimate consequence of the no-tracking/privacy stance (`[K]` context: the benchmark's privacy-friendly-analytics recommendation would suggest *some* cookieless aggregate analytics rather than none). More materially, the benchmark's operational-follow-up requirement is only half-present: there is a working submission pipeline, but no announced communication frequency, no confirmation email described, and no owned list. The Substack link offers no indication that signing up is connected to the study or the product.

---

## 4.11 Trust/legal content items the benchmark lists but the site does not address

| Benchmark trust/legal item | Site status |
|---|---|
| Imprint complete and published (P0) | Draft with placeholders, publicly linked — see 4.9.1 |
| Privacy policy matching the tool stack (P0) | Draft, placeholders, inaccurate fonts statement — see 4.9.2 |
| Non-essential trackers blocked before consent (P0) | N/A — no trackers at all |
| Security contact for risk questions | Absent (only general mailto) |
| Data flow/storage region for the **product** (as opposed to the form) | Kernel mentions EU-controlled region (`kernel.html:235`); no product-level trust page |
| Subprocessor list for the product | Absent (form subprocessors named only in the privacy policy) |
| Training-use policy in plain operational terms | Only "explicit opt-ins for … later, selective fine-tuning" (`philosophy.html:266`) |
| Audit/certification status without faking | Correctly absent; explicit refusal to make certification promises (`philosophy.html:269`) |
| Password/encryption/access-control status | Absent |
| Incident contact | Absent |
| Clear "not yet" statements | Present and strong (`kernel.html:473`) |

---

## 4.12 Sprint 4 summary of notable findings

**Strengths (matching or exceeding the benchmark):** no gamification anti-patterns, no fake scarcity, no countdown, no queue; zero third-party trackers and no unjustified consent banner; a correctly scoped, explicit contact-consent checkbox with stated legal basis; real, relationship-labeled advisors and team members; unusually explicit "not yet" and no-certification claims; specific hosting/subprocessor disclosure in the privacy notice; strong data-flow specificity in the Kernel.

**Principal gaps:** (1) three conflicting offers (study, beta, waitlist) behind one mislabeled destination; (2) every CTA lacks the benchmark's value-exchange/expectation elements; (3) the waitlist answers none of the benchmark's three waitlist questions; (4) the thank-you state lacks response window, selection logic, privacy deep link, and withdrawal/self-service; (5) no trust/security surface and no proximity of trust content to the form; (6) no owned follow-up channel and no measurement/analytics at all; (7) no privacy link on the conversion page and no BFSG review.

**Critical flags (4):**

1. ⚠️ **CRITICAL** — §4.9.1: publicly linked Imprint (`impressum.html`) is a draft with no provider identification (§ 5 DDG placeholders).
2. ⚠️ **CRITICAL** — §4.9.2: publicly linked privacy notice (`datenschutz.html`) is a draft with unfilled placeholders, an unconfirmed third-country transfer basis, and a Google-Fonts statement that contradicts the deployed self-hosted fonts.
3. ⚠️ **CRITICAL** — §4.7: homepage claims "Strategische Partner &amp; Ökosystem" over logos (`index.html:268–274`) without relationship disclosure, while one listed entity is a co-founder's employer (`team.html:92`); an unverifiable relationship presented as fact.
4. ⚠️ **CRITICAL** — §4.1/§4.3/§4.5 (carried from Sprint 1 §1.8): the only conversion path advertises a study "starting mid-June 2026" and contact "in June" while `index.html:90` and `status.html:78` state the pilot/Cervus phase is complete (May–August 2026), making the post-submit expectation and the availability claim unreliable.
