# Ouroboros source assets

Source of truth for the Disce Ouroboros emblem.

## Selected master

- **`N3.svg`** — the approved source master (design direction **N3**), chosen for its
  engraved, organic, surreal character and its **branching tail** (the antler-like
  continuation), which is the ownable Disce detail: a living iteration / branching
  continuation, not a generic snake mark.
- This archival file is kept **unmodified**, including its embedded **C2PA**
  provenance manifest.

## Production copy

- **`images/DISCE_D01_r2_ouroboros-branching-forest.svg`** — the single production
  asset, used only by `status.html` in the Kernel spotlight and shown only while
  that field is forest green. Derived from `N3.svg` by removing the C2PA
  `<metadata>` block and the full-canvas background path, and recolouring the
  engraving for the forest-green field (parchment body, ochre band, forest
  cut-outs). Path geometry, dimensions and composition are unchanged;
  `preserveAspectRatio` is `xMidYMid meet`; it was not rasterized.

## Hygiene

- `images/DISCE_D01_r1_ouroboros-branching.svg` (the earlier C2PA-stripped
  intermediate) and `images/DISCE_D01_r3_ouroboros-paper-trace.svg` (an ink
  paper-state variant) were **removed**: neither has a runtime consumer, and the
  local project marks are intentionally invisible on paper.
- The recolored `disce-ouroboros-light.svg` / `disce-ouroboros-dark.svg` derivatives
  and the exploration `.zip` were **removed** — they are not approved source assets
  and must not be used.
- The remaining files (`N1`, `N2`, `N4`–`N8`, `*.webp`) are **rejected exploration**
  and are git-ignored on purpose (see `.gitignore`).
