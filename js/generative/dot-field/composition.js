// Field definitions for the halftone-dot family.
//
// The static assets under images/derived/ are generated from the same maths by
// scripts/generate_dot_patterns.py; these functions are the animated form. All
// time dependence runs through sin/cos, so a full `phase` cycle (0 -> 1) returns
// to the start: every field loops seamlessly.
//
// Pure and node-checkable: pass a callback, no DOM, no canvas.

const TAU = Math.PI * 2;

// Per-field defaults; callers can override any of them via `params`.
const FIELD_DEFAULTS = {
  // radial bloom from an anchor (today's page-hero panel)
  bloom: { anchorX: 0.9, anchorY: 0.08, reach: 0.92, breathe: 0.10, wave: 96 },
  // concentric rings travelling outward from a centre (the "arena" focal).
  // `waves` = whole wavelengths travelled per cycle (integer => seamless);
  // `breathe` = gentle expansion/contraction of the whole field (the pulse).
  arena: { cx: 0.5, cy: 0.5, ring: 40, waves: 3, reach: 0.6, breathe: 0.08 },
  // organic drift along a smooth vector field
  current: { amp: 7.5 }
};

/**
 * Walk the dot lattice and yield (x, y, r, colorIndex) for every drawable dot.
 * colorIndex is 0 for the primary colour, 1 for the secondary.
 *
 * @param {string} field  'bloom' | 'arena' | 'current'
 * @param {object} opts   width, height, pitch, radius, minRadius, phase (0..1), params
 * @param {(x:number,y:number,r:number,colorIndex:number)=>void} cb
 */
export function forEachDot(field, opts, cb) {
  const {
    width = 1,
    height = 1,
    pitch = 17,
    radius = 6,
    minRadius = 0.06,
    phase = 0,
    params = {}
  } = opts || {};

  const cfg = Object.assign({}, FIELD_DEFAULTS[field] || FIELD_DEFAULTS.bloom, params);
  const ph = (((phase % 1) + 1) % 1) * TAU;
  const step = pitch;

  // Half-step offset keeps the lattice centred rather than edge-anchored.
  for (let y = step * 0.5; y < height; y += step) {
    for (let x = step * 0.5; x < width; x += step) {
      let r = 0;
      let ox = 0;
      let oy = 0;
      const colorIndex = 0;

      if (field === 'arena') {
        const ax = width * cfg.cx;
        const ay = height * cfg.cy;
        const reach = Math.min(width, height) * cfg.reach;
        // Whole-field breath so the rings expand and settle, not just drift.
        const breathe = 1 + cfg.breathe * Math.sin(ph);
        const d = Math.hypot(x - ax, y - ay) / breathe;
        if (d > reach) continue;
        // d/ring - waves*phase: `waves` full wavelengths per cycle, so the
        // rings travel outward and the loop closes.
        const wave = 0.5 + 0.5 * Math.sin(d / cfg.ring - cfg.waves * ph);
        r = radius * (minRadius + (1 - minRadius) * wave) * (1 - d / (reach * 1.1));
      } else if (field === 'current') {
        const a = Math.sin(x / 190 + ph) * Math.PI + Math.cos(y / 150 - ph) * Math.PI;
        ox = Math.cos(a) * cfg.amp;
        oy = Math.sin(a) * cfg.amp;
        r = radius * (minRadius + (1 - minRadius) * (0.5 + 0.5 * Math.sin(x / 140 - y / 110 + ph)));
      } else {
        // bloom
        const ax = width * cfg.anchorX;
        const ay = height * cfg.anchorY;
        const reach = Math.max(width, height) * cfg.reach * (1 + cfg.breathe * Math.sin(ph));
        const d = Math.hypot(x - ax, y - ay);
        const base = Math.max(minRadius, 1 - d / reach);
        r = radius * base * (0.8 + 0.2 * Math.sin(d / cfg.wave - ph));
      }

      if (r > 0.25) cb(x + ox, y + oy, r, colorIndex);
    }
  }
}
