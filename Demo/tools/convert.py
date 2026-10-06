#!/usr/bin/env python3
"""Paligo HTML5 -> GitBook markdown converter for the gitbook-paligo skill (verbatim import).
Only mechanical markup conversion; no text edits. Uses the skill's scripts for parsing, sizes,
videos, slugs (redirects.csv) and navigation (build_summary.py)."""
import csv, os, re, sys, json, html, shutil, collections, glob
SK = '/home/claude/skill-update/gitbook-paligo/scripts'
sys.path.insert(0, SK)
import verify_text as V
import find_image_sizes as FS
import find_videos as FV

SRC = glob.glob('/home/claude/sca/*/out/en/')[0]
WORK = '/home/claude/work/'
OUT = '/home/claude/work/out/gitbook-sca/'
SKIP_SPACES = {'checkmarx-sca--rest--api-documentation'}
SPACE_KEYS = {
    'checkmarx-sca-release-notes': 'RELEASE_NOTES', 'faq': 'FAQ',
    'checkmarx-sca---product-info': 'PRODUCT_INFO', 'checkmarx-sca---quick-start-tutorial': 'QUICK_START',
    'checkmarx-sca---user-guide': 'USER_GUIDE', 'checkmarx-sca-resolver': 'RESOLVER',
    'checkmarx-sca-integrations-and-plugins': 'INTEGRATIONS',
    'checkmarx-sca--rest--api-documentation': 'REST_API'}

ALL = list(csv.DictReader(open('/home/claude/sca-red/redirects.csv', newline='')))
BY_SRC = {os.path.basename(r['source_path']): r for r in ALL}
INC_MAP = {r['element_uuid']: r['include_file'] for r in
           csv.DictReader(open('/home/claude/reuse-out/includes-map.csv', newline=''))}
UUIDPAT = re.compile(r'^UUID-([0-9a-f-]{36})_UUID-([0-9a-f-]{36})$')

REP = collections.defaultdict(list)
ASSETS = collections.defaultdict(set)
INCLUDES = {}          # (space, name) -> text
INC_FIRST = {}         # (space, name) -> page of first rendering
HINT_TAGS = {'note', 'tip', 'notice', 'warning', 'caution', 'important', 'danger'}
INLINE_TAGS = {'span', 'strong', 'b', 'em', 'i', 'code', 'a', 'sup', 'sub', 'br', 'img', 'u', 'small',
               'abbr', 'cite', 'kbd', 'var', 'samp', 'q', 'mark'}
PLATFORM = re.compile(r'^(windows|linux|mac(os)?|linux ?/ ?mac|mac ?/ ?linux|docker|podman|vs ?code|'
                      r'visual studio( code)?|cursor|windsurf|kiro|intellij|eclipse|jetbrains|bash|powershell)', re.I)


# ------------------------------------------------------------------ helpers
def cls(n): return V.cls(n)
def nodes(n): return [c for c in n.children if isinstance(c, V.Node)]


def desc(n):
    for c in n.children:
        if isinstance(c, V.Node):
            yield c
            yield from desc(c)


def raw_text(n, skip_hidden=True):
    o = []
    for c in n.children:
        if isinstance(c, str):
            o.append(c)
        elif skip_hidden and hidden(c):
            continue
        else:
            o.append(raw_text(c, skip_hidden))
    return ''.join(o)


def hidden(n):
    st = n.attrs.get('style', '')
    return 'linktextprovider' in cls(n) or re.search(r'display:\s*none', st) is not None


def ws(t): return re.sub(r'[ \t\r\n]+', ' ', t)


def esc_md(t, cell=False):
    t = t.replace('\\', '\\\\')
    t = re.sub(r'([*`\[\]<>])', r'\\\1', t)
    t = re.sub(r'(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])', r'\\_', t)
    t = re.sub(r'\{(?=[%{])', r'\\{', t)
    t = re.sub(r'&(?=#?\w+;)', r'\\&', t)
    if cell:
        t = t.replace('|', r'\|')
    return t


def esc_start(s):
    s2 = re.sub(r'^(\s*)(\d+)([.)])(\s|$)', r'\1\2\\\3\4', s)
    s2 = re.sub(r'^(\s*)([-+])(\s)', r'\1\\\2\3', s2)
    s2 = re.sub(r'^(\s*)(#{1,6})(\s)', r'\1\\\2\3', s2)
    return s2


def etext(t, ctx):
    e = html.escape(t, quote=False)
    if ctx.md_cell:
        e = re.sub(r'([*`\[\]])', r'\\\1', e)
    return e


def md_url(u): return u.replace(' ', '%20').replace('(', '%28').replace(')', '%29')


class Ctx:
    def __init__(self, fn, space, faq=False):
        self.fn, self.space, self.faq = fn, space, faq
        self.in_cell = False
        self.in_acc = 0
        self.in_include = False
        self.md_cell = False      # html fragments inside a markdown table cell: markdown still applies to text


# ------------------------------------------------------------------ links / images
def map_href(href, text, ctx):
    href = html.unescape(href).strip()
    if not href:
        return href
    if re.match(r'^(https?:|mailto:|tel:|ftp:)', href, re.I):
        return href
    if href.startswith('/document/') or href.startswith('urn:'):
        REP['paligo_doc_links'].append((ctx.fn, text, href))
        return href
    if href.startswith('#'):
        REP['anchor_links'].append((ctx.fn, href))
        return href
    m = re.match(r'^(?:\.\./|\./)?(?:en/)?([^#?]+\.html)(#.*)?$', href)
    if m:
        base, frag = os.path.basename(m.group(1)), m.group(2) or ''
        r = BY_SRC.get(base)
        if r:
            if r['space'] == ctx.space:
                if frag:
                    REP['anchor_links'].append((ctx.fn, r['file'] + frag))
                return r['file'] + frag
            path = r['destination_path']
            pre = '/' + r['space']
            sub = path[len(pre):] if path.startswith(pre) else path
            REP['cross_space_links'].append((ctx.fn, text, href, r['space']))
            return 'https://app.gitbook.com/s/XSPACE_%s%s%s' % (SPACE_KEYS[r['space']], sub if sub else '/', frag)
        REP['unresolved_links'].append((ctx.fn, text, href))
        return href
    REP['unresolved_links'].append((ctx.fn, text, href))
    return href


def img_path(img, ctx):
    name = os.path.basename(img.attrs.get('src', ''))
    if not os.path.exists(SRC + 'image/' + name):
        REP['missing_images'].append((ctx.fn, name))
    ASSETS[ctx.space].add(name)
    return '.gitbook/assets/' + name


def size_label(val, unit):
    return FS.map_percent(val) if unit == '%' else FS.map_pixels(val)


def find_size(mo, img):
    cands = []
    for t in desc(mo):
        if t.tag == 'table' and 'image-viewport' in cls(t):
            for prop, (n, u) in FS.css_widths(t.attrs.get('style', '')).items():
                cands.append(('table ' + prop, n, u))
            break
    st = FS.css_widths(img.attrs.get('style', ''))
    if 'width' in st: cands.append(('img width', *st['width']))
    if 'max-width' in st: cands.append(('img max-width', *st['max-width']))
    c = FS.pick(cands)
    return c


def img_block(im, ctx, size, mo):
    p = img_path(im, ctx)
    if ctx.in_cell:
        REP['cell_images'].append((ctx.fn, p))
        return '<img src="%s" alt="">' % p
    if size is None:
        attr, label = None, 'Fit'
        REP['image_sizes'].append((ctx.fn, os.path.basename(p), 'none', '', 'Fit (defaulted)'))
    else:
        src_, val, unit = size
        label, attr = size_label(val, unit or 'px')
        attr = attr or None
        REP['image_sizes'].append((ctx.fn, os.path.basename(p), src_, '%g%s' % (val, unit or 'px'), label))
    w = ' width="%s"' % attr if attr else ''
    return '<div align="left"><figure><img src="%s" alt=""%s></figure></div>' % (p, w)


def mediaobject(n, ctx):
    res = []
    ifr = next((x for x in desc(n) if x.tag == 'iframe'), None)
    if ifr is not None:
        vid, h, emb = FV.embed_for(ifr.attrs.get('src', ''))
        if emb:
            REP['videos'].append((ctx.fn, vid, h or ''))
            return [emb]
        REP['check'].append((ctx.fn, 'non-vimeo iframe', ifr.attrs.get('src', '')))
        return []
    items = [x for x in desc(n) if x.tag == 'div' and 'flex-item' in cls(x)]
    if items:
        for it in items:
            w = re.search(r'width:\s*([\d.]+)%', it.attrs.get('style', ''))
            for im in [x for x in desc(it) if x.tag == 'img']:
                res.append(img_block(im, ctx, ('flex-item', float(w.group(1)), '%') if w else None, n))
        return res
    for cap in [x for x in desc(n) if x.tag == 'div' and 'caption' in cls(x)]:
        REP['captions'].append((ctx.fn, raw_text(cap).strip()))
    for im in [x for x in desc(n) if x.tag == 'img']:
        c = find_size(n, im)
        res.append(img_block(im, ctx, (c[0], c[1], c[2]) if c else None, n))
    return res


# ------------------------------------------------------------------ inline
def wrap(mark, inner, close=None):
    if not inner.strip():
        return inner
    lead = inner[:len(inner) - len(inner.lstrip())]
    trail = inner[len(inner.rstrip()):]
    return lead + mark + inner.strip() + (close or mark) + trail


def code_span(text):
    text = ws(text)
    if not text.strip():
        return text
    lead = ' ' if text.startswith(' ') else ''
    trail = ' ' if text.endswith(' ') else ''
    t = text.strip()
    if '`' in t:
        return lead + '`` ' + t + ' ``' + trail
    return lead + '`' + t + '`' + trail


def inline(kids, ctx, mode='md', cell=False):
    if isinstance(kids, V.Node):
        kids = kids.children
    out = []
    for c in kids:
        if isinstance(c, str):
            t = ws(c)
            out.append(etext(t, ctx) if mode == 'html' else esc_md(t, cell))
        else:
            out.append(inline_node(c, ctx, mode, cell))
    s = ''.join(out)
    s = re.sub(r' {2,}', ' ', s)
    if mode == 'md':
        s = re.sub(r'(?<!\\)\*\*\*\*', '', s)
    return s


def inline_node(c, ctx, mode, cell):
    t, cl = c.tag, cls(c)
    H = mode == 'html'
    if hidden(c):
        REP['hidden_spans'].append((ctx.fn, raw_text(c, False).strip()))
        return ''
    if t in ('strong', 'b'):
        inner = inline(c, ctx, mode, cell)
        return wrap('<strong>', inner, '</strong>') if H else wrap('**', inner)
    if t in ('em', 'i'):
        inner = inline(c, ctx, mode, cell)
        return wrap('<em>', inner, '</em>') if H else wrap('*', inner)
    if t == 'code':
        txt = ws(raw_text(c))
        if not txt.strip():
            return txt
        return '<code>%s</code>' % html.escape(txt, quote=False) if H else code_span(txt)
    if t in ('sup', 'sub'):
        return '<%s>%s</%s>' % (t, inline(c, ctx, mode, cell), t)
    if t == 'u' or (t == 'span' and 'underline' in cl):
        return wrap('<u>', inline(c, ctx, mode, cell), '</u>')
    if t == 'br':
        return '<br>'
    if t == 'img':
        p = img_path(c, ctx)
        return '<img src="%s" alt="">' % p if H else '![](%s)' % p
    if t == 'span' and 'bold' in cl:
        inner = inline(c, ctx, mode, cell)
        return wrap('<strong>', inner, '</strong>') if H else wrap('**', inner)
    if t == 'span' and 'emphasis' in cl:
        inner = inline(c, ctx, mode, cell)
        return wrap('<em>', inner, '</em>') if H else wrap('*', inner)
    if t == 'a':
        href = c.attrs.get('href')
        inner = inline(c, ctx, mode, cell)
        if not href:
            return inner
        text = ws(raw_text(c)).strip()
        tgt = map_href(href, text, ctx)
        if not inner.strip():
            return inner
        if H:
            return '<a href="%s">%s</a>' % (html.escape(tgt), inner)
        inner = re.sub(r'<u>|</u>', '', inner)
        return '[%s](%s)' % (inner.strip(), md_url(tgt))
    return inline(c, ctx, mode, cell)


# ------------------------------------------------------------------ blocks
def para_text(runs, ctx, cell=False):
    return inline(runs, ctx, 'md', cell).strip()


def heading(n, ctx):
    lvl = int(n.tag[1])
    txt = inline(n, ctx).strip()
    return '#' * lvl + ' ' + txt if txt else ''


def indent_block(s, pad, first=None):
    lines = s.split('\n')
    out = []
    for i, l in enumerate(lines):
        if i == 0 and first is not None:
            out.append(first + l)
        else:
            out.append((pad + l) if l.strip() else '')
    return '\n'.join(out)


def blocks(n, ctx):
    """Return list of block strings for the children of node n."""
    res = []
    run = []

    def flush():
        if run:
            t = para_text(list(run), ctx)
            if t:
                res.append(esc_start(t))
            run.clear()

    kids = n.children
    i = 0
    while i < len(kids):
        c = kids[i]
        if isinstance(c, str):
            run.append(c)
            i += 1
            continue
        if c.tag in INLINE_TAGS:
            run.append(c)
            i += 1
            continue
        flush()
        # accordion group
        if is_acc(c):
            grp = []
            while i < len(kids) and (isinstance(kids[i], str) and not kids[i].strip() or
                                     (isinstance(kids[i], V.Node) and is_acc(kids[i]))):
                if isinstance(kids[i], V.Node):
                    grp.append(kids[i])
                i += 1
            res.extend(accordions(grp, ctx))
            continue
        res.extend(block(c, ctx))
        i += 1
    flush()
    return res


def cl_(n): return cls(n)


def is_acc(c):
    if not isinstance(c, V.Node):
        return False
    cl = cls(c)
    return (c.tag == 'div' and 'sidebar' in cl and 'accordion' in cl) or (c.tag == 'section' and 'accordion' in cl)


def include_for(c, ctx):
    eid = c.attrs.get('id', '')
    m = UUIDPAT.match(eid)
    if m and m.group(2) in INC_MAP and not ctx.in_include and ctx.space not in SKIP_SPACES:
        return m.group(2)
    return None


def block(c, ctx):
    t, cl = c.tag, cls(c)
    if hidden(c) and t != 'span':
        return []
    u = include_for(c, ctx)
    if u:
        name = INC_MAP[u]
        key = (ctx.space, name)
        if key not in INCLUDES:
            sub = Ctx(ctx.fn, ctx.space, ctx.faq)
            sub.in_include = True
            body = '\n\n'.join(x for x in block_inner(c, sub) if x) + '\n'
            INCLUDES[key] = body
            INC_FIRST[key] = ctx.fn
        REP['include_use'].append((ctx.space, name, ctx.fn))
        return ['{%% include ".gitbook/includes/%s" %%}' % name]
    return render_element(c, ctx)


def render_element(c, ctx):
    return block_inner(c, ctx)


def block_inner(c, ctx):
    t, cl = c.tag, cls(c)
    if t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        if t == 'h3' and c.parent is not None and set(cls(c.parent)) & HINT_TAGS:
            return []
        h = heading(c, ctx)
        return [h] if h else []
    if t == 'p':
        txt = para_text(c.children, ctx, ctx.in_cell)
        return [esc_start(txt)] if txt else []
    if t in ('ul', 'ol'):
        return [list_block(c, ctx)]
    if t == 'div' and ('itemizedlist' in cl or 'orderedlist' in cl):
        out = []
        for k in nodes(c):
            out.extend(block(k, ctx))
        return out
    if t == 'div' and (set(cl) & HINT_TAGS) and ('note' in cl or t == 'div'):
        return [hint(c, ctx)]
    if t == 'div' and 'mediaobject' in cl:
        return mediaobject(c, ctx)
    if t == 'div' and ('informalfigure' in cl or 'flex-container' in cl):
        return mediaobject(c, ctx) if any(True for x in desc(c) if x.tag == 'div' and 'flex-item' in cls(x)) \
            else blocks(c, ctx)
    if t == 'pre':
        return [code_block(c, ctx)]
    if t == 'blockquote':
        inner = '\n\n'.join(blocks(c, ctx))
        return [indent_block(inner, '> ', '> ').replace('\n\n', '\n>\n')] if inner else []
    if t == 'table' and 'image-viewport' in cl:
        return []
    if t == 'table':
        return [table_block(c, ctx)]
    if t == 'div' and ('table-responsive' in cl or 'paligo-filter-table' in cl or 'informaltable' in cl):
        out = []
        for k in nodes(c):
            out.extend(block(k, ctx))
        return out
    if t == 'div' and 'caption' in cl:
        REP['captions'].append((ctx.fn, raw_text(c).strip()))
        return []
    if t in ('script', 'style', 'iframe', 'nav', 'header', 'footer', 'colgroup', 'col'):
        return []
    if t == 'hr':
        return ['---']
    if t == 'div' and 'result' in cl:
        return blocks(c, ctx)
    # structural containers: recurse
    known = ('div', 'section', 'article', 'span', 'dl', 'dd', 'dt', 'figure', 'li', 'a')
    if t not in known:
        REP['unknown'].append((ctx.fn, t, ' '.join(cl)))
    return blocks(c, ctx)


def list_block(l, ctx):
    if ctx.in_cell:
        return html_node(l, ctx)
    ordered = l.tag == 'ol'
    typ = l.attrs.get('type', '1')
    if ordered and typ not in ('1', ''):
        REP['ol_type'].append((ctx.fn, typ, ''))
    items = [k for k in nodes(l) if k.tag == 'li']
    start = l.attrs.get('start')
    n0 = int(start) if (start or '').isdigit() else 1
    out = []
    for idx, li in enumerate(items):
        bl = blocks(li, ctx)
        if not bl:
            bl = ['']
        marker = ('%d. ' % (n0 + idx)) if ordered else '- '
        pad = ' ' * len(marker)
        body = bl[0] if len(bl) == 1 else None
        parts = [indent_block(bl[0], pad, marker)]
        for b in bl[1:]:
            parts.append(indent_block(b, pad, pad))
        out.append('\n\n'.join(parts) if len(bl) > 1 else parts[0])
    tight = all('\n\n' not in o for o in out)
    return ('\n'.join(out)) if tight else '\n\n'.join(out)


def hint_style(title, classes):
    tl = title.strip().lower()
    table = {'note': ('info', None), 'tip': ('info', None), 'notice': ('info', 'pencil'),
             'important': ('success', 'key'), 'warning': ('warning', None),
             'caution': ('warning', None), 'danger': ('danger', None)}
    if tl in table:
        return table[tl]
    for k in ('danger', 'warning', 'caution', 'important', 'notice', 'tip', 'note'):
        if k in classes:
            return table[k]
    return ('info', None)


def hint(c, ctx):
    title = ''
    for k in nodes(c):
        if k.tag in ('h2', 'h3', 'h4', 'p') and 'title' in cls(k) and k.tag != 'p':
            title = raw_text(k).strip()
            break
    classes = cls(c)
    style, icon = hint_style(title, classes)
    exp = {'note': 'info', 'tip': 'info', 'notice': 'info', 'warning': 'warning', 'caution': 'warning',
           'important': 'success', 'danger': 'danger'}
    cset = {exp[k] for k in classes if k in exp}
    if cset and style not in cset:
        REP['hint_mismatch'].append((ctx.fn, ' '.join(classes), title, style))
    body = blocks(c, ctx)
    if ctx.in_cell:
        REP['cell_hints'].append((ctx.fn, title))
        return ('**%s** ' % title if title else '') + '<br>'.join(body)
    ic = ' icon="%s"' % icon if icon else ''
    return '{%% hint style="%s"%s %%}\n%s\n{%% endhint %%}' % (style, ic, '\n\n'.join(body))


def code_block(c, ctx):
    txt = raw_text(c, False)
    txt = txt.strip('\n').replace('\r', '')
    lang = c.attrs.get('data-language', '') or ''
    if ctx.in_cell:
        return '<pre><code>%s</code></pre>' % html.escape(txt, quote=False)
    fence = '```'
    while fence in txt:
        fence += '`'
    return '%s%s\n%s\n%s' % (fence, lang, txt, fence)


# ------------------------------------------------------------------ accordions
def acc_parts(a, ctx):
    title, body = '', None
    for d in desc(a):
        if d.tag == 'div' and 'sidebar-title' in cls(d) and not title:
            title = ws(raw_text(d)).strip()
        if d.tag in ('h2', 'h3', 'h4', 'h5', 'h6') and 'title' in cls(d) and not title:
            title = ws(raw_text(d)).strip()
        if d.tag == 'div' and 'panel-body' in cls(d) and body is None:
            body = d
    return title, body


def accordions(grp, ctx):
    parts = [acc_parts(a, ctx) for a in grp]
    titles = [p[0] for p in parts]
    nested = ctx.in_acc > 0
    if ctx.faq or nested:
        form = 'details'
    elif all(PLATFORM.match(t) for t in titles):
        form = 'tabs'
    elif 2 <= len(grp) <= 8:
        form = 'tabs'
    else:
        form = 'details'
    REP['accordions'].append((ctx.fn, len(grp), form, 'nested' if nested else ('faq' if ctx.faq else ''),
                              ' | '.join(titles)))
    ctx.in_acc += 1
    outs = []
    for title, body in parts:
        inner = '\n\n'.join(blocks(body, ctx)) if body is not None else ''
        outs.append((title, inner))
    ctx.in_acc -= 1
    if form == 'tabs':
        s = '{% tabs %}\n' + '\n'.join('{%% tab title="%s" %%}\n%s\n{%% endtab %%}' % (t.replace('"', "'"), b)
                                         for t, b in outs) + '\n{% endtabs %}'
        return [s]
    return ['<details>\n<summary>%s</summary>\n\n%s\n\n</details>' % (html.escape(t, quote=False), b)
            for t, b in outs]


# ------------------------------------------------------------------ tables
def cell_html(cell, ctx):
    ctx.in_cell = True
    parts = []
    for k in cell.children:
        if isinstance(k, str):
            if k.strip(): parts.append(html.escape(ws(k), quote=False))
        else:
            parts.append(html_node(k, ctx))
    ctx.in_cell = False
    return ''.join(parts)


def html_node(k, ctx):
    t, cl = k.tag, cls(k)
    if hidden(k): return ''
    if t == 'p':
        return '<p>%s</p>' % inline(k, ctx, 'html')
    if t in ('ul', 'ol'):
        return '<%s>%s</%s>' % (t, ''.join('<li>%s</li>' % cell_inner_html(li, ctx) for li in nodes(k) if li.tag == 'li'), t)
    if t == 'div' and ('itemizedlist' in cl or 'orderedlist' in cl):
        return ''.join(html_node(x, ctx) for x in nodes(k))
    if t == 'pre':
        return '<pre><code>%s</code></pre>' % html.escape(raw_text(k, False).strip('\n'), quote=False)
    if t == 'div' and 'mediaobject' in cl:
        return ''.join(img_block(im, ctx, None, k) for im in desc(k) if im.tag == 'img')
    if t == 'div' and (set(cl) & HINT_TAGS):
        title = ''.join(raw_text(x) for x in nodes(k) if x.tag == 'h3').strip()
        REP['cell_hints'].append((ctx.fn, title))
        return '<p><strong>%s</strong></p>' % title + ''.join(html_node(x, ctx) for x in nodes(k) if x.tag != 'h3')
    if t in INLINE_TAGS:
        return inline([k], ctx, 'html')
    return ''.join(html_node(x, ctx) if isinstance(x, V.Node) else etext(ws(x), ctx)
                   for x in k.children)


def cell_inner_html(li, ctx):
    return ''.join(html_node(x, ctx) if isinstance(x, V.Node) else etext(ws(x), ctx)
                   for x in li.children)


def table_rows(t):
    heads, body = [], []
    for k in nodes(t):
        if k.tag == 'thead':
            heads += [r for r in nodes(k) if r.tag == 'tr']
        elif k.tag in ('tbody', 'tfoot'):
            body += [r for r in nodes(k) if r.tag == 'tr']
        elif k.tag == 'tr':
            body.append(k)
    return heads, body


def table_block(t, ctx):
    heads, body = table_rows(t)
    allrows = heads + body
    cells = [[c for c in nodes(r) if c.tag in ('td', 'th')] for r in allrows]
    span = any(('colspan' in c.attrs or 'rowspan' in c.attrs) for row in cells for c in row)
    code = any(d.tag == 'pre' for row in cells for c in row for d in desc(c))
    nested = any(d.tag == 'table' and 'image-viewport' not in cls(d) for row in cells for c in row for d in desc(c))
    video = any(d.tag == 'iframe' for row in cells for c in row for d in desc(c))
    multihead = len(heads) > 1
    nohead = not heads
    if span or code or nested or video or multihead:
        reason = ','.join(k for k, v in (('span', span), ('code', code), ('nested', nested), ('video', video),
                                          ('multi-head', multihead)) if v)
        REP['html_tables'].append((ctx.fn, reason))
        return html_table(heads, body, ctx)
    ncols = max((len(r) for r in cells), default=0)
    if nohead:
        REP['no_thead'].append((ctx.fn, ''))
    old = ctx.in_cell
    ctx.in_cell = True
    ctx.md_cell = True

    def cell_md(c):
        bl = []
        for k in c.children:
            pass
        parts = blocks(c, ctx)
        s = '<br>'.join(p.replace('\n', '<br>') for p in parts)
        return s.replace('|', '\\|') if '\\|' not in s else s

    hdr = [cell_md(c) for c in nodes(heads[0]) if c.tag in ('td', 'th')] if heads else [''] * ncols
    rows = [[cell_md(c) for c in nodes(r) if c.tag in ('td', 'th')] for r in body]
    ctx.in_cell = old
    ctx.md_cell = False
    hdr += [''] * (ncols - len(hdr))
    lines = ['| ' + ' | '.join(hdr) + ' |', '| ' + ' | '.join(['---'] * ncols) + ' |']
    for r in rows:
        r += [''] * (ncols - len(r))
        lines.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(lines)


def html_table(heads, body, ctx):
    def row(r, tag):
        o = []
        for c in nodes(r):
            if c.tag not in ('td', 'th'): continue
            at = ''.join(' %s="%s"' % (a, c.attrs[a]) for a in ('colspan', 'rowspan') if a in c.attrs)
            o.append('<%s%s>%s</%s>' % (tag if c.tag == 'th' else 'td', at, cell_html(c, ctx), tag if c.tag == 'th' else 'td'))
        return '<tr>' + ''.join(o) + '</tr>'
    s = '<table>\n'
    if heads:
        s += '<thead>\n' + '\n'.join(row(r, 'th') for r in heads) + '\n</thead>\n'
    s += '<tbody>\n' + '\n'.join(row(r, 'td') for r in body) + '\n</tbody>\n</table>'
    return s


# ------------------------------------------------------------------ pages
def find_main(root):
    best = None
    for d in [root] + list(desc(root)):
        if d.tag == 'section' and 'data-permalink' in d.attrs:
            return d
    return V.find_main(root)


def convert_page(row):
    fn = os.path.basename(row['source_path'])
    space = row['space']
    t = V.Tree()
    t.feed(open(SRC + fn, encoding='utf-8', errors='replace').read())
    main = find_main(t.root)
    if main is None:
        REP['check'].append((fn, 'no main section', ''))
        return None
    title = ''
    for d in desc(main):
        if d.tag == 'h1':
            title = ws(raw_text(d)).strip()
            break
    ctx = Ctx(fn, space, faq=bool(re.search(r'faq|frequently asked', title, re.I)))
    body = blocks(main, ctx)
    md = '\n\n'.join(b for b in body if b is not None and b != '')
    md = re.sub(r'\n{3,}', '\n\n', md).strip() + '\n'
    return md


def main():
    pages = {}
    rows = [r for r in ALL if r['space'] not in SKIP_SPACES]
    for r in rows:
        md = convert_page(r)
        if md is None:
            continue
        d = OUT + r['space'] + '/'
        os.makedirs(d, exist_ok=True)
        open(d + r['file'], 'w', encoding='utf-8').write(md)
        pages[r['space'] + '/' + r['file']] = (r['space'], os.path.basename(r['source_path']))
    for (space, name), text in INCLUDES.items():
        d = OUT + space + '/.gitbook/includes/'
        os.makedirs(d, exist_ok=True)
        open(d + name, 'w', encoding='utf-8').write(text)
    for space, names in ASSETS.items():
        d = OUT + space + '/.gitbook/assets/'
        os.makedirs(d, exist_ok=True)
        for nme in names:
            p = SRC + 'image/' + nme
            if os.path.exists(p):
                shutil.copy(p, d + nme)
    json.dump({k: v for k, v in REP.items()}, open(WORK + 'report.json', 'w'), indent=1, default=list)
    json.dump(pages, open(WORK + 'pages.json', 'w'), indent=1)
    print('converted', len(pages), 'pages;', sum(len(v) for v in ASSETS.values()), 'asset refs;',
          len(INCLUDES), 'includes')
    for k, v in REP.items():
        print(' ', k, len(v))


if __name__ == '__main__':
    main()
