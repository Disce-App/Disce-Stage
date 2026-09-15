// Kernel working-loop (Development Status). Informative, SVG + CSS only.
//
// The plate's semantic text (stage labels, caption, description, pause control)
// is real markup in status.html; this module injects only the aria-hidden loop
// graphic and wires the pause control. Removing this module leaves the page
// unchanged apart from the hidden plate.
import { getTokens } from '../tokens.js';
import { loopSvgMarkup } from './composition.js';
import { frozenDashoffset } from './motion.js';

const DEFAULT_JITTER = 0.75;

export function mount(el, { seed = 'kernel-loop', motion = true, phase = 0 } = {}) {
  const canvas = el.querySelector('.gen-plate-canvas');
  const pause = el.querySelector('.gen-plate-pause');
  if (!canvas) return { destroy() {} };

  const tokens = getTokens();
  const jitter = Number.parseFloat(tokens['--gen-jitter']);
  canvas.innerHTML = loopSvgMarkup({
    seed,
    jitter: Number.isFinite(jitter) ? jitter : DEFAULT_JITTER
  });

  const setPaused = (paused) => {
    el.classList.toggle('is-paused', paused);
    if (pause) pause.setAttribute('aria-pressed', String(paused));
  };
  const onPause = () => setPaused(!el.classList.contains('is-paused'));

  if (!motion) {
    el.classList.add('is-static');
    el.style.setProperty('--gen-dashoffset', frozenDashoffset(phase));
    if (pause) pause.hidden = true;
  } else if (pause) {
    pause.addEventListener('click', onPause);
  }

  let destroyed = false;
  return {
    destroy() {
      if (destroyed) return;
      destroyed = true;
      if (pause) pause.removeEventListener('click', onPause);
      canvas.innerHTML = '';
      el.classList.remove('is-static', 'is-paused');
      el.style.removeProperty('--gen-dashoffset');
    }
  };
}
