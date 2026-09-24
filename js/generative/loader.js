// Discovers [data-gen] mounts and hands each one to its module.
//
// The plate markup ships hidden. It is revealed only after a successful mount,
// so a no-JS render, a failed import, or a thrown error leaves the page exactly
// as it was – the fallback is the current look of the section.
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

// Hero dot-field mounts are decorative and their static CSS plate is already
// visible at first render. Importing the canvas module and starting its rAF loop
// during initial load competes with the first paint, so those mounts are
// deferred to load + idle; every other mount keeps its immediate behavior.
const HERO_SELECTOR = '.dot-field--hero';
// Must match the CSS breakpoint that hides `.dot-field--hero` (display:none).
const HERO_HIDDEN_MAX_PX = 768;
// Bounded fallback so the enhancement is never deferred indefinitely, and so a
// browser without requestIdleCallback still mounts it. 1500 ms is comfortably
// after first paint/interactivity on a loaded page yet still prompt.
const HERO_IDLE_TIMEOUT_MS = 1500;

// Guards against double mounting if the loader is executed more than once.
const mounted = new WeakSet();

function isHeroHiddenByCss() {
  if (typeof window.matchMedia === 'function') {
    return window.matchMedia('(max-width: ' + HERO_HIDDEN_MAX_PX + 'px)').matches;
  }
  return window.innerWidth <= HERO_HIDDEN_MAX_PX;
}

// a. wait for window.load if the document is not fully loaded;
// b. then schedule with requestIdleCallback;
// c. fall back to setTimeout where requestIdleCallback is unavailable;
// d. both paths are bounded by HERO_IDLE_TIMEOUT_MS (never deferred forever).
function afterLoadIdle(callback) {
  const schedule = function () {
    if (typeof window.requestIdleCallback === 'function') {
      window.requestIdleCallback(callback, { timeout: HERO_IDLE_TIMEOUT_MS });
    } else {
      window.setTimeout(callback, HERO_IDLE_TIMEOUT_MS);
    }
  };
  if (document.readyState === 'complete') schedule();
  else window.addEventListener('load', schedule, { once: true });
}

function mountOne(el, name) {
  if (!el || mounted.has(el)) return; // avoid duplicate mounting
  const load = registry[name];
  if (!load) return;
  mounted.add(el);
  load().then(function (mod) {
    const seed = seedOverride || el.getAttribute('data-seed') || name;
    const phase = phaseOverride === null ? 0 : Number(phaseOverride);
    mod.mount(el, { seed, motion: resolveMotion(), phase });
    el.hidden = false;
  }).catch(function (error) {
    // Leave the plate as-is; the page keeps its current appearance.
    if (window.console && console.error) {
      console.error('[generative] mount failed:', name, error);
    }
  });
}

function init() {
  const mounts = Array.from(document.querySelectorAll('[data-gen]'));
  const heroMounts = mounts.filter(function (el) { return el.matches(HERO_SELECTOR); });
  const otherMounts = mounts.filter(function (el) { return !el.matches(HERO_SELECTOR); });

  // Non-hero mounts keep their existing immediate behavior.
  otherMounts.forEach(function (el) { mountOne(el, el.getAttribute('data-gen')); });

  // Nothing to schedule when the page has no hero dot field.
  if (heroMounts.length === 0) return;

  afterLoadIdle(function () {
    // The hero dot field is display:none at <=768px, so mounting it there has no
    // visible benefit. If the viewport grows after load, a reload mounts it.
    if (isHeroHiddenByCss()) return;
    heroMounts.forEach(function (el) { mountOne(el, el.getAttribute('data-gen')); });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init, { once: true });
} else {
  init();
}
