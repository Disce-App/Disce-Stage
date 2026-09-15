// One system, many instances: a seeded band of contour hairlines used as a
// section motif on the Philosophy page.
//
// The derived seed (base seed + section id) decides the line count, the
// undulation, and which line carries the ochre accent, so each essay gets a
// distinct instance of the same generator. Pure and node-checkable.
import { createPrng } from '../prng.js';

const WIDTH = 1000;
const HEIGHT = 120;

function round(value) {
  return Math.round(value * 10) / 10;
}

export function buildMotif({ seed = 'motif', section = '' } = {}) {
  const prng = createPrng(`${seed}:${section}`);
  const count = Math.round(prng.range(6, 9));
  const margin = 16;
  const span = HEIGHT - margin * 2;
  const accent = Math.floor(prng.next() * count);
  const lines = [];
  for (let i = 0; i < count; i += 1) {
    const baseY = margin + (span * i) / (count - 1);
    const amplitude = prng.range(2, 9);
    const frequency = prng.range(0.6, 1.6);
    const phase = prng.range(0, Math.PI * 2);
    const steps = 48;
    const points = [];
    for (let s = 0; s <= steps; s += 1) {
      const t = s / steps;
      points.push(`${round(t * WIDTH)} ${round(baseY + Math.sin(phase + t * Math.PI * 2 * frequency) * amplitude)}`);
    }
    lines.push({ d: `M ${points.join(' L ')}`, accent: i === accent });
  }
  return { width: WIDTH, height: HEIGHT, lines };
}

export function motifSvgMarkup(options) {
  const { width, height, lines } = buildMotif(options);
  const body = lines
    .map((line) => `<path class="${line.accent ? 'gen-motif-accent' : 'gen-motif-line'}" d="${line.d}" vector-effect="non-scaling-stroke" />`)
    .join('');
  return `<svg class="gen-motif-svg" viewBox="0 0 ${width} ${height}" role="presentation" aria-hidden="true" focusable="false">${body}</svg>`;
}
