# World-tree source assets

Source of truth for the Disce world tree (Yggdrasil) motif.

## Source master

- **`2.svg`** — the untouched generated source master for the world tree. Kept
  **byte-for-byte unmodified**, including its embedded generated metadata.
  Square `viewBox` (`0 0 2048 2048`); the artwork is a circular branch canopy
  with a trunk and winding roots.

## Production copy

- **`images/DISCE_D02_r1_world-tree-paper-background.svg`** — the production
  derivative used by `status.html`. Derived from `2.svg` by:

  - removing the single full-canvas opaque background path (all remaining paths,
    their `d` geometry and `transform` attributes are byte-identical);
  - adapting the artwork's appearance for the site's paper background —
    every remaining path is set to one quiet dark-forest colour
    (`#1E4B3A`, the `--green-forest` token), so no multiple original palette
    survives at low opacity;
  - overriding `preserveAspectRatio="none"` with `xMidYMid meet` (the square
    `viewBox` is preserved, so the tree can never be stretched);
  - stripping the generated `<metadata>` / C2PA block for runtime use;
  - adding `<title>` / `<desc>`.

  It is not rasterized, carries no gradients, filters, shadows or blend modes,
  and is rendered decorative (`aria-hidden="true"`, `alt=""`).

## Hygiene

- Do not keep a duplicate `2.svg` at the repository root; this directory is its
  only home.
- The remaining files in a typical exploration batch are rejected candidates and
  are git-ignored on purpose (see `.gitignore`).
