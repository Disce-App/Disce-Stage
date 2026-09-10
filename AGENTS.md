# AGENTS.md — Disce Stage

Repository-specific instructions for coding agents working in this repo.

## Stack

- Static HTML5 pages at the repository root (`index.html`, `philosophy.html`, `team.html`, `status.html`, `waitlist.html`, `impressum.html`, `datenschutz.html`).
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

## Accessibility guardrail

Preserve keyboard access, visible focus states, and WCAG AA contrast.

## Ask first

Ask before making assumptions that affect product behavior, content,
legal/privacy, or deployment.
