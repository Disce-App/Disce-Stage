# DISCE — Website Design Brief & Rework Plan

Version 2.1 · 2026-09-10 · Repo language: English · Scope: visual design and front-end implementation only
Ground truth for the website rework (stage.weltvorstellung.de) and for coding agents working in this repository.

---

## 1. Purpose & Scope

- This brief governs **design**: color, typography, layout, imagery, motion, accessibility, performance. It does **not** govern copy. Existing copy stays as-is; agents must not rewrite headlines, body text, CTAs, or the claim. Copy changes require explicit approval.
- The site is bilingual (DE primary, EN parallel). Every design decision must work in both languages — German strings run ~30 % longer, so test both.
- Product facts below were verified against internal strategy and research documents (April–June 2026). They exist here so that design decisions express what Disce actually is — not to brief copywriting.

## 2. Product Reality Check (what the design must express)

- Disce is **not** a generic language-learning app and not "for anyone learning German". It is an AI-powered speaking-performance system for **international professionals and graduate students in the DACH region** who already have B2–C2 German.
- Core construct: **professional visibility through language**. The user is not deficient — they are temporarily *invisible*. Their expertise is real; language blocks others from seeing it in one decisive, high-stakes moment (job interview, Fachsprachprüfung, team meeting, recognition procedure).
- Product shape: situational, adaptive training of specific high-stakes scenarios with register feedback (Fachsprache ↔ Umgangssprache), fluency under pressure, and measurable real-world outcomes — not certificates, not streaks, not vocabulary drilling.
- First product scenario (V0): the **German job interview** ("Bewerbungsgespräch · DACH") — this is where the Kernel beta on the website leads.
- The Kernel (beta prototype, WIP, testable via the site) states three feedback principles in its own UI: **context-bound · revisable · no overall verdict** ("Kontextgebunden · Revidierbar · Ohne Gesamturteil"). The design must never imply scoring, grading, or gamified judgment — no stars, no percentages-as-grades, no leaderboards.
- Trust is a product feature: GDPR-native, EU-hosted, explicit consent. "Datenschutz / Einwilligung" are first-class UI elements, not footer afterthoughts.
- Claim: **"Sag, was du meinst."** — fixed, do not rewrite or translate inside DE context.

## 3. Voice Guardrail (microcopy only)

Applies only to microcopy the rework inevitably touches (buttons, labels, alt texts, empty states, form hints):

- Factual, direct, sharp. Reference points: "Duolingo makes you fluent. DISCE makes you effective." and "Kursfortschritt ≠ Lebensfortschritt".
- No SaaS clichés ("Do more. Stress less.", "Supercharge your …"), no coaching fluff, no exclamation marks.
- Numbers and status claims stay sober and dated (existing Development-Status pattern).
- The mockup slide "Do more. Stress less." is **composition reference only** — its wording is off-strategy (generic productivity consulting) and must not leak into the site.

## 4. Art Direction & Meta-Concepts

Style: **editorial surrealism / retro-futurism** — vast empty landscapes, lone celestial bodies, impossible architecture, film grain, vintage print borders. Magritte-adjacent; old poster and postcard printing.

| Motif | Meaning | Usage |
|---|---|---|
| White stag | The user stepping into visibility — the identification figure. Grounded in the project's own naming layer (CERVUS, the study framework — Latin for the deer genus). | Hero, beta page, empty states, 404. Recurring brand totem. |
| Empty arena seating | The waiting audience — the high-stakes moment before one speaks | Hero key visual |
| Burgundy sphere / sun / moon | The decisive moment looming over the DACH skyline | Accent motif; may recur in illustration and iconography |
| Doors, corridors, staircases | Thresholds and progression: B2 → C1 → C2, one room per register | Beta page, "How Disce works" |
| Open landscape + skyline | The DACH region as terrain to be entered | About/Vision, newsletter |
| Film grain, vignette, paper border | Print-editorial texture | Global overlay, subtle |

**Icon vs. artwork — one motif, two registers.** The brand already has an established stag/antler icon (the logo signet). It stays exactly as it is: no redraws, no derivatives, no "refreshes". It serves functional contexts — logo lockup, favicon, small UI sizes. The full-figure stag in the artwork is the *same motif in editorial variation*: it appears deliberately and repeatedly across the imagery (arena, doorway, landscape). Agents must treat this recurrence as intentional brand language, not as inconsistency to be "unified". Visual hierarchy: icon in nav/footer/favicon and small formats; stag artwork in hero and section imagery. The two never appear merged (no artwork-derived icon replacements).

Key reading for everyone touching the design: **the stag stands where the user wants to be — visible, lit, inside the room.** Dark-to-light transitions in imagery echo the arc invisible → visible.

## 5. Color System

The current cream/green/black base stays. The palette is extended by the dark tones and two accents extracted from the approved mood assets (measured values below).

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#F7F1E3` | Background, light sections (current state, unchanged) |
| `--paper-2` | `#EEE8D6` | Cards/panels on light |
| `--ink` | `#161210` | Text, hairline borders |
| `--green-deep` | `#123329` | Dark sections, footer, hero surfaces, beta UI |
| `--green-sage` | `#77816A` | Secondary surfaces, hover states, icons on light |
| `--parchment` | `#D5C09D` | Text and headlines on dark surfaces |
| `--bordeaux` | `#612E31` | "Moment" accent — sphere motif, active states; very sparing |
| `--ochre` | `#E3AF50` | "Spotlight" accent — status dots, badges, markers (as in the Kernel UI) |

CSS starting point:

```css
:root {
  --paper: #F7F1E3;
  --paper-2: #EEE8D6;
  --ink: #161210;
  --green-deep: #123329;
  --green-sage: #77816A;
  --parchment: #D5C09D;
  --bordeaux: #612E31;
  --ochre: #E3AF50;
}
```

Rules:

- Light cream sections remain the default; dark green sections structure the rhythm (max. 1–2 per page plus footer).
- Bordeaux never sits behind text; it is a punctual accent only.
- Check contrast: `--parchment` on `--green-deep` for body text, `--paper` on `--green-deep` for headlines; WCAG AA (4.5:1) minimum.
- The current bright green survives as the functional accent on light surfaces only (buttons, links). On dark surfaces it is replaced by `--ochre` / `--parchment`.

## 6. Typography

- The existing bold uppercase grotesque remains the backbone (brutalist-editorial).
- Optional addition (open decision): a serif display face for large quotes and hero lines on dark image sections — reference: the mockup headline and "KERNEL" in the beta UI.
- Do not let agents improvise scale, tracking, or line-height: adopt existing values, document them, freeze as tokens.
- Self-host all fonts (GDPR), `font-display: swap`.

## 7. Imagery & Usage Matrix

Every placement below names a real, committed file under `images/`.

| Asset | Motif | Placement | Treatment |
|---|---|---|---|
| `DISCE_C01_r1_arena-stag-bordeaux.png` | Key visual: white stag in empty arena before the burgundy sphere (clean, text-free) | Homepage hero, full-bleed | Dark scrim (40–55 % black-green), headline in `--parchment`, fine grain overlay; focal point on stag + sphere (mind mobile crop) |
| `DISCE_B03_r3_canal-pavilions.png` | Kernel staircase / impossible architecture on deep green | Beta/prototype page hero; on homepage as card visual inside "How Disce works" | Little scrim needed (asset is dark), text right as in the mockup, keep ochre markers |
| `DISCE_C02_r1_corridor-stag-threshold.png` | Corridor with stag | Dark interstitial section (e.g. Problem or About) | Strong scrim, text left, stag stays visible right |
| `DISCE_C03_r1_zeppelin-forest.png` | Zeppelin with forest | About/Vision banner | 21:9 crop, calm surface, minimal text |
| `DISCE_B04_r4_causeway-palms.png` | Open landscape / palm causeway with stag | Newsletter closer; wide section imagery | Full-bleed or wide section background, parchment text |
| `DISCE_C04_r1_loop-train-violet.png` | Loop train (violet ring) | Insights/blog thumbnails, 404 page, possibly loading states | Small formats, card crops, never a fullscreen hero |
| `DISCE_C06_r1_stag-antlers-city.png` | Stag carrying a city on its antlers | Secondary / brand-totem visual; section card | Card or section imagery, parchment text |
| `DISCE_C07_r1_stag-path-bordeaux-city.png` | Stag on a path before the bordeaux sphere over the DACH skyline | Alternate / threshold visual | Scrim, keep a text-safe area |
| Mockup "Do more. Stress less." | Composition reference | Do **not** ship as an image; stays out of the repository | Template for hero composition only: badge top-left, large headline left, stat card right, testimonial card bottom-left |
| Sketch portraits (current site) | Editorial drawings | Stay as texture on light sections | Unchanged, optionally reduce opacity |

Global imagery rules:

- Consistent grade across all assets: deep green + parchment + a single warm accent. No saturated stock-photo looks.
- Grain overlay (PNG/SVG noise, ~4–6 % opacity) on all full-bleed images for the print feel.
- The stag is the identification motif: never covered, never cut off.
- No text over imagery without a scrim; legibility outranks effect.

## 8. Layout & UI Principles

- The brutalist grid (visible hairlines, hard edges, numbered cards) stays — it is the bridge between print aesthetics and interface.
- New counterpoint: dark, cinematic image sections against the light grid sections. Rhythm per page: light (problem/facts) → dark (image/emotion) → light (concrete/CTA).
- Corners stay square; radii belong to the beta UI, not the marketing pages.
- Adopt micro-details from the Kernel UI: ochre status dots, wide-tracked small-caps labels, hairline dividers.
- No scoring, grading, or gamification patterns anywhere (progress rings, stars, XP) — the product explicitly refrains from overall verdicts, and the marketing site must not contradict that.
- Motion stays restrained: gentle fades/parallax on hero images at most; nothing playful.

## 9. Technical Image Integration

- Formats: AVIF primary, WebP fallback, JPG last resort; serve via `<picture>` with art-directed crops (desktop/mobile).
- Responsive sizes: `srcset`/`sizes` for the target 768/1280/1920/2560 px widths; hero images get `fetchpriority="high"` and no lazy-loading; everything else lazy.
- Interim master-width rule: the widest masters in the repo are **1824 px** (curated `DISCE_*` assets) and **1376 px** (ComfyUI render plates). Until wider masters exist, a hero `srcset` tops out at the real master width — **do not upscale without approval**. Re-rendering hero-class assets at ≥ 2560 px is a later content task (Section 13).
- LQIP/blur placeholders for all large images to prevent CLS; fixed aspect ratios in CSS.
- Budgets: ≤ 250 KB per hero (AVIF, q~50), ≤ 120 KB per card image; commit an optimization script to the repo (e.g. `sharp`-based Node script) outputting into the asset directory; no external image CDN required.
- Alt texts in German and English; purely decorative overlays carry empty `alt=""`.
- All assets self-hosted in the repo — consistent with the GDPR-native, EU-hosted positioning; no third-party requests.

## 10. Accessibility & Performance Budgets

- WCAG AA contrast, especially text on imagery (tune scrim strength to contrast, not the other way round).
- Keep focus styling visible (currently black frame → `--ochre` on dark surfaces).
- Respect `prefers-reduced-motion` (parallax/fades must be switchable).
- Lighthouse targets: LCP < 2.5 s, CLS < 0.05, mobile performance ≥ 90.
- Full keyboard navigation including language toggle and waitlist form.

## 11. Do's & Don'ts

Do:
- Use dark image sections deliberately as counterpoints.
- Let the stag motif recur across artwork — the repetition is the brand language.
- Deploy ochre and bordeaux as rare, precise accents.
- Carry the print texture (grain, paper) consistently.

Don't:
- Never redraw, restyle, or "refresh" the existing stag icon; never derive new icons from the artwork.
- No generic SaaS gradient surfaces, no stock photos (especially no smiling-people-in-meetings imagery), no rounded "friendly tech" cards.
- No glassmorphism cards on marketing pages (mockup is composition reference only; if used at all: hero only, heavily darkened).
- No scoring/gamification UI patterns.
- No copy changes without explicit approval.
- No new colors outside the token list.

## 12. Agent Workflow (OpenCode)

Preparation:
1. Clone repo, create branch `rework/design-2026`.
2. Commit this file to repo root or `docs/`; create/extend `AGENTS.md` with: build/dev commands, conventions, "no new dependencies without approval", "one task = one commit", reference to this brief.
3. Confirm the stack in the repo (framework, CSS approach) and quote it in the first prompt.

Phase 1 — Audit (read-only): the agent inventories pages, components, and styles, and lists visible UI bugs as a table with `file:line`, description, and severity. Review and prioritize before anything changes.

Phase 2 — Design tokens: migrate CSS variables/Tailwind config to the new palette without touching layout or imagery. Acceptance: the page renders as before; all color values come from tokens.

Phase 3 — Bug fixes: one bug per prompt per commit. Each fix with an acceptance criterion and before/after screenshots (the model is multimodal — put screenshots straight into the prompt).

Phase 4 — Image pipeline: optimization script plus a hero/background component with scrim prop and art direction. Prove it on one section first, then roll out.

Phase 5 — Section rework, in order: Hero → Problem → "How Disce works" → Beta/prototype teaser → Footer. Per section: mockup reference image + this brief + concrete acceptance criteria in the prompt.

Phase 6 — Verification: clean build, Lighthouse run, contrast/keyboard check, EN version in sync, PR with before/after screenshots of every section.

Prompting rules for all phases:
- Small, bounded tasks; never "make the site prettier".
- Reference context files (`@DESIGN-BRIEF.md`, `@AGENTS.md`) instead of pasting full text into prompts.
- State explicitly what must NOT change.
- Instruct the agent to ask when uncertain rather than guess.
- After each task: require a short summary of changed files.

Example prompt (Phase 5, hero):
> Read @DESIGN-BRIEF.md sections 4, 5 and 7. Rework the homepage hero: full-bleed key visual `images/DISCE_C01_r1_arena-stag-bordeaux.png` (Phase 4 produces the optimized AVIF/WebP derivatives and `<picture>` art direction from this master) with a 45 % scrim in `--green-deep`, headline in `--parchment`, badge top-left, CTA unchanged. Mobile crop must keep stag and sphere visible. Do not touch navigation, copy, or other sections. Afterwards produce a screenshot comparison and list the changed files.

## 13. Open Decisions

- Serif display face for headlines on dark sections: yes/no (Section 6).
- Does the current bright green survive as the button color, or is it replaced by sage?
- Glass-card elements in the hero: adopt (darkened) or drop?
- 404 page motif: **decided** — loop train (`images/DISCE_C04_r1_loop-train-violet.png`).
- EN translations of new alt texts and captions: produce alongside or as a separate sprint?
- Icon on dark surfaces: the existing icon was designed for light backgrounds — is a parchment/inverted variant already available from the source files, or does one need to be exported (recolor of the existing asset, not a redraw)?
- Re-render hero-class assets at ≥ 2560 px width: needed to satisfy the full Section 9 `srcset`; current masters top out at 1824 px (curated `DISCE_*`) and 1376 px (ComfyUI render plates).
