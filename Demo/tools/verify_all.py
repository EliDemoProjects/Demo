#!/usr/bin/env python3
"""Wrapper around the skill's verify_text.py (same tokenizer + diff), with 4 documented adjustments:
 1. main-section finder falls back to section[data-permalink] (skill's finder needs class original-topic; 19 pages lack it)
 2. hint titles (Note/Notice/Tip/Warning/Caution) are ignored for every hint class, not only 'note' - unless the hint sits in a table cell (kept as bold lead there)
 3. display:none linktextprovider spans are ignored (invisible helper text)
 4. HTML entities in the converted markdown are decoded before tokenizing (needed for HTML tables / &lt;)
"""
import sys, os, re, json, html, difflib
sys.path.insert(0, '/mnt/skills/plugins/gitbook-paligo/scripts')
import verify_text as V
HINTS = {'note', 'tip', 'warning', 'caution', 'important', 'danger'}

def find_main(n):
    for c in n.children:
        if isinstance(c, V.Node):
            if c.tag == 'section' and ('data-permalink' in c.attrs or 'original-topic' in V.cls(c)):
                return c
            r = find_main(c)
            if r: return r
    return None

def in_cell(n):
    p = n.parent
    while p is not None:
        if p.tag in ('td', 'th'): return True
        p = p.parent
    return False

def html_text(n, out):
    for c in n.children:
        if isinstance(c, str):
            out.append(c); continue
        if c.tag in V.SKIP: continue
        cl = V.cls(c)
        if 'linktextprovider' in cl: continue
        if c.tag in ('h2', 'h3', 'h4') and 'title' in cl and c.parent is not None \
                and (set(V.cls(c.parent)) & HINTS) and c.parent.tag == 'div' and not in_cell(c):
            continue
        out.append(' '); html_text(c, out); out.append(' ')

def md_tokens(path, inc_dir):
    md = open(path, encoding='utf-8').read()
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    md = V.expand_includes(md, inc_dir)
    store = []
    def stash(text):
        store.append(text)
        return chr(0xE000 + len(store) - 1)
    # fenced code blocks and inline code spans are literal text: protect them from markup stripping
    md = re.sub(r'^[ \t]*(`{3,})[^\n]*\n(.*?)\n[ \t]*\1[ \t]*$', lambda m: ' ' + stash(m.group(2)) + ' ', md, flags=re.S | re.M)
    md = re.sub(r'(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)', lambda m: ' ' + stash(m.group(2).strip().replace('\\|', '|')) + ' ', md)
    # backslash escapes are literal characters
    md = re.sub(r'\\([\\`*_{}\[\]()#+\-.!|<>~&])', lambda m: stash(m.group(1)), md)
    md = '\n'.join(re.sub(r'\*', lambda m: stash('*'), l) if re.search(r'<t[dh][ >]', l) else l for l in md.split('\n'))
    md = re.sub(r'\{%\s*tab\s+title="([^"]*)"\s*%\}', r' \1 ', md)
    md = re.sub(r'\{%.*?%\}', ' ', md, flags=re.S)
    md = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r' \1 ', md)
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    md = re.sub(r'<[^>]+>', ' ', md)
    md = html.unescape(md)
    md = re.sub(r'^\s*\|?[\s:|\-]+\|?\s*$', '', md, flags=re.M)
    md = re.sub(r'^\s*(?:[-*+]|\d+\.)\s+', ' ', md, flags=re.M)
    md = re.sub(r'^\s{0,3}#{1,6}\s+', ' ', md, flags=re.M)
    md = re.sub(r'^\s*>\s?', ' ', md, flags=re.M)
    md = md.replace('**', ' ')
    # '|' is a delimiter only on markdown table rows; '*' is emphasis only outside HTML tables
    md = '\n'.join(re.sub(r'\|', ' ', l) if l.lstrip().startswith('|') else l for l in md.split('\n'))
    md = re.sub(r'(?<!\w)\*|\*(?!\w)', ' ', md)
    md = re.sub('[\ue000-\uf8ff]', lambda m: store[ord(m.group(0)) - 0xE000] if ord(m.group(0)) - 0xE000 < len(store) else m.group(0), md)
    return V.tokenize(md)

V.html_text = html_text
V.find_main = find_main

def run(src, md, inc, ctx=6, maxd=40):
    s = V.source_tokens(src); m = md_tokens(md, inc)
    sm = difflib.SequenceMatcher(None, s, m, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
    res = []
    for tag, i1, i2, j1, j2 in ops[:maxd]:
        res.append((' '.join(s[max(0, i1 - ctx):i1]), ' '.join(s[i1:i2]) or '-', ' '.join(m[j1:j2]) or '-', ' '.join(s[i2:i2 + ctx])))
    return len(s), len(m), len(ops), res

if __name__ == '__main__':
    pages = json.load(open('/home/claude/work/pages.json'))
    OUT = '/mnt/user-data/outputs/gitbook-sca/'
    SRC = '/home/claude/src/18662-Checkmarx_SCA-html5/out/en/'
    only = sys.argv[1:]
    bad = 0; total = 0
    for key, (space, fn) in sorted(pages.items()):
        if only and key.split('/')[-1] not in only and fn not in only: continue
        total += 1
        md = OUT + key
        ns, nm, nd, res = run(SRC + fn, md, OUT + space + '/.gitbook/includes')
        if nd:
            bad += 1
            print('\n### %s  (src %d / md %d tokens, %d diffs)' % (key, ns, nm, nd))
            for l, a, b, r in res[:8]:
                print('  ...%s [[SRC: %s]] [[MD: %s]] %s' % (l, a[:150], b[:150], r))
    print('\nverified %d pages, %d with differences' % (total, bad))
