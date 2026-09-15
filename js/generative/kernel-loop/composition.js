// Pure geometry for the kernel working-loop. No DOM and no globals, so it can be
// imported under plain `node` for deterministic checks.
//
// The loop passes through the centres of the four 2x2 grid cells; each stage
// label sits on a centre and masks the line behind it (see the plate CSS). Grid
// placement order is top-left -> top-right -> bottom-right -> bottom-left, which
// matches the path order below.
import { createPrng } from '../prng.js';

const NODES = [
  [25, 25], // draft
  [75, 25], // test
  [75, 75], // decide
  [25, 75]  // keep or discard
];

function round(value) {
  return Math.round(value * 100) / 100;
}

export function buildLoop({ seed = 'kernel-loop', jitter = 0.75 } = {}) {
  const amount = Number.isFinite(jitter) ? jitter : 0;
  const prng = createPrng(seed);
  const points = NODES.map(([x, y]) => [
    round(x + prng.range(-amount, amount)),
    round(y + prng.range(-amount, amount))
  ]);
  const [a, b, c, d] = points;
  const path = `M ${a[0]} ${a[1]} L ${b[0]} ${b[1]} L ${c[0]} ${c[1]} L ${d[0]} ${d[1]} Z`;
  return { viewBox: '0 0 100 100', path };
}

export function loopSvgMarkup(options) {
  const { viewBox, path } = buildLoop(options);
  return [
    `<svg class="gen-loop" viewBox="${viewBox}" preserveAspectRatio="none" aria-hidden="true" focusable="false">`,
    `<path class="gen-loop-track" d="${path}" pathLength="100" vector-effect="non-scaling-stroke" />`,
    `<path class="gen-loop-flow" d="${path}" pathLength="100" vector-effect="non-scaling-stroke" />`,
    `</svg>`
  ].join('');
}
