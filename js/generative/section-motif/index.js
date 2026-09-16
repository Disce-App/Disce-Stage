import { motifSvgMarkup } from './composition.js';

// Decorative section motif for the Philosophy page. Static by design for now:
// the stills are reviewed first, and motion (if any) is a later batch.
//
// Mounted by js/generative/loader.js from a hidden, aria-hidden plate anchored
// to its heading; the section identity comes from data-section, combined with
// the base seed. It carries no text and adds no semantics.
export function mount(el, { seed = 'motif' } = {}) {
  const section = el.getAttribute('data-section') || '';
  el.innerHTML = motifSvgMarkup({ seed, section });
  return {
    destroy() {
      el.innerHTML = '';
    }
  };
}
