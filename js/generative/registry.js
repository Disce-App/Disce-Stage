// Visual name -> lazy module. The loader imports only what a page mounts, so a
// page pays for exactly the one visual it uses.
export const registry = {
  'kernel-loop': () => import('./kernel-loop/index.js'),
  'section-motif': () => import('./section-motif/index.js')
};
