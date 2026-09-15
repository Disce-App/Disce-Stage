// Motion is entirely CSS-driven: one stroke-dashoffset loop defined in
// css/experimental.css, over a path normalised with pathLength="100".
//
// This module only provides the deterministic frozen offset used by
// prefers-reduced-motion, ?gen-motion=off, and screenshot captures. There is no
// requestAnimationFrame anywhere in this visual.
export function frozenDashoffset(phase = 0) {
  const value = Number(phase);
  const clamped = Number.isFinite(value) ? Math.min(1, Math.max(0, value)) : 0;
  return `${(-clamped * 100).toFixed(2)}`;
}
