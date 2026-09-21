# Sprint 2 — Information Architecture & Landing-Page Narrative

**Assessment / situation report (diagnostic only). No fixes, no rewrites, no prioritisation.**

- **Subject:** Disce website, repository `weltvorstellung`, staging host `stage.weltvorstellung.de`.
- **Benchmark:** `Pre-Launch-Website-Exhaustive-Report.md`, chiefly §3 "Recommended Information Architecture", §4 "Ideal Landing-Page Dramaturgy", §10 anti-pattern catalogue, §11 Master Checklist.
- **Method:** direct inspection of all tracked pages and their navigation/footer, plus `sitemap.xml`, `robots.txt`, `CNAME`, `site.webmanifest` and `js/site.js`. Line references are to the current tracked files.
- **Interview date:** 2026-09-21.

## 0. Page inventory as it actually exists

| File | In main nav? | In footer? | In `sitemap.xml`? | `noindex`? | Role as built |
|---|---|---|---|---|---|
| `index.html` | yes ("Start") | yes | yes | yes (`:6`) | Homepage |
| `philosophy.html` | yes ("Philosophie") | yes | yes | yes (`:6`) | Long-form philosophy essay (8 chapters) |
| `kernel.html` | yes ("Der Kernel") | yes | **no** | yes (`:6`) | Deep product/system mechanism |
| `team.html` | yes ("Team") | yes | yes | yes (`:6`) | Team + advisors + open CTO role |
| `status.html` | yes ("Entwicklungsstand") | yes | yes | yes (`:6`) | Development status/roadmap |
| `waitlist.html` | yes (CTA "Auf die Warteliste") | yes | yes | yes (`:6`) | Pilot-study recruitment form |
| `beta.html` | **no** (per `AGENTS.md`) | no (has its own footer) | no | yes (`:6`) | Unlinked placeholder |
| `impressum.html` | no | yes ("Impressum") | no | yes (`:6`) | Legal notice (draft) |
| `datenschutz.html` | no | yes ("Datenschutzerklärung") | no | yes (`:6`) | Privacy policy (draft) |

Source of nav: repeated header block e.g. `index.html:45–57`; footer blocks e.g. `index.html:285–317`. `sitemap.xml` lists five URLs. `robots.txt` is `Disallow: /`. `CNAME` is `stage.weltvorstellung.de`. Every page carries `<meta name="robots" content="noindex, nofollow">`.

### Structural fact that frames this whole sprint

The site operates as **two overlapping architectures in one tree**:

1. **A product/venture narrative** — Home → Philosophy → Kernel → Team → Status, with a study-signup conversion page.
2. **A learner-facing product narrative** — the homepage problem/for-whom/how-it-works sections plus the study form.

There is no page whose declared job is the *product* (no `/product`, no `/use-cases`, no `/security`, no `/faq`, no `/about`), and there is no page that is unambiguously the investor/partner conversion surface (that job is split across `kernel.html`, `team.html` and mailto links).

---

## 2.1 IA model: lean vs. comprehensive

**Benchmark expectation** (§3 "Lean model" vs "Comprehensive model"; "Don't inflate too early"): choose lean (homepage + `/beta` + `/privacy` + `/imprint`) for a small team/focused MVP/low complexity; choose comprehensive (dedicated `/product`, `/use-cases`, `/security`, `/ai-transparency`, `/about`, `/faq`, `/contact`, `/updates`) for an ambitious B2B/AI product with **sensitive data** and explanation-heavy workflow. The benchmark also warns that adding pages used by established SaaS sites, without visitor need, "expose[s] thinness rather than maturity".

**Current state on the website**

- The site is **neither** model. It has created depth pages that correspond to the *comprehensive* model's `/product` (`kernel.html`) and parts of `/about` (`team.html`) and `/updates` (`status.html`), but it **omits** the comprehensive model's `/security`, `/ai-transparency`, `/faq` and `/contact` pages.
- It also exceeds the lean model by linking `philosophy.html` (a ~2,900-word DE + ~2,800-word EN essay, `philosophy.html:138–421`) as a **top-level nav item** — a page the benchmark's lean model does not include and the comprehensive model includes only as `/about`.
- Data-sensitivity indicators that, per the benchmark §2 "Business-model dependency" (row "Data-sensitive AI product"), point toward the comprehensive model: the product processes "personenbezogene Sprachdaten" (`team.html:167`), the Kernel handles "Einwilligung, Widerruf, Zweckbindung und Löschung" (`kernel.html:437`), and voice data is planned (Kernel architecture mentions ASR providers, `kernel.html:173–174`).

**Gap / blind spot:** The architecture is **inverted relative to both models**: it has the comprehensive model's expensive deep pages (`Kernel`, a long `Philosophy` essay, a detailed `Status` roadmap) but lacks the comprehensive model's *trust and decision* pages (`Security`, `AI transparency`, `FAQ`, `Contact`). A data-sensitive AI product is expected to answer risk questions (`§3 Page decisions`: "Security / trust … P0 for sensitive B2B data"; "AI transparency … P0/P1 for AI") before it deepens mechanism content. Here the mechanism is deepened to a level the benchmark lists as a late/optional concern ("Details without narrative" anti-pattern, §10), while the risk questions have no navigational home. This is not "too many pages" in the benchmark's inflation sense; it is **depth in the wrong places**.

---

## 2.2 Header / navigation

**Benchmark expectation** (§4 wireframe row 1 "Header": "Logo, 3–5 links, primary CTA"; §10 "Overloaded navigation"; Master Checklist IA: "Does every navigation page answer a real visitor question?"; "Are there no empty blog, careers, or changelog sections?"). Primary CTA should be one main path.

**Current state on the website** (`index.html:38–59`)

- Brand + hamburger + nav with **five links** ("Start", "Philosophie", "Der Kernel", "Team", "Entwicklungsstand"), a **"Join the waitlist" CTA** styled as `nav-cta`, and a **DE/EN switch**.
- The nav is identical on `beta.html`, `team.html`, `kernel.html`, `status.html`, `impressum.html`, `datenschutz.html`, `philosophy.html` (only the `active`/`aria-current` marker changes).
- The mobile toggle is implemented in `js/site.js:1–25` with `aria-expanded`, `aria-controls`, Escape-close and outside-click-close.

**Gap / blind spot:**

- The five nav links each answer *some* real question, so the "empty page" risk is low — but two of them ("Philosophie" and "Der Kernel") are **long-form, high-effort, non-decision pages** occupying scarce header slots, while the decision-critical `/faq`, `/security` and `/about`-as-contact pages are absent. The header therefore routes first-time visitors into depth rather than into reassurance.
- The CTA label "Auf die Warteliste" (`index.html:51`) points to a **study-recruitment** page, not a product waitlist (see Sprint 1 §1.1 and Sprint 4). The nav CTA thus mislabels both the action and its destination.
- The nav is the same for an investor-first homepage and a learner-first study page; the benchmark notes the header should carry "one main path" (`§4`), but the site's main path changes meaning depending on audience.
- Count is within the benchmark's 3–5 links plus CTA; no "enterprise navigation before product maturity" was found. This item largely **meets** the benchmark on form while missing on routing logic.

---

## 2.3 Page-by-page purpose and priority vs. the benchmark table

**Benchmark expectation** (§3 "Page decisions" table): Homepage P0; Beta/early access P0 for a waitlist; How it works P0/P1; Use cases P1; Security P0 for sensitive B2B data; AI transparency P0/P1 for AI; About/team P1; FAQ P0 as a module; Changelog/updates P2; Roadmap P2; Blog P2; Contact P1; Privacy/Imprint P0.

**Current state, mapped:**

| Benchmark page | Present? | Where | Notes |
|---|---|---|---|
| Homepage (P0) | Yes | `index.html` | Carries problem/for-whom/how-it-works/team/CTA |
| Beta / early access (P0 with waitlist) | **No real page** | `beta.html` is a 2-line placeholder, unlinked | The function is served by `waitlist.html`, which is a *study* page, not a beta/early-access page |
| How it works (P0/P1) | Yes | `index.html:168–220`; deeper at `kernel.html` | Mechanism is split across two surfaces and the deep one is a nav item |
| Use cases (P1) | Partial | `index.html:144–165` persona cards | Two personas, not trigger→job→outcome case pages |
| Security / trust (P0 for sensitive data) | **Absent as a page** | Fragments in `kernel.html:445–474`, `philosophy.html:264–269` | No navigational entry point |
| AI transparency (P0/P1 for AI) | **Absent as a page** | `philosophy.html:264–269`, `kernel.html` | Same |
| About / team (P1) | Yes | `team.html` | Includes placeholders and an open role |
| FAQ (P0 as module) | **Absent** | Unused accordion in `css/experimental.css:1673`, `js/site.js:42` | See Sprint 1 §1.12 |
| Changelog / updates (P2) | Replaced by `status.html` | `status.html` | Directional roadmap rather than dated changelog; benchmark lists changelog P2, so acceptable |
| Roadmap (P2) | Yes | `status.html:218–258` | Explicitly "keine verbindlichen Termine" (`:224`) |
| Blog / resources (P2) | External only | Substack link in footer (`index.html:308`) | Not embedded; benchmark P2, acceptable |
| Contact (P1) | Partial | `mailto:` links in footer (`index.html:309`), `kernel.html:496`, `team.html` | No contact page or form; benchmark P1 |
| Careers (P2) | As a section | `team.html:162–170` open CTO | Not an empty careers page; acceptable |
| Privacy / imprint (P0) | Yes, but drafts | `impressum.html`, `datenschutz.html` | Both marked "Entwurf, nicht freigegeben" (`:70`, `:71`) — see Sprint 4 |

**Gap / blind spot:** Relative to the benchmark's P0/P1 table for a data-sensitive B2B/AI product, the site is missing three P0/P1 surfaces — **Beta/early access as such, Security/trust, FAQ** — and has under-built **Use cases** and **Contact**. Conversely it has built P2-depth content (a full roadmap page, a long philosophy essay). The single clearest IA blind spot is that **the only linked conversion page answers a study-recruitment question while the nav labels it a waitlist**, and there is no page that explains *what access is being applied for*.

---

## 2.4 Landing-page narrative flow vs. the recommended wireframe sequence

**Benchmark expectation** (§4 "Narrative flow" and "Wireframe sequence"): the recommended order is (1) Header → (2) Hero → (3) Relevance/pain → (4) Mechanism/How it works → (5) Product evidence → (6) Use cases → (7) Differentiation → (8) Trust → (9) Beta status → (10) Trust/data → (11) FAQ → (12) Final CTA → (13) Footer. Also: if the hero frames the problem and the mechanism follows directly, a separate generic problem section can be redundant; the ideal narrative moves comprehension → confidence → commitment.

**Current state: the actual `index.html` section order** (`<section>`/comment blocks):

1. Hero (`:61–94`)
2. The Problem (`:96–122`)
3. Corridor interstitial, decorative quote (`:124–139`)
4. Who it's for (personas) (`:143–165`)
5. How Disce Works (`:167–220`)
6. Outcome dark band, verbatim repeat of the hero quote (`:222–230`)
7. Team teaser (`:232–242`)
8. CTA band ("Follow the build / join the beta") (`:244–265`)
9. Partner ticker ("Strategische Partner & Ökosystem") (`:267–283`)
10. Footer (`:285–317`)

**Gap / blind spot (mapped to the benchmark order):**

- Steps 2–4 are **reordered**: the benchmark places mechanism (4) before use cases (6); here personas (4) precede mechanism (5). This is defensible, but it means the mechanism arrives after the visitor has already been asked to identify with a persona, and without a product depiction.
- **Step 5 "Product evidence" is absent.** There is no screenshot, prototype, walkthrough, or example-output artifact on the homepage. The closest assets are the kernel architecture SVG (`kernel.html:142–220`) and two decorative `alt=""` media cards (`index.html:201–218`). This is the benchmark's "No product demonstration" anti-pattern (§10).
- **Step 7 "Differentiation" is absent as a section.** The status-quo contrast ("Kursfortschritt ≠ Fortschritt im Leben", `:117`) is inside the problem cards, and `philosophy.html:247` has a full anti-app argument, but the homepage has no dedicated "why this instead of the status quo" block.
- **Step 8 "Trust" is partially outsourced** to `team.html` (teaser only, `:232–242`) and closed with an unexplained partner ticker (`:267–283`).
- **Step 9 "Beta status"** is present but late and weak: the CTA band at `:244–265` says "Die Entwicklung verfolgen oder Teil der Beta werden" and "trägt Sie in die Warteliste ein, um zur ersten Kohorte zu gehören" (`:257`) without selection, timing, or limits (benchmark §6 Beta status module).
- **Steps 10–11 (trust/data, FAQ)** are absent from the homepage entirely.
- **Step 12 final CTA** uses the *same* CTA type as the nav (waitlist), which satisfies "no new CTA type with different logic", but the waitlist destination contradicts the page's own status content (Sprint 1 §1.8).

Net: the page follows the benchmark's *sequence skeleton* for the middle (problem → mechanism → CTA) but **omits the confidence-building half** (evidence, differentiation, trust, status, FAQ) that the benchmark places between comprehension and commitment.

---

## 2.5 Hero structure

**Benchmark expectation** (§4 "Hero requirements"; §7 "Wireframe sequence" row 2): the hero should present a headline, subheadline, CTA, **status label**, and **product visual**; second CTA only for a genuinely different intent level.

**Current state** (`index.html:62–94`)

- Full-bleed decorative background (`:63–69`), a generative `dot-field` overlay (`:70`), a two-column grid: left = eyebrow/h1/lede/two CTAs/glass quote card; right = a six-row stat panel.
- The right-hand stat panel is an unusual substitute for a product visual: it communicates Fokus / Ansatz / Bereiche / Phase / Pilotphase / Team (`:86–91`).

**Gap / blind spot:** The stat panel is information-dense and honest, but it is a **fact sheet about the venture**, not a product depiction or a status label in the benchmark's sense. The benchmark's hero visual slot ("product interface, workflow, or credible prototype depiction", §4) is filled by an abstract artwork whose `alt=""` marks it purely decorative. There is no status label of the form the benchmark recommends ("Private Beta", "Applications Open", "MVP in development"); "Vor der Gründung" describes the legal entity. The hero therefore **fails the "evidence" requirement and partially fails the "status" requirement**, while satisfying "headline", "subheadline", "CTA" structurally.

---

## 2.6 Visual hero choice

**Benchmark expectation** (§4 "Visual hero choice" table): real screenshot when UI is stable; annotated mockup when workflow is viable; short interface video when motion explains the benefit; illustration/abstract only under specific conditions, and **never abstract as the only product depiction**; interactive demo only if robust.

**Current state on the website**

- The homepage hero uses an abstract/illustrative composition (`DISCE_C01_r1_arena-stag-bordeaux`, `index.html:63–69`) with an additional generative dot field (`:70`).
- `kernel.html` uses an abstract panorama hero (`DISCE_K02_r1_archway-golden-plain`, `kernel.html:65–72`) plus a **static, token-styled inline SVG architecture diagram** (`kernel.html:142–220`) with a bilingual `<figcaption>` textual equivalent (`:217–219`). This diagram is the closest thing on the site to a benchmark "product/mechanism artifact".
- `philosophy.html` uses an abstract hero (`PHIL_hero_stag-moon-skyline`, `:76–85`); `status.html`, `team.html`, `impressum.html`, `datenschutz.html` use generative dot fields instead of imagery.
- No screenshot, no mockup, no interface video, no interactive demo anywhere.

**Gap / blind spot:** The site is entirely in the "abstract visual / illustration" row of the benchmark table. The benchmark's condition for abstract visuals — "Use when … Strong brand and clear copy already exist" and "Don't use when … It remains the only product depiction" — is **not met**: it *is* the only product depiction. The Kernel architecture SVG partially compensates (it depicts a real system), but it lives on a different page and is `aria-hidden` (`kernel.html:144`), so it does not function as the site's product evidence. The choice is consistent with the binding art direction (`DESIGN-BRIEF.md:35–48`) but diverges from the benchmark's evidence requirement; that tension is a genuine design-vs-benchmark conflict, not an oversight.

---

## 2.7 Repetition logic

**Benchmark expectation** (§4 "Narrative flow"): repetition should restate a claim **at different levels of detail** (promise → mechanism → use case → conversion rationale), not restate the same claim in different adjectives.

**Current state on the website**

- The identical blockquote appears **three times verbatim** on the homepage: inside the hero glass card (`index.html:81`), in the corridor interstitial (`:135`), and in the dark outcome band (`:226`). It is attributed in all three places to "Was wir mit Disce verändern wollen" / "What we are building Disce to change" (`:82`, `:136`, `:227`).
- The "How Disce Works" three-step list (`:175–197`) is echoed later by the Kernel's six-step cycle (`kernel.html:313–356`) and by the status roadmap's four epochs (`status.html:226–255`) — these are genuinely different levels of detail, which matches the benchmark.

**Gap / blind spot:** The three verbatim quotes are the clearest miss of the benchmark's repetition logic: the same sentence at the same level of detail occupies three of the homepage's ten sections, giving the page a "restated once, three times" rhythm rather than the benchmark's progressive deepening. This consumes vertical attention that the missing product-evidence and differentiation sections would otherwise fill.

---

## 2.8 Progressive disclosure

**Benchmark expectation** (§3 "Lean model": progressive disclosure keeps the homepage light; §3 "What must appear early"). The homepage should handle first understanding; deeper pages answer remaining questions. The benchmark cites NN/g progressive disclosure.

**Current state on the website**

- Progressive disclosure exists: homepage summary → `kernel.html` deep mechanism → `status.html` detail; `index.html` problem cards link conceptually to the deeper pages via nav.
- However, there is **no disclosure of the conversion details**: `waitlist.html` is a full-page destination (not a lightweight disclosure) and it answers study questions, not the "what is Disce's beta" question.

**Gap / blind spot:** Disclosure is strong on the *mechanism* axis and absent on the *trust/decision* axis. A visitor who understands the mechanism cannot progressively deepen their understanding of data handling, security, selection, or AI limitations from the homepage — those topics have no home. The benchmark's progressive-disclosure rationale ("defer secondary information so systems are easier to learn") is met for mechanism but not for risk, which is the opposite of what a "data-sensitive AI product" row implies (§2 Business-model dependency).

---

## 2.9 Homepage self-sufficiency ("what must appear early")

**Benchmark expectation** (§3 "What must appear early in the journey"): the first screen and immediate follow-on content should make **category, audience, benefit, mechanism, and current availability** legible. The homepage should be understandable without unnecessary page depth (Master Checklist IA P0).

**Current state:** The homepage is long (322 lines, ~10 sections) and self-contained for problem/personas/how-it-works. It is **not** self-sufficient for current availability: the only availability statement is "Vor der Gründung" (`:73`) and the stat "Pilotphase Abgeschlossen" (`:90`), while the actual access offer lives on a separate study page.

**Gap / blind spot:** Against the benchmark's litmus test (§4: a qualified visitor should be able to restate "this is for people like me, it solves this specific task, it works roughly this way, and this is why the beta ask is reasonable"), the homepage supports the first three clauses well and the fourth poorly: the "beta ask" is a study signup that is not explained on the page, and the page's own CTA band calls it "zur ersten Kohorte zu gehören" (`:257`) without saying what the cohort receives.

---

## 2.10 Footer

**Benchmark expectation** (§4 wireframe row 13 "Footer": contact, legal, status, central links; §10 "Hiding legal information"): structured footer, legal permanent and findable.

**Current state** (`index.html:285–317`; identical on most pages)

- Four columns: brand/tagline; "Seiten" (Home, Philosophy, Kernel, Team, Status); "Rechtliches" (Impressum, Datenschutzerklärung); "Kontakt" (Warteliste, Substack, mailto `bjarne.dudzus@disce.de`).
- Bottom line: copyright + location.

**Gap / blind spot:** This is a **strong** match for the benchmark's structured-footer recommendation: legal links are permanent and directly accessible on every page, contact is real (a named mailbox), and the status page is linked. The footer does **not** surface the missing trust surfaces (no FAQ, no AI-transparency, no security link), and it links "Impressum"/"Datenschutzerklärung" to pages that are still marked as drafts (Sprint 4). On form, this item **meets** the benchmark.

---

## 2.11 Empty / unused / placeholder surfaces

**Benchmark expectation** (§3 "Don't inflate too early": no empty blog/careers/changelog; §10 "Empty states" QA row; §11 Master Checklist "Are there no empty blog, careers, or changelog sections?").

**Current state**

- `beta.html`: a real, committed page containing only a hero ("Prototyp in Arbeit." / "Diese Seite entsteht gerade. Weitere Details folgen in Kürze.", `beta.html:68–69`) and a footer; it is `noindex`, absent from the nav and the sitemap, and `AGENTS.md` forbids linking it without approval. It is effectively a parked placeholder.
- `index.html:275–280`: the partner ticker contains **seven empty `<div class="ticker-logo">` elements** in addition to the three that hold logos. `.ticker-logo:empty { display: none; }` (`css/experimental.css:1724`) hides them visually, so they are not broken, but they are committed empty slots.
- `team.html:106–111`: a placeholder team entry ("Joscha (Nachname & Funktion offen)" / "Platzhalter…").
- `js/generative/registry.js:3`: registers a `kernel-loop` module (`./kernel-loop/index.js`) for which **no directory exists** under `js/generative/`. It is not mounted by any page, so it does not error at runtime, but the registry references a non-existent lazy module.
- `impressum.html`/`datenschutz.html`: draft banners and bracketed placeholders (`impressum.html:70–103`, `datenschutz.html:71–103`).

**Gap / blind spot:** There is no empty *blog*, *careers* or *changelog* page — the benchmark's specific concern is avoided. The residual placeholder surfaces are (a) the unlinked `beta.html`, (b) empty ticker slots, (c) one placeholder team card, and (d) a dangling registry entry. All are contained, but collectively they indicate that parts of the IA exist in skeleton form without a defined role.

---

## 2.12 Routing, URLs and indexability

**Benchmark expectation** (not a named section; implied by IA and by "legal/trust findable"). The benchmark's comprehensive model uses path-style routes (`/product`, `/use-cases`, `/security`, `/privacy`, `/imprint`).

**Current state**

- All routes are flat `.html` files at repo root (e.g. `kernel.html`, `status.html`). The comprehensive model's route vocabulary (`/product`, `/security`, `/ai-transparency`, `/faq`, `/beta`) is not used.
- `sitemap.xml` lists `/`, `/philosophy.html`, `/team.html`, `/status.html`, `/waitlist.html` — omitting `kernel.html`, `beta.html`, the legal pages, and `impressum`/`datenschutz`.
- `robots.txt` is `Disallow: /`, and **every** page sets `noindex, nofollow`.
- `CNAME` = `stage.weltvorstellung.de`; `canonical` and OG URLs point to `weltvorstellung.de` (`index.html:15`, `:22`).

**Gap / blind spot:** The indexability configuration is internally consistent for a **staging/no-index posture** (robots disallow + noindex on all pages), and inconsistent with the production-style canonical/OG/sitemap metadata. This is likely an intentional staging state, but it means the "pre-launch website as a discovery/acquisition instrument" (`§1`) is currently not reachable by search, and the sitemap references pages that are simultaneously disallowed and noindex. If the intended next phase is acquisition, this is a launch-blocking configuration rather than a design gap; as an assessment item it should be recorded as an unresolved production-vs-staging decision, not as a bug. `beta.html` being noindex and unlinked is consistent with `AGENTS.md`.

---

## 2.13 Content model duplication and single-source problems

**Benchmark expectation** (implied by clarity/maintainability; §11 Master Checklist "Can a person correctly restate the product, target audience, and next step?").

**Current state**

- Header/footer blocks are duplicated verbatim across all eight pages (e.g. `index.html:38–59` vs `team.html:33–54`).
- Language switching is re-implemented twice: shared `js/site.js:66–91` and an inline copy in `waitlist.html:761–793`.
- Status facts are duplicated without a single source: homepage stats (`index.html:86–91`), `status.html` ledger (`:70–89`) and waitlist study dates (`waitlist.html:513–555`) each restate project state independently.

**Gap / blind spot:** There is no build system (by design, `AGENTS.md`), so duplication is expected; the assessment-relevant consequence is that the **availability/status fact is triplicated across three files** with no shared source, which is the mechanical cause of the contradiction flagged in Sprint 1 §1.8. This is an architectural fragility, not a visual one.

---

## 2.14 Sprint 2 summary of notable findings

**Strengths:** the footer meets the benchmark's structured/findable-legal bar; the Kernel architecture SVG and the Kernel page give the site genuine mechanism depth and a credible technical artifact; the status page's directional roadmap matches the benchmark's "direction, not binding dates" guidance; progressive disclosure is strong on the mechanism axis; there is no empty blog/careers/changelog page.

**Principal gaps:** (1) the site is neither the lean nor the comprehensive model — it has comprehensive-model depth (`Kernel`, `Philosophy`) while omitting comprehensive-model trust pages (`Security`, `AI transparency`, `FAQ`, `Contact`); (2) the narrative omits the benchmark's confidence half — product evidence, differentiation, trust, beta status detail, and FAQ; (3) `beta.html` is an unlinked placeholder and no page actually explains the beta/access being offered, while `waitlist.html` is a mislabeled study page; (4) the homepage repeats one quote verbatim three times instead of deepening; (5) status/availability facts are triplicated with no single source; (6) all pages are noindex with `robots: Disallow: /` while canonical/OG/sitemap are production-style — an unresolved staging-vs-production posture.

**Critical flags:** None added in this sprint (no empty blog/careers; no forced navigation dead-ends). The availability contradiction carried from Sprint 1 §1.8 remains ⚠️ **CRITICAL** and is materially worsened by the IA fact that the mislabeled waitlist link is the site's only conversion route (`index.html:51`, `:260`).
