# Website Team Page — WP I Implementation Log

**Document type:** Implementation record for work package **WP I — Team Page** (NEW-05).
**Date:** 2026-09-22
**Status:** Implemented in the repository. Not committed.
**Basis:** `website-revision-work-packages.md` WP I (NEW-05), `website-content-strategy-and-revision-plan.md` §5.6/§7.3 and Q6/Q11, `docs/website-round2/2026-09-14_Website_Round2_Notes_EN.md` §2/§3/§4, `Pre-Launch-Website-Exhaustive-Report.md` §3/§5 (trust labels, team credibility), `DESIGN-BRIEF.md` §7/§8/§11, and the resolved implementation decisions in this round.

> This log records WP I. It does not replace the changes themselves. The authoritative master checklist and work-package documents were not modified; NEW-05's status can be flipped by the owner on the evidence below.

---

## 1. Scope of this round

The team page was the last subpage still on its pre-rework treatment (portrait-card grid with placeholder graphics, a decorative full-bleed band, and a duplicated CTO block with no working CTA). This round gave it the same design-system treatment as the other subpages and resolved the three founder-flagged items:

1. **Portraits are not yet available** → the image column was removed entirely and the founders became a photo-free, information-parity roster.
2. **Revamp the CTO / co-founder CTA** → the two duplicate open-role blocks were merged into one dark section with a real, working call to action.
3. **The bottom image** → the uncaptioned greenhouse band was removed; the page now closes with the site-wide register-interest band, so its closing image has a clear purpose.

Per the guardrail, no product copy was rewritten: every founder role, bio, advisor entry and the hero copy are carried over verbatim. Only the newly required structural/microcopy (section head, open-role CTA, closing band) is new and is listed in §3.

---

## 2. Files changed

| File | Change |
|---|---|
| `team.html` | `<main>` rebuilt: photo-free founder roster, advisors kept, single dark open-role section with framed CTA, closing register-interest band. Head, header and footer unchanged. |
| `css/experimental.css` | Added the `.team-roster` / `.team-member` / `.team-member-mark` / `.team-member-role` component (§4); removed a now-stale comment reference to the image-bearing `.band` on Team. |
| `css/experimental.min.css` | Appended the minified equivalent of the new roster component so the linked stylesheet matches the source. |

No JavaScript, image, or configuration files were changed. No assets were added or deleted.

---

## 3. What the revamp does

### 3.1 Founders — photo-free roster
- The `team-grid` of six cards (five placeholder portraits + the green "Der sechste Platz" card) is replaced by one ruled `.team-roster`: each founder is a row with a monogram (`BD`, `CL`, `SI`, `CG`, `J`), name, role and the existing bio.
- No image column and no placeholder graphics: information parity is achieved by having **no** portraits rather than five placeholders.
- The green CTO card was removed from the grid; the open seat now lives only in its own section (§3.3), which removes the duplication.
- Joscha's entry is kept and still explicitly marked as a placeholder (`process-period` "Nachname & Funktion offen" / "surname & title pending"), unchanged.

### 3.2 Advisors
- The advisor list is unchanged in content and markup (`.advisor-list` / `.advisor-row`), still labelled by relationship type ("Technische Beratung", "Accelerator-Mentoring", "Startup Program Mentor"), consistent with the Pre-Launch report's rule that advisor relationships be named precisely.

### 3.3 Open role — the revamped CTA
- The former dark "Offene Position" block and the green grid card are merged into **one** dark `bg-forest` counterpoint section.
- It adds a `badge-row` of the three responsibility areas already named in the copy: Architecture, Engineering, Data Protection.
- The CTA is now real: a framed two-button panel (`.cta-frame` + `.cta-frame-inner`, the homepage/kernel pattern that keeps buttons at ink-on-paper contrast on dark) with
  - **primary** → `mailto:bjarne.dudzus@disce.de` ("Kontakt aufnehmen" / "Get in Touch"),
  - **secondary** → `status.html` ("Entwicklungsstand ansehen" / "See Development Status").
- The previous dead sentence "Kontakt über den Link unten." was dropped, since a working link now follows.

### 3.4 Closing band
- The uncaptioned greenhouse `.band` was removed from mid-page.
- The page now closes with the **site-wide register-interest band** (`.cta-band` + causeway-palms), the same template as Development Status and the homepage. This satisfies the Round-2 §4 request to roll the mailing-list band out to Team and gives the page's closing image a clear function.

### 3.5 New microcopy (requires founder approval)
- Founders section head: eyebrow "Gründungsteam" / "Founding Team"; h2 "Fünf Gründende, fünf Verantwortlichkeiten." / "Five founders, five responsibilities."
- Open-role CTA buttons: "Kontakt aufnehmen" / "Get in Touch" (reused from `kernel.html`) and "Entwicklungsstand ansehen" / "See Development Status".
- Closing band: eyebrow "Auf dem Laufenden bleiben" / "Stay Informed"; h2 "Melden Sie unverbindlich Ihr Interesse an." / "Register your interest."; a lede built from existing status/hero facts ("Disce bereitet die Gründung vor und entwickelt den nächsten Prototyp …").

---

## 4. CSS component

New, page-scoped component added after the advisor rules:

- `.team-roster` — single-column ruled list (`border-top`).
- `.team-member` — `120px 1fr` grid, hairline `border-bottom`, collapsing to one column at ≤ 640 px.
- `.team-member-mark` — display-font monogram in `--green-dark` with the ink text-stroke used by `.step-num`.
- `.team-member-role` — wide-tracked uppercase role label in `--green-dark` (same language as the old `.team-card .role`).
- `.team-member-body p` — `--muted`, `--fs-400`, max-width 720 px.

It uses only existing tokens (`--green-dark`, `--legacy-ink`, `--muted`, spacing/type scale). It is deletable: removing the block and the `.team-roster` markup leaves the page meaningful.

---

## 5. Verification performed

- **Markup:** tag-balance parser reports 0 errors, 0 unclosed tags, 0 duplicate IDs, exactly one `<main>`.
- **Bilingual parity:** `data-lang="de"` and `data-lang="en"` counts match (54 / 54).
- **JS:** the one inline script passes `node --check`.
- **CSS:** brace counts balanced in both `experimental.css` (605/605) and `experimental.min.css` (604/604); the new roster rules are present in both.
- **Residuals:** no remaining references to `team-card`, `team-grid`, `portrait`, `images/team/`, `greenery-greenhouse`, "Der sechste Platz", "Link unten", or `diamond-accent` in `team.html`.
- **Rendered check (headless Firefox):** desktop 1440 px and mobile 390 px. The roster, advisor list, dark open-role section with framed CTA, and closing band all render correctly; the roster collapses to one column on mobile; no horizontal overflow observed.

---

## 6. Intentionally not changed

- **Hero copy and head metadata** (`title`, description, OG/Twitter, canonical) are unchanged.
- **Header, footer, navigation and language switch** are unchanged.
- **N=150 RCT claim:** already removed from `team.html` in the content-revision round; nothing to do here (open question Q11 is effectively closed for this page).
- **Portrait assets** (`images/team/*.svg`) and the greenhouse derivative (`images/derived/greenery-greenhouse-doorway-steps-*`) are now unreferenced but were left in place; deleting committed assets was out of scope for this round.
- **Indexability (GATE-14):** `noindex, nofollow` remains; the page is still staging-only.

---

## 7. Remaining blockers / open questions

1. **Portrait photos (Round-2 §2/§3, open question #14):** still not available. The photo-free roster is the documented fallback; if photos arrive, the roster can gain a portrait column or revert to cards.
2. **Joscha's details** (surname, role, bio) are still missing; the placeholder entry remains.
3. **`DESIGN-BRIEF.md:109` tension:** the brief says the sketch portraits "stay as texture on light sections", while Round-2 calls for photos or none. This round followed Round-2 (no placeholders). The brief line may need a note that it is superseded for the team page.
4. **Partner/relationship labeling (Q6):** the homepage ticker still carries the relationship claim; unaffected by this page, left as-is per locked #4.
5. **Contact email (WP J / GATE-11):** the open-role CTA uses `bjarne.dudzus@disce.de`, matching the footer and `kernel.html`. If the mailbox or address changes, this CTA must change with it.

---

## 8. Recommended next step

WP I's code work is complete. The remaining items are founder-input (portraits, Joscha, the DESIGN-BRIEF note). WP J (contact/email) and WP K (Substack) remain, and the WP A legal gates still gate indexability.
