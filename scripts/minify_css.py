#!/usr/bin/env python3
"""Conservative, string-aware CSS minifier (stdlib only).

Removes comments, collapses whitespace runs, and drops insignificant
whitespace around block/declaration delimiters. It never rewrites token
content, and it copies quoted strings (including data URIs) verbatim, so
`content`, `url(...)`, `calc(...)` and custom-property values keep their
exact bytes apart from redundant whitespace.
"""
import sys


def minify(css: str) -> str:
    out = []
    i = 0
    n = len(css)
    depth = 0
    while i < n:
        c = css[i]

        # Comments (never inside strings).
        if c == '/' and i + 1 < n and css[i + 1] == '*':
            j = css.find('*/', i + 2)
            i = n if j == -1 else j + 2
            continue

        # String literal: copy verbatim.
        if c in '"\'':
            quote = c
            j = i + 1
            while j < n:
                if css[j] == '\\':
                    j += 2
                    continue
                if css[j] == quote:
                    j += 1
                    break
                j += 1
            out.append(css[i:j])
            i = j
            continue

        # Whitespace run -> at most one space, only where it is significant.
        if c.isspace():
            j = i
            while j < n and css[j].isspace():
                j += 1
            prev = out[-1][-1] if out else ''
            nxt = css[j] if j < n else ''
            drop = (
                prev in '{};,'
                or nxt in '{};,'
                or (depth > 0 and (prev == ':' or nxt == ':'))
            )
            if not drop:
                out.append(' ')
            i = j
            continue

        if c == '{':
            depth += 1
            while out and out[-1] == ' ':
                out.pop()
            out.append('{')
            i += 1
            continue

        if c == '}':
            if depth > 0:
                depth -= 1
            while out and out[-1] == ' ':
                out.pop()
            out.append('}')
            i += 1
            continue

        if c in ';,':
            while out and out[-1] == ' ':
                out.pop()
            out.append(c)
            i += 1
            continue

        # Declaration colon: only safe inside a block (depth > 0). In selector
        # context a space before ':' can be meaningful (`.a :hover`), so it is
        # left alone.
        if c == ':' and depth > 0:
            while out and out[-1] == ' ':
                out.pop()
            out.append(':')
            i += 1
            while i < n and css[i].isspace():
                i += 1
            continue

        out.append(c)
        i += 1

    return ''.join(out)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: minify.py <in.css> <out.css>", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding='utf-8') as fh:
        css = fh.read()
    with open(sys.argv[2], 'w', encoding='utf-8') as fh:
        fh.write(minify(css))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
