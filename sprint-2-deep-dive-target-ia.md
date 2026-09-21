# Sprint 2 Deep Dive — Target Information Architecture

**Document type:** IA decision/design document (document-only; no code changed by this document).
**Status:** Target specification for a later implementation step. Not the final master checklist.
**Date:** 2026-09-21
**Inputs:** baseline `sprint-2-information-architecture.md`; `sprint-0-triage-and-sprint-1-decision-pack.md`; `founder-decisions-locked.md`; tracked repository; benchmark `Pre-Launch-Website-Exhaustive-Report.md`.
**Locked decisions honored:** #2 (waitlist reframed as truthful interest registration; consistent status labels), #5 (homepage primary audience = international professionals in Germany, engineering/tech, consulting and comparable white-collar profiles, job-search/interview/career-advancement context), #6 (beta communicated only as planned; no separate apply mechanic), #7 (Substack external deep link only; no homepage-primary CTA; no new consent mechanism). Decision #4 (partner/ecosystem block unchanged, A.4 closed) is treated as fixed.

All claims below are grounded in repo file:line and benchmark section citations. No production copy is written; message formulas and placeholders are used.

---

## 1. Ist → Soll sitemap

The site has nine tracked public HTML pages. "Ist" is the current role (from Sprint 2 §0 and §2.3). "Soll" is the target role. "Disposition" uses the requested categories: **Keep / Rename / Reframe / Deep-link-only / Defer**.

| # | Page (Ist) | Ist role | Disposition | Soll role | Rationale (decision / benchmark) |
|---|---|---|---|---|---|
| 1 | `index.html` | Homepage; investor-leaning hero (`:75`) with product sections | **Keep + Reframe** | Public homepage for the **primary audience** (professionals) with the career context leading; secondary audiences reachable but not dominant | Locked #5. Benchmark §4 hero requirements + §3 "what must appear early"; Sprint 1 §1.1/§1.5 found the hero currently addresses investors, not the primary user. |
| 2 | `philosophy.html` | Long-form 8-chapter philosophy essay; top-level nav (`:57`) | **Keep + Deep-link-only** | Contextual/deep-page evidence of method and stance; linked from Status/About context, not a primary homepage path | Benchmark §3 (progressive disclosure); Sprint 2 §2.1 (depth in the wrong place). No new copy. |
| 3 | `kernel.html` | Deep mechanism/system page; nav item (`:43`); currently absent from `sitemap.xml` | **Keep + Reframe** | Mechanism proof (the "how") — the credible product-artifact/diagram surface (`:142–220`). Add to sitemap on production. | Benchmark §3 "How it works" P0/P1; §4 wireframe step 4. Decision #1/#8 do not change its chosen architecture. |
| 4 | `team.html` | Team + advisors + open CTO role | **Keep** | Secondary-audience credibility (about/contact for investors, partners, technical collaborators) | Benchmark §3 "About / team" P1. Contains an out-of-scope legal-form string to flag (see §5). |
| 5 | `status.html` | Development status + directional roadmap; canonical status surface (`:61` "Stand: September 2026") | **Keep + Reframe** | Single, dated status surface carrying the three locked labels ("Cervus research completed", "private beta planned", "next research phase in preparation") | Locked #2. Benchmark §3 "Changelog/updates", §4 wireframe step 9 "Beta status", §6 Beta status module. |
| 6 | `waitlist.html` | Study-recruitment form; nav/footer CTA destination | **Keep + Reframe (done in Phase 2)** | Truthful **interest registration** for the planned private beta; no queue, no fixed date, no guaranteed response | Locked #1/#2. Benchmark §6 weak pattern "Join the waitlist", §7 "Waitlist decision". |
| 7 | `beta.html` | Unlinked placeholder ("Prototyp in Arbeit.", `:68–69`); `noindex`; not in nav/sitemap | **Defer** | Keep deferred/unlinked until a real status deep-link role exists; do not surface as a signup page | Locked #6 (no apply mechanic). `AGENTS.md` forbids linking `beta.html` without approval. Benchmark §3 "Don't inflate too early". |
| 8 | `impressum.html` | Legal notice; footer-linked everywhere (`index.html:302`) | **Keep** | Legal/trust; still draft with marked founder-input placeholders | Locked #3; Sprint 0 A.2. Benchmark §8 Germany/EU; §11 IA "legal … permanently findable". |
| 9 | `datenschutz.html` | Privacy notice; footer-linked everywhere (`index.html:303`) | **Keep** | Legal/trust; font statement corrected, open items marked | Sprint 0 A.3a/A.3b; locked #1 (waitlist meaning) affects section 4 wording. Benchmark §8 privacy P0. |

**Non-page public destination (decision #7):** the Substack development-updates channel remains an **external deep link** (currently `index.html:308` in the footer "Kontakt" column), not a page and not a homepage-primary CTA. No consent mechanism is introduced. Target placement: a clearly labeled external deep link in Status / About / Contact contexts.

**Pages that must NOT be created in this phase:** `/use-cases`, `/security`, `/ai-transparency`, `/faq`, `/contact`, `/for/*`, or any role/industry landing page. The benchmark marks several of these as P0/P1, but the founder's locked scope requires no new pages now; their substance already exists in `kernel.html:445–474` and `philosophy.html:264–269`, and surfacing it can be sequenced later without new routes (see §5).

---

## 2. Funnel routing model

Principle (benchmark §7 "one or two CTAs"; §10 "Conflicting CTAs"; founder decision: one clear funnel per intent): each contact intent gets one truthful path with one post-submit expectation. The homepage has exactly one primary route.

### Route A — Professionals / future users (HOMEPAGE-PRIMARY)

- **Intended visitor:** international professionals in Germany; engineering/tech, consulting and comparable white-collar profiles; job-search / interview / career-advancement context (locked #5).
- **Legitimate current value exchange:** registering genuine interest in the planned private beta; optionally receiving development updates (decision #7, via Substack deep link). No access, no queue, no date.
- **CTA semantics (formula):** `[interest marker] + [for what: the planned private beta] + [non-binding, no date, no queue]`. Candidate label semantics: "Interesse anmelden" (not "apply", not "join the beta", not "join the waitlist" with access connotation).
- **Page destination:** `waitlist.html` (reframed).
- **Must not imply:** available product; open beta; guaranteed access; queue position; fixed timing; guaranteed response; that registering is an application.
- **Priority:** **Primary.**
- **Mechanism:** one interest-registration form; no separate beta application (locked #6).
- **Post-submit expectation:** on-page confirmation; "your interest is noted; we will contact you when the beta or the next study actually opens"; no date and no response promise. (Already reflected in the Phase 2 success message.)

### Route B — Research interest

- **Intended visitor:** people who want to participate in the planned next research phase.
- **Legitimate value exchange:** being informed if/when a next research phase opens.
- **CTA semantics:** "Interesse an der nächsten Forschungsphase" — recruitment **not open**.
- **Page destination:** currently none (no new pages); direct email or, later, a routed intent option.
- **Must not imply:** recruitment is open, eligibility, timing, compensation, selection.
- **Priority:** Secondary / deep-link-only or direct email.
- **Post-submit expectation:** acknowledgement only; state recruitment is not open.

### Route C — Partners / organizations / tutors / schools

- **Intended visitor:** organizations, tutors, schools, ecosystem partners.
- **Legitimate value exchange:** a conversation about collaboration and the current stage.
- **CTA semantics:** "Kontakt zu Zusammenarbeit" / contact.
- **Page destination:** direct email (`bjarne.dudzus@disce.de`); no dedicated page now.
- **Must not imply:** an existing partnership or endorsement beyond the founder-confirmed partner/ecosystem block (locked #4, unchanged).
- **Priority:** Secondary / deep-link-only.
- **Post-submit expectation:** receipt acknowledgement; no response-time promise.

### Route D — Investors / strategic contacts / potential technical collaborators

- **Intended visitor:** investors, strategic contacts, CTO/technical collaborators.
- **Legitimate value exchange:** a direct conversation about the venture and current stage.
- **CTA semantics:** "Kontakt aufnehmen" / start a conversation.
- **Page destination:** direct email (existing `mailto:` pattern, e.g. `kernel.html:496`).
- **Must not imply:** a described round/valuation or product availability.
- **Priority:** Secondary / deep-link-only.
- **Post-submit expectation:** acknowledgement; no response-time promise.

**Homepage primary route decision (locked #5/#6):** Route A is the homepage's single dominant conversion path. It avoids misleading availability claims because it names interest (not access) as the action and the planned private beta (not an open one) as the object, and it carries no queue, date, or response promise (locked #1).

---

## 3. Homepage narrative skeleton mapped to the benchmark flow

Mapping to benchmark §4 "Wireframe sequence" (steps 1–13). Every claim below is status-true per locked decisions. Cervus = completed proof-of-principle evidence context; Kernel = mechanism; no active-availability claim anywhere. No production copy.

| Benchmark step (§4) | Soll section (homepage) | Evidence available in repo (file:line) | Must not claim |
|---|---|---|---|
| 1 Header | Keep 5 links + one interest CTA | `index.html:45–57` | No product-availability implication in nav; CTA label aligned to Route A |
| 2 Hero | Category + primary audience + career context + truthful status label | Audience anchor exists in personas (`:148–162`); category frame lives in lede/meta (`:7`, `:75`); Kernel/mechanism `kernel.html` | No outcome/product-availability claim; status = project in development / private beta planned; no "available now" |
| 3 Relevance / pain | Keep problem section | `index.html:96–122` | No over-dramatized generic problem; benchmark §4 step 3 |
| 4 Mechanism / How it works | Keep process list; link to Kernel | `index.html:167–220`; `kernel.html:307–356` | No autonomous-AI claim; bounded-claim language preserved (`kernel.html:445–474`) |
| 5 Product evidence | Use **Cervus completed** as evidence context + Kernel architecture artifact | `status.html:78` "Cervus — Abgeschlossen"; `kernel.html:142–220` | Must not present Cervus as active, or the Kernel as a live product; benchmark §10 "No product demonstration" is mitigated by the architecture plate, not by a fake screenshot |
| 6 Use cases | Keep persona/context cards (engineering/tech, consulting, comparable) | `index.html:144–165` (currently clinical-led; needs reframe to locked #5) | Persona tiles must not become identical/un-differentiated (benchmark §4 step 6) |
| 7 Differentiation | Add/keep status-quo contrast (e.g. "not a substitute for general language instruction") | Concept only; existing status-quo line `index.html:117`; `philosophy.html:247` | No unsubstantiated "10x" claim (benchmark §4 step 7) |
| 8 Trust | Team/advisors + completed research context | `team.html:67–143`; `status.html:78` | No unsupported partner/customer claims; partner block stays exactly as locked (#4) |
| 9 Beta status | Status box carrying the three locked labels | `status.html:70–89`; `waitlist.html` (reframed) | "Private beta planned"; no fixed date; recruitment not open; benchmark §6 Beta status module |
| 10 Trust / data | Short data answers with deep links to `datenschutz.html` | `datenschutz.html` (font statement corrected; placeholders marked) | No "enterprise-grade" / unsupported security claims (benchmark §8) |
| 11 FAQ | **Absent now** (no new pages); acknowledged gap | Unused accordion in `css/experimental.css:1673–1682`, `js/site.js:42–64` | Do not create an empty FAQ or marketing-repetition FAQ; benchmark §3 FAQ P0 module — deferred, see §5 |
| 12 Final CTA | Same CTA type as nav (Route A), no new logic | `index.html:244–265` | No new CTA type/logic at page end (benchmark §4 step 12); current band copy says "join the beta / earliest cohort" (`:256–257`) and must be reframed to planned status |
| 13 Footer | Keep structured footer; legal findable | `index.html:285–317` | No hidden legal info (benchmark §4 step 13) |

**Net change vs. Ist:** the homepage keeps its section skeleton (no redesign) but changes its *frame*: primary audience and career context lead; Cervus is the completed evidence anchor; Kernel is the mechanism; beta is planned-only; the final CTA is the interest registration.

---

## 4. Staging-vs-production posture decision

**Current Ist:** `robots.txt` = `Disallow: /`; every page carries `<meta name="robots" content="noindex, nofollow">` (e.g. `index.html:6`, `waitlist.html:6`, `impressum.html:6`, `datenschutz.html:6`); yet `canonical`/OG URLs point to `https://weltvorstellung.de/...` (e.g. `index.html:15`, `:22`) and `sitemap.xml` lists five URLs. `CNAME` = `stage.weltvorstellung.de`. This is a coherent **staging** posture with production-style metadata (Sprint 2 §2.12).

**Soll policy (stay staging until trust/legal blockers clear, then switch consistently):**

| Signal | Staging phase (current, until blockers clear) | Production/indexable phase (after blockers clear) |
|---|---|---|
| `robots.txt` | Keep `Disallow: /` | Allow crawling; remove the global disallow |
| Per-page `<meta name="robots">` | Keep `noindex, nofollow` on all pages | Remove `noindex`; keep `noindex` only on any deliberately-parked page (e.g. `beta.html` if still deferred) |
| `canonical` | Keep pointing at the production host (`weltvorstellung.de`) | Keep canonical to the production host; verify host matches serv |
| OG/Twitter | Keep as-is | Keep; align OG titles/descriptions with the reframed page roles |
| `sitemap.xml` | Keep as a manifest but it will not be honoured while robots disallows | Update to include the real public set (`index`, `philosophy`, `kernel`, `team`, `status`, `waitlist`, plus legal); exclude `beta.html` while deferred |

**Legal/trust items that BLOCK switching to indexable launch (must be resolved first):**
1. **Imprint placeholders** (`impressum.html:79`, `:80`, `:86`, `:102`, `:118`) — address, telephone, notice date, and the MStV address line remain founder-input markers (locked #3; Sprint 0 A.2).
2. **Privacy placeholders** (`datenschutz.html:80`, `:81`, `:90`, `:102`, `:103`, `:125`) — controller address, third-country transfer basis, retention, notice date (Sprint 0 A.3b).
3. **Waitlist residual study/June references** in the form controls, consent text, and privacy notice (`waitlist.html:612`, `:620`, `:627`, `:634`, `:667–668`, `:730`, `:737`), which were explicitly out of scope for Phase 2 but contradict locked #1/#2 at launch (see §5).
4. **Legal-form claim on team page** (`team.html:61` and `:167` still say "UG (haftungsbeschränkt)"), which conflicts with locked #3 ("do not claim any legal form") — out of scope for this run, flagged for the next step.
5. **Legal review** of imprint and privacy notice (lock file §d).

Items **not** blocking: A.4 (partner block closed by locked #4), A.3a (font statement corrected this run), A.1 headline/timing copy (contained this run; residuals above still block as noted).

---

## 5. Pre-flight dependencies for Sprint 3 and Sprint 4 deep dives

Each item is a dependency this IA decision creates for the later deep dives. No implementation here.

1. **Substack link placement (decision #7).** Target: a clearly labeled external deep link in Status / About / Contact contexts, not homepage-primary, no consent mechanism. Sprint 4 depends on where it lives relative to the interest-registration route (`waitlist.html`) and the footer (`index.html:308`).
2. **Status label single source (locked #2).** The three labels ("Cervus research completed", "private beta planned", "next research phase in preparation — recruitment not open") must be consistent across `status.html`, `waitlist.html`, and any homepage status module. Sprint 4's trust/status module and Sprint 3's content surfaces both depend on this single vocabulary.
3. **Trust modules relative to the conversion path (Sprint 4).** The IA does not create a `/security` or `/ai-transparency` page now; the depth stays in `kernel.html:445–474` and `philosophy.html:264–269`. Sprint 4 must decide how (if at all) to surface a trust link near the interest-registration form and whether the footer gains a clearly labeled link, without new pages.
4. **FAQ placement (deferred).** The FAQ is a benchmark P0 module but remains absent. Sprint 3/4 deep dives must decide whether it becomes a homepage module (reusing the already-present accordion `css/experimental.css:1673–1682`) or stays deferred, given the "no new pages" scope.
5. **Homepage final-CTA reframe (locked #2/#6).** `index.html:256–257` currently says "join the beta / earliest cohort". Sprint 3 (content/UI) or Sprint 4 (conversion) must reframe it to planned status and Route A semantics; this IA decision fixes the destination and semantics.
6. **Residual waitlist study/consent wording.** Sprint 4 depends on a founder decision to update the form-control labels, consent checkbox text, and privacy-notice section 4 (`waitlist.html:612`, `:620`, `:627`, `:634`, `:667–668`, `:730`, `:737`) to match the locked interest-registration meaning; these were excluded from Phase 2.
7. **`sitemap.xml` and indexability switch.** Sprint 3 (technical QA) depends on the staging→production policy in §4 and on the list of blockers before any `robots.txt`/`noindex` change.
8. **Nav/header consistency.** The header is duplicated across pages (Sprint 2 §2.13). Any CTA label change for Route A must be applied consistently; Sprint 3 depends on the single agreed label semantics.

---

**Grounding summary.** Repo anchors used: `index.html:6/15/22/45–57/75/96–122/144–165/167–220/244–265/256–257/285–317/302/303/308`; `kernel.html:43/142–220/307–356/445–474/496`; `team.html:61/67–143/167`; `status.html:61/70–89/78`; `waitlist.html:6/612/620/627/634/667–668/730/737` (plus Phase 2 changes); `philosophy.html:57/247/264–269`; `impressum.html:79/80/86/102/118`; `datenschutz.html:80/81/90/102/103/125`; `css/experimental.css:1673–1682`; `js/site.js:42–64`; `robots.txt`; `sitemap.xml`; `CNAME`. Benchmark anchors: §3 (Information Architecture), §4 (Landing-Page Dramaturgy), §6 (Content/Messaging/Beta communication), §7 (Conversion and Waitlist Strategy), §8 (Trust/Transparency/Legal UX), §10 (Anti-Pattern Catalog), §11 (Master Checklist).
