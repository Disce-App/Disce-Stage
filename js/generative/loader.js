// Discovers [data-gen] mounts and hands each one to its module.
//
// The plate markup ships hidden. It is revealed only after a successful mount,
// so a no-JS render, a failed import, or a thrown error leaves the page exactly
// as it was — the fallback is the current look of the section.
//
// Test hooks (used by the dev-only CDP harness, never by production code):
//   ?gen-seed=<value>   override the per-plate data-seed
//   ?gen-motion=off|on  force motion off/on (off = frozen frame)
//   ?gen-phase=<0..1>   fractional position of the frozen frame
import { registry } from './registry.js';

const params = new URLSearchParams(window.location.search);
const seedOverride = params.get('gen-seed');
const phaseOverride = params.get('gen-phase');
const motionOverride = params.get('gen-motion');

function prefersReducedMotion() {
  return typeof window.matchMedia === 'function'
    && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

function resolveMotion() {
  if (motionOverride === 'off') return false;
  if (motionOverride === 'on') return true;
  return !prefersReducedMotion();
}

async function mountAll() {
  const mounts = Array.from(document.querySelectorAll('[data-gen]'));
  for (const el of mounts) {
    const name = el.getAttribute('data-gen');
    const load = registry[name];
    if (!load) continue;
    try {
      const mod = await load();
      const seed = seedOverride || el.getAttribute('data-seed') || name;
      const phase = phaseOverride === null ? 0 : Number(phaseOverride);
      mod.mount(el, { seed, motion: resolveMotion(), phase });
      el.hidden = false;
    } catch (error) {
      // Leave the plate hidden; the page keeps its current appearance.
      if (window.console && console.error) {
        console.error('[generative] mount failed:', name, error);
      }
    }
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', mountAll, { once: true });
} else {
  mountAll();
}
