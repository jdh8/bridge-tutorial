#!/usr/bin/env python3
"""Join soft line breaks next to CJK characters, in place: cjk.py src/*.md

A newline renders as a space, which Chinese does not want.  The rules follow
CLAUDE.md: Han characters are spaced from western text, full-width punctuation
touches everything, and emphasis and link markup are looked past.
"""
import re
import sys

HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
PUNCT = re.compile(r"[\u2014\u2026\u3000-\u303f\uff00-\uffef]")
# Never join onto a line that starts a block: list item, quote, heading, table, HTML
# Look past emphasis and link markup: "[text](url)**" before, "**[" after
BREAK = re.compile(
    r"([^\s*_\]])((?:\]\([^)\s]*\)|\]\[[^\]]*\])?[*_]*)\n"
    r"(?![ \t]*(?:[-+*][ \t]|\d+[.)][ \t]|[>#|<]))[ \t]*(?=[*_\[]*(\S))"
)
FENCE = re.compile(r"^(```|~~~).*?^\1", re.M | re.S)


def join(m):
    a, mark, b = m.groups()
    line = m.string[m.string.rfind("\n", 0, m.start()) + 1:m.start()]
    if line.lstrip().startswith(("#", "|")):
        return m[0]
    han = bool(HAN.match(a)) + bool(HAN.match(b))
    if PUNCT.match(a) or PUNCT.match(b) or han == 2:
        return a + mark
    return a + mark + " " if han else m[0]


def fix(text):
    out, last = [], 0
    for m in FENCE.finditer(text):
        out += BREAK.sub(join, text[last:m.start()]), m[0]
        last = m.end()
    return "".join(out) + BREAK.sub(join, text[last:])


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as f:
            text = f.read()
        fixed = fix(text)
        if fixed != text:
            with open(path, "w") as f:
                f.write(fixed)
