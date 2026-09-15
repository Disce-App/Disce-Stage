// Deterministic seeded pseudo-randomness. Pure, dependency-free, and safe to
// import under plain `node` for checks outside a browser.
//
// Variation in every generative visual derives from an explicit seed (see the
// plan's seed strategy): the same seed must always produce the same output.

// FNV-1a 32-bit — turns a stable string id into a numeric seed.
export function hashSeed(value) {
  const str = String(value);
  let hash = 0x811c9dc5;
  for (let i = 0; i < str.length; i += 1) {
    hash ^= str.charCodeAt(i);
    hash = Math.imul(hash, 0x01000193);
  }
  return hash >>> 0;
}

// mulberry32 — small, fast, good enough for visual jitter.
export function mulberry32(seed) {
  let a = seed >>> 0;
  return function next() {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function createPrng(seed) {
  const next = mulberry32(typeof seed === 'number' ? seed : hashSeed(seed));
  return {
    next,
    range(min, max) {
      return min + (max - min) * next();
    },
    pick(list) {
      return list[Math.floor(next() * list.length)];
    }
  };
}
