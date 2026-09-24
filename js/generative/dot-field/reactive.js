// Pointer-reactive suppression for dot fields.
//
// While the cursor is over a dot field, a soft radial mask clears the dots
// directly beneath it. The mask lives on the field mount, so it covers the
// static background image and the injected canvas alike – the animated and the
// still plate react identically.
//
// One shared, passive pointer listener drives every participating field; the
// mask position is written as `--dot-x` / `--dot-y` and the `is-reactive` class
// is toggled only while the pointer is near. Nothing runs when no field is on
// the page or the pointer is coarse (touch), where there is no hover.
//
// Decorative: conveys no meaning, carries no text, does not gate any function,
// and is deletable – without it the fields are exactly the previous look.
// Pointer-initiated and local, so it is not treated as autonomous motion.

const fields = new Map();
let x = 0;
let y = 0;
let raf = 0;
let listening = false;

function apply() {
  raf = 0;
  for (const [el, clear] of fields) {
    const rect = el.getBoundingClientRect();
    // Keep the reaction alive slightly outside the plate so the clearing edge
    // is already visible as the cursor approaches.
    const near = x >= rect.left - clear && x <= rect.right + clear
      && y >= rect.top - clear && y <= rect.bottom + clear;
    if (near) {
      el.style.setProperty('--dot-x', `${Math.round(x - rect.left)}px`);
      el.style.setProperty('--dot-y', `${Math.round(y - rect.top)}px`);
      el.classList.add('is-reactive');
    } else {
      el.classList.remove('is-reactive');
    }
  }
}

function schedule() {
  if (!raf) raf = requestAnimationFrame(apply);
}

function onMove(event) {
  x = event.clientX;
  y = event.clientY;
  schedule();
}

function onLeave() {
  for (const el of fields.keys()) el.classList.remove('is-reactive');
}

function start() {
  if (listening) return;
  listening = true;
  window.addEventListener('pointermove', onMove, { passive: true });
  document.documentElement.addEventListener('pointerleave', onLeave);
  window.addEventListener('blur', onLeave);
}

function stop() {
  listening = false;
  window.removeEventListener('pointermove', onMove);
  document.documentElement.removeEventListener('pointerleave', onLeave);
  window.removeEventListener('blur', onLeave);
  if (raf) {
    cancelAnimationFrame(raf);
    raf = 0;
  }
}

function supported() {
  return typeof window.matchMedia === 'function'
    && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
}

/**
 * Make one dot-field mount react to the pointer.
 * @param {HTMLElement} el
 * @returns {() => void} detach
 */
export function attachReactive(el) {
  if (el.getAttribute('data-gen-hover') === 'off' || !supported()) return () => {};
  const clear = parseFloat(getComputedStyle(el).getPropertyValue('--dot-clear')) || 150;
  fields.set(el, clear);
  if (fields.size === 1) start();
  return () => {
    fields.delete(el);
    el.classList.remove('is-reactive');
    if (fields.size === 0) stop();
  };
}
