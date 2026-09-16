# LLM-Assisted Generative Coding for Modern Website Design

**Status: September 15, 2026**

## Executive Summary

1. **LLM-assisted generative coding is production-ready in bounded use cases, but it is not “prompt-to-production.”** Frontier models can generate convincing Canvas, SVG, CSS, Three.js, and basic shader prototypes. Visual precision, mobile performance, accessibility, architecture, and browser QA still require expert human review.
2. **The strongest use cases are bounded, brand-bearing components:** hero visuals, product metaphors based on data, ambient backgrounds, interactive demonstrations, and narrative transitions—not permanently animated full-page experiences.
3. **Choose technology from the information model:** CSS for semantic UI motion, SVG for accessible scalable shapes, Canvas 2D for many dynamic 2D primitives, and WebGL/Three.js for GPU effects and 3D. WebGPU is powerful, but should still be treated as progressive enhancement with a fallback strategy.
4. **LLMs work best for boilerplate, known algorithms, structured variants, refactoring, and reproducible bugs.** They are less reliable for underspecified art direction, advanced shader work, long-term scene architecture, and subjective visual refinement.
5. **An agent workflow is superior to a single prompt:** brief → plan → small implementation → browser render → screenshot/video review → profiling → refactoring.
6. **Performance is a product requirement.** Animations must be profiled under constrained conditions, paused when invisible or in background tabs, and degraded adaptively for weaker devices.
7. **Accessibility cannot be retrofitted.** Canvas pixels do not inherently provide HTML semantics. Core information and interactions need DOM equivalents, keyboard access, contrast control, reduced-motion behavior, and—where appropriate—pause controls.
8. **Seeded generativity is more professional than uncontrolled randomness.** Reproducible seeds enable art direction, visual regression testing, consistent campaign variants, and debugging.
9. **The most convincing results come from a small set of coherent rules:** a limited palette, a clear movement rhythm, controlled density, distinctive line behavior, and intentional irregularity.
10. **Coding benchmarks are only partial evidence.** Repository-patch benchmarks do not measure brand fit, visual quality, animation comfort, or production robustness. Teams should evaluate models in their own repository and browser environment.
11. **The competitive advantage is not access to a model.** It is an ownable visual system: proprietary parameters, brand metaphors, curated seeds, motion tokens, data binding, and a repeatable review process.
12. **A sensible first professional experiment is a two-week, asset-free hero proof of concept using Canvas 2D or SVG**, with constrained interaction, a static fallback, a performance budget, and a concrete hypothesis about product or brand impact.

## Evidence Framework

This report distinguishes four types of statements:

- **Documented:** browser standards, official documentation, repositories, or direct project credits.
- **Empirical:** a benchmark, study, or reproducible test with a stated method.
- **Case-study-derived:** a practical observation inferred from a published project and its available credits.
- **Expert assessment:** a reasoned recommendation; useful, but neither a standard nor a universal measurement.

Vendor statements about model capabilities should not be treated as independent proof. They can establish that a capability is advertised or exposed in a product, but not that every output is reliable, accessible, performant, or production-ready.

## Concepts and Technical Context

### Definitions

| Term | Core mechanism | Typical outcome | Key distinction |
|---|---|---|---|
| Classical web animation | Predefined states and transitions of DOM, SVG, or Canvas objects | Fade, slide, morph, page transition | Usually a deterministic choreography; it does not need continuous image synthesis |
| Generative art / creative coding | Rules, algorithms, randomness, and input create an open visual output | Flow fields, particles, recursive forms | Broad artistic-methodological term; product utility is optional |
| Procedural graphics | Pixels, geometry, or textures are computed from parameters at runtime | Noise textures, terrain, gradient shaders | Technical mechanism; can be generative or fully deterministic |
| AI-generated images/videos | A media model generates raster images or video frames | PNG, JPEG, MP4 | The generated media asset is primarily displayed or played in the browser |
| AI-generated frontend code | An LLM produces HTML, CSS, JavaScript, shaders, or components | Executable source code and UI | The model emits instructions; the browser renders the resulting experience |
| Canvas 2D | Immediate-mode drawing into a bitmap | Lines, particles, pixels, sprites, trails | Efficient for dynamic 2D, but lacks inherent scene structure and semantics |
| SVG | DOM-based vector markup | Paths, charts, icons, morphs | Scalable, addressable, and semantically augmentable; many nodes can become expensive |
| CSS | Declarative layout, styling, and animation of DOM/SVG | UI motion, gradients, masks, filters | Best when the visual object is already semantic HTML |
| WebGL | Low-level GPU rendering API exposed through a canvas | 2D/3D scenes, shaders, post-processing | Broadly supported, but device and driver behavior matters |
| WebGPU | Modern GPU API for rendering and compute | Large particle systems, simulation, 3D | More capable model, but should still be deployed with explicit fallbacks |

### How an LLM “draws” without drawing

In this workflow, an LLM does not paint an image. It translates a visual direction—for example, “a calm ink-like field that converges into three brand-colored areas”—into a program model:

- Data structures for particles, paths, or grid cells.
- Mathematical rules for movement, color, deformation, and timing.
- Rendering commands for Canvas, SVG, WebGL, or WebGPU.
- Input logic for mouse, touch, scroll, audio, or live data.
- Responsive, accessibility, and lifecycle behavior.

The browser then executes the program. Canvas 2D writes drawing operations into a bitmap; SVG updates a vector DOM; WebGL or WebGPU processes geometry and shader programs on the GPU. The result can be responsive, interactive, data-driven, and resolution-independent in a way that a fixed image asset cannot be. It is still only as good as the design rules, rendering implementation, and quality assurance behind it.

### Common building blocks

| Building block | Role | Production note |
|---|---|---|
| Canvas 2D API | Draws paths, text, filled areas, image data, and composites into a bitmap | Good for 2D heroes, illustration styles, and many simple dynamic primitives |
| `requestAnimationFrame` | Schedules updates in coordination with browser rendering | Use delta time; prevent duplicate loops; stop on unmount |
| Particle systems | Manage many entities with position, velocity, age, and appearance | Avoid object allocation each frame; use typed arrays or pools where needed |
| Perlin/Simplex/FBM noise | Produces spatially correlated variation | Treat frequency, octaves, and amplitude as design tokens |
| Bézier curves and paths | Shape controlled organic contours and linework | Strong for branded organic forms and illustration |
| Sine/cosine motion | Creates periodic motion, waves, and phase offsets | Combine carefully and keep amplitudes modest |
| Seeded pseudo-randomness | Produces reproducible variation | Persist seeds per campaign, page, or content item |
| Layering, alpha, blend modes | Create depth, grain, light, and material impression | Monitor overdraw and contrast behind text |
| OffscreenCanvas | Decouples a canvas from the visible DOM context | Use after profiling indicates main-thread pressure |
| Web Workers | Move computation off the UI thread | Useful for simulation or layout; DOM work still stays on the main thread |
| WebGL/WebGPU fragment shaders | Calculate color per pixel/fragment | Powerful for gradients, noise, fluidity, and distortion; more demanding to debug |
| Input systems | Connect mouse, touch, scroll, audio, or live data to visual rules | Do not block core navigation; provide non-pointer alternatives when interaction matters |

### Small conceptual example

A surprisingly rich “fiber field” can be created from a small number of rules:

1. Start several hundred thin lines at positions on a grid.
2. At every step, determine each line’s direction from a smoothly changing vector field built from sine, cosine, or noise.
3. Add very small seeded deviations rather than fully random turns.
4. Draw lines with low opacity, so repeated trajectories gradually become visually dense.
5. Offset a second stroke slightly to simulate an imperfect hand-made contour.

The effect feels organic because nearby positions behave similarly but not identically; many simple agents travel through the same field; and transparent layering reveals recurring paths. In production, derive variation from a stable seed and the line ID rather than consuming randomness freely, so a resize or re-render produces the same result.

## Relevance for Website Design

| Use case | Product or brand value | Main risk | Realistic complexity | Sensible MVP |
|---|---|---|---|---|
| Landing-page hero | Differentiation, product metaphor, premium first impression | CTA contrast, LCP/INP, generic “AI demo” appearance | Medium | One light Canvas layer with minor pointer influence |
| Brand/campaign site | Creates a distinct world and memorability | Self-indulgence, slow introductions, difficult QA | High | One iconic scene rather than a whole virtual world |
| SaaS product page | Makes an abstract process visible | Visual may imply capabilities the product does not have | Medium | Data-flow metaphor with three states and a static fallback |
| Portfolio/creative studio | Demonstrates creative and technical capability | Navigation becomes a game; contact and work become harder to find | High | Experimental hero plus conventional work/contact navigation |
| Editorial/magazine | Adds atmosphere and narrative structure | Reading friction and scroll fatigue | Medium–high | A chapter illustration or a single narrative sequence |
| Data product/dashboard | Makes patterns, relations, and live status tangible | Aesthetic form may displace accuracy | Medium–high | Data-driven highlight next to accessible standard charts |
| Event/music/culture | Emotional, time-based identity system | Audio autoplay, photosensitivity, device variability | Medium–high | User-initiated audio response or time-based variation |
| Onboarding | Explains progression and reduces perceived waiting | Motion can lengthen the flow or conceal options | Low–medium | Brief, functional state transitions that can be skipped |
| Loading/transitions | Provides continuity and feedback | Fake loading and blocking cinematic transitions | Low–medium | Short microtransition; real progress for long operations |
| Scrollytelling | Explains causality, sequence, and spatial models | Scroll hijacking, motion discomfort, mobile instability | High | Native scrolling with two or three scenes |
| Interactive product demo | Learning through direct manipulation | Demo does not replace clear value proposition | Medium–high | One core use case with reset, keyboard support, and text alternative |
| Ambient interface | Adds atmosphere without external assets | Continuous device load and peripheral distraction | Low–medium | 15–30 fps, low density, paused when offscreen |
| Generative illustration | Unique, scalable visual language | Inconsistent style or randomness mistaken for direction | Medium | Three to five curated seeds and a static fallback |

### When it creates value

Motion and generative visuals create product value when they help users understand relationships, available actions, state changes, outcomes, or a narrative sequence. They are decorative when their only justification is that they look technically impressive.

A useful decision rule is: **if a team cannot state in one sentence what perception, understanding, or decision the visual improves, it is probably decoration.**

For trust-sensitive and transactional websites, visual systems should support—not replace—the chain of evidence: problem, value, product proof, price, and call to action. Particularly risky patterns include high-motion backgrounds behind copy, custom cursors with lag, artificial loading screens, and visuals that look like product functionality but are only scenery.

## Design Patterns and Inspiration

### Curated pattern library

| Project / source | Category | Technology | Visual and interaction principle | Transferable lesson | Complexity | Classification / limits |
|---|---|---|---|---|---|---|
| Bruno Simon Portfolio | Creative-developer portfolio | Three.js | Drivable 3D world controlled by keyboard/touch | Interaction can function as a capability demonstration when navigation remains clear | High | Brand showcase; high mobile and navigation QA effort |
| Active Theory | Digital studio | Custom immersive web-experience stack | Spatial transitions and interactive branded worlds | Technology should serve narrative and positioning | High | Brand experience; expensive and specialist-heavy |
| Unseen WebGL Rain | Studio lab | WebGL | Procedural rain; press-and-hold manipulates time | A simple interaction can transform a natural-system visual into an understandable experience | Medium–high | Aesthetic experiment; potentially demanding visually |
| Resn Labs | Studio lab | WebGL experiments | Playful real-time studies | Internal labs can yield reusable technical and visual vocabulary | High | Experiments are not automatically product patterns |
| The Boat | Editorial story | WebGL / interactive illustration | Scroll-linked narrative scenes | Motion works when it deepens the editorial content itself | High | Content-specific; technically heavy |
| Patatap | Music interaction tool | Two.js / browser audio | Keyboard/touch creates sound and abstract animated form | Immediate input-feedback loops make complexity approachable | Medium | Requires sensitivity to flashing and audio accessibility |
| Blob Opera | Cultural music experiment | ML-driven audio interaction | Dragging changes pitch and vowel behavior | Complex technology feels legible through direct manipulation | High | Not purely procedural graphics; needs accessible audio alternatives |
| Silk | Generative art tool | Browser-rendered procedural line system | Mirrored flowing fibers controlled by pointer | Few rules can create high visual reward | Medium | Strong aesthetic tool, limited information utility |
| Shadertoy | Shader platform | GLSL/WebGL | Real-time shader experiments with parameters | Excellent source of isolated procedural-material techniques | High | Reuse requires individual licensing and production adaptation |
| WebGL Fluid Simulation | Open-source demo | WebGL | Pointer injects color and force into a fluid simulation | Material behavior can reward direct manipulation | High | GPU, battery, and motion risks |
| Three.js examples | Framework gallery | Three.js/WebGL/WebGPU | 3D, particles, postprocessing, shader examples | Use official examples to reduce fabricated API use by coding models | Medium–high | Technical references, not production architecture |
| p5.js examples | Creative-coding ecosystem | p5.js / Canvas | Small sketches for noise, shapes, input, and animation | Very fast visual proofs of concept | Low–medium | Often needs refactoring for product integration |
| Generative Art Gallery | Open source | p5.js | Flow fields, fractals, particles, reaction-diffusion | Good algorithm catalog for early exploration | Medium | Style and performance must be made product-specific |
| Rough.js | Graphics library | Canvas/SVG | Jittered, multi-stroke primitives | Controlled imperfection creates hand-made quality without raster assets | Low–medium | Can become illustrative or generic if overused |
| Matter.js demos | Physics engine | 2D physics | Collision, gravity, drag, constraints | Physics is useful for playful, understandable microinteractions | Medium | UI states must remain predictable and resettable |
| tsParticles | Particle engine | JavaScript/TypeScript | Configurable particles, confetti, fireworks | Fastest route to conventional particle effects | Low–medium | High risk of template-like visual language |
| Codrops Creative Hub | Demo/tutorial archive | GSAP, SVG, Three.js, WebGL/WebGPU | Scroll, typography, shaders, 3D, dithering | Strong source for targeted technical research | Variable | Verify license and production readiness per demo |
| D3 | Data visualization library | SVG, Canvas, HTML | Data binding, scales, layouts, interaction | Generative rules can communicate real data rather than decoration | Medium–high | Needs accessibility and alternative views |

### Recurrent motifs

- **Flow fields and organic particles:** a directional field controls many simple agents. Quality depends more on trail length, density, palette, and compositing than on elaborate individual geometry.
- **Generative typography:** text becomes paths, points, or shader masks. Powerful in campaigns and portfolios; risky for readability, SEO, selection, and localization.
- **Hand-drawn lines:** multiple strokes, jitter, variable width, and grain create materiality. The style is most effective when line hierarchy remains controlled.
- **Virtual materials:** shaders simulate light, reflection, dispersion, dithering, or fluidity. They work best when the material encodes a credible brand metaphor.
- **Natural systems:** smoke, water, light, and swarms create believable motion, but need strong constraints around performance and motion intensity.
- **Cursor-reactive interfaces:** strongest when a pointer lightly changes an existing state—not when a custom cursor replaces the operating system’s interaction conventions.
- **Data-driven generativity:** data controls density, color, topology, or behavior. This makes a visual explainable and product-relevant.
- **Subtle local effects:** small islands of motion are often more professional, accessible, and economical than a continuously animated full screen.

## What LLMs Can Realistically Do

### Strengths

Strong current models can usually create useful first versions of:

- Canvas render loops, resize behavior, and basic lifecycle management.
- SVG paths, masks, filters, and simple morphs.
- CSS keyframes and UI transitions.
- Basic particle systems, flow fields, L-systems, geometric patterns, and seeded pseudo-randomness.
- Simple Three.js scenes with camera, lights, materials, meshes, and pointer interaction.
- Basic fragment shaders for gradients, noise, distortion, or simple procedural materials.
- Refactoring an isolated demo into TypeScript modules and configurable components.
- Adding `ResizeObserver`, `IntersectionObserver`, Page Visibility behavior, and `prefers-reduced-motion` handling.
- Debugging reproducible console, build, and test failures.

### Common failure modes

- **Ambiguous direction:** “cinematic,” “premium,” and “organic” are not executable specifications.
- **Visual precision:** the code may be plausible while the actual render does not match the intended composition or material quality.
- **Architecture over time:** prototypes can become coupled classes, global state, and untestable animation loops.
- **Browser and device variability:** touch behavior, device pixel ratio, GPUs, drivers, and feature support are easy to overlook.
- **Resource management:** duplicate `requestAnimationFrame` loops, orphaned listeners, unfreed WebGL resources, and repeated initialization under React Strict Mode.
- **Complex shaders:** incorrect coordinate spaces, precision artifacts, unstable loops, and portability problems.
- **Accessibility theater:** an ARIA label on a canvas does not create an accessible interaction model or replace a data table.

### Maturity matrix

| Task | LLM suitability today | Typical quality | Human control needed | Main risks |
|---|---|---|---|---|
| Canvas background animation | High | Usually quickly runnable; generic without art direction | Medium | Unlimited loops, DPR cost, resize/cleanup bugs |
| Generative hero illustration | Medium–high | Good initial composition; refinement depends on briefing | High | CTA contrast, inconsistent seeds, generic branding |
| Interactive particles | High for standard patterns | Solid pointer/touch response | Medium–high | O(n²) neighbor search, mobile jank, no keyboard alternative |
| Hand-drawn style | Medium | Convincing with explicit line parameters or Rough.js | High | “Wobbly” rather than refined; unstable text |
| Scroll animation | Medium–high | Good for isolated sequences | High | Scroll hijacking, resize issues, focus/reduced-motion problems |
| Data visualization | High for conventional charts; medium for novel forms | Good when data and scale rules are explicit | High | Misleading encoding, missing alternatives, edge cases |
| 3D/WebGL scene | Medium | Good boilerplate and simple scenes | Very high | GPU differences, resource lifecycle, mobile thermal load |
| Shader effect | Medium | Basic noise/gradient shaders are feasible; advanced simulation is fragile | Very high | Compilation errors, banding, driver variation |
| Mobile performance optimization | Medium | Strong checklist, not guaranteed improvement | Very high | Optimizing without profiling the real bottleneck |
| Accessibility integration | Medium | Good boilerplate for media queries and attributes | Very high | False compliance; inaccessible core interaction |
| Production React/Next.js component | Medium–high with constrained scope | Good structure if lifecycle and API are specified | High | SSR/hydration, cleanup, bundle, Strict Mode, design-system drift |

### Single prompt vs. iterative agent workflow

| One-off code generation | Iterative agent workflow |
|---|---|
| Optimizes for a plausible textual response | Optimizes for verifiable browser behavior |
| Often does not see the real rendered state | Can open the app, inspect console/DOM, and capture screenshots |
| Has no stable measurement loop | Repeats build, test, visual diff, and profile loops |
| Tends toward one large file and hidden assumptions | Uses a plan, small diffs, review, and refactoring |
| May claim success in prose | Shows success through test output, screenshots, and traces |

**Recommended operating model:** work component by component. First establish a strong static composition, then add movement, then interaction, then responsive and reduced-motion behavior, and only then optimize and integrate. Screenshots are useful for composition; a five-to-ten-second reference video or motion storyboard is much more useful for timing and movement quality.

## Best Practices

### Art direction

1. **Start with a deliberate intent.** Define an effect hypothesis, such as: “The visual shows how scattered signals converge into a clear decision.”
2. **Treat parameters as a design system.** Specify palette, background, contrast, line weight, density, maximum speed, easing, jitter, grain, radius, interaction strength, and resting states.
3. **Use one dominant metaphor.** Do not combine fluid simulation, particles, 3D glass, and generative typography without a clear conceptual reason.
4. **Approve a static composition first.** The still frame must already carry hierarchy and brand expression.
5. **Design rest deliberately.** Use low amplitudes, pauses, local change rather than global movement, and constrained reaction ranges.
6. **Treat mobile as a new composition.** It is not merely a smaller desktop canvas.
7. **Curate seeds.** Review a selection, approve a small set, and constrain production randomness to safe ranges.
8. **Give motion a job.** Motion should clarify relation or feedback, not exist merely to attract attention.

### Performance strategy

Suggested starting budgets below are expert recommendations, not universal standards. They must be validated against a real route baseline and real target devices.

| Budget | Conservative SaaS/content page | Campaign/portfolio page | Measurement |
|---|---|---|---|
| Additional visual JavaScript | Target ≤ 80 kB gzip | Target ≤ 180 kB gzip | Bundle analyzer, network panel |
| Canvas DPR | 1–1.5 mobile; max. 2 desktop | Max. 2, adaptive | Device matrix |
| Active particles | 150–500 mobile | 500–2,000 depending on GPU/LOD | FPS/frame profile |
| Frame rate | 30 fps ambient; 60 fps only for direct interaction | 30–60 fps adaptive | DevTools frames/FPS |
| Main-thread long tasks | No visual-induced task above 50 ms in ordinary flow | Same target | Performance trace |
| Offscreen behavior | Fully pause | Fully pause | Intersection/page visibility tests |
| Reduced motion | Static frame or minimal opacity motion | Alternative calm scene | OS and DevTools emulation |
| Fallback | CSS/SVG/static state | Simplified Canvas/SVG state | Feature and error tests |

Implementation practices:

- Cap Canvas resolution using `cssWidth * min(devicePixelRatio, cap)`.
- Use adaptive detail: particle count, shader octaves, blur radius, shadow use, and post-processing should reduce on weaker devices.
- Keep ambient effects at roughly 20–30 fps unless direct response genuinely requires more.
- Pause rendering with `IntersectionObserver` when not visible and with the Page Visibility API in hidden tabs.
- Prefer `transform` and `opacity` for DOM animation where possible.
- Cache static layers in an offscreen canvas.
- Move expensive non-DOM calculation to workers only after profiling indicates that the main thread is the bottleneck.
- Explicitly release WebGL resources and clean up render loops, observers, and listeners on component unmount.
- Use progressive enhancement: core content and calls to action must work without Canvas, JavaScript, or a capable GPU.

### Accessibility and user control

1. Respect `prefers-reduced-motion`.
2. Provide a pause, stop, or hide control for non-essential automatically moving content that persists alongside other content.
3. Keep core text, links, data, and controls in the DOM. Canvas should remain decorative unless a full alternative interaction model exists.
4. Test contrast over time: start frame, end frame, animated extremes, interaction states, and every palette mode.
5. Provide keyboard equivalents for pointer, touch, drag, and scroll interactions.
6. Avoid large parallax shifts, strong zoom journeys, constant peripheral motion, and spatial rotation that can trigger discomfort.
7. Avoid flashing and high-frequency luminance changes.
8. Offer a visible “reduce animation” or “pause animation” option for intense experiences, in addition to honoring system preferences.

### Maintainable production architecture

```text
GenerativeVisual/
  index.tsx              # semantic wrapper, public props, fallback
  renderer.ts            # Canvas/WebGL lifecycle
  simulation.ts          # pure update logic
  interaction.ts         # normalized pointer/touch/scroll input
  tokens.ts              # palette, density, motion, LOD
  prng.ts                # seed and deterministic derivations
  accessibility.ts       # reduced motion, labels, controls
  __tests__/             # unit, browser, and visual tests
```

- Document each parameter with unit, permitted range, default, and visual effect.
- Test simulation as pure logic wherever possible; keep the renderer separate.
- Clean up `requestAnimationFrame`, event listeners, observers, workers, and GPU resources.
- Test React Strict Mode, route transitions, tab changes, and hot reload for duplicate initialization.
- Use fixed seeds and frozen time for visual regression tests.
- Use automated accessibility tooling as a baseline, then manually test keyboard paths, screen readers, zoom, motion settings, and cognitive load.
- Review licenses for every library, demo, code fragment, shader, asset, and reference. Public visibility does not imply permission to reuse.

## Technology Decision Guide

Legend: **++ strongly suitable**, **+ suitable**, **0 possible with trade-offs**, **– generally unsuitable**.

| Requirement | CSS | SVG | Canvas 2D | WebGL / Three.js | WebGPU | Recommendation |
|---|---:|---:|---:|---:|---:|---|
| Simple UI animations | ++ | + | – | – | – | CSS/Web Animations; use motion libraries only for orchestration |
| Organic decorative backgrounds | + | + | ++ | ++ | 0 | Canvas for 2D; shaders for high pixel complexity |
| Interactive 2D particles | – | 0 | ++ | ++ | + | Canvas at modest scale; GPU for many instances |
| Hand-drawn illustrations | 0 | ++ | ++ | 0 | – | SVG for addressable paths; Canvas for many strokes |
| Data-rich visualization | 0 | + | ++ | ++ | + | D3 with SVG/Canvas; WebGL for very large point counts |
| Responsive infographics | + | ++ | 0 | – | – | Semantic HTML/SVG with text alternatives |
| 3D product presentation | – | – | – | ++ | + | Three.js/WebGL; WebGPU progressively |
| Shader-based effects | – | – | 0 | ++ | ++ | WebGL baseline; WebGPU with fallback |
| Immersive campaign website | 0 | + | + | ++ | + | Three.js/WebGL plus semantic DOM layer |
| Mobile-first SaaS landing page | ++ | ++ | + | 0 | – | CSS/SVG or lightweight Canvas; WebGL only with clear value |
| SEO-critical content page | ++ | ++ | – | – | – | HTML content first; visual as enhancement |
| Accessible corporate website | ++ | ++ | 0 | – | – | Semantic HTML/CSS/SVG with minimal optional motion |

### Library choices

| Tool | Use when | Avoid when | Production position |
|---|---|---|---|
| p5.js | Fast creative-coding sketches, learning, flow-field exploration | A small native Canvas loop is enough | Excellent for PoC; often refactor for product integration |
| PixiJS | Many 2D sprites, filters, a scene graph, GPU-backed 2D | You only need a few lines or paths | Strong for interactive 2D if lifecycle is well encapsulated |
| Three.js | 3D, camera, materials, postprocessing, shaders | The need is purely 2D decoration | Mature abstraction; GPU knowledge remains necessary |
| GSAP | Complex timelines, SVG, ScrollTrigger, cross-framework orchestration | Two or three simple CSS transitions are sufficient | Strong for production motion; implement cleanup and reduced motion |
| Motion / Framer Motion | React DOM/SVG microinteractions, gestures, layout animation | You do not use React or CSS can solve the state | Product-UI tool, not a particle/shader engine |
| D3 | Scales, layouts, data binding, bespoke visualization | Static standard charts are enough | Excellent; choose SVG or Canvas by data volume |
| regl | Custom WebGL rendering with explicit commands and state | A Three.js scene graph is more appropriate | Good for specialized GPU visualization |
| Matter.js | 2D collisions, constraints, playful physics | Simple tweening is enough | Solid engine; preserve determinism and UI predictability |
| Native browser APIs | The effect is small, controlled, and dependency cost matters | You need robust timeline, scene, physics, or GPU abstractions | Strong long-term option if the team can maintain it |

Do not add a library when an effect can be implemented stably with roughly 50–150 lines of native browser code, affects a single route, and does not need a scene graph, physics engine, complex timeline, or GPU abstraction. Add one when it removes tested lifecycle or rendering complexity that the team would otherwise need to own permanently.

## Ten Implementable Concepts

### 1. Converging brand landscape

- **Website type:** calm B2B SaaS landing page.
- **Visual idea:** fine lines begin in distributed positions and converge into three quiet “decision islands.”
- **Interaction:** pointer affects the field only locally and subtly.
- **Technology:** Canvas 2D, seeded flow field, CSS fallback.
- **MVP:** 250 lines, 30 fps, one seed, static reduced-motion frame.
- **Production version:** three LOD tiers, curated seeds per campaign, visual-regression tests, worker only if profiling requires it.
- **Effort:** MVP 3–5 days; production 2–3 weeks.
- **Risks:** low–medium performance risk; low accessibility risk if decorative and pausable.
- **Quality review:** check CTA contrast at multiple time points; ensure attention flows toward copy rather than away from it.

### 2. Interactive data mist

- **Website type:** analytics or observability product page.
- **Visual idea:** data points form clusters; filters condense or disperse a visual mist without pretending to be an exact chart.
- **Interaction:** hover and keyboard focus reveal a segment; click opens actual product information.
- **Technology:** PixiJS or instanced WebGL points with a DOM legend.
- **MVP:** 500 clearly marked demo data points and three filters.
- **Production version:** real aggregate data, accessible data table, fallback renderer, monitoring.
- **Effort:** MVP one week; production 3–4 weeks.
- **Risks:** medium–high performance; medium accessibility risk.
- **Quality review:** ensure color, point size, and legend never make unsupported statistical claims.

### 3. Living paper surface

- **Website type:** research, consulting, or editorial brand.
- **Visual idea:** nearly static fibers, micro-grain, and a very slow lighting drift create material presence.
- **Interaction:** none, or one-to-two-pixel parallax at most.
- **Technology:** CSS gradients plus a small Canvas layer; SVG filters only if profiling supports them.
- **MVP:** generated and cached texture; fully static in reduced-motion mode.
- **Production version:** light/dark tokens, contrast testing, deterministic server/client seed.
- **Effort:** 1–2 days MVP; 4–6 days production.
- **Risks:** low performance and accessibility risk.
- **Quality review:** no moiré at 100% or 200% zoom; material, not video-noise, appearance.

### 4. Hand-drawn hero scene

- **Website type:** education, culture, social innovation.
- **Visual idea:** a scene of Bézier paths and sketchy primitives draws itself in, then settles into minimal local motion.
- **Interaction:** focus or pointer triggers small detail responses.
- **Technology:** SVG plus Rough.js, or Canvas 2D.
- **MVP:** one scene, five objects, 1.5-second draw-on animation, then rest.
- **Production version:** semantic description, curated seeds, responsive recomposition.
- **Effort:** 4–6 days MVP; 2–3 weeks production.
- **Risks:** low–medium performance; medium accessibility when the illustration carries meaning.
- **Quality review:** line hierarchy, readability of objects, no accidental overlap with copy.

### 5. Scroll-driven product story

- **Website type:** explanatory SaaS or hardware page.
- **Visual idea:** a process object moves through input → analysis → result, with one visual state per content chapter.
- **Interaction:** native scrolling only; direct chapter navigation.
- **Technology:** GSAP ScrollTrigger or native CSS scroll timelines for simple cases.
- **MVP:** three sections in CSS/SVG, no mobile pinning.
- **Production version:** URL and focus states, reduced-motion slides, resize/back-navigation tests.
- **Effort:** one week MVP; 3–5 weeks production.
- **Risks:** medium performance; high accessibility risk without alternative navigation.
- **Quality review:** every section must make sense with animation disabled; avoid empty scroll distance.

### 6. Audio-reactive cultural visual

- **Website type:** festival, music label, exhibition.
- **Visual idea:** frequency bands control circular lines, color, and particle density.
- **Interaction:** explicit “start audio” control with volume and pause.
- **Technology:** Web Audio API with Canvas or WebGL.
- **MVP:** 64 frequency bins and a calm default state.
- **Production version:** track information, intensity settings, no-audio fallback, accessible playback controls.
- **Effort:** one week MVP; 3–4 weeks production.
- **Risks:** medium–high performance and high accessibility risk.
- **Quality review:** no hard flashes; visual should reflect structure without destabilizing typography.

### 7. Generative portfolio grid

- **Website type:** design or creative-development portfolio.
- **Visual idea:** project metadata controls variable grid cells; filters animate lines and transitions.
- **Interaction:** filters and focus; drag only if it genuinely helps; conventional list mode remains equivalent.
- **Technology:** CSS Grid with SVG/Canvas overlay; Motion or GSAP.
- **MVP:** six projects, two filters, deterministic placement in fixed grid rules.
- **Production version:** deep links, stable ordering, screen-reader list, visual diff tests.
- **Effort:** 4–6 days MVP; 2–4 weeks production.
- **Risks:** low–medium performance; medium accessibility risk.
- **Quality review:** test project findability against a conventional grid; avoid layout shift.

### 8. Data-driven network view

- **Website type:** knowledge graph, research, or learning product.
- **Visual idea:** nodes represent real categories and edges documented relationships; clusters come from a transparent logic.
- **Interaction:** search, filter, zoom, focus path, detail panel; core actions available by keyboard.
- **Technology:** D3 layout plus Canvas 2D; HTML controls and accessible result list.
- **MVP:** 100–300 nodes, precomputed layout, no continuous physics.
- **Production version:** worker layout, LOD, server search, alternative table/list.
- **Effort:** 1–2 weeks MVP; 4–6 weeks production.
- **Risks:** high performance and accessibility risk at scale.
- **Quality review:** verify visual relationships against source data; never imply links that do not exist.

### 9. Calm evidence ambient visual

- **Website type:** consulting, research, science-adjacent product.
- **Visual idea:** small points move slowly from “observation” through “review” to “evidence,” while uncertainty remains visible as controlled dispersion.
- **Interaction:** optional focus by process stage; otherwise passive.
- **Technology:** SVG or Canvas 2D.
- **MVP:** 60 points, three zones, 20–30 fps or SVG/CSS timeline.
- **Production version:** semantic legend, contextual design tokens, CMS-configurable message.
- **Effort:** 2–3 days MVP; 1–2 weeks production.
- **Risks:** low performance; low–medium accessibility.
- **Quality review:** should feel credible rather than like generic “technology particles.”

### 10. Interactive Canvas configurator

- **Website type:** product configurator, pricing, or customization flow.
- **Visual idea:** user parameters change form, material pattern, and labeling in real time.
- **Interaction:** semantic sliders and selects, undo/reset, presets; Canvas mirrors state.
- **Technology:** Canvas 2D for flat products; Three.js for genuine 3D geometry.
- **MVP:** three parameters and five validated presets.
- **Production version:** URL/cart state, export, server validation, 3D LOD, error fallback.
- **Effort:** 1–2 weeks MVP; 5–8 weeks production.
- **Risks:** medium–high performance and accessibility risk.
- **Quality review:** preview and purchasable configuration must derive from the same state source.

## End-to-End Team Workflow

| Step | Deliverables | Typical failure | Quality criteria | Tools/tests | Decide early |
|---|---|---|---|---|---|
| 1. Define goal, users, and brand effect | One-sentence hypothesis, target metric, no-go list | “Make something cool” without a job | Value and risk each explainable in one sentence | Workshop, user journey | Decorative, explanatory, or interactive role |
| 2. Gather references and style rules | Moodboard, three stills, motion storyboard, tokens | Copying references instead of abstracting principles | Clear sources, credits, and parameters | Figma, Are.na, screen recordings | Material, rhythm, density, contrast |
| 3. Choose technology and budget | Architecture decision record, support matrix, budgets | Choosing WebGL for prestige | Simplest suitable technology | MDN, support checks, bundle estimate | Baseline, fallback, target devices |
| 4. Build a minimal PoC | Isolated demo, fixed seed URL, performance baseline | Building the complete page first | One visual hypothesis is testable | Vite, Storybook, DevTools | Stop criteria |
| 5. Define parameter design system | Token file, valid ranges, presets | Magic numbers inside renderer | Designers can vary the system without code edits | Storybook controls, JSON schema | Public component API |
| 6. Iterate with LLMs/agents | Plan, small diffs, prompt log, tests | Mega-prompts and unreviewed full pages | Each iteration has a verifiable goal | Coding agent, Git worktree, browser | File scope, dependencies, definition of done |
| 7. Review visually | Screenshots at three viewports, 10-second video, review log | Checking only developer laptop | Still frame, timing, and interaction reviewed separately | Playwright, manual review | Reference seeds and review scale |
| 8. Test responsive, performance, accessibility | Device matrix, traces, audit report, keyboard protocol | Checking only a Lighthouse score | Real devices, throttling, reduced motion | DevTools, Lighthouse, axe, manual tests | Minimum device/browser support |
| 9. Refactor and integrate | Component, API docs, tests, cleanup checklist | Merging demo code directly | No globals, stable lifecycle, SSR-safe | TypeScript, ESLint, unit/E2E | Ownership and maintenance |
| 10. Deploy and monitor | RUM dashboard, error/fallback events | Lab metrics only | Field metrics segmented by device and route | Web Vitals/RUM, error monitoring | Feature flag and kill switch |
| 11. Secure degradation | Static/light version and feature detection | Blank canvas on errors | Core content always works | Context-loss and JS-off tests | Fallback ordering |
| 12. Evaluate impact | Experiment plan, interviews, metrics | Celebrating time-on-page alone | Predefined success and guardrail metrics | A/B test, recall/trust questions | Sample size, duration, segmentation |

### Review loop

1. Review the plan: APIs, dependencies, fallbacks, and what remains semantic HTML.
2. Approve the static frame: composition, hierarchy, brand fit, and contrast.
3. Approve motion: rhythm, duration, amplitude, rest phases, and reduced motion.
4. Approve interaction: pointer, touch, keyboard, reset, and error states.
5. Measure: CPU/GPU, frame time, long tasks, memory, bundle, and field metrics.
6. Refactor: separate renderer, simulation, state, and tokens; update regression tests.

## Reusable Prompting Framework

```text
ROLE
Act as a senior creative developer, motion designer, and frontend engineer.
Treat visual quality, semantics, performance, and accessibility as equal acceptance criteria.

PRODUCT AND BRAND CONTEXT
- Product:
- Brand promise:
- Tone:
- Existing design tokens:
- Associations to avoid:

PURPOSE
- Job of the visual element:
- User understanding or decision it should improve:
- Hypothesis / target metric:
- Is it decorative, informative, or interactive?

AUDIENCE AND USE
- Target audience:
- Primary devices and networks:
- Usage context:
- Languages and internationalization:

VISUAL ART DIRECTION
- References and the principles that may be borrowed:
- Style words with operational definitions:
- Shape language:
- Material/texture:
- Composition and negative space:
- Forbidden tropes:

COLOR AND TYPOGRAPHY
- Palette as tokens:
- Contrast requirements:
- Text remains HTML: yes/no and why:
- Blend mode/transparency limits:

MOTION
- Motion principle:
- Speed, amplitude, frequency:
- Easing/rhythm:
- Idle behavior and rest phases:
- Start/stop/pause behavior:
- Seed and reproducibility:

INTERACTION
- Pointer:
- Touch:
- Keyboard:
- Scroll:
- Audio/data:
- Reset/undo/error state:

TECHNICAL PLATFORM
- Browser/device support:
- Framework/version:
- Renderer: CSS/SVG/Canvas/WebGL/WebGPU:
- Allowed libraries and versions:
- Project structure and relevant files:
- SSR/hydration requirements:

RESPONSIVENESS
- Breakpoints/container queries:
- Mobile composition:
- Landscape/ultrawide:
- Resize behavior:

PERFORMANCE BUDGET
- Maximum additional JavaScript transfer:
- DPR cap:
- Target FPS/frame budget:
- Maximum particles/geometry/shader octaves:
- Offscreen/hidden-tab behavior:
- Target device and measurement method:

ACCESSIBILITY
- prefers-reduced-motion behavior:
- Pause/stop control:
- Semantic alternative:
- Keyboard/focus model:
- Contrast/flashing/vestibular limits:
- Screen-reader description:

CONSTRAINTS
- No external assets, Base64, or external requests.
- No unapproved dependencies.
- No telemetry or audio capture without consent.
- Respect the project’s Content Security Policy.

CODE QUALITY
- TypeScript strict.
- Separate rendering, simulation, interaction, and tokens.
- Clean up RAF, listeners, observers, workers, and GPU resources.
- No globals or magic numbers.
- Document public props and allowed parameter ranges.
- Include error and fallback states.

DOCUMENTATION AND EVIDENCE
- README explaining architecture, parameters, and trade-offs.
- List of commands executed.
- Build/test output.
- Screenshots at agreed viewports, seeds, and timestamps.
- Performance profile on the target device or defined throttling.

ACCEPTANCE CRITERIA
- Functional:
- Visual:
- Responsive:
- Performance:
- Accessibility:
- Tests:

WORKING METHOD
1. Inspect the repository and requirements without changing files.
2. Present a short plan, risks, and unresolved decisions.
3. Implement only the smallest vertical slice.
4. Run build, tests, and browser rendering.
5. Capture screenshots/profile and compare against the criteria.
6. Iterate no more than [N] cycles and report residual risks honestly.
```

## Critical Assessment and Recommendation

### Is it practically usable?

**Yes—LLM-assisted generative coding is practical for professional web work in 2026 when the model is used as a creative-engineering collaborator, not as an autonomous art director.** The economic value is greatest for teams that already have frontend and design-review competence, want to accelerate exploration, and can keep the visual scope bounded.

LLMs reduce the cost of boilerplate, experimentation, iteration, and refactoring. The scarce resources shift toward taste, specification quality, measurement, and review discipline. This does not mean that teams can skip rendering knowledge: the closer a project gets to GPU simulation, advanced 3D, sophisticated shaders, or accessible core interaction, the more specialist knowledge remains necessary.

### Where genuine advantage emerges

- An ownable generative brand system with curated rules, seeds, and motion tokens.
- Visual systems that explain actual product data or states and therefore cannot be replaced by a generic stock loop.
- A repeatable agent-and-review workflow with browser-based evaluation.
- Asset-free personalization by context, language, content, campaign, or data.
- Fast exploration of many variants inside stable technical and brand constraints.

Generic aurora gradients, glowing spheres, glass effects, particles, and cursor lenses rarely create durable advantage. They are easy to generate and quickly become recognizable as borrowed visual vocabulary.

### When to use other media

| Need | Better choice | Reason |
|---|---|---|
| Highly precise figurative illustration | Human illustration or curated artwork | Composition, character, and consistency are easier to control |
| Photoreal brand world | Video, 3D asset pipeline, or rendered media | Procedural browser code is often less predictable and more expensive |
| Exact product geometry | Optimized 3D model | Generated geometry does not replace CAD/DCC assets |
| Simple state feedback | CSS or UI motion library | Lower bundle cost, stronger semantics, easier maintenance |
| SEO/content-heavy page | HTML/CSS/SVG | Content and accessibility should dominate |
| A background needed only once | Optimized static asset | Continuous runtime cost is not justified |
| High-stakes data communication | Standard chart plus table | Accuracy, comparability, and accessibility outweigh novelty |

### Competencies that remain essential

Teams still need art direction, typography, motion design, perception and interaction psychology, JavaScript/TypeScript, rendering fundamentals, vector mathematics, shader basics, performance profiling, accessibility, browser QA, data-visualization ethics, and license review. LLMs lower the entry barrier while also increasing the amount of plausible-looking but insufficiently verified code.

### Avoiding AI slop

1. Define a specific brand metaphor and prohibited tropes.
2. Break references into transferable principles rather than copying their look.
3. Review static composition separately from motion.
4. Use curated seeds rather than unlimited randomness.
5. Remove an effect if it has no explainable product value.
6. Treat mid-range mobile and reduced motion as first-class scenarios.
7. Combine human design critique with screenshots, video, and measured performance evidence.
8. Integrate the visual into the real design system, content model, and user goal.

## Priorities

### Implement now

- An isolated, asset-free Canvas 2D or SVG hero proof of concept with a clear effect hypothesis.
- Seeded randomness, design tokens, and three curated presets.
- Reduced motion, static fallback, offscreen/hidden-tab pause, and DPR cap from day one.
- An agent workflow with plan, small diff, screenshot review, and executable checks.
- Three target viewports and at least one mid-range mobile device as acceptance baseline.
- Visual regression tests using fixed seed and time.

### Test later

- PixiJS or WebGL after demonstrating a real Canvas bottleneck.
- Workers/OffscreenCanvas after main-thread profiling, not preemptively.
- Data binding, contextual personalization, and multiple campaign seeds.
- Complex scrollytelling with native scroll timelines or GSAP.
- WebGPU as a progressive high-performance path with WebGL/Canvas fallback.
- Audio reactivity only where there is a clear cultural or product rationale and an explicit user gesture.

### Avoid

- Prompts such as “make a futuristic AI website” without brand, purpose, budgets, or acceptance criteria.
- Monolithic one-file demos in production code.
- Permanent 60-fps backgrounds when 20–30 fps or event rendering is sufficient.
- Text, navigation, or core data existing only inside Canvas.
- Scroll hijacking, blocking introductions, and lagging custom cursors.
- Unreviewed shader/demo code or unclear reuse licenses.
- Selecting a model solely from benchmark rankings.
- Performance or accessibility claims without tests.

## Two-Week Proof-of-Concept Roadmap

| Day | Focus | Deliverable / gate |
|---|---|---|
| 1 | Goal and hypothesis | One-pager: users, brand effect, KPI, no-go list |
| 2 | Art direction | Three still frames, motion storyboard, parameter list |
| 3 | Technology and QA | Architecture decision, browser matrix, performance/accessibility budget |
| 4 | Static composition | First Canvas/SVG still at three viewports |
| 5 | Base simulation | Deterministic loop, seed test, no interaction yet |
| 6 | Motion review | Ten-second recordings; select one rhythm |
| 7 | Interaction | Limited pointer/touch or scroll layer |
| 8 | Responsive/fallback | Mobile composition, reduced motion, feature fallback |
| 9 | Profiling | Trace FPS, memory, bundle; adjust LOD |
| 10 | Integration | Encapsulated component, props, cleanup, SSR safety |
| 11 | Tests | Playwright screenshots, E2E flow, automated accessibility audit, keyboard test |
| 12 | Stakeholder/user review | Five to eight qualitative sessions or structured review |
| 13 | Decision | Benefit, cost, risks, remaining production work |
| 14 | Demo and documentation | Reproducible build, README, go/no-go decision |

A successful proof of concept communicates its intended metaphor without explanation, does not weaken CTA visibility or readability, meets the target-device budget, and has a convincing calm fallback. A positive subjective impression alone is not enough.

## Six-to-Eight-Week Production Roadmap

| Week | Focus | Outcome |
|---|---|---|
| 1 | Discovery and art direction | Validated hypothesis, storyboard, reference principles, risks |
| 2 | Technical spike | Renderer choice, baseline profiles, fallback strategy, architecture |
| 3 | Visual system | Tokens, seeds, LODs, responsive compositions, approved presets |
| 4 | Interaction and content | Real states/data, keyboard/touch support, semantic alternatives |
| 5 | Integration | React/Next component, routing/SSR, CMS/analytics, cleanup |
| 6 | Hardening | Browser/device QA, memory, context loss, reduced motion, accessibility testing |
| 7 | Validation | Usability/brand test, conversion guardrails, bug fixes |
| 8 | Rollout | Feature flag, real-user monitoring, kill switch, ownership and backlog |

A six-week version is feasible only when discovery and technical spike work can run in parallel and visual variance remains constrained. Eight weeks are more realistic once real data, WebGL, audio, multiple scenes, or demanding accessibility requirements are involved.

## Final Review Checklists

### Design review

- [ ] The effect has a named product or brand function.
- [ ] A static frame already works compositionally.
- [ ] Palette, contrast, line weight, density, grain, and motion are tokenized.
- [ ] There are explicit rest phases and no competing motion centers.
- [ ] Mobile has an independent composition.
- [ ] Several seeds have been curated and extremes reviewed.
- [ ] Copy, CTA, and navigation remain dominant and conventional to operate.
- [ ] The output avoids generic AI visual tropes.

### Engineering review

- [ ] Rendering, simulation, interaction, state, and tokens are separated.
- [ ] Seed and time can be controlled in tests.
- [ ] RAF, listeners, observers, workers, and GPU resources are cleaned up.
- [ ] Resize, DPR, route transitions, Strict Mode, and hot reload do not create duplicate instances.
- [ ] No unauthorized assets, Base64 blobs, or external requests exist.
- [ ] Dependencies and copied code have reviewed licenses.
- [ ] Errors, lost WebGL context, and unavailable features have fallbacks.
- [ ] Build, type checking, linting, unit, E2E, and visual tests are reproducible.

### Performance review

- [ ] Budget and baseline were defined before optimization.
- [ ] A mid-range mobile device or constrained CPU test was used.
- [ ] DPR is capped and LOD reduces particles, geometry, shader, and blur cost.
- [ ] There is no unnecessary continuous RAF; offscreen and hidden-tab rendering pause.
- [ ] Frame times, long tasks, memory, and bundle size were measured rather than estimated.
- [ ] DOM motion primarily uses transform/opacity where applicable.
- [ ] Static layers are cached and per-frame allocations minimized.
- [ ] Real-user monitoring and a kill switch exist for rollout.

### Accessibility review

- [ ] Core content, navigation, and controls exist as semantic HTML.
- [ ] Canvas is either correctly hidden as decoration or has a genuine textual/functional alternative.
- [ ] Every action works by keyboard and has visible focus states.
- [ ] `prefers-reduced-motion` provides an equivalent experience.
- [ ] Automatically moving content offers pause/stop/hide where needed.
- [ ] Contrast was checked over multiple animation frames and states.
- [ ] No information is conveyed only by color, movement, or spatial position.
- [ ] Flashing, large zoom/parallax motion, and peripheral continuous movement are avoided or tightly constrained.
- [ ] Automated checks, keyboard, zoom, screen reader, and reduced-motion modes were tested manually.

## Final Recommendation

For professional product websites, the safest default is: **start with semantic HTML and a strong static composition, then add one procedural visual layer as progressive enhancement.** Canvas 2D and SVG cover most valuable hero, illustration, and ambient-interface applications with less risk than a full WebGL experience. Three.js/WebGL is justified when spatial representation, GPU particles, material simulation, or direct manipulation is central to the product story. WebGPU should be treated as a progressive option with an explicit fallback.

Model selection matters less than workflow quality. A capable model with browser access, a tightly scoped file boundary, executable checks, and a disciplined review loop is more useful than a marginally stronger benchmark score without real visual validation. The durable quality advantage comes from precise art direction, reproducible seeds, component-level agent work, real-device profiling, and informed human design criticism.
