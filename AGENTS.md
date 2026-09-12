# AGENTS.md — Disce Stage

Repository-specific instructions for coding agents working in this repo.

## Stack

- Static HTML5 pages at the repository root (`index.html`, `philosophy.html`, `team.html`, `status.html`, `beta.html`, `waitlist.html`, `impressum.html`, `datenschutz.html`).
- `beta.html` is a minimal closed-beta placeholder built from the shared header/footer and `css/experimental.css`. It is **not linked from the navigation yet**; deciding and wiring up routing/links is a future task, so do not add links to it without explicit approval.
- One shared stylesheet: `css/experimental.css`. `waitlist.html` carries its own inline styles.
- Vanilla JavaScript: `js/site.js`, plus inline scripts in `waitlist.html`.
- No build system, package manager, framework, test runner, or CI. There is nothing to install or compile.

## Local preview

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. Serve from the repository root; there is no build step.

## Binding design reference

`DESIGN-BRIEF.md` is the binding reference for all visual design and front-end
implementation. Read it before any design task.

## Scope guardrail

Do not change product copy, headlines, CTAs, claims, translations, legal copy,
or content unless explicitly instructed.

## Dependency guardrail

Do not add dependencies, package managers, build tooling, CDNs, analytics, or
third-party services without explicit approval. Assets and fonts stay
self-hosted.

## Git guardrail

- One bounded task per commit.
- Never force-push.
- Do not commit generated files, local server artifacts, or secrets.
- Stage only files you can clearly identify as belonging to the current task.

## Image guardrail

Use only assets already committed to the repository. Do not generate, download,
or substitute images without explicit approval.

## Image pipeline

`scripts/optimize_images.py` is the single image pipeline. It reads a master from
`images/` and writes responsive derivatives into `images/derived/`.

- **Masters are read-only.** Never edit or overwrite files in `images/`; crops and
  resizes live only in the generated derivatives.
- Run it with Pillow + `pillow-avif-plugin` installed *outside* the tree (not
  vendored, no project dependency):
  `PYTHONPATH=/tmp/pylibs python3 scripts/optimize_images.py images/<master>.png --kind hero --widths 768,1280,1824`
- Outputs AVIF (primary) + WebP (fallback) at the requested widths, plus a ~24 px
  WebP LQIP placeholder. Never upscales past the master width.
- Crop options (masters stay untouched): `--crop-inset PCT` removes a symmetric
  printed paper-mat border; `--crop-box left,top,width,height` takes an explicit
  region; `--no-native` skips the appended master width for oversized sources;
  `--background #RRGGBB` flattens image transparency over a colour (default: site paper).
- Budgets and asset classes follow `DESIGN-BRIEF.md` §9: `--kind hero` ≤ 250 KB
  AVIF, `--kind card` ≤ 120 KB AVIF at the largest width.
- **Derivatives are committed.** GitHub Pages serves the tracked tree as-is with
  no build step, so `images/derived/` must be staged alongside the HTML/CSS that
  references it.

## Preview screenshots

`_screenshots/` is a local, untracked preview directory for rendered screenshots
and visual checks. It is excluded via `.git/info/exclude` and must never be
committed; keep the tracked tree clean.

## Accessibility guardrail

Preserve keyboard access, visible focus states, and WCAG AA contrast.

## Ask first

Ask before making assumptions that affect product behavior, content,
legal/privacy, or deployment.
