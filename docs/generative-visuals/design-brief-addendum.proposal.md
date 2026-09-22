# Proposed `DESIGN-BRIEF.md` addendum — generative visuals

**Status:** proposal only — **not applied** to `DESIGN-BRIEF.md`.
**Approved in principle:** 2026-09-15 (owner decision #8). This file exists so the
diff can be reviewed before it touches the binding brief.

**Outcome log (2026-09-15):** Track A — the first kernel-loop plate was reverted
(`ad8dec4`, composition under redesign; groundwork `63e12a3` kept, inert) and is
being redesigned as static candidates. Track B — the Philosophy motif system
shipped on base seed `motif-02` (`e90b99f`), then the four Philosophy AI image
placements and their sole-use derivatives were removed (`e010cdb`), replaced by
the motif system; the two bands keep their pull-quote copy via `.band--text`.

`DESIGN-BRIEF.md` currently governs static raster imagery only and contains no
generative, motion, or animation guidance. The section below is written to match
the brief's existing voice and sits after the current §13.

## Proposed diff

```diff
@@ end of DESIGN-BRIEF.md (after §13 Open Decisions) @@
+
+## 14. Generative visuals (code-rendered)
+
+Generative visuals are an optional enhancement, never a rework. They inherit the
+§7 rule — an image or a visual either serves a function or it goes.
+
+- **Deletable by default.** A generative visual must survive removal without the
+  page losing meaning. Its static, reduced-motion, and JavaScript-free fallback
+  is the current look of that section; it is mounted by JavaScript and revealed
+  only on success.
+- **Palette from tokens only.** No new hues. `--ochre` stays the single loud
+  accent; surfaces, hairlines, and type come from the existing custom properties.
+  Square corners, 1–2px hairlines, ochre diamond markers, controlled seeded
+  irregularity. No gradients, no glassmorphism, no rounded "friendly tech" cards,
+  no gamification patterns (§8, §11).
+- **Motion scale.** Ambient motion uses the `--gen-*` tokens, not the UI
+  durations (`--dur-*`, 120–260ms). Motion is one calm loop with an explicit rest
+  phase, local rather than full-screen.
+- **`prefers-reduced-motion: reduce`** shows a meaningful static frame, never a
+  blank or broken state. Any persistent automatic motion carries a keyboard
+  pause/play control, labelled in both languages.
+- **Budgets.** No generative visual enters the LCP path. CLS stays 0 (explicit
+  dimensions/aspect-ratio). Diagram-class SVG carries no `requestAnimationFrame`;
+  Canvas-class visuals cap DPR (1.5 mobile / 2 desktop), target 20–30 fps, pause
+  offscreen and in hidden tabs, and clean up fully on destroy. Default additional
+  JS budget: ≤ 8 kB gzip per diagram-class visual.
+- **Accessibility.** Core copy, labels, and controls stay semantic HTML. A
+  decorative rendering surface is `aria-hidden`; an informative one has an
+  equivalent DOM description. Contrast is verified over the whole animation cycle.
+- **Architecture.** Plain ES modules under `js/generative/`, no build step and no
+  dependencies. Tokens, simulation, and rendering stay separate.
+- **Copy.** Any user-facing string a visual needs (label, caption, description,
+  control) is bilingual DE/EN and needs the same copy sign-off as every other
+  string on the site.
+- **Evidence.** Verification uses the dev-only CDP harness: fixed seed and
+  frozen time, 375/768/1440 in DE and EN, console/overflow/asset checks,
+  reduced-motion and keyboard review, and a measured JS weight.
```

## Notes for the reviewer

- This adds guidance only; it does not change any existing rule.
- If preferred, the same text can be inserted as a new §10.5 (after
  Accessibility & Performance Budgets) with renumbering of §11–§13; appending as
  §14 keeps the diff minimal.
- On approval, apply the section to `DESIGN-BRIEF.md` in its own bounded commit.
