# Website Content Revision — Implementation Log

**Document type:** Implementation record for the first website-wide messaging and public-content revision.
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Strategic basis:** `Disce — Making Expertise Visible.md`, `website-content-strategy-and-revision-plan.md`, and the resolved decisions in the implementation brief.
**Source hierarchy applied:** repository legal/technical/factual reality → locked decisions and `DESIGN-BRIEF.md` → the Strategy → existing planning documents → no invented facts.

> This log documents what was changed. It does not replace the changes themselves. No existing planning document (`master-checklist-website-revision.md`, `website-revision-work-packages.md`, `website-content-strategy-and-revision-plan.md`) was modified.

---

## 1. Files changed

| File | Nature of change |
|---|---|
| `index.html` | Homepage category/audience/approach/outcome messaging; metadata; hero panel; footer tag |
| `kernel.html` | Claim/tense qualification; removal of EU-hosting and moat/competitor language; metadata; footer tag; internal-comment cleanup |
| `philosophy.html` | Chapter rewrites (why German, measurement, active practice, AI/governance); removal of unsupported science, privacy-hosting, monetization, platform/institution, competitor framing; footer tag; comment cleanup |
| `status.html` | Roadmap and Cervus wording; founding-date framing; removal of internal planning comments and hidden beta block; footer tag |
| `team.html` | Removed N=150/RCT; footer tag |
| `waitlist.html` | Level range B2–C1 → B2–C2 |
| `impressum.html` | Footer tag only (no legal copy changed) |
| `datenschutz.html` | Footer tag only (no legal copy changed) |
| `beta.html` | Footer tag only |

Shared footer tag replaced on all nine pages. No CSS, JS, image, route, or configuration files were changed. No new files except this log.

---

## 2. Major messaging changes

### Category language
- Replaced the site-wide footer description **"KI-gestütztes Deutschlernen für fortgeschrittene Lernende" / "AI-powered German learning for advanced learners"** with **"Professionelles Deutsch für internationale Fachkräfte" / "Professional German for international professionals"** on all pages.
- Homepage meta description, OG description, and Twitter description now read: *"Disce macht Expertise sichtbar: professionelles Deutsch auf B2–C2 für internationale Fachkräfte, die im Beruf auf Deutsch überzeugen müssen."*
- Homepage hero lede now frames Disce as an **"KI-gestütztes Lernsystem für professionelles Deutsch auf B2–C2"** and names the professional situations where expertise must become visible.
- The fixed public claim **"Sag, was du meinst."** is retained everywhere it existed; "expertise visible" is used only as supporting category/positioning language (meta descriptions, hero, vision band).

### Audience
- Homepage "who it's for" lede reframed from a two-group start ("doctors + professionals") to **international professionals broadly**, with concrete examples (doctors preparing for the *Fachsprachprüfung*; professionals in engineering, consulting, finance, administration, research). Example cards are explicitly labelled as examples ("Beispiel:").
- Removed the unsourced clinical assertion ("clinical knowledge is rarely the obstacle").
- Philosophy audience list (youth, teachers, diaspora, employers, EdTech partners) was removed and replaced with the focused professional audience.

### Level range
- Harmonised to **B2–C2** where a target range is stated: homepage meta, hero, panel stat, problem headline, waitlist info block. (Other `B2` mentions are legitimate: the philosophy measurement critique of a single "B2" label, a form-select option, and a team member's language proficiency.)

### Positioning and approach
- Homepage "How it works" eyebrow changed from "So arbeitet Disce" to "Der Ansatz"; the learning-psychology claim was replaced with concrete feedback on tone, register, and communicative effect.
- Homepage stat "Wirkungsorientiert, KI-personalisiert" → "Situationsbezogen, rückmeldungsorientiert"; domains "Klinisch · Beruflich" → "Berufliche Kommunikation".
- Homepage third repeated pull-quote replaced with a distinct outcome statement: *"Sprachkompetenz ist ein Niveau. Berufliche Wirkung ist das, was im entscheidenden Moment ankommt. Disce arbeitet an der Lücke dazwischen."*
- Philosophy chapter 06 retitled from "Kultur, Gemeinschaft und Ko-Kreation" to **"Aktive Praxis statt passiver Konsum" / "Active Practice over Passive Consumption"** and rewritten around active, situational practice and professional relevance.

### Product/status truthfulness
- Kernel present-tense architecture claims qualified as **intended design**: hero lede, definition, provider-neutral card, runtime plate ("geplante Laufzeitarchitektur"), figcaption, compounds section, and boundaries lede.
- Kernel "compounds" section reframed from a commercial/moat argument ("The Data Advantage", "what a wrapper around a model cannot copy") to **"Wie der Kernel arbeitet" / "How the Kernel works"**.
- Status page long-range vision reframed as a **directional, non-binding perspective**; "interne Roadmap" wording removed; founding date now reads **"Geplantes Ziel · Q4 2026 (unverbindlich)" / "Planning target · Q4 2026 (non-binding)"**.

### Internal-strategy leakage removed
- `status.html`: removed/neutralised internal comments referencing "Batch 3", "structural overhaul", `DESIGN-BRIEF §8`, "Round 2 §4", and an entire hidden, commented-out "Beta" project entry containing "pilot partners" copy and internal authoring instructions.
- `philosophy.html`: removed "intern als Doktrin", the "Animal-Crossing-Paradigma" internal term, the internal data taxonomy, monetization/creator-economy discussion, and design-brief comment references.
- `kernel.html`: removed "owner decision", `DESIGN-BRIEF` references, and the commercial/moat comment; investor-facing CTA softened from "Partnerschaft, Investment" to "ein Gespräch über die Architektur oder eine mögliche Zusammenarbeit".

---

## 3. Claims removed or qualified

| Claim | Action |
|---|---|
| **EU-hosting / EU-region / EU-EEA architecture** (kernel `Anbieterneutral und EU-gehostet`; philosophy technology chapter) | **Removed.** No privacy-forward hosting claim remains on any public page. |
| **GDPR-native / privacy-by-design architecture as marketing** (philosophy) | **Removed** as a public commitment; replaced with restrained data-minimisation and purpose-limitation language. Legal facts remain only in `datenschutz.html` (unchanged). |
| **No third-party commercial model training** (implied by the technology chapter) | **Removed**; no such public promise was added. |
| **"Many language-AI products are a surface around a model" / competitor comparison** (kernel) | **Removed.** |
| **"The Data Advantage" / moat framing** (kernel) | **Reframed** to a neutral explanation of how the Kernel is designed. |
| **Unsupported learning-science claim** — "auf gesicherter Lernpsychologie" (homepage) | **Removed**; replaced with concrete feedback description. |
| **Unsupported statistics** — "most learners who reach B2 stall there" (homepage); uncited psycholinguistic findings ("Studien zeigen…", philosophy) | **Removed/softened** to hedged, non-numeric statements. |
| **ALTE "~80% success probability" and CAF "reliably predicts CEFR level"** (philosophy) | **Removed**; the four reference frames are described without numeric or predictive claims. |
| **Present-tense dashboard / weekly-dialogue / adaptive-testing capability** (philosophy, kernel) | **Qualified** to intended design ("soll", "angelegt", "is intended"). |
| **Teuken-7B / 3-phase AI roadmap / proprietary compute / European-hosted compute** (philosophy) | **Removed** as internal strategy/tech-plan material. |
| **N=150 RCT and "Wirksamkeit KI-generierten Feedbacks"** (`team.html`) | **Removed**; replaced with a neutral "Vorstudie Cervus zu KI-gestütztem Feedback beim professionellen Deutschlernen" (topic only, no result/effectiveness claim). |
| **Cervus "Methodik und Ergebnisse" as validation starting point** (`status.html`) | **Qualified**; now states results are **not publicly reported**. |
| **Roadmap monetization / creator economy / premium modules / "international center for language research"** (`status.html`) | **Removed**; roadmap reframed to restrained product/learning phases. |
| **"Primärmarkt: DACH"** | Changed to "Fokus: deutschsprachiger Raum". |
| **Institutional/employer adoption, pilot, or workflow claims** | **None introduced** (none existed publicly). |

---

## 4. Occurrences intentionally retained, and why

- **"Sag, was du meinst."** — the binding fixed public claim (`DESIGN-BRIEF.md:22`); retained on homepage and philosophy.
- **"Proof of Principle (Cervus) — abgeschlossen" / "Cervus proof of principle is complete"** — locked founder status wording; truthful and consistent across homepage, status, and waitlist.
- **"Kernel v0 — in Entwicklung" and the V0 non-claims paragraph** (`kernel.html`) — explicit, truthful limitation; kept as a trust signal.
- **Existing partner ticker** (`index.html`) — locked decision #4: kept visually and structurally unchanged; no labels or logos added.
- **"B2" as a level concept** in the philosophy measurement critique and as a form-select option — not a target-range statement.
- **Waitlist consent, success, trust, and FAQ text** — already compliant and truthful; only the level range changed. Legal copy was not altered.
- **`datenschutz.html` processor/transfer/retention placeholders** — left untouched; they are legally required factual statements still pending founder/legal input.
- **`beta.html`** — deferred, unlinked, `noindex` per locked decision #2; only the shared footer tag changed.
- **Ordinary implementation code comments** (performance, image pipeline, accessibility) — retained; they are technical, not strategy/monetization leakage.

---

## 5. Unresolved issues (blocked by legal, technical, evidence, or founder decisions)

1. **Legal gates remain open** (`master-checklist-website-revision.md` GATE-01…12): imprint address/phone/date, privacy controller address, third-country transfer basis, Art. 28 DPA status, retention period, and legal review. `impressum.html` and `datenschutz.html` remain drafts. No privacy-forward marketing was added, so no new gate dependency was created.
2. **Mailbox verification (GATE-11)** — `bjarne.dudzus@disce.de` must still be confirmed and monitored before public promotion.
3. **Research-report publication** — whether any Cervus report/results may be published (and in what form) remains undecided; all research-report material stays internal per the resolved decisions.
4. **Indexability (GATE-14)** — the site remains `noindex` with `robots.txt` disallow; unchanged.
5. **`sitemap.xml` mismatch** — still lists only five pages and omits `kernel.html`, `impressum.html`, `datenschutz.html`; not changed in this round (routing/sitemap was out of scope).
6. **`waitlist.html` OG locale** — `og:locale="en_US"` on a DE-primary page; pre-existing metadata bug, not a messaging issue, left unchanged.
7. **`beta.html` heading skip (`h1→h4`)** — pre-existing, out of scope.
8. **Accessibility/manual verification** — the changes are content-only and preserve existing markup patterns, but rendered visual, keyboard, screen-reader, and contrast checks (previously MEASURE-ONLY) were not performed here.

---

## 6. Verification performed

- **Prohibited-term grep:** zero occurrences of `KI-gestütztes Deutschlernen` / `AI-powered German learning`, `B2–C1`/`B2-C1`, `N=150`, `RCT`/`randomisiert`, `EU-gehostet`/`EU-hosted`/`EU- und EWR`/`EU/EEA`/`EU-Region`.
- **Internal-leakage grep:** zero occurrences of `Batch N`, `DESIGN-BRIEF`, `Round 2 §`, `owner decision`, "interne Roadmap", "internal roadmap" in public HTML. (The word "intern" remains only in the ordinary phrase "interne Notiz".)
- **Competitor/moat grep:** zero occurrences of "Gegenmodell"/"counter-model", "Oberfläche um ein Modell"/"wrapper around a model", "Datenvorteil"/"Data Advantage", "Monetarisierung"/"monetization", "Creator-Ökonomie"/"creator economy" in public pages.
- **Level-range grep:** all target-range statements read B2–C2.
- **HTML structure:** all nine pages parsed with a tag-balance checker — **0 errors, 0 unclosed tags, 0 duplicate IDs, exactly one `<main>` per page**.
- **Heading order:** no heading-level skips on any edited page (the pre-existing `beta.html h1→h4` is unchanged and out of scope).
- **Anchors:** all in-page `#` links resolve to existing IDs (philosophy TOC intact after chapter retitling).
- **Language parity:** `data-lang="de"` / `data-lang="en"` counts balanced on all bilingual pages (index 82/82, kernel 133/133, philosophy 29/29, status 67/67, team 46/46).
- **Link check:** no broken internal `.html` links introduced.

---

## 7. Recommended next step

Proceed to **WP C (Information Architecture)** to reconcile `sitemap.xml` with the real public page set and to re-verify page roles now that the messaging is coherent — followed by the previously planned **WP F (waitlist redesign)** and **WP I (team page)**. Legal gates (WP A) continue in parallel and remain the precondition for any indexable launch. No further public claims should be added until GATE-07/08/12 (privacy/transfer/legal review) and the research-report publication decision are resolved.
