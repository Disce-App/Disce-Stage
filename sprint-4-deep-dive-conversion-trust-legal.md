# Sprint 4 Deep Dive — Conversion, Trust & Legal-UX Specification

**Document type:** Implementable specification (document-only; no code changed by this document beyond the two founder-confirmed fixes reported separately).
**Status:** Target spec for a later implementation step. Not the master checklist.
**Date:** 2026-09-21
**Inputs:** baseline `sprint-4-conversion-trust-legal.md`; `founder-decisions-locked.md`; `sprint-0-triage-and-sprint-1-decision-pack.md`; `sprint-2-deep-dive-target-ia.md`; `sprint-3-deep-dive-a11y-performance-evidence.md`; tracked repository; benchmark `Pre-Launch-Website-Exhaustive-Report.md`.
**Locked decisions honored:** #1 (waitlist = genuine interest in the planned private beta; no queue, no fixed date, no guaranteed contact/response), #2 (truthful interest registration; consistent status labels), #3 (Bjarne Dudzus responsible; no invented provider data; incorporation planned), #4 (partner/ecosystem block confirmed, unchanged), #5 (primary audience = international professionals in Germany), #6 (no separate beta-apply mechanic; beta planned only), #7 (Substack external deep link; no homepage-primary CTA; no new consent mechanism).

No legal advice is given. Where data must come from the founder or legal review, it is marked as such and never invented.

---

## 1. CTA and routing semantics pass

### 1.1 Problem

Every primary and footer CTA currently uses the generic benchmark weak-pattern label "Auf die Warteliste" / "Join the Waitlist" (benchmark §6 "Weak patterns"; §7 "CTA principles"). The destination page now means interest registration for a **planned** private beta (locked #1/#2), so the label is inconsistent with the page's own semantics.

Affected instances: `index.html:51,260,307`; `beta.html:46,95`; `datenschutz.html:46,166`; `impressum.html:46,146`; `kernel.html:46,525`; `philosophy.html:61,480`; `status.html:46,276,302`; `team.html:46,194`.

### 1.2 Recommended uniform label set (single primary + one secondary variant)

- **Primary (all nav CTAs, footer CTAs, and page final CTAs):**
  DE **"Interesse anmelden"** · EN **"Register interest"**
- **Secondary variant (use only where additional context is needed, e.g. the homepage final band or the status CTA):**
  DE **"Interesse anmelden – Private Beta"** · EN **"Register interest – private beta"**

No other new CTA copy is proposed. `status.html:276` (status CTA) currently pairs a "notify me" lede (`status.html:275`); the primary label applies there, with the secondary variant acceptable if the planned-beta context is already visible in the heading.

### 1.3 `index.html:256–257` fix (remove the access implication)

- **Current (repo):** `h2` "Die Entwicklung verfolgen oder Teil der Beta werden." / "Follow the build, or join the beta."; lede "…tragen Sie sich in die Warteliste ein, um zur ersten Kohorte zu gehören." / "…join the waitlist to be part of the earliest cohort."
- **Problem:** "join the beta" + "first cohort" implies access and a cohort slot (post-launch/availability language), contradicting locked #1/#6.
- **Target wording (for implementation):**
  - `h2` DE: **"Die Entwicklung verfolgen oder Interesse anmelden."** · EN: **"Follow the build, or register interest."**
  - lede DE: **"Disce steht vor der Eintragung mitten in der Validierung. Verfolgen Sie den Entwicklungsstand oder melden Sie unverbindlich Ihr Interesse an der geplanten Private Beta an."** · EN: **"Disce is in active validation ahead of incorporation. Track the development status, or register your interest in the planned private beta."**
- **Acceptance:** no "cohort", no "join the beta", no access promise; CTA label from §1.2; status phrase "planned private beta".

### 1.4 Routing (locked #5/#6/#7)

- One homepage-primary route: professionals → `waitlist.html` (interest registration). Secondary intents (research interest, partners, investors/technical collaborators) remain direct email; Substack is a clearly labeled external deep link, not a CTA (locked #7). Full model: `sprint-2-deep-dive-target-ia.md` §2.

---

## 2. Conversion-flow specification — `waitlist.html` as interest registration

### 2.1 Value exchange / commitment / expectation (locked #1)

Content requirements (structure; existing truthful wording may be reused — no new promises):

| Element | Requirement | Anchored in |
|---|---|---|
| **Action** | Registering interest only; not an application, not a purchase | locked #1; `waitlist.html:479`, `:498` |
| **Value exchange** | You signal interest; DISCE stores it and contacts you if/when the private beta or next study actually opens; optionally development updates via Substack | locked #1/#7; `waitlist.html:513–514` |
| **Commitment** | Non-binding; takes a few minutes; no obligation | `waitlist.html:525` (current "Was bedeutet das für dich?") |
| **Expectation** | No queue position; no fixed date; no guaranteed response | locked #1; `waitlist.html:520` |
| **Must not imply** | available product, open beta, guaranteed access, priority, timing | locked #6; benchmark §6 weak patterns |

### 2.2 Thank-you / success-state spec (`waitlist.html:704–708`, JS `:882–883`)

| Requirement | Target |
|---|---|
| Visible on-page confirmation | Keep the existing success banner; ensure it is an `aria-live`/`role="status"` region and receives focus (see Sprint 3 deep dive §1.2) |
| Realistic follow-up language | Must state contact happens only when the beta/next study actually opens; no month, no response-time promise |
| Privacy deep link | Add a link to `datenschutz.html` inside the privacy block (currently absent) |
| Correction / withdrawal | State that the entry can be corrected or withdrawn by email (`waitlist.html:731`/`:738` already say withdrawal by email; add "or change"); keep it factual, no self-service form required |
| No second mandatory form | Confirm no additional form is required post-submit (benchmark §7 "Thank-you flow") |
| Withdrawal contact | `bjarne.dudzus@disce.de` (authoritative; see §6) |

### 2.3 Follow-up runbook

| Aspect | Specification |
|---|---|
| **Who responds** | The mailbox owner (Bjarne Dudzus via `bjarne.dudzus@disce.de`) |
| **Trigger** | Only when the private beta or the next research phase actually opens (locked #1/#2), or when development updates are published on Substack |
| **Medium** | Direct email for the beta/study; Substack for updates (locked #7) |
| **No-trigger case** | If access is not possible or is significantly delayed, a message is sent (benchmark §7 follow-up step 5); no fixed timing is promised |
| **Dependency** | **Blocked on mailbox verification** — the address must be confirmed as existing and monitored before the page is publicly promoted (founder to-do) |
| **No new consent scope** | The existing contact consent (`waitlist.html:665–668`) covers this; do not add consent scopes (locked #7) |

---

## 3. Form-data specification (field-by-field, data minimization)

Current fields: `first_name` (`waitlist.html:560`), `email` (`:576`), `german_level` (`:592`), availability (`:610`), `has_microphone` (`:658`), `consent_contact` (`:665`), `source_channel` (`:690`). No role/career field exists.

| Field | Purpose today | Minimization assessment | Disposition | Rationale |
|---|---|---|---|---|
| First name | Personal address | Minimal | **Keep** | Lowest-friction identifier |
| Email | Contact channel | Necessary | **Keep** | Required for the stated purpose; benchmark §7 Model A/B |
| Role / career data | Would support ICP segmentation | Not currently collected | **Defer** | Not needed for interest registration; benchmark §2 "Conversion vs. lead quality"; avoids scope creep |
| German level (self-assessment) | Screening / ICP | Useful but not required to contact | **Simplify → optional; defer full assessment** | For interest registration the level can be asked later; benchmark EAS "remove non-essential fields" |
| Availability (general flexibility) | Was study scheduling | No longer needed (no date) | **Drop/defer** | Direct consequence of locked #1 (no scheduling); currently the only purpose was June scheduling |
| Microphone + quiet space | Study logistics | No longer needed | **Drop/defer** | Tied to a study session that is not scheduled; benchmark data minimization |
| Consent to contact | Legal basis for contact | Required | **Keep** | Art. 6(1)(a) contact consent; locked #1; do not alter basis |
| Referral source (optional) | Acquisition insight | Low sensitivity, optional | **Keep optional** | Supports low-traffic measurement (benchmark §7) |

**Notes:** Dropping the availability and microphone fields removes the last consumer of the stale study-scheduling frame and reduces friction; it also requires adjusting the JS validation block (`waitlist.html:823–836`) accordingly — a functional change to be scoped in implementation, not done here. No field may be added that implies a study application (locked #6).

---

## 4. Consent and tracking posture (report only)

- **Current state:** zero third-party trackers; only a `localStorage` language preference (`js/site.js:88`; `waitlist.html:787`), justified as strictly necessary (`datenschutz.html:109`). No analytics and no consent manager (Sprint 4 §4.9.3).
- **Does the consent text suffice for interest registration?** The scoped contact consent (`waitlist.html:665–668`) plus the stated purpose (`waitlist.html:730`/`:737`; `datenschutz.html:100`) is appropriate for a single-purpose Art. 6(1)(a) contact consent. **No consent manager is introduced.** The purpose description has been aligned to interest registration; legal review of the final wording remains (§6).
- **Substack (locked #7):** the link must **not** read as an on-site email subscription (e.g. "subscribe/newsletter") and must not place any cookie or tracker before the click. The current label "Substack" (external `https://disce.substack.com`, `index.html:308`) is acceptable; Substack's own consent applies after navigation. No new consent mechanism, no embedded widget.
- **Report only:** if any analytics is later introduced, it must be cookieless/consent-free by configuration or gated; the benchmark prefers privacy-friendly analytics for low-traffic sites (benchmark §8 "Privacy-friendly analytics").

---

## 5. Trust surface near conversion (structure & content requirements)

Add a compact trust/status block adjacent to the interest form (above or directly below it). Structure and required content (not final copy):

| Slot | Required content | Must not imply |
|---|---|---|
| Status | Project in development; private beta planned; next research phase in preparation (recruitment not open) | open beta / available product |
| Data use | One-line summary: what is collected and why (interest registration + contact), pointing to `datenschutz.html` | "secure by design" / unsupported security claims |
| Privacy link | Explicit link to `datenschutz.html` (currently missing from the conversion page) | — |
| Contact | `bjarne.dudzus@disce.de` for questions/correction/withdrawal | a response-time promise |
| Evidence | Completed Cervus proof-of-principle as context (text only) | active study / product capability |

Reference: benchmark §8 "Legitimate pre-launch proof", "Trust modules"; §4 wireframe step 10; Sprint 4 §4.8.

---

## 6. Legal-UX release gate

Consolidated founder-input list. "Status" reflects the repo as of this run; nothing is invented.

| # | Item | Needed input | Repo location | Status | Blocks indexable launch |
|---|---|---|---|---|---|
| 1 | Imprint — responsible person | Bjarne Dudzus | `impressum.html:78` | **Resolved** | — |
| 2 | Imprint — ladungsfähige Anschrift | Street, house number | `impressum.html:79` | Open (`Gründer-Input`) | Yes |
| 3 | Imprint — PLZ, Ort | Postal code, city | `impressum.html:80` | Open | Yes |
| 4 | Imprint — telephone | Phone number | `impressum.html:86` | Open | Yes |
| 5 | Imprint — MStV address | Address line | `impressum.html:102` | Open | Yes |
| 6 | Imprint — notice date | Date | `impressum.html:118` | Open | Yes |
| 7 | Privacy — controller address | Address | `datenschutz.html:80–81` | Open | Yes |
| 8 | Privacy — third-country transfer basis (hosting) | Legal basis | `datenschutz.html:90` | Open (founder/legal) | Yes |
| 9 | Privacy — transfer basis + DPA status (Cloudflare/Airtable) | Legal basis, Art. 28 | `datenschutz.html:102` | Open | Yes |
| 10 | Privacy — retention period | Period | `datenschutz.html:103` | Open | Yes |
| 11 | Privacy — notice date | Date | `datenschutz.html:125` | Open | Yes |
| 12 | Privacy §4 / waitlist purpose | Aligned to interest registration | `datenschutz.html:97–103`; `waitlist.html:730/737` | **Aligned** (this run) | review still needed |
| 13 | Controller contact consistency | `bjarne.dudzus@disce.de` | `waitlist.html:733/740`; `impressum.html:87`; `datenschutz.html:82` | **Aligned** (this run) | — |
| 14 | Legal review — imprint + privacy | Lawyer review | — | Open | Yes |
| 15 | BFSG applicability review | Assessment | — | Open (Sprint 4 §4.9.5) | Review |

**Gate rule:** items 2–11 and 14 must close before switching from the current non-indexable staging posture (`robots.txt` `Disallow: /`; per-page `noindex`) to an indexable public launch (see `sprint-2-deep-dive-target-ia.md` §4).

---

## 7. FAQ and dead-code disposition

- **Recommendation:** add a small FAQ as a module **on `waitlist.html`** (the conversion page), because the benchmark places FAQ as a P0 module and the questions are conversion-relevant (benchmark §3 "FAQ — P0 as a module"; §6 "Pre-launch FAQ"). Optionally surface 2–3 items on `index.html` near the final CTA; do **not** create a standalone page (no new pages).
- **Content it must answer** (adapted to interest registration, not study recruitment): what currently exists (completed Cervus research; no public product); what registering interest means (and does not: no queue, no date, no guaranteed access); who is eligible; when contact happens; what data is processed and how to withdraw; status of the private beta and next research phase.
- **Dead accordion code:** the existing accordion (`js/site.js:42–64`; `css/experimental.css:1673–1682`) is currently mounted nowhere (Sprint 3 deep dive §1.8). **Recommendation: repurpose it for this FAQ module** rather than writing new interaction code (adapted for `aria-expanded`/keyboard if not already adequate). Effort: **low** (mount + content) if repurposed; **low** to remove instead, but removal would forfeit a ready component.
- **Effort estimate:** FAQ content + mounting = low; if the accordion needs accessibility hardening, low–med.

---

## 8. Claim register (final public wording constraints)

| Claim type | Allowed now | Evidence pointer | Must avoid |
|---|---|---|---|
| **Research** | Cervus research / proof-of-principle completed; research report completed; methodologically rigorous development | locked #8; `status.html:78`; `team.html:74` (now past tense, "Cervus"); `sprint-0` A.1 | active/ongoing study; recruiting; results/effectiveness figures not in repo |
| **Beta** | Private beta planned; details not final | locked #6; `waitlist.html:498`; `status.html:82` | open beta; fixed date; access promise |
| **Waitlist / interest** | Register interest in the planned private beta; no queue, no fixed date, no guaranteed response | locked #1; `waitlist.html:479/498/520` | queue position; guaranteed contact; "join the beta" |
| **Partners / ecosystem** | Existing partner/ecosystem block as-is (confirmed accurate) | locked #4; `index.html:269–274` | changing names/framing; implying unconfirmed relationships |
| **Team roles** | Named founders/roles/advisors; completed pilot led by named founder | `team.html:61–143`; `team.html:74` | legal-form claims (removed at `team.html:61`); active-study tense |
| **Data statements** | What is collected, why, legal basis, retention placeholder, no tracking | `waitlist.html:730/737`; `datenschutz.html:97–111` | invented transfer basis/retention; "GDPR compliant" blanket seal (benchmark §8) |
| **AI / product capability** | Bounded system description; explicit non-claims | `kernel.html:445–474`; `philosophy.html:264–269` | autonomy, accuracy, or availability claims not established |
| **Status labels (uniform)** | "Cervus research completed"; "private beta planned"; "next research phase in preparation — recruitment not open" | locked #2; `status.html:78/82` | any present-tense recruitment or availability |

---

**Grounding summary.** Repo anchors: `index.html:51/256–257/260/269–274/307/308`; `waitlist.html:479/498/513–525/551/560/576/592/610/658/665/690/704–708/730–741/789–890`; `datenschutz.html:80–81/82/90/97–103/102/109/125`; `impressum.html:78–80/86–87/102/118`; `team.html:61/74/92`; `status.html:78/82/275–276`; `kernel.html:445–474`; `philosophy.html:264–269`; `js/site.js:42–64/88`; `css/experimental.css:1673–1682`; `robots.txt`. Benchmark sections: §3 (Information Architecture, FAQ), §6 (Content/Messaging/Beta communication, FAQ), §7 (Conversion and Waitlist Strategy, Thank-you flow, Measurement), §8 (Trust/Transparency/Legal UX), §10 (Anti-Patterns), §11 (Master Checklist).
