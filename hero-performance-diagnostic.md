# Hero Performance Diagnostic — Public Homepage (`index.html`)

**Status:** diagnostic only. **No optimization was implemented.** No repository file other than this document was created; nothing was staged, committed, moved, renamed, or deleted.

**Date:** 2026-09-21
**Scope:** `index.html` and the CSS / JS / images / fonts / generative visuals actually involved in the initial above-the-fold hero render.
**Authority:** source in the working tree (post Batch D/E) + a local, cold-cache, headless render (Firefox 156 WebDriver BiDi). No deployed field/lab trace was available.

### Evidence labels used below
- **[VERIFIED]** — established directly from tracked source or file bytes.
- **[LOCAL-MEASUREMENT]** — measured in this environment (localhost, cold cache, headless Firefox 156). Indicative only, **not** deployed/field data.
- **[HYPOTHESIS]** — inferred from source; needs a real deployed-browser trace to confirm.
- **[NEEDS-TRACE]** — cannot be decided without a deployed Chrome/DevTools trace.

---

## 0. Summary

The hero background image is almost certainly the LCP element on desktop **[LOCAL-MEASUREMENT + HYPOTHESIS]**. Locally it is fast (localhost, no throttling), but the homepage cold start loads a large amount of **non-critical bytes in parallel with the hero**: ~**834 KB of self-hosted fonts**, a **130 KB render-blocking stylesheet**, and several **decorative / below-the-fold images that load eagerly** (~**1.1 MB** of portrait, botanical, brand-mark and partner-logo images). Under real network latency these compete with the LCP image and the hero fonts, which is the most plausible reason the deployed hero *feels* slow while localhost looked fast.

Top hypotheses, in order (all **[HYPOTHESIS]** until traced):
1. **Bandwidth contention from eager non-hero images** (portrait layer, botanical wash, partner logos, brand mark).
2. **Large font payload** (≈834 KB) with only one face preloaded; the body/UI face (Inter, 348 KB) is not preloaded.
3. **Render-blocking 130 KB stylesheet** (uncompressed in-repo; hosting compression unknown) delaying first paint.
4. **Generative dot-field + grain overlay** adding main-thread/paint work to the hero after load.
5. **Hosting/TTFB** on GitHub Pages.

---

## 1. Exact initial hero render path **[VERIFIED]**

### 1.1 Head (parser, blocking and early)
- `index.html:6` — `<meta name="robots" content="noindex, nofollow">` (staging; not a perf factor).
- `index.html:9` — tiny inline language script (blocking, trivial).
- `index.html:10` — `<link rel="stylesheet" href="css/experimental.css">` — **single render-blocking stylesheet**, **130,266 bytes** on disk.
- `index.html:11–14` — PERF-01 preload of the hero headline face `fonts/newsreader-roman-var.woff2` (215,344 B).
- `index.html:15–18` — icons + `site.webmanifest`.
- `index.html:19–29` — canonical/OG/Twitter metadata.

### 1.2 Hero DOM (`index.html:70–106`)
- `index.html:70` — `<section class="hero">`.
- `index.html:71–77` — `<picture class="hero-bg">` with:
  - AVIF `<source sizes="100vw">` `index.html:72–73`,
  - WebP `<source sizes="100vw">` `index.html:74–75`,
  - `<img src="images/DISCE_C01_r1_arena-stag-bordeaux.png" … loading="eager" fetchpriority="high" decoding="async" width="1376" height="1024">` `index.html:76`.
- `index.html:78` — `<div class="dot-field dot-field--hero dot-field--hero-dark" data-gen="dot-field" … aria-hidden="true">` (generative mount). **Note: no `hidden` attribute** (see §4.5).
- `index.html:79` — `.wrap.hero-grid`.
  - `index.html:80` — `.eyebrow`; `index.html:82` — `<h1>` (Newsreader roman, `css/experimental.css:384–391`).
  - `index.html:83` — `.lede`; `index.html:84–87` — `.hero-actions` (primary CTA → `waitlist.html`).
  - `index.html:88–91` — `.glass-card.glass-testimonial`; `index.html:93–…` — `.hero-panel` stat rows.
- Styling: `.hero` `css/experimental.css:320–327` (`position:relative; overflow:hidden; isolation:isolate`); `.hero-bg` (absolute, inline LQIP background) `:329–341`; `.hero-bg img` `:342–347`; `.hero::before` scrim gradients `:350–356`; `.hero::after` film grain `:357–361`; `.hero h1` `:384–393`; `.hero .eyebrow`/`.lede` `:400–403`; `.hero-actions` `:405`; `.hero .glass-card` `:437–447`; `.hero .hero-panel` `:449–460`.
- Responsive hero: `css/experimental.css:492–507` (single-column, `--hero-band` 340 px), `:2059–2063` (`--hero-band` 280 px), `:3104` (`.dot-field--hero { display:none }` ≤768 px).

### 1.3 Page-level decorative layers (paint behind the hero)
- `index.html:39–41` — `.portrait-layer` with two eager `<img>`: `img.goethe.png` (`:40`) and `img.wittgenstein.png` (`:41`). CSS `css/experimental.css:1971–1988`: `position:fixed; inset:0; z-index:0`; imgs 360 px wide, `opacity:0.12`, `filter: grayscale(100%)`; **`display:none` ≤1100 px**.
- `css/experimental.css:3006–3016` — `body::after` fixed botanical wash `background-image: var(--botanical-image)` at `opacity: 0.25`, `z-index:-1`.
  - `css/experimental.css:2970–2974` — base `body` value `greenery-horizon-watertower-2560.webp`.
  - `css/experimental.css:2975–2979` — homepage override `body:has(.hero)` → `greenery-conservatory-moon-1254.webp`.

### 1.4 JavaScript initializers
- `index.html:333` — `<script src="js/site.js">` (3,131 B, classic, runs on `DOMContentLoaded`): mobile nav, ticker duplication, ticker pause control, language switching (`js/site.js:1–104`). The ticker duplication loop (`js/site.js:30–40`) touches the below-the-fold ticker.
- `index.html:334` — `<script type="module" src="js/generative/loader.js">` (deferred). Loader (`js/generative/loader.js:29–48`) queries `[data-gen]`, lazily imports the registry module, mounts each visual, then unhides it.
  - First import chain: `js/generative/registry.js` → `dot-field/index.js` (4,599 B) → `composition.js` (3,457 B), `reactive.js` (3,023 B), `../tokens.js` (958 B), `prng.js` (1,213 B). ≈ 15.5 KB uncompressed.
  - `dot-field/index.js:20–47` creates a `<canvas>`, adds `.is-gen-active`, sizes it to the mount, and (motion allowed) starts a `requestAnimationFrame` loop; DPR capped at 2. Cycle `--gen-cycle: 26s` (`css/experimental.css:128`).
  - Reduced-motion: `loader.js:18–27` + `dot-field/index.js:26` leave the static CSS plate; `.ticker-track` animation disabled (`css/experimental.css:1727`).

### 1.5 Fonts **[VERIFIED]**
`css/experimental.css:13–42` declares four self-hosted faces, all `font-display: swap`:
| Face | File | Bytes | Used above the fold on index? |
|---|---|---|---|
| Archivo Black 400 | `fonts/archivo-black-400.woff2` | 30,708 | not hero; light-section headings/footer |
| Inter 400–800 | `fonts/inter-var.woff2` | **348,704** | yes (eyebrow, lede, CTA, nav, panel) |
| Newsreader italic 500 | `fonts/newsreader-italic-var.woff2` | 239,620 | below fold (pull-quotes) |
| Newsreader roman 200–800 | `fonts/newsreader-roman-var.woff2` | 215,344 | yes (hero `<h1>`), preloaded |

Total font bytes available to a cold homepage load ≈ **834,376 B**.

---

## 2. Resource inventory (cold homepage load)

Sizes are exact file bytes **[VERIFIED]**. Discovery/priority columns are source-derived **[VERIFIED]**; the "loaded early?" column is from the local trace **[LOCAL-MEASUREMENT]**.

| Resource | Type | Bytes | Discovered via | Parser-discoverable | loading / priority | Above fold? | Loaded early (local trace) | May block first render / LCP |
|---|---|---|---|---|---|---|---|---|
| `css/experimental.css` | CSS | 130,266 | HTML `:10` | yes | render-blocking | yes | yes (start 69/32 ms) | **yes — blocking** |
| `fonts/newsreader-roman-var.woff2` | font | 215,344 | preload `:14` + `@font-face` `css:41` | yes | preload | yes (h1) | yes | LCP text paint |
| `fonts/inter-var.woff2` | font | 348,704 | `@font-face` `css:20–26` | after CSS | auto | yes | yes (start 215 ms) | LCP text paint |
| `fonts/newsreader-italic-var.woff2` | font | 239,620 | `@font-face` `css:27–33` | after CSS | auto | no | yes (start 215 ms) | contended bytes |
| `fonts/archivo-black-400.woff2` | font | 30,708 | `@font-face` `css:13–19` | after CSS | auto | no | yes (start 215 ms) | contended bytes |
| Hero AVIF 1376/1280/768 | image | 78,985 / 67,606 / 21,188 | HTML `<picture>` `:71–76` | yes | `loading=eager fetchpriority=high` | yes | yes | **likely LCP** |
| Hero WebP (alt source) | image | 95,878 / 78,456 / 26,050 | HTML `<picture>` | yes | eager | yes | not fetched when AVIF supported | fallback only |
| Hero PNG fallback | image | **2,256,186** | `img@src :76` | yes | eager | yes | not fetched when AVIF supported | only legacy UA |
| `.hero-bg` inline LQIP | data URI | 132 B (file) / inline | CSS `:331` | after CSS | n/a | yes | inline | no request |
| `images/derived/dot-bloom-ochre.png` | image | 2,780 | CSS `css:3072` | after CSS | auto | yes (hero dot field, opacity .4) | yes (start 50 ms) | paint |
| `images/goethe.png` | image | **522,801** | HTML `:40` | yes | eager (no `loading`) | hidden ≤1100 px; decorative | yes (start 69 ms) | **wasted bytes** |
| `images/wittgenstein.png` | image | 122,279 | HTML `:41` | yes | eager | decorative | yes | wasted bytes |
| `images/antlers-green.png` | image | 63,475 | HTML `:47` (brand mark) | yes | eager | yes (header) | yes | paint |
| botanical `greenery-…-2560.webp` | image | 140,026 | CSS `css:2972` (`body::after`) | after CSS | auto | behind page | yes (desktop, start 37 ms) | paint; see §4.10 |
| botanical `greenery-…-1254.webp` | image | 242,564 | CSS `css:2977` (`body:has(.hero)`) | after CSS | auto | behind hero | not observed locally | see §4.10 |
| `images/paper-grain.webp` | image | 13,716 | CSS `css:93,293` | after CSS | auto | low-opacity | yes (start 138 ms) | minor |
| `images/partners/stromgold-logo.png` | image | 29,255 | HTML `:280` | yes | eager (no `loading`) | below fold | yes (start 70 ms) | wasted bytes |
| `images/partners/potsdam-startup-service.jpg` | image | **171,664** | HTML `:281` | yes | eager | below fold | yes | wasted bytes |
| `images/partners/gruenden-in-brandenburg.jpg` | image | 34,433 | HTML `:282` | yes | eager | below fold | yes | wasted bytes |
| `js/site.js` | JS | 3,131 | HTML `:333` | yes | classic (blocking-parse, end of body) | n/a | yes | minor |
| `js/generative/loader.js` | JS module | 1,991 | HTML `:334` | yes | deferred | n/a | yes | main-thread after load |
| dot-field module chain | JS module | ~15,500 | dynamic import | deferred | lazy module | n/a | yes | rAF loop |
| `images/derived/icon-192.png` | image | 26,705 | HTML `:16` | yes | auto | n/a | yes | minor |
| `favicon.ico` | image | 15,086 | HTML `:15` | yes | auto | n/a | yes | minor |
| grain film | data URI SVG | inline | CSS `css:91` | after CSS | n/a | yes (`::after`) | inline | rasterization (§4.6) |

Not requested by `index.html` (context): `fonts/noto-serif-var.woff2` (285,628 B, waitlist page only).

---

## 3. LCP candidates

### 3.1 Hypotheses **[HYPOTHESIS]**
- **H1 — hero background image (`img` inside `.hero-bg`, AVIF).** Largest above-the-fold paint area; it is the natural LCP element at wide viewports.
- **H2 — hero `<h1>` (“Sag, was Du meinst.”).** Large text; can be LCP on narrow viewports or if the image is slow.
- **H3 — hero section paint** (scrim + grain + dot field) at very narrow widths where `.hero-bg` is only 280–340 px tall.

### 3.2 Local cold-cache observation **[LOCAL-MEASUREMENT]**
Headless Firefox 156, fresh profile, localhost, no throttling:
- **1440×900:** LCP element = `img` → `…/DISCE_C01_r1_arena-stag-bordeaux-1376.avif`, `startTime` 63 ms, `renderTime` 63 ms, painted size 1,165,248 px². → **supports H1 on desktop.**
- **390×844:** LCP element = `section.hero`, url = the inline `feTurbulence` grain data URI, `startTime` 340 ms, size 287,280 px². → suggests the hero’s **composite/grain paint** is the largest late candidate on mobile (H3), and that the hero image alone was not the mobile LCP. Firefox LCP attribution differs from Chrome, so treat as indicative only.

**A real deployed Chrome trace is still required** to identify the LCP element and its timing under throttling. **[NEEDS-TRACE]**

---

## 4. Likely causes of a slow perceived hero (classified)

### 4.1 TTFB / hosting **[HYPOTHESIS]**
Hosted on GitHub Pages; `CNAME` = `stage.weltvorstellung.de`; `.nojekyll` present; **no** `_headers`/`netlify.toml`/`vercel.json`/CI in the repo. Cache-control/compression are hosting-managed and unknown from source. Confirm TTFB and compression in the deployed trace.

### 4.2 Resource load delay **[VERIFIED source + HYPOTHESIS impact]**
- The hero `<img>` is parser-discoverable and `fetchpriority="high"` (`index.html:76`) — good.
- **But many non-hero assets are also discovered immediately and eagerly:** `.portrait-layer` PNGs (`index.html:40–41`, no `loading`), brand mark (`:47`, no `loading`), and all three partner logos (`:280–282`, no `loading`), plus four fonts and the botanical/CSS background images. On a constrained connection this delays the hero image/font download.

### 4.3 Resource download duration **[VERIFIED bytes]**
- Hero AVIF ≤ 78,985 B — reasonable.
- **Over-weight peers:** `potsdam-startup-service.jpg` 171,664 B; portrait PNGs 522,801 + 122,279 B; botanical webp 140,026 / 242,564 B; hero PNG fallback 2,256,186 B (legacy UA only).

### 4.4 Render delay / CSS blocking **[VERIFIED source]**
One render-blocking stylesheet of **130,266 B**, uncompressed in-repo, covering the whole site (not split critical/hero). Parse/style cost is highest on low-end mobile.

### 4.5 JavaScript / main-thread work **[VERIFIED source + HYPOTHESIS]**
- Deferred module loader + dot-field mount creates a **full-hero canvas** and runs a continuous `requestAnimationFrame` loop (`dot-field/index.js:20–47+`), DPR ≤ 2 (`:14`). This is post-load main-thread/compositing work that can hurt responsiveness and perceived smoothness.
- `js/site.js:30–40` duplicates ticker DOM (`track.innerHTML` up to 2×) — below the fold but synchronous on `DOMContentLoaded`.
- **Markup/loader inconsistency [VERIFIED]:** `loader.js:1–4` states “the plate markup ships hidden,” and `loader.js:40` does `el.hidden = false`, but the homepage mount (`index.html:78`) has **no `hidden` attribute** and no `[hidden]` CSS rule exists for `.dot-field`. So the static dot PNG paints **and** is later covered by the canvas (double paint), rather than deferring the static plate until mount.

### 4.6 Generative-visual initialization **[VERIFIED source]**
The hero dot field is decorative (`aria-hidden`), sits at `z-index:2` above the scrim (`css:3066–3073`), `opacity:0.4`, and is replaced by an animated canvas after the module mounts. Two paint passes + animation.

### 4.7 Animation **[VERIFIED source]**
- `.hero::after` film grain is an **inline SVG `feTurbulence` filter** (`css:91`, applied `:357–361`) — turbulence rasterization over the full hero can be costly on low-end devices.
- Dot-field `26s` cycle (`css:128`) and ticker `34s` marquee (`css:1712`).

### 4.8 Font loading **[VERIFIED bytes]**
≈**834,376 B** of fonts on a cold homepage load; only the headline face is preloaded (`index.html:14`). The body/UI face Inter (348,704 B) is not preloaded and is used for the eyebrow/lede/CTA/nav, so a swap/invisible-text window is possible despite `font-display: swap`. Full variable fonts are served (no subsetting evident).

### 4.9 Responsive asset mismatch **[HYPOTHESIS]**
- Hero `<source sizes="100vw">` with derivatives up to **1376 w** while the master is 1376×1024 (`index.html:76`). On large/hi-DPI screens the image is upscaled (quality, not bytes); on ≤390 px the browser chooses the 768 w AVIF (~21 KB) — efficient.
- The `.hero-bg` mobile crop shows the same composition in a 280–340 px band (`css:2059–2063`), so much of the downloaded image is cropped away.

### 4.10 Other — botanical wash variant **[NEEDS-TRACE]**
`body::after` uses `--botanical-image` (`css:3006–3016`); the homepage override is `greenery-conservatory-moon-1254.webp` (`css:2975–2979`), confirmed live **[LOCAL-MEASUREMENT]**. However the desktop local trace fetched **`greenery-horizon-watertower-2560.webp` (140,026 B)**, not the homepage variant, at `startTime` 37 ms. Whether the deployed homepage fetches the base or the `:has(.hero)` variant (or both) needs confirmation; if both load, that is redundant ~382 KB of decorative background.

---

## 5. Ordered remediation menu — *analysis only, do not implement here*

> Each row is a candidate. Nothing below was applied. Validate every change against §6.

| # | Candidate fix | Prerequisites | Risks | Files/lines likely affected | Validation after fix |
|---|---|---|---|---|---|
| R1 | Make below-the-fold/decorative images non-eager: add `loading="lazy" decoding="async"` to partner logos and the portrait-layer imgs (or remove the hidden portrait imgs at ≤1100 px via `media`/`<picture>`), so they do not compete with the hero | Confirm the images are not needed above the fold; confirm mobile `display:none` intent | Visual regression in the ticker/portrait watermark; portrait layer is `position:fixed` and always in viewport, so `loading=lazy` may not defer it on desktop — may need a different technique | `index.html:40–41`, `:280–282`; `css/experimental.css:1971–1988` | Chrome Network waterfall: hero AVIF/fonts start earlier; LCP unchanged-or-better; ticker/watermark visual diff |
| R2 | Preload the LCP image with `imagesrcset`/`imagesizes` mirroring the `<picture>` sources | Exact `srcset`/`sizes` match, or the wrong candidate is fetched | **Wrong preload candidate** on some viewports → duplicate fetch; can also delay fonts | `index.html:11–14` (add), mirror `:71–76` | Network: one hero image fetch (no duplicate), earlier start; LCP element unchanged |
| R3 | Preload or subset the body/UI face (Inter) — or subset all faces | Subsetting needs a build step (currently none); confirm glyph coverage | Adds up to 348 KB to the preload queue; may delay the LCP image; FOUT already mitigated by `swap` | `index.html:11–14`; `css/experimental.css:20–26` | Font is render-critical earlier; LCP not worse; no missing glyphs |
| R4 | Reduce render-blocking CSS: split a small critical hero stylesheet or minify/compress | Build step or manual split; keep single-source parity | FOUC/flash if split wrongly; divergence risk | `css/experimental.css` (whole, 130 KB) | DevTools Coverage + LCP/CLS before/after |
| R5 | Gate/defer the heroic dot-field animation until after first paint/idle or below-the-fold intersection; keep the static plate | Keep static fallback; preserve no-JS/reduced-motion | Visible late paint change; must keep decorative semantics | `index.html:78`, `:334`; `js/generative/loader.js`; `js/generative/dot-field/index.js` | Main-thread/INP + paint timing; visual diff; reduced-motion unchanged |
| R6 | Ship the dot-field plate `hidden` (as the loader contract already documents) so the static PNG is not painted twice | Add `hidden` to the mount(s) and confirm loader unhides on success | If JS fails, the plate stays hidden — verify the fallback still matches the intended section look | `index.html:78` (and other `[data-gen]` mounts) | No-JS and JS render compare; one paint instead of two |
| R7 | Reduce/omit the `feTurbulence` grain on the hero, or rasterize it once to a small tiled raster | Visual sign-off | Subtle texture change | `css/experimental.css:91,357–361` | Paint/CPU profile; visual diff |
| R8 | Investigate the botanical-wash variant: ensure only the `:has(.hero)` image loads | Confirm the correct homepage asset | If both variants load, removing one changes the backdrop | `css/experimental.css:2970–2979,3006–3016` | Network: exactly one botanical request; visual diff |
| R9 | Re-encode/optimise the port-ticker JPG/PNG logos and the portrait PNGs to AVIF/WebP | Pipeline run (`scripts/optimize_images.py`) | Quality drift; new derivatives must be committed | `images/partners/*`, `images/goethe.png`, `images/wittgenstein.png` | Bytes down, visual parity |
| R10 | Add a larger hero derivative for >1376 CSS px @2x (or cap hero display size) | Master resolution; pipeline widths | More bytes; may hurt LCP on large screens | `index.html:71–76`; `images/derived/*` | LCP/quality trade-off measurement |
| R11 | Hosting: ensure Brotli/gzip + long-lived cache for `/images` and `/fonts` | GitHub Pages may not allow custom headers — verify platform | Platform constraint | hosting config (not in repo) | Response headers in DevTools; repeat-visit timing |

---

## 6. Live-browser measurement protocol (founder-run, Chrome/Chromium DevTools)

1. **Setup:** serve the deployed site (or the local repo via `python3 -m http.server 8000`). Open DevTools → **Network** → tick **Disable cache**. Device toolbar → **Mobile** (e.g., Moto G Power) with **Fast 3G / Slow 4G** and **4× CPU** throttling.
2. **Record:** DevTools → **Performance** → record → hard reload → stop after the hero is painted (≈5 s). Use **Lighthouse** (`Performance`) as a second opinion with the mobile preset.
3. **Identify the LCP element:**
   - Performance panel → **Timings** track → click the **LCP** marker → the **Elements** panel highlights the LCP element; or
   - Console: `new PerformanceObserver(l=>console.log(l.getEntries().at(-1).element, l.getEntries().at(-1).startTime, l.getEntries().at(-1).size)).observe({type:'largest-contentful-paint',buffered:true})`.
   - Note the element selector, its resource URL, and **LCP time** (target ≤ 2.5 s).
4. **Network priority & timing:** in **Network**, show **Priority** and **Waterfall**; for each candidate record **request start**, **duration**, **transfer size**, **priority**, and whether it is `Highest/High/Medium/Low`. Confirm the hero image and its preload/priority; look for non-hero assets competing.
5. **CLS/INP:** Performance → **Experience** track; Interactions for INP; Layout Shifts for CLS.
6. **Send back:** LCP element (selector/URL), **request start + duration + byte size + priority** for that resource, a **screenshot/waterfall** (export HAR), the device/network/CPU profile, and the **TTFB** of the document. Also send the Network panel filtered to `Img`/`Font`/`Media` for the first 2 s.

---

## 7. Local Firefox WebDriver BiDi harness — what it can and cannot establish

A reproducible local harness exists (Firefox 156 `--headless --remote-debugging-port`, WebDriver BiDi `ws://127.0.0.1:9333/session`, dependency-free Node client, `python3 -m http.server`). It produced the §3.2 observations.

**It can:**
- Load a **cold profile** (true cold cache) and measure `LCP element`, `LCP startTime`, `CLS`, and `resource` timings (`startTime`, `duration`, `encodedBodySize`, order) on **localhost**.
- Verify structural/network facts (which assets are requested, in what order, at what weight) and DOM effects of a change.

**It cannot:**
- Reproduce **real network latency/bandwidth** (no DevTools-equivalent network throttling) or **CPU throttling** in this setup.
- Reproduce **deployed** TTFB/compression/cache behaviour (GitHub Pages), **field data**, or real-device rendering.
- Match **Chrome LCP attribution** exactly (Firefox reported `section.hero`/grain as the mobile LCP candidate vs an `img` on desktop).

**Therefore it does not substitute for deployed/field data.** Use it for cold-cache structure and quick local before/after checks; use §6 for the authoritative deployed trace.

---

## Appendix A — Local trace detail **[LOCAL-MEASUREMENT]**

Cold profile, `index.html`, no throttling (start ms / duration / encoded bytes).

- **390×844:** `experimental.css` 69/49 ms/130,266; `newsreader-roman-var.woff2` 69/49/215,344; `goethe.png` 69/54/**522,801**; `wittgenstein.png` 69/53/122,279; `antlers-green.png` 69/54/63,475; `site.js` 70/48/3,131; `loader.js` 70/50/1,991; hero AVIF 768w 70/51/21,188; `stromgold-logo.png` 70/54/29,255; `potsdam-startup-service.jpg` 70/55/**171,664**; `gruenden-in-brandenburg.jpg` 70/55/34,433; `icon-192.png` 84/173/26,705; `favicon.ico` 85/172/15,086; `paper-grain.webp` 138/4/13,716; `dot-arena-green.png` 139/3/2,473; `archivo-black-400.woff2` 215/7/30,708; `inter-var.woff2` 215/8/**348,704**; `newsreader-italic-var.woff2` 215/8/239,620; then dot-field modules 230–268 ms. **LCP = `section.hero` (grain data URI) @340 ms.**
- **1440×900:** `experimental.css` 32/0/130,266; `newsreader-roman-var.woff2` 32/19/215,344; `site.js` 32/20/3,131; `loader.js` 32/20/1,991; `greenery-horizon-watertower-2560.webp` 37/19/**140,026**; `icon-192.png`/`favicon.ico` 42/36; `dot-bloom-ochre.png` 50/8/2,780; then dot-field modules. **LCP = `img` → `DISCE_C01_r1_arena-stag-bordeaux-1376.avif` @63 ms.**

## Appendix B — Source index (file:line)
- `index.html`: `:6` robots; `:9` pre-paint lang; `:10` stylesheet; `:11–14` font preload; `:39–41` portrait layer; `:44` header; `:47` brand mark; `:67` `<main>`; `:70–77` hero picture; `:76` hero `<img>`; `:78` dot-field mount; `:79–106` hero copy/panel; `:280–282` partner logos; `:333–334` scripts.
- `css/experimental.css`: `:13–42` `@font-face`; `:91` grain film; `:128` `--gen-cycle`; `:293,2970–2979,3006–3016` paper/botanical backgrounds; `:320–405` hero rules; `:437–476` glass/panel; `:492–507,2059–2063` responsive hero; `:1712` ticker keyframes; `:1727` reduced motion; `:1971–1988` portrait layer; `:3032–3104` dot-field; `:3104` mobile dot-field hidden.
- `js/site.js`: `:1–104` (nav `:2–25`, ticker dup `:27–40`, accordion removed, language `:66–103`).
- `js/generative/loader.js`: `:1–54`; `dot-field/index.js`: `:1–136`; `composition.js`, `reactive.js`, `tokens.js`, `prng.js`.
- Assets: `images/derived/DISCE_C01_r1_arena-stag-bordeaux-{768,1280,1376}.{avif,webp}`, `images/DISCE_C01_r1_arena-stag-bordeaux.png` (2,256,186 B), `images/derived/dot-bloom-ochre.png`, `images/{goethe,wittgenstein}.png`, `images/antlers-green.png`, `images/paper-grain.webp`, `images/derived/greenery-*.webp`, `images/partners/*`, `fonts/*.woff2`.
- Deployment/config present: `CNAME` (`stage.weltvorstellung.de`), `.nojekyll`, `robots.txt`, `sitemap.xml`. Absent: `_headers`, `_config.yml`, `netlify.toml`, `vercel.json`, `.github/workflows`.

---

## Pass 1 implementation (post-diagnostic, 2026-09-21)

### PageSpeed-evidence note (deployed homepage)
A Google PageSpeed Insights report for the deployed homepage established: the hero background `<img>` is the **LCP element**; LCP breakdown ≈ **240 ms resource load delay + ≈240 ms download + ≈80 ms render delay**; **~670 KiB** image-delivery savings opportunity; oversized decorative assets `images/goethe.png` ≈511 KiB and `images/wittgenstein.png` ≈120 KiB (each displayed ≈360×360 px) and `images/antlers-green.png` ≈63 KiB (displayed ≈28×28 px); the three partner logos were eager without explicit dimensions; the hero AVIF was already eager + `fetchpriority="high"`.

### Phase 1 — responsive hero AVIF preload [DONE]
- `index.html:19–21` — one `<link rel="preload" as="image" type="image/avif" fetchpriority="high" imagesrcset="…768.avif 768w, …1280.avif 1280w, …1376.avif 1376w" imagesizes="100vw">`, mirroring the hero AVIF `<source>` (`index.html:91–92`) **exactly**. WebP/PNG fallbacks deliberately **not** preloaded. The hero `<picture>` and `<img>` are unchanged (`index.html:90, 95`, still `loading="eager" fetchpriority="high"`).
- **Duplicate-request validation (cold profile, local Firefox BiDi):** exactly **one** hero request at every tested width — 1440 px → `…-1376.avif` with `initiatorType="link"` (the preload response reused by the `<picture>`); 320/375/390/430 px → `…-768.avif`. No WebP/PNG fallback fetched in the AVIF-capable browser. Because the preload carries `type="image/avif"`, non-AVIF browsers skip the hint entirely (no wasted fetch, no duplicate).

### Phase 2 — partner-image deferral + CLS prevention [DONE]
- `index.html:299–301` — the three below-the-fold partner logos now carry `loading="lazy" decoding="async"` **and** intrinsic `width`/`height` (`1953×300`, `1258×429`, `800×305`). Alt text, links, order, framing and ticker behaviour unchanged. (A preceding narrow pass added `loading="lazy" decoding="async"`; Pass 1 added the intrinsic dimensions.)

### Phase 3 — decorative asset modernization [DONE, existing approved pipeline]
- **Pipeline used:** `scripts/optimize_images.py` (masters read-only; writes `images/derived/<stem>-<width>.{avif,webp}` + `-lqip.webp`). Its documented out-of-tree dependency `pillow-avif-plugin` was **not** installed; per `AGENTS.md` it was installed outside the tree (`/tmp/pylibs`) — **no project/vendored dependency, no repo dependency added**.
- **Generated (originals preserved):** `goethe-360/-720`, `wittgenstein-360/-720`, `antlers-green-28/-56` (AVIF + WebP, **alpha preserved** — verified RGBA).
- **Wired in `index.html`** via `<picture>` (AVIF preferred → WebP fallback → PNG last): portraits `index.html:47–56`, brand mark `index.html:62–66`. Decorative semantics preserved (`alt=""`; `aria-hidden` inherited from `.portrait-layer`). Portraits keep 360×360 rendering and the same crop/position/opacity; the brand mark keeps 28×28.
- **One minimal CSS rule** (strictly necessary to preserve layout after wrapping in `<picture>`): `css/experimental.css:252` `.brand picture { display: inline-flex; flex-shrink: 0; }`.

### Exact byte counts before → after
| Asset | Before (PNG) | After AVIF (1× / 2×) | After WebP (1× / 2×) |
|---|---|---|---|
| `goethe` (portrait, 360 px) | **522,801** | 28,743 (360) / 79,820 (720) | 55,502 (360) / 182,718 (720) |
| `wittgenstein` (portrait, 360 px) | **122,279** | 9,530 (360) / 21,916 (720) | 17,438 (360) / 46,510 (720) |
| `antlers-green` (brand, 28 px) | **63,475** | 4,125 (28) / 4,613 (56) | 750 (28) / 1,838 (56) |

(Each also emits a `-lqip.webp` by pipeline convention: goethe 508 B, wittgenstein 356 B, antlers-green 554 B; not referenced.)

### Local cold-cache eager-byte / order differences
- **390 px cold:** total fetched image bytes (`.png/.jpg/.avif/.webp`) **1,007,989 → 106,480 B (−901,509 B ≈ −880 KiB)**.
- **Partner logos:** no longer fetched before scroll (previously 235,352 B eager).
- **Hero request start:** 70 ms → 18 ms (localhost, indicative only).
- **1440 px cold (after):** total fetched image bytes 409,621 B (incl. the unchanged botanical wash `greenery-conservatory-moon-1254.webp` 242,564 B).

### Scope and limitations
- Local Firefox BiDi only — **not** deployed/field data. No deployed LCP target is claimed; the local harness cannot emulate real network/CPU throttling or GitHub Pages TTFB/compression.
- **Mobile portraits:** `.portrait-layer` remains `display:none` ≤1100 px, but `display:none` does **not** suppress `<img>` fetching, so mobile still requests one AVIF per portrait (now 38,273 B total vs 645,080 B of PNGs). No duplicate requests. Suppressing the fetch entirely would need JS or a CSS-background architecture change (out of Pass 1 scope).
- Untouched: hero copy/composition, forms, JS/generative visuals, grain/dot-field/ticker, fonts/preloads, legal pages, robots/sitemap/canonical/OG, cache headers, CSS architecture, partner framing.

### Follow-up instruction
**Re-run PageSpeed Insights on the deployed site after this commit before considering R5/R7/R8 or CSS/font architecture changes.** Manual checks: deployed PageSpeed rerun; desktop portrait visual check; mobile hero + partner-section check.

---

## Hero Performance Pass 2a — deferred decorative hero dot-field (2026-09-21)

**Nature:** a targeted **main-thread / initial-paint mitigation** for the homepage hero. It is **not** a claimed deployed LCP fix; deployed PageSpeed Insights must be re-run after commit.

**Change (one file):** `js/generative/loader.js`. The decorative `.dot-field--hero` mounts (identified by the existing hero class) are no longer imported/mounted during the initial DOMContentLoaded pass. The static CSS dot plate remains the immediate visual; the animated canvas is a deferred enhancement. **No `hidden` attribute was added** and no markup/CSS changed, so the hero is never blank while JS loads.

### Scheduling strategy (final)
1. **Wait for `window.load`** if the document is not already `complete` (`load` listener, `{ once: true }`).
2. Then schedule with **`requestIdleCallback(callback, { timeout: 1500 })`**.
3. If `requestIdleCallback` is **unavailable**, fall back to **`setTimeout(callback, 1500)`**.
4. Both paths are **bounded by `HERO_IDLE_TIMEOUT_MS = 1500 ms`** — the enhancement is never deferred indefinitely.
5. Inside the deferred callback, **skip if the viewport is ≤768 px** (matches the CSS `@media (max-width: 768px) { .dot-field--hero { display:none } }`), so no hidden work is done on mobile.
6. **No hero mount scheduled when no hero element is present.**
7. A module-level **`WeakSet`** guard prevents duplicate mounting if the loader runs more than once.
8. **Non-hero mounts** (e.g. `.dot-field--focal`) keep their existing immediate behavior; **reduced-motion**, no-JS fallback, registry semantics, canvas cleanup and error handling are unchanged. Module import/mount still flows through the same `registry` and `mount()` contract.

**Why 1500 ms:** long enough that the deferred work lands after first paint/interactivity on a loaded page, short enough to be a prompt enhancement; it is a ceiling only — `requestIdleCallback` normally fires much earlier.

### Validation (local Firefox 156 WebDriver BiDi; cold profile; **not deployed data**)
- **Desktop 1440 (`index.html`):** at DOMContentLoaded the hero canvas count is **0** and `is-gen-active` is **false** (static plate visible); the hero canvas is first observed at **≈195 ms** and exactly **one** exists afterwards (`is-gen-active` true). No duplicate canvas. **CLS = 0.** No console errors.
- **Hero-only page (`datenschutz.html`) 1440:** at DOMContentLoaded canvas 0 / not active; after load+idle exactly one canvas. The **module import itself is deferred** — `dot-field/index.js` resource start **79 ms**, after DOMContentLoaded at **54 ms**.
- **Mobile 390:** `index.html` → hero canvas **0**, `is-gen-active` false (static correct); `.dot-field--focal` still mounts (canvas 1). `datenschutz.html` (hero-only) → hero canvas **0** and **no `dot-field/index.js` import at all** (`moduleImported: false`), confirming the hidden hero mount triggers no module work on mobile.
- **Reduced motion (`?gen-motion=off`, same `motion:false` code path):** hero canvas **0**, `is-gen-active` false — static/non-animated behavior preserved (the module leaves the plate untouched).
- **Regression:** other generative mounts still operate (`.dot-field--focal` canvas present on `index.html` and `status.html`; `status.html` hero deferred then mounted, canvas 1). No-JS/static state is demonstrated by the pre-idle DOM (canvas absent, CSS plate visible). Hero image request/preload unchanged — `index.html` still makes exactly one hero request (`…-1376.avif`).

### Local before/after timing (observed only; indicative)
- Pre-change, every `[data-gen]` mount ran during the DOMContentLoaded pass, so the hero canvas was created as soon as the module resolved. Post-change, the hero canvas is **absent at DOMContentLoaded** and appears only after load+idle (**≈195 ms locally**).
- On `index.html` the `dot-field` module import remains early (**57 ms**) because the below-fold `.dot-field--focal` mount still imports it immediately (unchanged); the **hero canvas creation** is what is deferred. On hero-only pages the **import itself** is deferred (79 ms) and skipped entirely on mobile.
- Localhost compresses the window (load completes in ~100 ms); on a real network the load gate moves later, widening the deferral.

### Limitations / remaining manual verification
- Local harness only; no deployed performance claim. **Re-run PageSpeed Insights after commit.**
- `prefers-reduced-motion` was exercised via the loader's `?gen-motion=off` hook (identical `motion:false` path); real OS-level reduced-motion emulation was not available in this harness.
- Viewport growth mobile→desktop after load does **not** mount the hero enhancement in this pass (no resize observer, by design); a normal reload mounts it at desktop width.
- Manual: confirm the hero static plate is visible before the canvas appears on a real device, and that the canvas fades in without a visible jump.


---

## Hero Performance Pass 2b — dot-field offscreen-opacity fix (2026-09-22)

**Symptom:** the page feels slow/stuttery while the hero is on screen; smooth once scrolled past it. Because the dot-field animation pauses via `IntersectionObserver` when off screen, the top-of-page slowness tracked exactly with the hero being visible. The prior attempts (Pass 1/2a) addressed load and scheduling but not this steady-state cost.

**Root cause (measured, Firefox 156 WebDriver BiDi, localhost, 1440×900):**
The animated canvas sits inside a mount with `opacity: 0.4` (`.dot-field--hero-dark`, `.dot-field--focal`). A mount opacity < 1 makes the browser render the element and its animating canvas into an **offscreen blend group that is re-rasterised every frame**. With the hero field animating, `requestAnimationFrame` intervals at the top of the page averaged **97.6 ms (~10 fps)**; scrolled past the hero (field paused) they were **17.4 ms (~57 fps)**.

Frame-interval isolation at the top of the page:

| Variant | mean frame | reading |
|---|---:|---|
| baseline (animation on) | 107.9 ms | ~9 fps |
| animation off (`?gen-motion=off`) | 16.7 ms | ~60 fps |
| canvas `display: none` (JS still runs) | 16.7 ms | composite-bound, not JS |
| canvas `will-change: transform` | 74.3 ms | partial |
| mount `will-change: transform` | 69.1 ms | partial |
| mount `contain: paint` | 56.3 ms | partial |
| **mount `opacity: 1`** | **16.7 ms** | the offscreen opacity group is the cost |

A single JS `draw()` was separately measured at only ~5 ms (DPR 2) — so the bottleneck was compositing, not the draw loop.

**Fix (CSS only, one source file + its minified twin):** carry the mount's `0.4` strength in the dot colours and drop the offscreen blend group while the canvas is live; the static plate keeps the mount opacity, so the look is unchanged.
- `css/experimental.css` — `.dot-field--hero-dark`: `--dot-color-a/b` → `rgba(...)` at 0.4; added `.dot-field--hero-dark.is-gen-active { opacity: 1 }`.
- `css/experimental.css` — `.dot-field--focal`: added `--dot-color-a/b` `rgba(...)` at 0.4; added `.dot-field--focal.is-gen-active { opacity: 1 }`.
- `css/experimental.min.css` — both edits mirrored.

No JS, markup, image, token, or algorithm change. The pulse, the static plate, reduced-motion, no-JS fallback, pointer reactive mask and offscreen/hidden pausing are all unchanged.

**Result (re-measured, same harness):**

| Condition | before | after |
|---|---:|---:|
| @top, static (hero visible) | mean 97.6 ms / max 117 ms | **mean 16.66 ms / max 17.1 ms** |
| scroll @top | mean 118.5 ms / max 299 ms | **mean 16.67 ms** |
| canvas active | yes | **yes (pulse preserved)** |

Visual check: a rendered hero crop confirms the ochre halftone still reads at the same strength.

**Limitations:** local headless Firefox only (software compositing), not deployed/field data; a deployed PageSpeed/Lighthouse rerun is still the authority. The same offscreen-opacity pattern was the only field configuration found; the light `.dot-field--hero` already used full opacity and needed no change.
