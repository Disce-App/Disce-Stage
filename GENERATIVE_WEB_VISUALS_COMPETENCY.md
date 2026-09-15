# Generative Web Visuals — OpenCode Competency Source

**Purpose:** Project-local operating guidance for AI-assisted generative coding in a production website.

**Intended use:** Keep this document in the repository root as `GENERATIVE_WEB_VISUALS_COMPETENCY.md`. Add the short rule below to the root `AGENTS.md` so OpenCode explicitly reads it before it changes generative visual code.

> **Important:** A root Markdown file is *not* automatically injected into every OpenCode session. `AGENTS.md` is the always-on project instruction file. OpenCode’s official documentation recommends using project rules in `AGENTS.md` and can be instructed there to read additional, detailed source files only when relevant. Its native Skills mechanism is loaded on demand from `.opencode/skills/<skill-name>/SKILL.md`.[web:364][web:359]

---

## Root `AGENTS.md` addition

Paste this concise block into the project-root `AGENTS.md`:

```md
## Generative web visuals

Before planning, implementing, refactoring, or reviewing Canvas, SVG, CSS motion, WebGL, Three.js, shader, particle, procedural-illustration, scrollytelling, or animation code, read `GENERATIVE_WEB_VISUALS_COMPETENCY.md`.

Treat visual quality, semantic HTML, accessibility, responsive behavior, performance, and cleanup as equal acceptance criteria. Do not add a generative effect merely because it looks impressive. First state its user, product, or brand purpose; if none exists, propose a simpler static or CSS/SVG alternative.
```

Do **not** paste this whole document into `AGENTS.md`: that would consume every session’s context, including backend and non-visual tasks. OpenCode supports modular instruction sources and on-demand project skills specifically to avoid that unnecessary context load.[web:359][web:364]

---

## Operating Contract

### Objective

Build distinctive, responsive, production-safe browser visuals from code rather than externally embedded image or video assets. Suitable outcomes include:

- Procedural hero illustrations and brand landscapes.
- Ambient backgrounds with low visual and battery cost.
- Interactive particles, flow fields, diagrams, and product metaphors.
- SVG or Canvas hand-drawn illustration systems.
- Data-bound network views and explanatory product demos.
- Scroll-linked narrative scenes only when the animation improves understanding.

The target is **not** a generic “AI website.” Every visual system must make a specific product, story, or brand quality more legible.

### Mandatory first questions

Before implementation, answer these questions in the plan:

1. What user understanding, decision, or perceived brand quality should this visual improve?
2. Is it decorative, informative, or interactive?
3. What is the quiet, static, and JavaScript-free fallback?
4. Which rendering technology is the simplest appropriate one?
5. Which target devices, browsers, viewports, and input modes matter?
6. What are the measurable performance and accessibility acceptance criteria?
7. What deterministic seed, time control, and visual test strategy make the output reproducible?

If requirements do not answer these questions, ask targeted questions or propose conservative defaults. Do not invent a product narrative.

---

## Technology Selection

Choose the smallest rendering surface capable of the actual requirement.

| Requirement | First choice | Use instead only when justified | Avoid |
|---|---|---|---|
| Button, card, menu, state transition | CSS / Web Animations | Motion/GSAP for complex sequencing | Canvas or WebGL |
| Icon, diagram, line illustration, accessible infographic | SVG + semantic HTML | Canvas for very high primitive counts | Encoding essential text only as paths |
| Asset-free 2D hero, grain, trails, many dynamic lines | Canvas 2D | WebGL/PixiJS after profiling proves Canvas is insufficient | Unbounded full-resolution Canvas |
| Many GPU-instanced sprites or filtered 2D objects | PixiJS/WebGL | Canvas for modest counts | DOM node per particle |
| 3D products, camera, real-time material/shader effects | Three.js/WebGL | WebGPU as progressive enhancement | WebGL for a simple gradient or DOM motion |
| Data visualization | D3 for scales/layout + SVG or Canvas renderer | WebGL for very large point clouds | Aesthetic simulation without an accessible data view |
| Physics/collisions | Matter.js only if physical behavior is meaningful | Simple tween or custom constrained motion | Unpredictable physics in critical UI |
| Advanced GPU compute/simulation | WebGPU with an explicit baseline fallback | WebGL if broadly sufficient | WebGPU as the only implementation path |

Canvas is a bitmap drawing surface and does not expose its drawn content to assistive technologies as semantic HTML does. Core information, links, controls, and data must remain available in the DOM.[web:256]

---

## Design Rules

### Art direction before implementation

Translate subjective direction into measurable parameters.

| Dimension | Define explicitly |
|---|---|
| Brand role | Product metaphor, campaign message, or emotional quality |
| Composition | Focal point, copy-safe zone, negative space, depth layers |
| Palette | Token names, exact colors, dark/light mode behavior, contrast constraints |
| Form language | Geometry, line endings, corner behavior, symmetry, irregularity |
| Density | Maximum elements, local clustering, empty-space ratio |
| Material | Grain, paper, ink, light, glass, fluidity—plus what must be avoided |
| Motion | Maximum speed, amplitude, frequency, easing, duration, idle rest period |
| Interaction | Pointer/touch/keyboard equivalence, influence radius, reset behavior |
| Responsiveness | Desktop, tablet, mobile composition—not merely a smaller canvas |
| Variation | Seed source, allowed range, curated presets, deterministic test seed |

### Quality bar

- Start from a static composition. It must work before animation begins.
- Use one dominant visual metaphor; avoid mixing particles, liquid, 3D glass, neon, and generative type without a reason.
- Preserve substantial negative space around meaningful copy and calls to action.
- Treat animation as a second layer. It must never be required to understand essential content.
- Use controlled imperfection: small seeded jitter, layered opacity, or variable line width—not arbitrary noise everywhere.
- Prefer local movement over full-screen movement.
- Include rest. Ambient systems should not look equally active forever.
- Do not use custom cursors that delay or obscure the system cursor.
- Do not use scroll hijacking. Native scrolling, accessible anchors, and normal back-navigation take precedence.

### Useful visual primitives

- **Flow field:** a vector direction varies smoothly over space; many lines or particles follow it.
- **Seeded pseudo-randomness:** variation derives from one stable seed, enabling repeatable output.
- **Noise / FBM:** smoothly correlated irregularity; use frequency, octaves, and amplitude as named tokens.
- **Bézier curves:** controlled organic linework and path animation.
- **Sine/cosine with phase offsets:** calm periodic movement and wave-like fields.
- **Layered alpha / blend modes:** density, light, grain, and depth; test contrast beneath text.
- **Distance fields:** subtle reaction to pointer, touch, or focal points without per-element ad hoc rules.
- **Instancing:** many repeated GPU primitives without many DOM nodes or draw calls.

---

## Performance Contract

### Default budgets

These are conservative starting points, not universal guarantees. Keep project-specific budgets in the component’s acceptance criteria.

| Constraint | Content/SaaS default | More expressive campaign ceiling |
|---|---:|---:|
| Additional visual JavaScript | ≤ 80 kB gzip | ≤ 180 kB gzip |
| Canvas DPR cap | 1–1.5 on mobile, max. 2 desktop | max. 2, adaptive |
| Ambient target FPS | 20–30 | 30–60 only where interaction justifies it |
| Mobile Canvas particles | 150–500 | Only increase after profiling |
| Idle render loop | Paused or low-FPS | Never unconstrained by default |
| Visual long task | No ordinary-flow task > 50 ms | Same expectation |

### Required implementation behavior

- Cap physical canvas size: `width = cssWidth * min(devicePixelRatio, DPR_CAP)`.
- Use `ResizeObserver` or a deliberate resize handler. Never render at a stale resolution.
- Use exactly one `requestAnimationFrame` loop per mounted visual.
- Pass delta time into simulation; clamp extreme deltas after tab restoration.
- Pause work when the component is outside the viewport using `IntersectionObserver`.
- Pause work when the document is hidden using the Page Visibility API.
- Start at a conservative detail level and adapt only through defined LOD rules.
- Reduce particle count, blur, shadow, shader octaves, and post-processing on constrained devices.
- Cache static layers rather than repainting them every frame.
- Avoid allocating arrays, objects, gradients, paths, or closures inside hot frame loops.
- Move pure heavy calculation to a worker only after a performance trace identifies the main thread as the bottleneck.
- On component cleanup, cancel RAF, remove listeners/observers, terminate workers, and dispose GPU resources.
- For DOM motion, prefer `transform` and `opacity` where they satisfy the desired effect.

Use Chrome DevTools performance recordings, CPU throttling, the FPS meter, and frame-level analysis rather than assuming an effect is fast based on a developer laptop.[web:212]

---

## Accessibility Contract

### Non-negotiables

- Core copy, navigation, data, and product controls must be semantic HTML—not pixels in Canvas.
- Treat a visual-only Canvas as decorative with `aria-hidden="true"` when it conveys no new information.
- If a Canvas or WebGL experience is informative, provide an equivalent textual summary, DOM controls, and where relevant a table/list representation.
- Every pointer-only interaction must have an equivalent keyboard-accessible control.
- Ensure visible focus indicators are not covered by the rendering surface.
- Never encode essential meaning by color, motion, position, or hover alone.
- Use `prefers-reduced-motion: reduce`. Reduced motion should show a meaningful static state or a minimal fade, not a blank broken experience.
- Provide pause/stop/reduce controls for significant automatic motion that persists alongside content.
- Avoid flashing, high-frequency brightness changes, strong camera rotation, large parallax movement, and continuous high-contrast peripheral motion.
- Verify copy contrast over the entire animation cycle, including gradient and blend-mode extremes.

Motion should explain relationships or outcomes and should not overshadow the experience. It should be optional and cancelable where it could distract or cause discomfort.[web:227][web:228]

---

## Architecture and Code Quality

Use an architecture similar to the following, adapting it to the actual framework:

```text
components/generative/<VisualName>/
  <VisualName>.tsx        # semantic wrapper, public API, static fallback
  renderer.ts             # canvas/WebGL setup, draw/render lifecycle
  simulation.ts           # pure deterministic state update functions
  interaction.ts          # normalized pointer, touch, scroll, keyboard inputs
  tokens.ts               # visual, motion, LOD, and responsive design tokens
  prng.ts                 # seeded random functions and derivation strategy
  accessibility.ts        # reduced-motion / pause / alternative description
  types.ts                # public and internal types
  README.md               # intent, parameters, constraints, tests
  __tests__/              # unit, E2E, and screenshot tests
```

### Required engineering conventions

- TypeScript strict; no untyped mutable global scene state.
- Separate simulation from rendering so the model can test deterministic behavior without a browser canvas.
- Keep user-visible state in a single explicit source of truth. A renderer mirrors state; it does not secretly own business state.
- Derive all random variation from a seed. Store the seed in props, configuration, or a deliberate URL/content identifier.
- Do not use a monolithic demo file as production architecture.
- Do not add a dependency before checking whether native browser APIs or an existing project dependency solve the requirement.
- Document public properties, defaults, parameter ranges, lifecycle behavior, fallback behavior, and known trade-offs.
- Explicitly handle WebGL context loss if WebGL is used.
- Verify SSR/hydration boundaries in React/Next.js. Render static/semantic markup on the server; initialize browser-only rendering client-side without layout shift.

---

## Agent Working Method

### Plan before edit

Before changing code, produce a short plan containing:

1. The visual’s purpose and static fallback.
2. Chosen technology and rejected simpler alternatives.
3. Affected files and public API.
4. Performance budget and adaptive-detail strategy.
5. Accessibility behavior: reduced motion, semantic alternative, keyboard/pause behavior.
6. Test plan: unit, browser, visual regression, and manual checks.
7. Residual uncertainty or question requiring human design direction.

### Implement in slices

Do not build a complete immersive page in one pass.

1. Build a static, responsive composition.
2. Add deterministic rendering with a fixed seed.
3. Add controlled motion.
4. Add interaction and keyboard equivalents.
5. Add responsive composition and LOD.
6. Add fallback/reduced-motion behavior.
7. Profile and optimize measured bottlenecks.
8. Refactor, document, and test.

### Evidence, not assertions

An implementation is not complete merely because the agent says it is. Report:

- Files changed and why.
- Commands run and their actual result.
- Build, typecheck, lint, and focused test result.
- Screenshots at agreed seed, viewport, and timestamp.
- Browser console status.
- Performance trace summary before and after optimization.
- Accessibility-tool output plus manual keyboard/reduced-motion findings.
- Known limitations or scenarios not tested.

OpenCode’s MCP servers can add substantial tool context. Enable MCPs only for the agent/task that needs them, rather than making every server available to every session.[web:374]

---

## LLM Strengths and Boundaries

### Use the agent confidently for

- Canvas/SVG/Three.js boilerplate and lifecycle scaffolding.
- Known algorithms: particles, flow fields, Bézier paths, seeded variation, simple noise fields.
- CSS/SVG state transitions and simple scroll-linked sequences.
- Extracting visual tokens into typed configuration.
- Refactoring an isolated demo into modules.
- Adding test harnesses, fixed seeds, screenshot capture, and basic fallbacks.
- Diagnosing reproducible build, TypeScript, console, and test errors.

### Require heightened human review for

- Visual judgment, composition, typography, and brand distinctiveness.
- Complex shaders and advanced GPU simulation.
- Performance claims without traces on target devices.
- Accessibility claims without keyboard, screen-reader, and reduced-motion review.
- Browser compatibility and mobile GPU behavior.
- Data visualization semantics and interpretive claims.
- Long-lived component architecture and integration with application state.
- Any request that is merely “make it more premium,” “more cinematic,” or “more creative.” Convert those into concrete art-direction parameters first.

---

## Reference MCP and Skill Stack

### Recommended OpenCode project configuration

OpenCode uses `AGENTS.md` for always-on project rules. It supports local and remote MCP servers under `mcp` in `opencode.json`; configure only servers needed for the current project and limit tool access per agent where possible.[web:364][web:374]

| Capability | Recommended integration | Value for generative web work | Caution |
|---|---|---|---|
| Design inspiration | **Inspo MCP** (`inspo-mcp`) | Searches real website references; useful before the design/plan phase | Use it to extract principles, not to clone a website; verify licensing and source attribution |
| Official technical docs | Context7 MCP | Reduces hallucinated library/API usage; use for Three.js, GSAP, Web APIs, etc. | Prefer official docs for technical decisions |
| Browser execution and screenshots | Playwright MCP or browser-capable agent integration | Supports visual review, interaction testing, console checks, and screenshot evidence | Fix seed/time and mask intentionally dynamic regions |
| Accessibility checks | axe-core via project tests / browser workflow | Fast baseline audits for HTML UI | It does not replace manual keyboard, screen-reader, or motion review |
| Repository search / GitHub examples | Grep MCP or GitHub MCP | Finds project conventions and implementation patterns | GitHub MCP can create large context overhead |
| Error monitoring | Sentry MCP | Useful after deployment to inspect real frontend errors | Grant minimum data access |
| Issue/PR workflow | GitHub MCP | Lets the agent link evidence, tests, and code review artifacts | Make writes approval-gated |

### Inspo MCP: recommended role

Inspo is relevant to this workflow because it gives a coding agent design references during planning, instead of relying only on generic latent patterns. Public descriptions state that the newer Inspo design MCP searches roughly 800 sites for design inspiration and is designed for coding agents including OpenCode; the reported installer is `npx inspo-mcp install`.[web:384]

Treat that as a **vendor/community capability claim requiring local verification**. Before adopting it:

1. Confirm the exact npm package name, publisher, source repository, license, privacy terms, required API key, and supported OpenCode installation route.
2. Pin a reviewed package version rather than silently executing a changing `@latest` package in a production workflow.
3. Run it first in a non-sensitive repository.
4. Grant no repository write, credential, or broad filesystem access unless the server demonstrably needs it.
5. Ask it for *design principles*: composition, information hierarchy, palette relationships, interaction pattern, and performance-friendly implementation idea.
6. Do not ask it to duplicate branded layouts, visual identities, screenshots, or copyrighted assets.

A useful planning prompt after installation:

```text
Use the Inspo MCP only during research. Find 5–8 public references for an asset-free, calm, research-oriented B2B SaaS hero that uses procedural 2D motion or SVG rather than video or image assets.

For each reference, return: URL, observed visual principle, content hierarchy, movement/interaction principle, likely browser technology if documented, accessibility or performance risk, and one abstracted idea that can be reinterpreted without copying the visual design. Do not write code yet. Do not reproduce source copy, assets, layouts, or branded visual identity.
```

### Skills to create locally

OpenCode’s project-local skills live at `.opencode/skills/<name>/SKILL.md`; each must start with YAML frontmatter containing at least a lowercase hyphenated `name` and a specific `description`.[web:359]

Create the following skills rather than placing their complete instructions in root `AGENTS.md`.

| Skill name | Trigger | What it should enforce |
|---|---|---|
| `generative-web-visuals` | Canvas, SVG motion, particles, WebGL, procedural hero, shader, scrollytelling | This entire competency contract: purpose, rendering choice, deterministic seed, fallback, LOD, cleanup, and evidence |
| `design-reference-research` | Inspiration, redesign, hero direction, visual references | Inspo MCP research; abstract principles, source/credit capture, anti-copying guardrails, moodboard-to-token output |
| `frontend-visual-qa` | Screenshot review, visual regression, polish, responsive design | Fixed seed/time, viewport matrix, Playwright screenshots, animation stability, visual-diff review |
| `frontend-performance` | FPS, jank, slow animation, mobile performance, bundle | Profile first; DevTools traces, long tasks, DPR/LOD, observer/visibility behavior, before/after evidence |
| `motion-accessibility` | Reduced motion, animation, scroll, canvas interaction, keyboard | Semantic alternative, `prefers-reduced-motion`, pause/stop, keyboard equivalents, contrast-over-time checks |
| `threejs-production` | Three.js, WebGL, shaders, 3D hero | Client-only boundaries, context loss, renderer disposal, DPR caps, LOD, WebGL fallback, target-device profiling |
| `data-visualization-integrity` | Chart, network, heat map, visualized data | Explicit encoding table, data-source validation, table/list alternative, no color-only meaning, no fabricated inferences |
| `open-source-license-review` | Copy demo, reuse shader, add library, inspiration repo | License/attribution check, dependency provenance, no copy-paste from unclear sources |

### Minimal `SKILL.md` starter: `generative-web-visuals`

Create `.opencode/skills/generative-web-visuals/SKILL.md` with the following content:

```md
---
name: generative-web-visuals
description: Plan, implement, review, or refactor production-safe generative web visuals using CSS, SVG, Canvas, WebGL, Three.js, shaders, particles, procedural illustration, or scroll-linked motion.
license: Proprietary
compatibility: OpenCode project skill
metadata:
  domain: frontend-creative-coding
  priority: production-quality
---

# Generative Web Visuals

Read `GENERATIVE_WEB_VISUALS_COMPETENCY.md` before editing relevant code.

## Required workflow

1. State the user/product/brand purpose and classify the visual as decorative, informative, or interactive.
2. Propose the simplest renderer: CSS, SVG, Canvas 2D, WebGL/Three.js, or WebGPU.
3. Define static fallback, reduced-motion behavior, semantic alternative, target viewports, and performance budget.
4. Implement in order: static composition → deterministic renderer → motion → interaction → responsive/LOD → tests.
5. Derive variation from an explicit seed; make seed and time controllable for tests.
6. Clean up RAF, event listeners, observers, workers, and GPU resources on unmount.
7. Run build, typecheck, lint, focused tests, browser console review, and screenshots at agreed fixed seeds/times.
8. Report evidence and residual risks. Never claim performance or accessibility compliance without measurements and manual checks.

## Non-negotiables

- Core text, navigation, controls, and data remain semantic HTML.
- Pointer-only actions have keyboard-accessible equivalents.
- Respect `prefers-reduced-motion`; pause work offscreen and in hidden tabs.
- Do not add motion without an explicit purpose.
- Do not use unbounded pixel density, uncontrolled randomness, scroll hijacking, or monolithic demo architecture.
```

### Skill permission approach

Keep high-value, low-risk skills available by default: `generative-web-visuals`, `motion-accessibility`, and `frontend-visual-qa`. Set research, browser, GitHub, Sentry, and any write-capable integration to **ask** or to a dedicated specialist agent. OpenCode documents permission-based skill loading and per-agent tool enablement; this supports an intentional least-context, least-privilege setup.[web:359][web:374]

---

## Suggested Specialist Agent Roles

Instead of one unrestricted “full-stack design agent,” separate work by task:

| Agent | Enable | Deliverable | Must not do alone |
|---|---|---|---|
| `visual-researcher` | Inspo, web/docs research, design-reference skill | Principles, citations/links, anti-copying constraints, moodboard-to-token proposal | Modify product code |
| `creative-implementer` | Generative visuals skill, repo read/write, browser screenshots | Isolated component and tests | Declare aesthetic approval or production performance without review |
| `visual-qa` | Browser/Playwright, visual-QA, motion-accessibility | Screenshot matrix, interaction video, a11y findings | Modify unrelated code |
| `performance-engineer` | DevTools/browser trace, performance skill | Baseline/after profile and targeted patches | Change visual direction without design approval |
| `release-reviewer` | Read-only repo, test outputs, license review | Go/no-go review with evidence and residual risk | Direct deploy or broad refactor |

---

## Prompt Patterns

### Implement a calm B2B procedural hero

```text
Use the `generative-web-visuals` skill. Before editing, read `GENERATIVE_WEB_VISUALS_COMPETENCY.md` and inspect the relevant existing hero/component files.

Goal: build an asset-free, calm B2B hero visual that communicates [PRODUCT METAPHOR]. It is decorative; headline, body, and CTA must remain semantic HTML and visually dominant.

Art direction: [PALETTE TOKENS], [LINE/SHAPE LANGUAGE], [NEGATIVE SPACE RULE], [FORBIDDEN TROPES]. Use a seeded 2D flow-field composition: [NUMBER] lines on desktop, [NUMBER] on mobile. Motion should be slow, with [MAX SPEED], [REST PERIOD], and pointer influence no greater than [VALUE].

Technical constraints: [FRAMEWORK], Canvas 2D only unless you first justify a different renderer; no external assets, Base64 data, external requests, or new dependencies. Cap DPR at [VALUE]; target [FPS] idle; pause offscreen and on hidden tabs. Reduced motion must be a deterministic static composition.

Deliverables: plan before changes; component architecture; testable seed and frozen-time option; build/typecheck/lint; screenshots at [VIEWPORTS] for t=0 and t=5 seconds; browser-console report; a performance trace under [THROTTLING]; residual risks.
```

### Research references before coding

```text
Use `design-reference-research` and the Inspo MCP only for research. Do not modify code.

Find public references relevant to [WEBSITE TYPE] and [DESIRED VISUAL PRINCIPLE]. Exclude image/video-asset-led designs. For each of 5–8 references, capture URL, observed hierarchy, visual mechanism, interaction pattern, likely/documented technology, accessibility/performance risk, and one transferable abstract principle.

Then synthesize: a non-copying art-direction proposal, 4–6 design tokens, the simplest browser technology, a static fallback, and three explicit anti-patterns to avoid. Do not reproduce branded layouts, copy, or assets.
```

### Profile an existing visual

```text
Use `frontend-performance` and `motion-accessibility`. Do not optimize before establishing a baseline.

Profile the existing [COMPONENT/ROUTE] at [VIEWPORTS] under [CPU/NETWORK TEST CONDITIONS]. Identify whether the limiting cost is JavaScript, layout, paint, GPU/raster, memory growth, or bundle transfer. Check behavior when hidden, offscreen, resized, route-changed, and reduced motion is enabled.

Make only targeted changes addressing measured bottlenecks. Then repeat exactly the same measurements. Report before/after evidence, changed files, trade-offs in visual fidelity, and any remaining risks.
```

---

## Definition of Done

A generative web visual is ready for merge only when all are true:

- [ ] It has an explicit user, product, or brand purpose.
- [ ] The static state is visually approved before motion is considered complete.
- [ ] The chosen renderer is justified against simpler alternatives.
- [ ] Core content and interaction remain semantic and accessible.
- [ ] The visual has reduced-motion and feature-fallback behavior.
- [ ] It uses a reproducible seed and test-controllable time.
- [ ] It adapts detail and caps pixel density for constrained devices.
- [ ] It pauses offscreen and in hidden tabs.
- [ ] Its lifecycle cleans all resources correctly.
- [ ] It passes build, typecheck, lint, focused behavior tests, visual tests, and accessibility baseline checks.
- [ ] It has been viewed at mobile, tablet, desktop, and ultrawide sizes as applicable.
- [ ] It has been profiled on a target device or defined throttled environment.
- [ ] Library, shader, demo, and reference licenses have been checked.
- [ ] The review includes screenshots/recording, actual test output, and a documented residual-risk statement.

---

## Primary Sources Used

- OpenCode: [Agent Skills](https://opencode.ai/docs/skills/), [Rules / AGENTS.md](https://opencode.ai/docs/rules/), and [MCP Servers](https://opencode.ai/docs/mcp-servers/).
- OpenCode documentation establishes the project skill locations, required skill frontmatter, project/root `AGENTS.md` behavior, modular instructions, MCP configuration, and the context cost of MCP tools.[web:359][web:364][web:374]
- MDN: [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas), which documents the semantic/accessibility limitation of Canvas content.[web:256]
- Chrome for Developers: [Analyze runtime performance](https://developer.chrome.com/docs/devtools/performance), for CPU throttling, FPS, frame, and runtime-performance inspection.[web:212]
- Inspo information: [Inspo MCP public description](https://www.inspoai.io/mcp) and contemporary reporting on the `inspo-mcp` OpenCode-compatible installer. Treat service/package specifics as locally verifiable configuration, not a permanent guarantee.[web:382][web:384]
