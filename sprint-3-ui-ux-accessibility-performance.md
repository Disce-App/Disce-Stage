# Sprint 3 — UI/UX, Accessibility & Performance

**Assessment / situation report (diagnostic only). No fixes, no rewrites, no prioritisation.**

- **Subject:** Disce website, repository `weltvorstellung`, staging host `stage.weltvorstellung.de`.
- **Benchmark:** `Pre-Launch-Website-Exhaustive-Report.md` §5 "UI/UX State of the Art" (Must/Should/Nice/Avoid, B2B/consumer/AI, Motion, Mobile blind spots, Accessibility minimum, Performance minimum, Pre-launch QA), §10 anti-patterns, §11 Master Checklist.
- **Repo-internal rules that also apply:** `DESIGN-BRIEF.md` §5–§11 (binding design reference), `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and `docs/generative-visuals/implementation-plan.md` (generative visuals), `AGENTS.md` (accessibility guardrail).
- **Method:** direct inspection of `css/experimental.css` (3,064 lines), `js/site.js`, `js/generative/*`, all HTML pages, and the image pipeline outputs under `images/derived/`. No automated Lighthouse/CWV run was performed; where a claim would require measurement, that is stated explicitly rather than asserted.
- **Interview date:** 2026-09-21.

## 0. Surfaces and tooling in scope

- **One shared stylesheet:** `css/experimental.css`. **One shared script:** `js/site.js` (92 lines: mobile nav, ticker duplication, accordion, language). **Generative modules:** `js/generative/loader.js`, `registry.js`, `tokens.js`, `prng.js`, `dot-field/`, `section-motif/`.
- `waitlist.html` is an outlier: its own inline `<style>` (`waitlist.html:28–450`), its own inline script (`:761–909`), no shared header/footer, self-hosted Inter + Noto Serif (`:33–46`).
- All fonts self-hosted under `fonts/` via `@font-face` in `css/experimental.css:13–41` (`font-display: swap`). No third-party requests, no analytics, no consent manager (verified: the only `cookie`/`tracking` references are the privacy text in `datenschutz.html:110`, `:137`).

---

## 3.1 Design principle

**Benchmark expectation** (§5 "Design principle"): pre-launch state of the art is **not maximum visual complexity**; it is a clear focal point, distinctive but coherent brand traits, real/verifiable product depiction, clean responsive behavior, accessible interactions, low technical friction, and motion with an explainable function. Trends are only helpful when they improve attention, legibility, or product understanding.

**Current state on the website**

- The site has a coherent, documented editorial-surrealist visual system: a token palette (`css/experimental.css:44–99`), a typographic pairing (Archivo Black grotesque + Newsreader serif; `:13–41`), grain/paper texture, and a recurring stag motif — all specified in `DESIGN-BRIEF.md:33–48`, `:94–116`.
- Clear focal points exist per section (hero artwork, dot fields, project-spine spotlight, chapter covers). Hierarchy is generally strong.
- "Real/verifiable product depiction" is absent (see Sprint 2 §2.6): all imagery on the site is decorative/AI-generated (`alt=""` on hero `index.html:68`, corridors `:131`, media cards `:206`, `:215`, CTA band `:252`, and all chapter covers), except the Kernel's inline SVG architecture plate (`kernel.html:142–220`).

**Gap / blind spot:** The design principle is met on "clear focal point, distinctive coherent brand traits, accessible interactions (mostly), low technical friction" and **not met on "real or verifiable product depiction"**. The system is deliberately elaborate (generative dot fields, portrait layers, grain, full-bleed editorial imagery) relative to the benchmark's "not maximum visual complexity" framing, though the complexity is in service of brand rather than added arbitrarily. The repo itself acknowledges open art-direction questions and unresolvable prototype-grade assets (`DESIGN-BRIEF.md:191–209`).

---

## 3.2 “Must have” patterns

**Benchmark expectation** (§5 "Must have" table): clear typography scale; consistent grid; visible hierarchy; real product evidence; responsive product depiction; one dominant accent; accessible states and forms; performance budget.

| Must-have | Current state | Gap / blind spot |
|---|---|---|
| **Clear typography scale** | Tokens `--fs-100 … --fs-700` used throughout (`css/experimental.css`), two display faces, uppercase editorial labels. | No ultralight weights observed; scale is consistent. **Meets** the benchmark. |
| **Consistent grid** | A visible hairline brutalist grid and repeated card/grid patterns (`problem-grid`, `persona-grid`, `team-grid`, `process-list`). | **Meets**. Repo notes a uniform-template risk is accepted as brand language (`DESIGN-BRIEF.md:120`). |
| **Visible hierarchy** | Hero → section heads → cards; `eyebrow` + `h2` + `lede` pattern is reused consistently. | **Meets**, but hierarchy is diluted by three co-equal dark/quote bands on the homepage (Sprint 2 §2.7). |
| **Real product evidence** | **Absent.** No screenshot/mockup/demo. Kernel architecture SVG is the only technical artifact (`kernel.html:142–220`) and is `aria-hidden`. | Direct miss of a benchmark Must-have; see §3.1 and Sprint 2 §2.6. |
| **Responsive product depiction** | Not applicable in the benchmark sense (no product UI shown); the Kernel SVG is made horizontally scrollable on narrow viewports rather than shrunk (`css/experimental.css:2410` `min-width: 900px`; `:2449` `min-width: 820px`; wrapper `tabindex="0"` at `kernel.html:143`). | No product depiction to be responsive; the SVG fallback scrolls inside its own region, which is a reasonable pattern for a diagram. |
| **One dominant accent** | Green is the functional accent on light; ochre/bordeaux are "rare, precise accents" per `DESIGN-BRIEF.md:150–152`; `.hero .eyebrow::before` uses ochre (`css/experimental.css:395`). | Mostly disciplined. Bordeaux is used in artwork; no evidence of accent overuse. **Meets**. |
| **Accessible states and forms** | Global `*:focus-visible { outline: 3px solid … }` (`css/experimental.css:1908–1913`), hover/active states for buttons (`:412–423`), waitlist form has real `<label>`s, 16 px inputs, error text, disabled/loading state (`waitlist.html:558–720`, `:336–357`). | Form errors are **not** programmatically associated (`no aria-invalid`, no `aria-describedby`, no `role="alert"`/`aria-live`; verified by grep across all HTML/JS). Success/failure messages (`waitlist.html:711–718`) are not announced to screen readers. This is an accessibility gap in the core conversion form (see §3.8). |
| **Performance budget** | Hero images are AVIF-primary with WebP fallback and `fetchpriority="high"` (`index.html:63–69`, `kernel.html:65–72`); no AVIF derivative exceeds 250 KB (largest 139 KB); responsive `srcset` present; below-fold images lazy-loaded. | No measured CWV; fonts are **not preloaded** (no `rel="preload"` anywhere); `waitlist.html` re-declares two `@font-face` families inline. Budgets in `DESIGN-BRIEF.md:143` (LCP < 2.5 s, CLS < 0.05, mobile perf ≥ 90) are targets, not measured outcomes. |

---

## 3.3 “Should have” patterns

**Benchmark expectation** (§5 "Should have" table): annotated screenshots; short workflow demo; subtle microinteractions; distinct but restrained brand system; mobile-specific composition; contextual trust modules.

| Should-have | Current state | Gap |
|---|---|---|
| **Annotated screenshots** | Absent (no screenshot at all). | Miss; explanation-heavy product has no annotated visual. |
| **Short workflow demo** | Absent on the homepage. The Kernel describes a 6-step cycle as text steps (`kernel.html:313–356`); `kernel.html:134` notes "A future animated trace would be a separate data-gen module with this plate as its static fallback." | Miss; mechanism is text-only. |
| **Subtle microinteractions** | Present and restrained: nav toggle, project-spine hover/focus fields (`css/experimental.css:1300–1317`), dot-field pointer reaction (disabled on coarse pointers per `dot-field/README.md`), ticker scroll. Loader reveals plate only after successful mount (`loader.js`). | Avoids motion-without-purpose; **meets** the benchmark's intent. |
| **Distinct but restrained brand system** | Strong and documented (`DESIGN-BRIEF.md:33–48`). | **Exceeds**; possible risk of brand system crowding the (missing) product evidence. |
| **Mobile-specific composition** | Dedicated breakpoints throughout (`css/experimental.css` ~209, 281, 485, 588, 627, 664, 692, 745, 786, 814, 815, 821, 914, 921, 1129, 1142, 1146, 1534, 1564, 1595, 1668, 1740, 1947, 1990, 2010, 2154, 2218, 2343, 2371, 2448, 2499, 2759, 2853, 2950, 2978, 3062); the hero switches to a single column and a solid `--green-forest` band (`:486`, `:494–495`); the architecture plate scrolls rather than shrinks. | **Meets** the "recompose, don't just stack" requirement in several places (hero, plate). |
| **Contextual trust modules** | Absent. Kernel's "Die Grenzen" (`kernel.html:445–474`) and the homepage's status-adjacent stats are the closest things, but they are not positioned near the CTA or the form. | Miss; benchmark §8 says privacy/trust reassurance belongs near the point of submission. |

---

## 3.4 “Nice to have” patterns

**Benchmark expectation** (§5 "Nice to have"): these are explicitly optional and only valuable once fundamentals are strong. Present on the site: **choreographed transitions** (ticker, project-spine, generative reveals) and a **bespoke illustration system** (the stag/arena art family). Absent: interactive product demo, 3D metaphor, dark/light theme, dynamic personalization. The benchmark's rule of thumb ("advanced motion, 3D, and elaborate illustration systems help only if the fundamentals — typography, hierarchy, real product evidence, accessible forms, mobile clarity — are already strong") is directly relevant: the site has advanced motion and an elaborate illustration system while the fundamental **real product evidence** is missing. Not a defect in itself, but the repo is investing in "nice to have" while a "must have" (product evidence) is absent.

---

## 3.5 “Avoid or use carefully”

**Benchmark expectation** (§5 "Avoid or use carefully"): glassmorphism, aurora gradients, endless logo marquees, scroll hijacking, auto-rotating hero content, cursor effects, ambient hero video, and combined glass+gradient+3D+noise.

| Anti-pattern | Present? | Evidence / assessment |
|---|---|---|
| **Glassmorphism** | **Yes, in the hero** | `index.html:80` `.glass-card glass-testimonial`; styles `css/experimental.css:431–483`. This is a permitted exception per the binding brief (`DESIGN-BRIEF.md:122`, `:197`: "heavily darkened, parchment-tinted variant only … thin hairline border, square corners, no blur-heavy `backdrop-filter` stacks; used in the hero only"). The benchmark warns glass "loses contrast on complex backgrounds". Here it sits over a scrimmed dark artwork. Repo rule and benchmark partially conflict; the repo documents the exception. |
| **Aurora gradients** | Not found | — |
| **Endless logo marquees** | **Yes** | `index.html:267–283` `.ticker-section` / `.ticker-track`; CSS `css/experimental.css:1712` `animation: ticker-scroll 34s linear infinite`; JS duplicates the DOM run to make it seamless (`js/site.js:27–40`). This is exactly the benchmark's "endless logo marquee" (motion makes verification harder and can mask weak evidence). It is also the surface carrying an unverifiable "Strategische Partner" claim (Sprint 4 §4.7). |
| **Scroll hijacking** | Not found | No scroll-linked JS observed. |
| **Auto-rotating hero content** | Not found | The hero is static; motion is ambient (dot field, portraits). |
| **Cursor effects** | Partial/controlled | The dot field reacts to the pointer (`js/generative/dot-field/reactive.js`) but the README states it is disabled on coarse pointers (touch), decorative, `aria-hidden`, `pointer-events:none`, and no meaning is gated behind it. The benchmark lists cursor effects as "meaningless on touch devices"; the repo's own rule makes it pointer-initiated, not autonomous. Borderline but documented and bounded. |
| **Ambient video in hero** | Not found | No video on the site. |
| **Combined glass+gradient+3D+noise** | Partially present as texture stack | The site layers grain/paper texture (`--paper-grain`, `css/experimental.css:98–99`), full-bleed imagery, glass hero card, generative dot fields and portrait layers. The benchmark's "visual competition" warning applies at a stylistic level; the binding brief treats grain as intentional brand texture (`DESIGN-BRIEF.md:114`). |

**Gap / blind spot:** Two benchmark anti-patterns are present and one of them (the logo marquee) materially interacts with a trust claim. The hero glass card is a documented, bounded exception rather than an oversight. The cursor-reactive dot field is bounded and touch-disabled, so it does not match the benchmark's "meaningless on touch" failure mode, but it is still decorative motion.

---

## 3.6 Motion and microinteractions

**Benchmark expectation** (§5 "Motion and microinteractions"; §1 point 12): motion must explain state, causality, or product behavior; harmful when decorative, continuous, or impossible to reduce. WCAG 2.2 requires interaction-triggered motion to be disable-able unless essential. "Treat motion as a scarce resource."

**Repo-internal rules** (`GENERATIVE_WEB_VISUALS_COMPETENCY.md`; `docs/generative-visuals/implementation-plan.md` §5): one `requestAnimationFrame` maximum; pause offscreen (`IntersectionObserver`) and in hidden tabs (Page Visibility); delta-time clamping; no per-frame allocations; no scroll hijacking; no custom cursor; no flashing >3 Hz; no large parallax; contrast ≥ 4.5:1 over the cycle; every pointer interaction has a keyboard equivalent; **any persistent automatic motion gets a pause control**; reduced motion shows a meaningful static state; no-JS fallback is the current look; DPR cap 1.5/2; ambient FPS 20–30.

**Current state on the website**

- **Reduced motion is handled** in three CSS contexts (`css/experimental.css:1318` project-spine focus changes, `:1727` ticker animation disabled, `:1948` portrait transitions disabled) and in JS (`js/generative/loader.js` `prefersReducedMotion()` gates `motion` in `resolveMotion()` before mounting). `waitlist.html:444–449` disables all animation/transition durations under reduced motion.
- **No-JS fallback is implemented**: the generative plate ships hidden and is only revealed after a successful module mount (`js/generative/loader.js`; module data attributes like `index.html:70` are `aria-hidden`).
- **One rAF / lazy load**: `dot-field/README.md:19` states the module "drives one `requestAnimationFrame`"; `:84` states "One rAF per mount, DPR capped at 2, pause via `IntersectionObserver` offscreen" plus Page Visibility. These are module-doc claims, **not independently measured** in this assessment.
- **CSS motion inventory:** 16 `animation`/`transition` declarations in `css/experimental.css` (grep count), the most prominent being the ticker (`:1712`) and the project-spine hover fields (`:1300–1317`). Portrait layers use transitions (`:1940–1948`).
- **Ticker is persistent automatic motion** (`34s linear infinite`). The repo's own implementation-plan rule says "any persistent automatic motion gets a pause control". **No pause control exists for the ticker** in the markup (`index.html:267–283`), and there is no `aria-live`/reduced-motion-only fallback beyond disabling the CSS animation. This is a concrete divergence from the repo's own stated rule.

**Gap / blind spot**

- Reduced-motion support is broad and above the benchmark minimum.
- Two divergences from the repo's own strict rules: (a) the **logo ticker has no pause control**; (b) the dot field is mounted **in the hero / LCP context** (`index.html:70`, `team.html:57`, `status.html:57`), whereas the implementation plan budgets hero generative work as "lazy post-LCP, 20–30 FPS, ≤150/400 primitives" — the loader mounts all `[data-gen]` on `DOMContentLoaded` (`loader.js`) with no post-LCP deferral, and the README contains no measured FPS/JS-size figures. Per the competency's Definition of Done ("profiled on a target device or defined throttled environment") and the evidence rule ("Never claim performance or accessibility compliance without measurements"), these remain **unverified**, not proven violations.
- No `prefers-reduced-motion` handling for the **hero glass card / scrim**, but those are static.

---

## 3.7 Mobile blind spots

**Benchmark expectation** (§5 "Mobile blind spots"): desktop screenshots shrunk instead of recomposed; sticky CTA covering consent/form/browser UI; nav requiring multiple interactions to reach primary CTA; autoplay video on mobile bandwidth; cards → long monotonous stacks; small tap targets; wrong keyboards / small-text zoom; trust/status only after long scroll. Baseline: pointer targets ≥ 24×24 CSS px (`§5`), with a larger practical target recommended.

**Current state on the website**

| Blind spot | Status |
|---|---|
| Screenshots shrunk | Not applicable (no screenshots); the architecture SVG scrolls instead of shrinking (`css/experimental.css:2410`, `:2449`). |
| Sticky CTA covering UI | No sticky CTA exists. `waitlist.html` uses fixed controls (`language-toggle` top-right `waitlist.html:100–117`, `back-link` top-left `:119–131`); at ≤640 px they shrink to 42/13 px (`:433–434`) but remain in corners, not over the form. |
| Nav needs multiple interactions for primary CTA | Mobile nav is a hamburger (`index.html:44`), so the waitlist CTA is one tap away after opening the menu; it is not in the closed bar. |
| Autoplay video | No video. |
| Cards → long stacks | Multiple grids collapse to single column at defined breakpoints (`css/experimental.css:627` personas, `:692` media cards, `:815` team, `:821` advisors, `:1740` footer). This is standard stacking; the benchmark warns against "mere vertical stacking", and the site compensates with full-bleed recomposed bands (hero, corridor, CTA band) between stacked sections. |
| Small tap targets | Buttons have `min-height: 48px` on the waitlist page (`waitlist.html:338`). Site-wide `.btn-primary`/`.btn-secondary` padding is defined (`css/experimental.css:401–411`); explicit ≥24 px sizing for nav links/ticker not verified in this pass. |
| Wrong keyboards / zoom on small text | Waitlist inputs are `font-size: 16px` (`waitlist.html:250`), preventing iOS zoom, and use `autocomplete` (`:568`, `:584`). **Meets.** |
| Trust/status only after long scroll | Homepage status appears in the hero stat panel (`index.html:89–90`) but beta/study specifics are on a separate page reachable only via the nav CTA. **Partial gap.** |

**Gap / blind spot:** The waitlist form's mobile ergonomics are deliberately handled (16 px inputs, labels, 48 px buttons, 1-column availability grid at `waitlist.html:436`), which meets the benchmark's form-on-mobile concerns. The main mobile questions that remain unverified are tap-target dimensions for nav/ticker links and the actual legibility of the decorative imagery at 375 px (the design system accepts strong crops, e.g. `kernel.html:63` comments "strong crop at 375 is accepted").

---

## 3.8 Accessibility minimum

**Benchmark expectation** (§5 "Accessibility minimum", 11 items) plus Master Checklist P0 items.

| Accessibility item | Current state | Gap |
|---|---|---|
| **Semantic landmarks & heading hierarchy** | One `<h1>` per page (verified: all seven content pages), `<header>`, `<nav>`, `<main>` on `waitlist.html`, `<footer>`, `<section>`. `index.html` has no `<main>` wrapper around section content (sections are direct children of `<body>`); `waitlist.html` is the only page with `<main>` (`:485`). | Minor semantic gap on most pages (no `<main>` landmark). |
| **Full keyboard operability** | Nav toggle, language switch, accordion (unused), form controls, links are native. Escape closes mobile nav (`js/site.js:13–18`). The architecture plate region is focusable (`kernel.html:143`). No skip-to-content link exists (verified). | No skip link; no obvious keyboard trap found. |
| **Visible focus for every interactive element** | Global `*:focus-visible` outline, with light/dark variants (`css/experimental.css:1908–1913`), plus `.arch-plate-scroll:focus-visible` (`:2406`). | **Meets**; the only concern is that `:focus-visible` (not `:focus`) may not show for all legacy browsers, but this is the modern recommended pattern. |
| **Real labels instead of placeholders** | Waitlist form uses `<label for>` on every field (`waitlist.html:562–599`, `:689`); placeholders are supplementary (e.g. `:569`). | **Meets**. |
| **Textual, field-adjacent, programmatically announced errors** | Errors are textual and field-adjacent (`waitlist.html:570–573`, `:586–589`, `:610–613`, `:653–656`, `:679–682`). But there is **no `aria-invalid`, no `aria-describedby`, no `role="alert"`/`aria-live`** (verified by grep). The submit button carries no `aria-busy`. | **Gap** in programmatic announcement, which is the benchmark's explicit requirement. The visual error experience is correct. |
| **Alt text for meaningful images** | Decorative imagery correctly uses `alt=""` (hero, corridors, bands, chapter covers). Meaningful images: brand mark `alt="" aria-hidden` (decorative, correct); waitlist hero logo `alt="Disce Logo"` (`waitlist.html:473`); team portraits `alt="Portrait placeholder: X"` (`team.html:70–106`) — honest but placeholders. | **Meets** for semantic correctness; team portraits are pending real assets. |
| **Subtitles/transcripts for content videos** | No videos. | N/A. |
| **No information conveyed by color alone** | Status uses text labels plus color: status tags read "Abgeschlossen / In Entwicklung / Geplant" (`status.html:125`, `:144`, `:171`), not color only. | **Meets**. |
| **Text contrast ≥ 4.5:1 (3:1 large)** | Tokens are chosen for AA (`DESIGN-BRIEF.md:84`), and the brief instructs tuning scrim to contrast. Hero lede uses `--legacy-paper` on a scrimmed dark band (`css/experimental.css:397`). | Not independently measured in this pass; the repo states AA intent. **Unverified**, not proven deficient. |
| **Zoom/reflow without horizontal scroll** | Architecture plate scrolls inside its region (`css/experimental.css:2410`, `:2449`), not the page; CTA buttons use `overflow-wrap: break-word` and min-width resets (`:2005–2016`). | Likely **meets**; no 200%/320 px zoom test was run in this assessment. |
| **Respect `prefers-reduced-motion`** | Implemented in CSS (`:1318`, `:1727`, `:1948`), JS loader, and `waitlist.html:444`. | **Meets**, with the caveat that the ticker is disabled but has no pause control (see §3.6). |
| **Announce form and status messages** | Not implemented (no `aria-live`/`role=status`). | **Gap**, same as the error item. |

**Additional benchmark QA-item checks:**
- **Privacy/consent:** no non-essential trackers exist at all, so there is nothing to gate; this item is largely N/A and is assessed in Sprint 4.
- **Error handling (API failure/timeout/offline/duplicate submit):** the waitlist form disables the button during submit and re-enables on error (`waitlist.html:850–895`); the `catch` covers network failure and shows a text error. There is no explicit offline/timeout handling or duplicate-submit suppression beyond the disabled state, and no spam/rate protection. **Partial gap.**
- **Empty states:** no social-proof/changelog placeholders; the empty ticker slots are hidden by `.ticker-logo:empty { display:none }` (`css/experimental.css:1724`). The placeholder team card is content, not an empty state.

---

## 3.9 Performance minimum

**Benchmark expectation** (§5 "Performance minimum"; Core Web Vitals "good": LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1): compress/size the hero medium and don't lazy-load the LCP resource; lazy-load below the fold and reserve dimensions; remove unnecessary JS/third-party scripts; subset/preload fonts; prefer `transform`/`opacity` animations; include consent/chat/tracking in performance tests.

**Current state on the website**

| Priority | Status |
|---|---|
| Hero medium optimized, not lazy-loaded | `loading="eager" fetchpriority="high" decoding="async"` on homepage hero (`index.html:68`), kernel hero (`kernel.html:71`), philosophy hero (`philosophy.html:83`), beta hero (`beta.html:64`). AVIF primary + WebP fallback + fixed `width`/`height`. Largest AVIF derivative = 139 KB (CTA band), below the repo's 250 KB hero budget. **Meets.** |
| Lazy-load below fold + reserve dimensions | Below-fold pictures use `loading="lazy"` with explicit `width`/`height` (`index.html:131`, `:206`, `:215`, `:252`; `philosophy.html:145`, etc.). **Meets.** |
| Remove unnecessary JS / third-party scripts | No third-party scripts; JS is `js/site.js` (92 lines) + lazy ES-module generative code + inline waitlist script. No analytics/consent/chat. **Meets** (and exceeds: zero third-party requests). |
| Reduce/subset/preload fonts | Four self-hosted WOFF2 families; `font-display: swap`. **No `rel="preload"`** for fonts (verified). `waitlist.html` duplicates two `@font-face` inline (`:33–46`). **Partial gap.** |
| Animations via `transform`/`opacity` | Ticker uses `transform: translateX` (`css/experimental.css` `@keyframes ticker-scroll`); transitions use opacity/transform. Canvas dot field is composited. No layout-triggering animation observed. **Meets.** |
| Include consent/chat/tracking in perf tests | None present. N/A. |
| Core Web Vitals | No measured LCP/INP/CLS available in the repo. The binding brief sets internal targets (LCP < 2.5 s, CLS < 0.05, mobile perf ≥ 90; `DESIGN-BRIEF.md:143`). | **Unverified.** The competency's evidence rule explicitly forbids claiming performance compliance without measurement, so this assessment records the targets as unmet-by-evidence rather than met or failed. |

**Additional performance facts:** `images/` totals ~57 MB in the working tree, of which `images/derived/` is ~6.5 MB / 126 files; bulk masters (`images/`) are also committed. Only a subset is referenced per page, so transfer weight is lower than the repository size suggests — but the repo ships committed masters and unused derived assets (`greenery-conservatory-moon-1254.webp` ≈ 242 KB, `greenery-horizon-watertower-2560.webp` ≈ 140 KB) whose page usage was not traced in this pass. There is one inline render-blocking `<script>` in `<head>` on every page for the pre-EN class flash (`index.html:9`, mirrored on all pages) — small and intentional.

---

## 3.10 Pre-launch QA table

**Benchmark expectation** (§5 "Pre-launch QA" table, P0/P1 checks).

| Area | P0 checks | Current state |
|---|---|---|
| **Desktop** | Hero/core message clear without scrolling; CTA visible; no broken layout; 200% zoom | Hero message is visible without scroll; CTAs in hero; layout is grid-based. No 200% zoom test run. Not verified. |
| **Mobile** | No horizontal scroll; nav/hero/CTA obvious at 320–430 px; product visual readable; menu usable | Menu is a hamburger with Escape/outside-click close (`js/site.js`). Product visual N/A. No 320 px test run. Not verified. |
| **Forms** | Labels attached; required fields indicated; submit/validation/success/duplicate/retry function; errors visible in text | Labels and required `*` marks present (`waitlist.html:239–242`, `:565`). Validation, success, retry present (`:796–896`). Duplicate submit suppressed only by disabling during request; **errors are not programmatically announced**. |
| **Accessibility** | Keyboard traversal; focus visible; labels/contrast/heading structure; motion reducible | Focus visible globally; labels present; headings valid; reduced motion in 3 CSS blocks + JS. **Contrast and keyboard traversal not independently verified.** |
| **Performance** | Hero medium optimized; no severe layout shift; limited third-party scripts; LCP/CLS/video | Hero optimized, no third-party scripts, dimensions reserved. **LCP/CLS not measured.** |
| **Privacy / consent** | Tracking respects consent; no non-essential trackers before consent; form purpose disclosed; privacy link visible | No trackers at all; form purpose is stated (`waitlist.html:736–749`); privacy link: the waitlist page has **no link to `datenschutz.html`** — it states the responsible party and a mailto (`:740–741`) instead. See Sprint 4. |
| **Error handling** | API failure/timeout/offline/duplicate submit/invalid email handled | API failure and invalid email handled (`:820–822`, `:880–895`); offline via `catch`; timeout not explicit; no spam/rate-limit. |
| **Empty states** | No social-proof/changelog placeholders; sensible fallbacks | Empty ticker slots hidden; no empty changelog. Partially met (one placeholder team card). |

**Automated vs. manual:** The benchmark notes Lighthouse helps but does not replace manual keyboard/screen-reader/zoom testing. `AGENTS.md` and the generative implementation plan describe a dev-only CDP screenshot harness (reduced-motion, 375/768/1440, DE/EN) but **no automated a11y/perf test runner exists in the repo** (no CI, no test runner, per `AGENTS.md`). The `_screenshots/` directory contains visual-check artifacts only.

---

## 3.11 Technical quality / code-health items relevant to UX

- **Dead code:** the accordion implementation (`js/site.js:42–64`; `css/experimental.css:1673–1682`) is mounted on no page (Sprint 1 §1.12). The generative `registry.js:3` references a `kernel-loop` module directory that does not exist. Neither causes a runtime error today.
- **Duplicated header/footer/language logic** across pages and a second inline language implementation in `waitlist.html` (Sprint 2 §2.13) increase the chance of visual/behavioral drift; `waitlist.html` already looks structurally different from the rest of the site (own stylesheet tokens, green `#4FAC4E` vs the shared palette, own footer).
- **`disce-kernel-architecture.html` / `.json`** exist at repo root but are untracked (`git status`), so they are not part of the served site; the Kernel page embeds a hand-built inline SVG instead (`kernel.html:142–220`).
- **No `<main>` landmark** on `index.html`, `philosophy.html`, `kernel.html`, `team.html`, `status.html`, `beta.html`, `impressum.html`, `datenschutz.html` (only `waitlist.html` has one).
- **Bilingual markup risk:** `data-lang` spans are toggled via `display:none`/`revert` (`css/experimental.css` language-toggle block, `waitlist.html:424–426`). Both languages are in the DOM simultaneously; the inactive language is `display:none`. This is workable but means screen readers encounter hidden duplicated content only if display handling fails.

---

## 3.12 Sprint 3 summary of notable findings

**Strengths (matching or exceeding the benchmark):** coherent, token-driven visual system; visible focus states site-wide; reduced-motion support in three CSS contexts plus the generative loader; no-JS fallback for generative visuals; zero third-party scripts/analytics; well-optimized responsive AVIF/WebP imagery within the repo's budgets; form uses real labels, 16 px inputs, autocomplete and 48 px buttons; no scroll hijacking, no autoplay video, no aurora gradients.

**Principal gaps:** (1) no real product evidence or product depiction anywhere (a benchmark Must-have); (2) no programmatic error/status announcement (`aria-invalid`/`aria-describedby`/`aria-live`) in the core conversion form; (3) an endless logo ticker is present (benchmark "use carefully"), has no pause control despite the repo's own rule, and carries a contested trust claim; (4) fonts are not preloaded and `waitlist.html` duplicates font declarations; (5) no documented measurement of Core Web Vitals, contrast, keyboard traversal, or device testing; (6) missing `<main>` landmarks; (7) the waitlist page is visually and structurally detached from the shared design system; (8) dead accordion code and a dangling generative registry entry.

**Critical flags:** None added in this sprint. No inaccessible-core-form gross violation was proven: the form is keyboard-operable, labelled, and has visible textual errors; the missing attribute-level announcement is a real WCAG-oriented gap but not a total inaccessibility. Core Web Vitals could not be measured in this pass, so no performance failure is asserted.
