// Frozen reads of the CSS custom properties the generative modules depend on.
//
// Values live in css/experimental.css (:root) and are never duplicated in JS.
// CSS references them directly wherever it can; this module exists for the
// places JS genuinely needs the value (e.g. geometry jitter).
const NAMES = [
  '--ochre',
  '--legacy-ink',
  '--legacy-paper',
  '--line-soft',
  '--muted',
  '--ink-soft',
  '--parchment',
  '--green',
  '--green-dark',
  '--green-sage',
  '--green-forest',
  '--font-body',
  '--fs-100',
  '--fs-200',
  '--gen-cycle',
  '--gen-jitter'
];

let cache = null;

export function getTokens() {
  if (cache) return cache;
  const out = {};
  if (typeof window !== 'undefined' && window.getComputedStyle) {
    const styles = window.getComputedStyle(document.documentElement);
    for (const name of NAMES) {
      out[name] = styles.getPropertyValue(name).trim();
    }
  }
  cache = Object.freeze(out);
  return cache;
}
