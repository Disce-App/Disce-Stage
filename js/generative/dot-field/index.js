// Animated halftone-dot field.
//
// Progressive enhancement: the mount element already carries the matching
// static PNG as its background, so a no-JS render, a failed import, or
// `prefers-reduced-motion: reduce` all keep exactly the intended still. When
// motion is allowed the module covers it with a canvas that drives the same
// field over time (see composition.js).
//
// Contract (GENERATIVE_WEB_VISUALS_COMPETENCY.md): one rAF, DPR capped, pause
// offscreen and in hidden tabs, resize-aware, full cleanup in destroy(),
// decorative (aria-hidden), no dependencies.
import { forEachDot } from './composition.js';
import { attachReactive } from './reactive.js';
import { getTokens } from '../tokens.js';

const DPR_CAP = 2;
const TAU = Math.PI * 2;

export function mount(el, { motion = true, phase = 0 } = {}) {
  // The pointer reaction is independent of motion, so the static plate reacts
  // under `prefers-reduced-motion` and `?gen-motion=off` as well.
  const detachReactive = attachReactive(el);

  // No motion: leave the static CSS fallback untouched (also the test hook
  // `?gen-motion=off`). Reduced motion must never get a blank or broken state.
  if (!motion) return { destroy: detachReactive };

  const field = el.getAttribute('data-field') || 'bloom';
  const tokens = getTokens();
  const colorA = tokens['--green'] || '#4FAC4E';
  const colorB = tokens['--green-dark'] || '#357435';
  const cycleMs = (parseFloat(tokens['--gen-cycle']) || 26) * 1000;

  const style = getComputedStyle(el);
  const pitch = parseFloat(style.getPropertyValue('--dot-pitch')) || 17;
  const radius = parseFloat(style.getPropertyValue('--dot-radius')) || 6;
  const minRadius = parseFloat(style.getPropertyValue('--dot-min')) || 0.06;

  const canvas = document.createElement('canvas');
  canvas.className = 'dot-field-canvas';
  canvas.setAttribute('aria-hidden', 'true');
  el.appendChild(canvas);
  // Hide the static fallback only once the canvas is live.
  el.classList.add('is-gen-active');

  const ctx = canvas.getContext('2d');
  const dpr = Math.min(window.devicePixelRatio || 1, DPR_CAP);
  let w = 1;
  let h = 1;
  let running = false;
  let raf = 0;
  let start = performance.now();
  let lastPhase = phase;

  function size() {
    const rect = el.getBoundingClientRect();
    w = Math.max(1, Math.round(rect.width));
    h = Math.max(1, Math.round(rect.height));
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function draw(phaseValue) {
    ctx.clearRect(0, 0, w, h);
    let current = -1;
    forEachDot(field, { width: w, height: h, pitch, radius, minRadius, phase: phaseValue }, (x, y, r, colorIndex) => {
      if (colorIndex !== current) {
        ctx.fillStyle = colorIndex ? colorB : colorA;
        current = colorIndex;
      }
      ctx.beginPath();
      ctx.arc(x, y, r, 0, TAU);
      ctx.fill();
    });
  }

  function frame(now) {
    if (!running) return;
    raf = requestAnimationFrame(frame);
    lastPhase = ((now - start) % cycleMs) / cycleMs;
    draw(lastPhase);
  }

  function play() {
    if (running) return;
    running = true;
    start = performance.now();
    raf = requestAnimationFrame(frame);
  }

  function pause() {
    running = false;
    cancelAnimationFrame(raf);
  }

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) play();
      else pause();
    });
  }, { threshold: 0.02 });
  io.observe(el);

  function onVisibility() {
    if (document.hidden) pause();
    else play();
  }
  document.addEventListener('visibilitychange', onVisibility);

  const ro = new ResizeObserver(() => {
    // Resizing a canvas clears it, so always repaint — even mid-animation —
    // rather than relying on the next frame (which may be paused offscreen).
    size();
    draw(lastPhase);
  });
  ro.observe(el);

  size();
  draw(phase); // paint one frame immediately, even before it scrolls into view
  play();

  return {
    destroy() {
      pause();
      io.disconnect();
      ro.disconnect();
      document.removeEventListener('visibilitychange', onVisibility);
      el.classList.remove('is-gen-active');
      if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
      detachReactive();
    }
  };
}
