// Visual name -> lazy module. The loader imports only what a page mounts, so a
// page pays for exactly the one visual it uses.
export const registry = {
  'section-motif': () => import('./section-motif/index.js'),
  'dot-field': () => import('./dot-field/index.js')
};
