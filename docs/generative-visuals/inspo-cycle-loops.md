# Research brief — cycle / loop visuals for an editorial research brand

**Scope:** the Development Status loop slot only (four stages: draft → test → decide → keep/discard). No implementation; no stills.
**Date:** 2026-09-15
**Method:** plain web research with attributed sources. The Inspo MCP was vetted and **not registered** (see the round report); the fallback was used deliberately so every source below is citable and directly inspectable.
**Design constraints assumed:** calm; paper/ink/hairline; a single ochre accent; DE/EN; hairline SVG; static frame must carry the metaphor on its own.

---

## 1. How credible editorial / research / science-adjacent sites show cyclical processes

| # | Source (URL) | Visual mechanism | Hierarchy | Motion principle | Likely / documented tech | Accessibility & performance risk | One transferable principle |
|---|---|---|---|---|---|---|---|
| 1 | Wikipedia, *PDCA* — <https://en.wikipedia.org/wiki/PDCA> (ring `File:PDCA_Cycle.svg`; spiral `File:PDCA-Multi-Loop.png`) | Four labelled nodes on a circle joined by directional arrows; a second image re-draws the same four steps as an open spiral across iterations | Stage labels dominate; arrows carry direction; the ring is the frame | Usually static; the point is the *sequence*, not movement | SVG (and a staircase/spiral export) | Direction conveyed by arrowheads only → needs a textual order; colour carries nothing | **Name the stations and show the return explicitly** — a bare ring is tautological; the sequence is the content |
| 2 | Ellen MacArthur Foundation, *butterfly diagram* — <https://www.ellenmacarthurfoundation.org/circular-economy-diagram> (PNG/PDF download) | Two stacked loops (technical / biological) that share a vertical spine; branch arrows fall out of and return to the spine | Two nested cycles read left-to-right; dense labels sit on the loops | Static infographic; motion is not part of the argument | Static vector/illustration, offered as downloadable assets | Very dense small type; no DOM text; fails as a text alternative without a described version | **Two cycles can share one spine**; branching in and out of a common axis is legible without a full diagram |
| 3 | USGS Water Science School, *Water cycle* — <https://www.usgs.gov/special-topics/water-science-school/science/water-cycle> | A "pools and fluxes" grammar: reservoirs (where water is stored) plus arrows (where it moves), across a landscape | Prose first; the diagram is a summary; a separate *pools & fluxes data tables* page carries the numbers | Static; human impact described in words | Illustrated diagram, downloadable, plus an explicit data-table companion | The illustrated diagram alone is not accessible; the **table equivalent** is what makes it so | **Pair the diagram with a DOM/data equivalent** — make the picture a view of data, not the data itself |
| 4 | Wikipedia, *Causal loop diagram* — <https://en.wikipedia.org/wiki/Causal_loop_diagram> | Variables as words, directed edges marked `+`/`−`, loops labelled `R` (reinforcing) or `B` (balancing); delays drawn as a bar across an edge | Edge labels and loop labels matter more than node positions | One animated example shows links drawing on; the semantics are static | SVG / animated GIF | Relies on `+`/`−` glyphs and arrow direction; colour is not the only cue (good) but the glyphs need a legend | **Mark the role of each link, not just its direction** — say what the edge *does* |
| 5 | Wikipedia, *Ouroboros* — <https://en.wikipedia.org/wiki/Ouroboros> | A single closed body devouring its tail; no start, no end, no nodes | One figure; meaning is in the closure itself | Static by nature; animation would have to justify itself | Historical illustration; vector redraws | If used decoratively, no risk; if it carries meaning it needs a text label | **Closure can be the payload** — the figure can mean "loop" with no arrows at all |
| 6 | Wikimedia Commons, *Category:SVG Ouroboros* — <https://commons.wikimedia.org/wiki/Category:SVG_Ouroboros> (e.g. `File:Ouroboros-benzene.svg`) | Reusable vector ouroboros, including a benzene/technical variant where the ring holds interior structure | The ring is the silhouette; interior detail is secondary | Static | SVG, CC-licensed redraws | Licensing varies per file; some are stylised enough to be brand-like | **A hairline ring can hold interior structure** (nodes, bonds, labels) without boxes |

**Cross-cutting read:** the credible examples earn the cycle in one of two ways — either they **label the stations and show the return** (PDCA, butterfly), or they **make the closure itself the meaning** (ouroboros). The failure mode on our page was neither: a ring drawn around four chips, with the ring adding no information.

---

## 2. Ouroboros conventions in line-illustration / engraving traditions

Verified examples and what each demonstrates:

| Source (URL) | Convention it shows |
|---|---|
| *Chrysopoeia of Cleopatra*, MS Marciana gr. Z. 299 (3rd c. Alexandria, 10th c. copy) — <https://commons.wikimedia.org/wiki/File:Chrysopoea_of_Cleopatra_1.png> | The canonical **single closed snake**, tail in mouth, enclosing the words *hen to pan* (ἓν τὸ πᾶν, "the all is one"); the body is divided into **black and white halves** — a built-in two-value contrast with no extra ornament |
| Alchemical dragon ouroboros, 1478 tract — <https://commons.wikimedia.org/wiki/File:Serpiente_alquimica.jpg> | **Dragon/wyvern register**: scales, limbs, a heavier body; the tail enters the mouth at the lower-left, so the junction is placed off the vertical axis rather than at top-centre |
| *Book of Kells*, fol. 124r (c. 800) — <https://commons.wikimedia.org/wiki/File:KellsFol124rTuncCrucifixerant.jpg> | **Interlaced/ornamental** register: the body is a continuous ribbon woven around itself; barely reads as a creature — closure as pure ornament |
| Lucas Jennis, *De Lapide Philosophico*, 1625 (engraving) — <https://commons.wikimedia.org/wiki/File:Ouroboros_1.jpg> | **Engraved emblem**: hatch-drawn wyvern in a ring, used as a symbol for mercury; the loop frames a single concept and sits inside a titled plate |
| *Aurora Consurgens* (15th c.) — <https://commons.wikimedia.org/wiki/File:Aurora_consurgens_zurich_044_f-21v-44_dragon-pot.jpg> | Ouroboros among sun/moon/mercury emblems — the loop as one element in a **symbol set**, not a standalone diagram |
| Kekulé, benzene ring — <https://commons.wikimedia.org/wiki/File:Ouroboros-benzene.svg> | **Technical register**: the same closure re-read as a structural ring, with interior bonds — the point where ornament becomes notation |
| Theosophical Society seal — <https://commons.wikimedia.org/wiki/File:Theosophicalsealfrench.svg> | **Framing register**: the ouroboros as an outer border enclosing an emblem; the loop bounds content rather than being the content |

**Conventions, distilled:**

1. **Body continuity** — one continuous line (Chrysopoeia, Kells) versus a segmented/articulated body (Jennis, the 1478 dragon). A continuous line reads older, calmer, and survives hairline rendering; segmentation invites scale/detail we do not want.
2. **Head/tail junction** — the classic junction is the mouth taking the tail. Placement matters: on-axis (top/bottom) reads heraldic and symmetrical; off-axis (1478 dragon) reads naturalistic and less rigid.
3. **Two-value body** — the Chrysopoeia's black/white halves are the precedent for a **two-tone body**: this maps cleanly onto ink + paper (or ink + a single ochre segment) without inventing colour.
4. **Ornamental vs. technical** — ornamental (Kells) hides structure; technical (Kekulé) exposes it. Our slot is informative, so the transferable move is the **technical ouroboros**: keep the closure, but let the ring carry readable stations.
5. **Framing vs. central** — the seal tradition shows the loop can *enclose*: four station labels could sit inside the ring rather than on boxes outside it.

**Which of these translate to hairline SVG in this palette:**
- A **single continuous hairline ring** (ink on paper) with one **ochre segment** for the active stage — the two-value body, reduced to two tokens.
- **Head/tail junction off the top axis**, drawn as a simple tapered overlap (no eyes/teeth): the closure reads without illustration.
- **Stations as small-caps labels inside the ring** (seal framing), or as short ticks on the ring — no chips, no rail.
- **Resist scale and interlace** (Kells/Jennis): they fight the hairline and the calm.

---

## 3. Art-direction proposals (textual; no code, no stills this round)

### Proposal A — "The quiet ouroboros" (closure is the meaning)
- **Metaphor (one sentence):** the kernel is a single line that returns to itself — draft enters test, test enters decide, decide keeps or discards, and the tail meets the mouth.
- **Why the static frame carries it:** one continuous hairline ring with four small-caps labels placed *inside* the ring at the four stations, plus a single ochre segment marking one stage. No boxes, no rail; the closure is legible at a glance and there is no dead space because the figure is a single ring.
- **How motion later adds meaning (not movement):** an ochre segment travels the ring, stage by stage, pausing at each label — the pause, not the travel, is the information ("decision", "rest"). A discard branch could briefly reverse the segment.
- **Honest risk:** an ouroboros without a head/tail junction is just a circle; with a too-literal head it becomes a creature and breaks the editorial register. The junction must be minimal and deliberate, and the four labels must stay legible at 375 px inside a shrinking ring.

### Proposal B — "Emblem plate" (seal framing)
- **Metaphor (one sentence):** the loop is a seal around the kernel's method — a ring that bounds four named stages, like an alchemical emblem rather than a flowchart.
- **Why the static frame carries it:** the ring frames the stations; the stations sit on a quiet central axis or cross inside it. It reads as a *plate* (matching the site's print/emblem language) and sizes to content.
- **How motion later adds meaning:** the ring's ochre segment advances only when a stage completes; the emblem itself stays still, so motion is a state indicator rather than decoration.
- **Honest risk:** emblem/ring composition can tip into decorative mysticism (occult/alchemical connotations) that a research brand may not want; and a ring plus four labels is the closest to the reverted design, so it must not become "boxes inside a circle".

### Proposal C — "Stations on a serpent" (technical ouroboros)
- **Metaphor (one sentence):** the process *is* the body — four stations are ticks along one continuous line whose head and tail meet.
- **Why the static frame carries it:** the sequence is unavoidable because the labels sit *on* the path in order; the head/tail junction is the only junction, so the loop is explicit without a separate return rail. Reads like the Kekulé/technical register.
- **How motion later adds meaning:** a single token walks the body and *stops* at each tick; the keep/discard decision appears as the token either continuing or crossing back at the junction.
- **Honest risk:** placing text on a curved path hurts legibility at small sizes and is hard to keep accessible; the "serpent" can read as gimmick if the taper/head are over-drawn.

**Recommendation (owner decides):** **Proposal A** as the primary, with **Proposal C's** single-path discipline as a constraint — one continuous hairline, labels inside the ring, one ochre segment, and a minimal off-axis head/tail junction. Prefer A over C because on-path text is the main accessibility and mobile risk, and A keeps labels as ordinary DOM text. Proposal B is the most "plate-like" and should be kept as the fallback if A's junction reads as a mere circle.

---

## 4. Question list — what I need to turn a chosen proposal into stills

1. **Metaphor emphasis:** should the loop read as *self-renewing* (ouroboros: eternal return) or as *iterative-with-exit* (draft → … → keep/discard, then a new pass)? The two pull the junction and the ochre marker in different directions.
2. **Figuration vs. abstraction:** how far toward a creature may the line go — a bare overlapping stroke, a tapered tail, or a recognisable (if minimal) head? A hard "no head" answer changes the composition.
3. **Where the plate sits:** inside `.status-projects` after the project cards (as the first attempt did), or in the `.long-range` dark band, or as a full-width band of its own? This decides palette inversion (ink-on-paper vs parchment-on-forest) and size.
4. **Ring vs. rail:** is a radial/closed composition acceptable, given the reverted design was criticised for a "tautological static loop"; or would a path with an explicit return read as less circular-for-its-own-sake?
5. **Labels:** keep the four approved stage labels exactly (Entwurf / Prüfung / Entscheidung / Behalten oder verwerfen), and keep the approved caption below the plate? Any change to either is new copy sign-off.
6. **Ochre budget:** confirm the single ochre element per plate (the travelling/parked segment), with the pause control's indicator neutral when running and ochre only when paused — as proposed in the reverted round.
7. **Static-only or motion-ready:** should the stills already reserve the geometry for the later token motion (fixed ring radius, a junction that can host a reversal), or is pure still framing enough for the pick?

---

## Sources

- Wikipedia, *PDCA* — <https://en.wikipedia.org/wiki/PDCA> (accessed 2026-09-15)
- Ellen MacArthur Foundation, *The butterfly diagram* — <https://www.ellenmacarthurfoundation.org/circular-economy-diagram> (accessed 2026-09-15)
- USGS Water Science School, *Water cycle* — <https://www.usgs.gov/special-topics/water-science-school/science/water-cycle> (accessed 2026-09-15)
- Wikipedia, *Causal loop diagram* — <https://en.wikipedia.org/wiki/Causal_loop_diagram> (accessed 2026-09-15)
- Wikipedia, *Ouroboros* — <https://en.wikipedia.org/wiki/Ouroboros> (accessed 2026-09-15)
- Wikimedia Commons, *Category:Ouroboros* and *Category:SVG Ouroboros* — <https://commons.wikimedia.org/wiki/Category:Ouroboros> · <https://commons.wikimedia.org/wiki/Category:SVG_Ouroboros> (accessed 2026-09-15)
- File pages cited in §2 (Chrysopoeia of Cleopatra, 1478 alchemical dragon, Book of Kells, Jennis 1625, Aurora Consurgens, Kekulé benzene, Theosophical seal) — all on <https://commons.wikimedia.org> (accessed 2026-09-15)

*No layouts, copy, or branded identity are reproduced above; each entry yields one abstracted principle only.*
