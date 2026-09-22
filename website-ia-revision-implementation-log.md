# Website Information Architecture — WP C Implementation Log

**Document type:** Implementation record for work package **WP C — Information Architecture & Page Structure**.
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Basis:** `master-checklist-website-revision.md` §2.2 (IA-01…IA-06), `website-revision-work-packages.md` WP C, `website-content-strategy-and-revision-plan.md` §5, and the resolved implementation decisions.

> This log records WP C. It does not replace the changes themselves. The authoritative master checklist and work-package documents were not modified; their IA-06 status can be flipped to DONE by the owner on the evidence below.

---

## 1. Scope of this round

WP C's five earlier tasks are already recorded `DONE` (IA-01 page dispositions, IA-02 `beta.html` role, IA-03 waitlist FAQ, IA-04 one funnel per intent, IA-05 Substack deep link). The only open code task was **IA-06 — update `sitemap.xml` to the real public set**. This round implemented IA-06 and re-verified the IA invariants after the messaging revision.

No new pages, routes, or navigation entries were created (per the resolved implementation scope: no audience, institutional, research-results, or privacy-marketing pages).

---

## 2. Files changed

| File | Change |
|---|---|
| `sitemap.xml` | Expanded from 5 to 8 URLs; added `kernel.html`, `impressum.html`, `datenschutz.html`; `beta.html` remains excluded |
| `index.html` | Brand claim corrected to the binding lowercase form "Sag, was du meinst." (title, `data-title-de`, OG title, Twitter title, H1) |
| `philosophy.html` | Brand claim corrected to lowercase "du" (H1 and four prose references, DE and EN) |
| `website-content-revision-implementation-log.md` | Claim reference updated to lowercase "du" for record accuracy |

No CSS, JS, image, or configuration files were changed. `robots.txt`, canonical URLs, OG fields, and the `noindex` staging posture were left unchanged.

---

## 3. IA-06 result

`sitemap.xml` now lists the real public page set, each matching the page's own `rel="canonical"`:

1. `https://weltvorstellung.de/`
2. `https://weltvorstellung.de/philosophy.html`
3. `https://weltvorstellung.de/kernel.html`
4. `https://weltvorstellung.de/team.html`
5. `https://weltvorstellung.de/status.html`
6. `https://weltvorstellung.de/waitlist.html`
7. `https://weltvorstellung.de/impressum.html`
8. `https://weltvorstellung.de/datenschutz.html`

`beta.html` is deliberately absent (locked decision #2: deferred, unlinked, `noindex`, outside the sitemap).

**Acceptance check:** sitemap matches the indexable public set — pass.

---

## 4. Verification performed

- **XML validity:** `sitemap.xml` parses as well-formed XML; 8 `<url>` entries.
- **Completeness:** every sitemap URL resolves to an existing file; every non-deferred public page is listed; no sitemap entry lacks a file.
- **Exclusion:** `beta.html` is not in the sitemap.
- **Canonical alignment:** all 8 pages' `rel="canonical"` values exactly match their sitemap `<loc>`.
- **Navigation/footer consistency:** the eight public pages that use the shared chrome (`index`, `philosophy`, `kernel`, `team`, `status`, `impressum`, `datenschutz`, `beta`) expose the same header and footer link set, including "Philosophie / Philosophy" (IA-01 founder correction).
- **Orphan check:** no public page is unreachable; `beta.html` is intentionally unlinked.
- **One funnel per intent (IA-04):** every `nav-cta` across pages points to `waitlist.html`; the homepage's primary CTAs point to `waitlist.html`; no competing homepage-primary CTA was introduced. Deep pages (`kernel`) keep their own secondary deep-page CTAs (status/contact).
- **Page dispositions:** `kernel.html` remains the mechanism page, `status.html` the canonical status page, `philosophy.html` a public secondary page — unchanged.

---

## 5. Intentionally not changed

- **Indexability (GATE-14):** `robots.txt` still disallows all and every page still carries `noindex, nofollow`. The sitemap is forward-looking for the launch state; flipping indexability remains gated on GATE-01…12.
- **Primary domain:** the sitemap continues to use `weltvorstellung.de`. The `weltvorstellung.de` vs `disce.de` question (Round-2 notes §5) is unresolved and was not silently decided.
- **`waitlist.html` chrome:** it remains on its own stylesheet and minimal footer/language switcher (DEF-03 / WP F), so its header/footer link set differs from the shared chrome. This is a known, deferred item, not a regression.
- **Legal page content:** `impressum.html` and `datenschutz.html` were not edited; their placeholders remain subject to WP A gates.

---

## 6. Remaining blockers / open questions

1. **GATE-14 (indexability)** — must close before the sitemap can take effect; currently all pages are `noindex` and `robots.txt` disallows all.
2. **Primary domain decision** — `weltvorstellung.de` vs `disce.de`; affects canonical, OG, and sitemap URLs simultaneously.
3. **`waitlist.html` design-system migration (DEF-03 / NEW-02)** — would unify chrome and enable the deferred font/`@font-face` dedup.
4. **Legal gates (GATE-01…12)** — imprint/privacy placeholders and legal review remain open.

---

## 7. Recommended next step

Proceed to **WP F (Conversion & Waitlist)** — the waitlist redesign naturally resolves the remaining IA/chrome inconsistency (DEF-03) and can reconcile the on-page privacy summary with the legal page. **WP I (Team Page)** is the other ready candidate. WP A gates continue in parallel and remain the precondition for GATE-14.
