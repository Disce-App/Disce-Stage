#!/usr/bin/env python3
"""Subset the self-hosted fonts to the glyphs the site actually renders.

Masters in `fonts/` are read-only; the script writes `fonts/<name>.subset.woff2`
next to them. The @font-face rules in css/experimental.css reference the
subsets.

Why glyph subsetting only (no axis instancing)
----------------------------------------------
The variable fonts expose `wght` and `opsz` axes. Both are live: `wght` is set
by CSS, and `opsz` is applied automatically by the browser
(`font-optical-sizing: auto`). Restricting either axis range rewrites the
`avar` normalisation, which changes the interpolated outlines at the very same
user-space weight/size. That produces sub-pixel raster differences and breaks
the site's "rendered output must stay pixel-identical" constraint, so the axes
are deliberately left intact. Subsetting the glyph set alone is byte-identical
to the original rendering (verified with before/after screenshots) and removes
~70% of the font payload.

The glyph set is derived from the decoded text of every page plus the CSS and
JS. Re-run this script whenever copy changes so new glyphs are included.

Requires fontTools with the Brotli extension, installed outside the tree:
    pip install --target /tmp/pylibs fonttools brotli
    PYTHONPATH=/tmp/pylibs python3 scripts/subset_fonts.py
"""
import glob
import html
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = [
    'inter-var',
    'newsreader-roman-var',
    'newsreader-italic-var',
    'archivo-black-400',
]


def collect_text():
    chars = set()
    for pattern in ('*.html', 'css/*.css', 'js/**/*.js', 'js/*.js'):
        for path in glob.glob(os.path.join(ROOT, pattern), recursive=True):
            with open(path, encoding='utf-8') as fh:
                text = fh.read()
            if path.endswith('.html'):
                text = html.unescape(text)
            chars.update(text)
    chars = {c for c in chars if ord(c) >= 32 and c not in '\u2028\u2029'}
    return ''.join(sorted(chars))


def main():
    try:
        from fontTools import subset  # noqa: F401
    except ImportError:
        print('Missing dependency: fontTools. See the module docstring.', file=sys.stderr)
        return 1

    text_file = os.path.join('/tmp', 'disce-font-subset-text.txt')
    with open(text_file, 'w', encoding='utf-8') as fh:
        fh.write(collect_text())

    for name in FONTS:
        master = os.path.join(ROOT, 'fonts', name + '.woff2')
        out = os.path.join(ROOT, 'fonts', name + '.subset.woff2')
        if not os.path.exists(master):
            print('skip (no master):', master, file=sys.stderr)
            continue
        subprocess.check_call([
            sys.executable, '-m', 'fontTools.subset', master,
            '--text-file=' + text_file,
            '--flavor=woff2',
            '--output-file=' + out,
        ])
        print('{}: {} -> {} bytes'.format(
            name, os.path.getsize(master), os.path.getsize(out)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
