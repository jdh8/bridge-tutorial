#!/usr/bin/env python3
"""Typeset the book as a PDF: SUMMARY.md order -> one Markdown file -> pandoc -> xelatex.

Needs pandoc, xelatex with xeCJK, rsvg-convert, Libertinus (fontconfig) and Noto Serif CJK TC.
Output: book/bridge-tutorial.pdf; intermediates in build/.
"""
import datetime, os, pathlib, posixpath, re, shutil, subprocess

SRC, OUT = pathlib.Path('src'), pathlib.Path('build')
OUT.mkdir(parents=True, exist_ok=True)

def fid(path):  # 'game-force/opener.md' -> 'f-game-force-opener'
    return 'f-' + re.sub(r'[^a-z0-9]+', '-', path[:-3].lower())

def slug(s):  # mdbook heading ids; smart punctuation turns -- into a dash first, which is then dropped
    s = s.replace('---', '').replace('--', '')
    return ''.join(c if c.isalnum() or c in '_-.' else '-' if c.isspace() else '' for c in s.lower())

# SUMMARY.md -> [(depth, title, path)] with depth -1 for prefix/suffix chapters, None path for parts
toc = []
for line in (SRC / 'SUMMARY.md').read_text().splitlines():
    if m := re.match(r'( *)- \[(.*)\]\((.*)\)', line):
        toc.append((len(m[1]) // 2, m[2], m[3]))
    elif m := re.match(r'\[(.*)\]\((.*)\)', line):
        toc.append((-1, m[1], m[2]))
    elif (m := re.match(r'# (.*)', line)) and m[1] != 'Summary':
        toc.append((None, m[1], None))
files = {p for _, _, p in toc if p}

def convert(depth, title, path):
    d = posixpath.dirname(path)
    me = fid(path)

    def resolve(target):
        if target.startswith('#'):
            return f'#{me}--{target[1:]}'
        if re.match(r'[a-z]+:', target):
            return target
        p, _, anchor = target.partition('#')
        p = posixpath.normpath(posixpath.join(d, p))
        if p in files:
            return f'#{fid(p)}--{anchor}' if anchor else f'#{fid(p)}'
        if p.endswith('.svg') and (SRC / p).exists():  # xelatex takes PDF, not SVG
            pdf = OUT / pathlib.Path(p).with_suffix('.pdf').name
            svg = (SRC / p).read_text().replace('<svg ', '<svg font-family="\'Libertinus Sans\', \'Noto Sans CJK TC\'" ', 1)  # the website's inline SVG inherits Open Sans; print matches the PDF's sans
            # Libertinus caps are 0.63 em to Open Sans's 0.71, so shrink CJK labels to keep their web proportion
            svg = re.sub(r'(<text[^>]*font-size=")([\d.]+)("[^>]*>[㐀-鿿]+</text>)',
                         lambda m: f'{m[1]}{float(m[2]) * 0.63 / 0.71:.3g}{m[3]}', svg)
            subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', pdf], input=svg.encode(), check=True)
            return str(pdf)
        return str(SRC / p) if (SRC / p).exists() else target

    text = (SRC / path).read_text()
    text = re.sub(r'<figure>\s*(?:<img src="|\{\{#include )([^"}]+)(?:"[^>]*>|\}\})\s*<figcaption>(.*?)</figcaption>\s*</figure>',
                  lambda m: f'![{m[2]}]({m[1]})', text, flags=re.S)
    text = re.sub(r'<summary>(.*?)</summary>', r'**\1**', text)  # <details> opens in print
    text = re.sub(r'<var>(.*?)</var>', r'$\1$', text)
    text = re.sub(r'\]\(([^)\s]+)\)', lambda m: f']({resolve(m[1])})', text)

    out, seen = [], {}
    for line in text.splitlines():
        if m := re.match(r'(#+) (.*?)(?: \{#([^}]+)\})?$', line):  # keep mdbook custom ids verbatim
            level = len(m[1]) + max(depth, 0) + 1
            if len(m[1]) == 1:
                line = f'{"#" * level} {title} {{#{me}{" .unnumbered" if depth < 0 else ""}}}'
            else:
                anchor = m[3] or slug(m[2])
                seen[anchor] = seen.get(anchor, -1) + 1  # mdbook suffixes repeats with -1, -2, ...
                line = f'{"#" * level} {m[2]} {{#{me}--{anchor}{"-%d" % seen[anchor] if seen[anchor] else ""}}}'
        out.append(line)
    return '\n'.join(out) + '\n\n'

today = datetime.date.today()
doc = [f'''---
title: 橋牌入門
subtitle: 從規則到二蓋一
author: Chen-Pang He
date: {today.year} 年 {today.month} 月
documentclass: scrbook
classoption: [11pt, oneside, numbers=noendperiod]
papersize: a4
mainfont: Libertinus Serif
sansfont: Libertinus Sans
CJKmainfont: Noto Serif CJK TC  # pdffonts says NotoSerifCJKjp: the TTC's faces share one CFF FontName, but the glyphs are TC's
# Not KR, despite its older printed forms: it sets ，。、 low-left, Taiwan centres them
CJKoptions: BoldFont=Noto Serif CJK TC Bold
linestretch: 1.25
toc: true
toc-title: 目錄
toc-depth: 1
numbersections: true
secnumdepth: 2
indent: true
colorlinks: true
linkcolor: MidnightBlue
urlcolor: MidnightBlue
---
''']
started = False
for depth, title, path in toc:
    if depth is None:
        if not started:
            doc.append('```{=latex}\n\\mainmatter\\setcounter{secnumdepth}{2}\n```\n')
            started = True
        if title == '附錄':
            doc.append('```{=latex}\n\\backmatter\\setcounter{secnumdepth}{-2}\n```\n')
        doc.append(f'# {title}\n\n')
    else:
        doc.append(convert(depth, title, path))
(OUT / 'book.md').write_text(''.join(doc))

(OUT / 'preamble.tex').write_text(r'''
\setCJKsansfont{Noto Sans CJK TC}[BoldFont=Noto Sans CJK TC Bold]  % XeTeX guesses Black from the weight TTCs; pandoc's CJKoptions is the serif's
\xeCJKsetup{CJKecglue={}}  % the source already spaces CJK from Latin
\usepackage{xeCJKfntef}
\renewcommand\emph[1]{\CJKunderdot{#1}}  % 著重號, as the website's text-emphasis
\definecolor{suitred}{HTML}{BB2222}
% Red hearts and diamonds everywhere, links included
\let\♥=♥ \let\♦=♦  % one-char control symbols survive hyperref bookmark strings
\catcode`♥=\active \catcode`♦=\active
\def♥{\texorpdfstring{\textcolor{suitred}{\♥}}{\♥}}
\def♦{\texorpdfstring{\textcolor{suitred}{\♦}}{\♦}}
% Page reference after an internal link, omitted when the target is on this page
\usepackage{refcount}
\newcommand\pref[1]{\ifnum\getpagerefnumber{#1}=\value{page}\else（第 \pageref{#1} 頁）\fi}
% Front matter: swallow pandoc's \mainmatter so the preface stays in it
\let\realmainmatter\mainmatter
\renewcommand\mainmatter{\global\let\mainmatter\realmainmatter}
\renewcommand\arraystretch{1.15}
\AtBeginDocument{\renewcommand*\figurename{圖}\renewcommand*\tablename{表}}\renewcommand*\captionformat{\quad}  % KOMA sets the names at \begin{document}
\setcounter{secnumdepth}{-2}  % no section numbers in the front matter; restored at \mainmatter
\usepackage{graphicx}
\AtBeginDocument{\hypersetup{bookmarksdepth=2}}
\subject{\includegraphics[height=3cm]{favicon.pdf}}
'''.replace('favicon.pdf', str(OUT / 'favicon.pdf')))

subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', OUT / 'favicon.pdf', 'theme/favicon.svg'], check=True)
subprocess.run(['pandoc', OUT / 'book.md', '-o', OUT / 'bridge-tutorial.tex', '-s', '--top-level-division=part',
                '--columns=10000', '--lua-filter=print.lua', '-H', OUT / 'preamble.tex'], check=True)
# Close every page of a broken table with the bottom rule.  Room reserved for \endfoot also keeps
# \endlastfoot on the last row's page, where pandoc's lone \endlastfoot could start an empty continuation.
tex = OUT / 'bridge-tutorial.tex'
tex.write_text(tex.read_text().replace('\\bottomrule\\noalign{}\n\\endlastfoot', '\\bottomrule\\noalign{}\n\\endfoot\n\\bottomrule\\noalign{}\n\\endlastfoot'))
# Hide Fedora's variable Noto CJK from XeTeX, which prefers it to the static TTCs xdvipdfmx can embed
(OUT / 'fonts.conf').write_text('''<?xml version="1.0"?>
<fontconfig>
  <include>/etc/fonts/fonts.conf</include>
  <selectfont><rejectfont><glob>*-VF.ttc</glob></rejectfont></selectfont>
</fontconfig>
''')
env = dict(os.environ, FONTCONFIG_FILE=str((OUT / 'fonts.conf').resolve()))
for _ in range(3):
    if subprocess.run(['xelatex', '-interaction=batchmode', '-halt-on-error', '-output-directory', OUT, tex],
                      stdout=subprocess.DEVNULL, env=env).returncode:
        log = (OUT / 'bridge-tutorial.log').read_text(errors='replace').splitlines()
        raise SystemExit('\n'.join(log[-40:]))
pathlib.Path('book').mkdir(exist_ok=True)
shutil.copy(OUT / 'bridge-tutorial.pdf', 'book/bridge-tutorial.pdf')
print('book/bridge-tutorial.pdf')
