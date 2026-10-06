#!/usr/bin/env python3
"""Paligo HTML5 -> GitBook markdown converter (rules from the gitbook-paligo skill).
Verbatim import: only mechanical markup conversion, no text edits."""
import csv, os, re, sys, json, html, shutil, collections
sys.path.insert(0, '/mnt/skills/plugins/gitbook-paligo/scripts')
import verify_text as V

SRC = '/home/claude/src/18662-Checkmarx_SCA-html5/out/en/'
WORK = '/home/claude/work/'
OUT = '/mnt/user-data/outputs/gitbook-sca/'
SKIP_SPACES = {'checkmarx-sca--rest--api-documentation'}
SPACE_KEYS = {
    'checkmarx-sca-release-notes': 'RELEASE_NOTES', 'faq': 'FAQ',
    'checkmarx-sca---product-info': 'PRODUCT_INFO', 'checkmarx-sca---quick-start-tutorial': 'QUICK_START',
    'checkmarx-sca---user-guide': 'USER_GUIDE', 'checkmarx-sca-resolver': 'RESOLVER',
    'checkmarx-sca-integrations-and-plugins': 'INTEGRATIONS', 'checkmarx-sca--rest--api-documentation': 'REST_API'}

ALL = list(csv.DictReader(open(WORK + 'redirects-out/redirects.csv', newline='')))
BY_SRC = {os.path.basename(r['source_path']): r for r in ALL}
INC_MAP = {}
for r in csv.DictReader(open(WORK + 'reuse-out/includes-map.csv', newline='')):
    INC_MAP[r['element_uuid']] = r['include_file']

REP = collections.defaultdict(list)       # report buckets
ASSETS = collections.defaultdict(set)     # space -> image files
INCLUDES = {}                              # (space, name) -> text
INC_RENDERS = {}                           # (space, name) -> first rendering page
MARKS = re.compile(r'')


# ---------------------------------------------------------------- helpers
def cls(n):
    return V.cls(n)


def nodes(n):
    return [c for c in n.children if isinstance(c, V.Node)]


def desc(n):
    for c in n.children:
        if isinstance(c, V.Node):
            yield c
            yield from desc(c)


def raw_text(n):
    o = []
    for c in n.children:
        o.append(c if isinstance(c, str) else raw_text(c))
    return ''.join(o)


def ws(t):
    return re.sub(r'[ \t\r\n]+', ' ', t)


def esc_md(t, cell=False):
    t = t.replace('\\', '\\\\')
    t = re.sub(r'([*`\[\]<>~])', r'\\\1', t)
    t = re.sub(r'(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])', r'\\_', t)
    t = re.sub(r'\{(?=[%{])', r'\\{', t)
    t = re.sub(r'&(?=#?\w+;)', r'\\&', t)
    if cell:
        t = t.replace('|', r'\|')
    return t


def esc_mdhtml(t):
    t = html.escape(t, quote=False)
    t = t.replace('\\', '\\\\')
    t = re.sub(r'([*`\[\]~])', r'\\\1', t)
    t = re.sub(r'(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])', r'\\_', t)
    t = re.sub(r'\{(?=[%{])', r'\\{', t)
    return t.replace('|', r'\|')


def esc_start(s):
    if re.match(r'^\d+[.)]( |$)', s):
        return re.sub(r'^(\d+)([.)])', r'\1\\\2', s)
    if re.match(r'^[-+] ', s) or s in ('-', '+'):
        return '\\' + s
    if s.startswith('#'):
        return '\\' + s
    return s


def elem_uuid(n):
    m = re.search(r'_UUID-([0-9a-f-]{36})$', n.attrs.get('id', ''))
    return m.group(1) if m else None


def hint_kind(n):
    c = set(cls(n))
    if 'div' != n.tag:
        return None
    if c & {'note', 'tip', 'warning', 'caution', 'important', 'danger'}:
        return True
    return None


class Ctx:
    def __init__(self, page_fn, space, faq=False):
        self.fn, self.space, self.faq = page_fn, space, faq
        self.in_cell = False
        self.in_acc = 0
        self.root_uuid = None   # element being rendered as an include (don't re-include)


# ---------------------------------------------------------------- links / images
def map_href(href, ctx, text=''):
    if not href:
        return href
    if href.startswith('mailto:') or re.match(r'^[a-z][a-z0-9+.-]*://', href, re.I) and 'docs.checkmarx.com/en/' not in href:
        return href
    m = re.match(r'^(?:https?://docs\.checkmarx\.com)?(?:/?en/)?([^/#?:]+\.html)(#.*)?$', href)
    if m:
        base, frag = m.group(1), m.group(2) or ''
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
    if href.startswith('/document/'):
        REP['paligo_doc_links'].append((ctx.fn, text, href))
        return href
    if href.startswith('#'):
        REP['anchor_links'].append((ctx.fn, href))
        return href
    if not re.match(r'^[a-z][a-z0-9+.-]*:', href, re.I):
        REP['unresolved_links'].append((ctx.fn, text, href))
    return href


def md_url(u):
    return u.replace(' ', '%20').replace('(', '%28').replace(')', '%29')


def img_path(img, ctx):
    src = img.attrs.get('src', '')
    name = os.path.basename(src)
    if not os.path.exists(SRC + 'image/' + name):
        REP['missing_images'].append((ctx.fn, src))
    ASSETS[ctx.space].add(name)
    return '.gitbook/assets/' + name


def size_from(width, unit):
    """returns (attr or None, label)"""
    v = round(float(width))
    if unit == '%':
        if v >= 90: return None, 'Fit'
        if v >= 60: return '75%', 'Large'
        if v >= 40: return '50%', 'Medium'
        return '25%', 'Small'
    if v >= 720: return None, 'Fit'
    if v >= 480: return '75%', 'Large'
    if v >= 320: return '50%', 'Medium'
    return '25%', 'Small'


def find_size(mo, img):
    """returns (value, unit, source) or None"""
    for t in desc(mo):
        if t.tag == 'table' and 'image-viewport' in cls(t):
            m = re.search(r'width:\s*([\d.]+)\s*(px|%)', t.attrs.get('style', ''))
            if m:
                return m.group(1), m.group(2), 'image-viewport'
    st = img.attrs.get('style', '')
    m = re.search(r'max-width:\s*([\d.]+)\s*px', st)
    if m:
        return m.group(1), 'px', 'img max-width'
    m = re.search(r'(?<![-\w])width:\s*([\d.]+)\s*(px|%)', st)
    if m:
        return m.group(1), m.group(2), 'img width'
    return None


# ---------------------------------------------------------------- inline
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
    if '`' in text:
        return '`` ' + text.strip() + ' ``'
    return '`' + text + '`'


def inline(n_or_list, ctx, mode='md', cell=False):
    kids = n_or_list.children if isinstance(n_or_list, V.Node) else n_or_list
    out = []
    for c in kids:
        if isinstance(c, str):
            t = ws(c)
            out.append(html.escape(t, quote=False) if mode == 'html' else esc_mdhtml(t) if mode == 'mdhtml' else esc_md(t, cell))
            continue
        out.append(inline_node(c, ctx, mode, cell))
    s = ''.join(out)
    return re.sub(r' {2,}', ' ', s)


def inline_node(c, ctx, mode, cell):
    t, cl = c.tag, cls(c)
    H = mode in ('html', 'mdhtml')
    if t == 'span' and 'linktextprovider' in cl:
        REP['hidden_spans'].append((ctx.fn, raw_text(c)))
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
        if H:
            return '<code>%s</code>' % (esc_mdhtml(txt) if mode == 'mdhtml' else html.escape(txt, quote=False))
        sp = code_span(txt)
        return sp.replace('|', '\\|') if cell else sp
    if t == 'sup' or t == 'sub':
        return '<%s>%s</%s>' % (t, inline(c, ctx, mode, cell), t)
    if t == 'span' and 'underline' in cl:
        return wrap('<u>', inline(c, ctx, mode, cell), '</u>')
    if t == 'br':
        return '<br>'
    if t == 'img':
        p = img_path(c, ctx)
        return '<img src="%s" alt="">' % p if H else '![](%s)' % p
    if t == 'a':
        href = c.attrs.get('href', '')
        inner = inline(c, ctx, mode, cell)
        if 'data-toggle' in c.attrs:
            return inner
        inner = re.sub(r'</?u>', '', inner)
        text = raw_text(c).strip()
        if not inner.strip():
            return inner
        u = map_href(href, ctx, text)
        if H:
            return '<a href="%s">%s</a>' % (html.escape(u), inner)
        lead = inner[:len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        return '%s[%s](%s)%s' % (lead, inner.strip(), md_url(u), trail)
    if t in ('span', 'u', 'small', 'font', 'abbr', 'cite', 'q', 'time', 'label'):
        return inline(c, ctx, mode, cell)
    REP['unhandled_inline'].append((ctx.fn, t, ' '.join(cl)))
    return inline(c, ctx, mode, cell)


# ---------------------------------------------------------------- block rendering
INLINE_TAGS = {'span', 'strong', 'b', 'em', 'i', 'code', 'a', 'sup', 'sub', 'img', 'br', 'u', 'small'}
HINT_STYLE = {'Notice': ('info', 'pencil'), 'Note': ('info', None), 'Tip': ('info', None),
              'Warning': ('warning', None), 'Caution': ('warning', None),
              'Important': ('success', 'key'), 'Danger': ('danger', None)}


def is_accordion(n):
    c = cls(n)
    if n.tag == 'div' and 'sidebar' in c and 'accordion' in c:
        return True
    if n.tag == 'section' and any(x.startswith('accordion') for x in c):
        return True
    return False


def indent(s, n, first=None):
    lines = s.split('\n')
    pad = ' ' * n
    out = []
    for i, l in enumerate(lines):
        if i == 0 and first is not None:
            out.append(first + l)
        else:
            out.append((pad + l) if l.strip() else '')
    return '\n'.join(out)


def blocks(kids, ctx):
    """convert a child list to a list of markdown block strings"""
    out = []
    pend = []           # pending inline nodes (implicit paragraph)
    i = 0
    kids = list(kids)

    def flush():
        nonlocal pend
        if pend:
            s = inline(pend, ctx).strip()
            if s:
                out.append(esc_start(s))
            pend = []

    while i < len(kids):
        c = kids[i]
        if isinstance(c, str):
            pend.append(c)
            i += 1
            continue
        if c.tag in INLINE_TAGS:
            pend.append(c)
            i += 1
            continue
        flush()
        if is_accordion(c):
            grp = [c]
            j = i + 1
            while j < len(kids):
                k = kids[j]
                if isinstance(k, str) and not k.strip():
                    j += 1
                    continue
                if isinstance(k, V.Node) and is_accordion(k):
                    grp.append(k)
                    j += 1
                    continue
                break
            out.append(accordions(grp, ctx))
            i = j
            continue
        out.extend(block(c, ctx))
        i += 1
    flush()
    return [b for b in out if b is not None and b.strip()]


def block(n, ctx):
    t, cl = n.tag, cls(n)
    # reused content -> include
    u = elem_uuid(n)
    if u and u in INC_MAP and u != ctx.root_uuid and not ctx.in_cell and \
            ((t == 'div' and hint_kind(n)) or t == 'section'):
        name = INC_MAP[u]
        key = (ctx.space, name)
        c2 = Ctx(ctx.fn, ctx.space, ctx.faq)
        c2.root_uuid = u
        body = '\n\n'.join(block_inner(n, c2))
        if key in INCLUDES:
            if INCLUDES[key] != body:
                REP['include_mismatch'].append((name, ctx.fn, INC_RENDERS[key]))
        else:
            INCLUDES[key] = body
            INC_RENDERS[key] = ctx.fn
        REP['include_use'].append((ctx.space, name, ctx.fn))
        return ['{%% include ".gitbook/includes/%s" %%}' % name]
    return block_inner(n, ctx)


def block_inner(n, ctx):
    t, cl = n.tag, cls(n)
    if t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        s = inline(n, ctx).strip()
        return ['%s %s' % ('#' * int(t[1]), s)] if s else []
    if t == 'p':
        s = inline(n, ctx, cell=False).strip()
        return [esc_start(s)] if s else []
    if t == 'section':
        return blocks(n.children, ctx_section(n, ctx))
    if t == 'div' and hint_kind(n):
        return [hint(n, ctx)]
    if t == 'div' and ('mediaobject' in cl or 'informalfigure' in cl):
        return media(n, ctx)
    if t == 'div' and ('flex-container' in cl):
        return blocks(n.children, ctx)
    if t == 'div' and 'caption' in cl:
        REP['captions'].append((ctx.fn, raw_text(n).strip()))
        return []
    if t in ('ul', 'ol'):
        return [lst(n, ctx)]
    if t == 'div' and ({'itemizedlist', 'orderedlist', 'procedure'} & set(cl)):
        return blocks(n.children, ctx)
    if t == 'div' and 'blockquote' in cl or t == 'blockquote':
        inner = blocks(n.children, ctx) if t == 'div' else blocks(n.children, ctx)
        if t == 'div':
            return inner
        return ['\n>\n'.join('> ' + b.replace('\n', '\n> ') for b in inner)]
    if t == 'table' and 'image-viewport' in cl:
        return media(n, ctx)
    if t == 'table' or (t == 'div' and 'informaltable' in cl):
        tb = n if t == 'table' else next((x for x in desc(n) if x.tag == 'table'), None)
        return [table(tb, ctx)] if tb else []
    if t == 'pre':
        return [code_block(n, ctx)]
    if t == 'iframe':
        return video(n, ctx)
    if t in ('script', 'style', 'nav', 'header', 'footer', 'noscript'):
        return []
    if t == 'div' or t == 'span' or t == 'article' or t == 'main':
        return blocks(n.children, ctx)
    REP['unhandled_block'].append((ctx.fn, t, ' '.join(cl)))
    return blocks(n.children, ctx)


def ctx_section(n, ctx):
    return ctx


# ---------- hints
def hint(n, ctx):
    title = None
    body = []
    for c in n.children:
        if isinstance(c, V.Node) and c.tag in ('h2', 'h3', 'h4') and 'title' in cls(c) and title is None:
            title = raw_text(c).strip()
            continue
        body.append(c)
    cset = set(cls(n))
    if title not in HINT_STYLE:
        REP['hint_odd_title'].append((ctx.fn, title, ' '.join(cl for cl in cls(n))))
        style, icon = ('info', None)
    else:
        style, icon = HINT_STYLE[title]
    expect = {'Notice': 'notice', 'Note': 'note', 'Tip': 'tip', 'Warning': 'warning', 'Caution': 'caution'}.get(title)
    if expect and expect not in cset or (title == 'Note' and cset & {'tip', 'warning', 'caution'}):
        REP['hint_class_title_conflict'].append((ctx.fn, title, ' '.join(cls(n))))
    inner = '\n\n'.join(blocks(body, ctx))
    attrs = 'style="%s"' % style + (' icon="%s"' % icon if icon else '')
    return '{%% hint %s %%}\n%s\n{%% endhint %%}' % (attrs, inner)


# ---------- lists
def lst(n, ctx):
    ordered = n.tag == 'ol'
    if ordered and n.attrs.get('type') not in (None, '1'):
        REP['ol_type'].append((ctx.fn, n.attrs.get('type'), raw_text(n).strip()[:60]))
    items = [c for c in nodes(n) if c.tag == 'li']
    out = []
    for k, li in enumerate(items, 1):
        bl = blocks(li.children, ctx)
        if not bl:
            continue
        marker = ('%d. ' % k) if ordered else '- '
        body = '\n\n'.join(bl)
        out.append(indent(body, len(marker), first=marker))
    return '\n'.join(out)


# ---------- code
def code_block(n, ctx):
    txt = raw_text(n).replace('\r\n', '\n').strip('\n')
    lang = n.attrs.get('data-language', '')
    if not lang:
        s = txt.lstrip()
        if re.match(r'^<[A-Za-z?]', s):
            lang = 'xml'
        elif re.match(r'^(USE|update|select|insert|SELECT|UPDATE)\b', s):
            lang = 'sql'
    fence = '```'
    while fence in txt:
        fence += '`'
    return '%s%s\n%s\n%s' % (fence, lang, txt, fence)


# ---------- media
def video(ifr, ctx):
    src = ifr.attrs.get('src', '')
    m = re.match(r'https://player\.vimeo\.com/video/(\d+)(?:\?(.*))?$', src.replace('&amp;', '&'))
    if not m:
        if 'googletagmanager' in src:
            return []
        REP['video_check'].append((ctx.fn, src))
        return []
    vid, q = m.group(1), m.group(2) or ''
    h = re.search(r'(?:^|&)h=([0-9a-f]+)', q)
    url = 'https://vimeo.com/%s%s' % (vid, '/' + h.group(1) if h else '')
    REP['videos'].append((ctx.fn, vid, 'hash' if h else ''))
    return ['{%% embed url="%s" %%}' % url]


def media(n, ctx):
    """div.mediaobject / div.informalfigure / table.image-viewport"""
    res = []
    # video?
    ifr = next((x for x in desc(n) if x.tag == 'iframe'), None)
    if ifr is not None:
        return video(ifr, ctx)
    # flex container: each flex-item is its own image
    items = [x for x in desc(n) if x.tag == 'div' and 'flex-item' in cls(x)]
    if items:
        for it in items:
            imgs = [x for x in desc(it) if x.tag == 'img']
            w = re.search(r'width:\s*([\d.]+)%', it.attrs.get('style', ''))
            for im in imgs:
                res.append(img_block(im, ctx, (w.group(1), '%', 'flex-item') if w else None, n))
        return res
    for cap in [x for x in desc(n) if x.tag == 'div' and 'caption' in cls(x)]:
        REP['captions'].append((ctx.fn, raw_text(cap).strip()))
    for im in [x for x in desc(n) if x.tag == 'img']:
        res.append(img_block(im, ctx, find_size(n, im), n))
    return res


def img_block(im, ctx, size, mo):
    p = img_path(im, ctx)
    if ctx.in_cell:
        REP['cell_images'].append((ctx.fn, p))
        return '<img src="%s" alt="">' % p
    if size is None:
        attr, label = None, 'Fit'
        REP['image_sizes'].append((ctx.fn, os.path.basename(p), 'none', '', 'Fit (defaulted)'))
    else:
        val, unit, src = size
        attr, label = size_from(val, unit)
        REP['image_sizes'].append((ctx.fn, os.path.basename(p), src, val + unit, label))
    w = ' width="%s"' % attr if attr else ''
    return '<div align="left"><figure><img src="%s" alt=""%s></figure></div>' % (p, w)


# ---------- accordions
PLATFORM = re.compile(r'^(windows|linux|mac(os)?|linux ?/ ?mac|mac ?/ ?linux|docker|podman|vs ?code|visual studio( code)?|cursor|windsurf|kiro|intellij|eclipse|jetbrains|bash|powershell)', re.I)


def acc_parts(a, ctx):
    title = ''
    body = None
    for d in desc(a):
        if d.tag == 'div' and 'sidebar-title' in cls(d) and not title:
            title = raw_text(d).strip()
        if d.tag in ('h2', 'h3', 'h4', 'h5', 'h6') and 'title' in cls(d) and not title:
            title = raw_text(d).strip()
        if d.tag == 'div' and 'panel-body' in cls(d) and body is None:
            body = d
    return ws(title).strip(), body


def accordions(grp, ctx):
    parts = [acc_parts(a, ctx) for a in grp]
    titles = [p[0] for p in parts]
    nested = ctx.in_acc > 0
    if ctx.faq:
        form = 'details'
    elif nested:
        form = 'details'
    elif all(PLATFORM.match(t) for t in titles):
        form = 'tabs'
    elif 2 <= len(grp) <= 8:
        form = 'tabs'
    else:
        form = 'details'
    REP['accordions'].append((ctx.fn, len(grp), form, 'nested' if nested else ('faq' if ctx.faq else ''), ' | '.join(titles)[:90]))
    ctx.in_acc += 1
    outs = []
    for (title, body) in parts:
        inner = '\n\n'.join(blocks(body.children, ctx)) if body is not None else ''
        outs.append((title, inner))
    ctx.in_acc -= 1
    if form == 'tabs':
        s = ['{% tabs %}']
        for title, inner in outs:
            if '"' in title:
                REP['tab_title_quote'].append((ctx.fn, title))
                title = title.replace('"', '&quot;')
            s.append('{%% tab title="%s" %%}\n%s\n{%% endtab %%}' % (title, inner))
        s.append('{% endtabs %}')
        return '\n'.join(s)
    res = []
    for title, inner in outs:
        res.append('<details>\n<summary>%s</summary>\n\n%s\n\n</details>' % (html.escape(title, quote=False), inner))
    return '\n\n'.join(res)


# ---------- tables
def cell_blocks(cell, ctx, mode):
    """return list of line-strings for a table cell (joined by <br>)"""
    parts = []
    pend = []

    def flush():
        nonlocal pend
        if pend:
            s = inline(pend, ctx, mode, cell=True).strip()
            if s:
                parts.append(s)
            pend = []

    def walk(kids):
        nonlocal pend
        for c in kids:
            if isinstance(c, str) or c.tag in INLINE_TAGS:
                pend.append(c)
                continue
            flush()
            cl = cls(c)
            if c.tag == 'p':
                s = inline(c, ctx, mode, cell=True).strip()
                if s:
                    parts.append(s)
            elif c.tag in ('ul', 'ol'):
                parts.append(html_list(c, ctx, mode))
            elif c.tag == 'div' and {'itemizedlist', 'orderedlist', 'procedure'} & set(cl):
                walk(c.children)
            elif c.tag == 'div' and hint_kind(c):
                title = None
                rest = []
                for x in c.children:
                    if isinstance(x, V.Node) and x.tag in ('h2', 'h3', 'h4') and 'title' in cls(x) and title is None:
                        title = raw_text(x).strip()
                    else:
                        rest.append(x)
                REP['cell_hints'].append((ctx.fn, title))
                sub = cell_blocks_list(rest, ctx, mode)
                lead = ('<strong>%s</strong> ' % title) if mode in ('html', 'mdhtml') else ('**%s** ' % title)
                if sub:
                    sub[0] = lead + sub[0]
                else:
                    sub = [lead.strip()]
                parts.extend(sub)
            elif c.tag == 'div' and ('mediaobject' in cl or 'informalfigure' in cl):
                for b in media(c, ctx):
                    parts.append(b)
            elif c.tag == 'table' and 'image-viewport' in cl:
                for b in media(c, ctx):
                    parts.append(b)
            elif c.tag == 'pre':
                parts.append('<pre>%s</pre>' % html.escape(raw_text(c).strip('\n'), quote=False))
                REP['cell_pre'].append((ctx.fn,))
            elif c.tag == 'div' and 'caption' in cl:
                REP['captions'].append((ctx.fn, raw_text(c).strip()))
            elif c.tag in ('div', 'span', 'section'):
                walk(c.children)
            elif c.tag.startswith('h') and len(c.tag) == 2:
                parts.append(inline(c, ctx, mode, cell=True).strip())
            else:
                REP['unhandled_cell'].append((ctx.fn, c.tag, ' '.join(cl)))
                walk(c.children)
        flush()

    walk(cell.children)
    return parts


def cell_blocks_list(kids, ctx, mode):
    fake = V.Node('div', [])
    fake.children = kids
    return cell_blocks(fake, ctx, mode)


def html_list(l, ctx, mode='html'):
    tag = l.tag
    items = []
    for li in [c for c in nodes(l) if c.tag == 'li']:
        sub = cell_blocks(li, ctx, 'mdhtml' if mode in ('md', 'mdhtml') else 'html')
        items.append('<li>%s</li>' % '<br>'.join(sub))
    return '<%s>%s</%s>' % (tag, ''.join(items), tag)


def table(tb, ctx):
    secs = nodes(tb)
    trs = []
    thead_rows = []
    for s in secs:
        if s.tag == 'thead':
            thead_rows += [r for r in nodes(s) if r.tag == 'tr']
        elif s.tag == 'tbody':
            trs += [(r, False) for r in nodes(s) if r.tag == 'tr']
        elif s.tag == 'tr':
            trs.append((s, False))
    rows_h = [(r, True) for r in thead_rows]
    allrows = rows_h + trs
    has_span = any(('colspan' in c.attrs or 'rowspan' in c.attrs) for r, _ in allrows for c in nodes(r))
    prev = ctx.in_cell
    ctx.in_cell = True
    try:
        ncols = [len([c for c in nodes(r) if c.tag in ('td', 'th')]) for r, _ in allrows]
        has_pre = any(d.tag == 'pre' for d in desc(tb))
        if has_span or has_pre or not thead_rows or len(thead_rows) > 1 or len(set(ncols)) > 1:
            REP['html_tables'].append((ctx.fn, 'span' if has_span else ('code block in cell' if has_pre else 'no thead / ragged')))
            lines = ['<table>']
            if thead_rows:
                lines.append('<thead>')
                for r in thead_rows:
                    lines.append(html_row(r, ctx))
                lines.append('</thead>')
            lines.append('<tbody>')
            for r, _ in trs:
                lines.append(html_row(r, ctx))
            lines.append('</tbody>')
            lines.append('</table>')
            return '\n'.join(lines)
        def mdrow(r):
            cells = [c for c in nodes(r) if c.tag in ('td', 'th')]
            return '| ' + ' | '.join('<br>'.join(cell_blocks(c, ctx, 'md')) for c in cells) + ' |'
        hdr = mdrow(thead_rows[0])
        sep = '| ' + ' | '.join('---' for _ in range(ncols[0])) + ' |'
        body = [mdrow(r) for r, _ in trs]
        return '\n'.join([hdr, sep] + body)
    finally:
        ctx.in_cell = prev


def html_row(r, ctx):
    cells = []
    for c in nodes(r):
        if c.tag not in ('td', 'th'):
            continue
        a = ''
        for k in ('colspan', 'rowspan'):
            if k in c.attrs:
                a += ' %s="%s"' % (k, c.attrs[k])
        cells.append('<%s%s>%s</%s>' % (c.tag, a, '<br>'.join(cell_blocks(c, ctx, 'html')), c.tag))
    return '<tr>' + ''.join(cells) + '</tr>'


# ---------------------------------------------------------------- page
def find_main(root):
    def go(n):
        for c in n.children:
            if isinstance(c, V.Node):
                if c.tag == 'section' and ('data-permalink' in c.attrs or 'original-topic' in cls(c)):
                    return c
                r = go(c)
                if r:
                    return r
        return None
    return go(root)


def convert_page(row):
    fn = os.path.basename(row['source_path'])
    t = V.Tree()
    t.feed(open(SRC + fn, encoding='utf-8').read())
    main = find_main(t.root)
    if main is None:
        REP['no_main'].append(fn)
        return None
    # title
    h1 = None
    for d in desc(main):
        if d.tag == 'h1':
            h1 = d
            break
    title = inline(h1, Ctx(fn, row['space'])).strip() if h1 is not None else ''
    faq = bool(re.search(r'\bFAQ\b|Frequently Asked', raw_text(h1) if h1 is not None else '', re.I)) or 'faq' in fn
    ctx = Ctx(fn, row['space'], faq)
    # drop the h1 from the body: render children skipping that h1
    kids = []

    def strip_h1(n):
        out = []
        for c in n.children:
            if c is h1:
                continue
            out.append(c)
        return out
    body_blocks = []
    # Walk: main's children; h1 sits inside div.titlepage
    def render_children(n):
        res = []
        pend = []
        for c in n.children:
            res.append(c)
        return res
    # temporarily remove h1 from its parent
    if h1 is not None:
        h1.parent.children = [c for c in h1.parent.children if c is not h1]
    bl = blocks(main.children, ctx)
    md = ('# %s\n\n' % title if title else '') + '\n\n'.join(bl) + '\n'
    if not title:
        REP['no_title'].append(fn)
    return md, title, ctx


if __name__ == '__main__':
    only = sys.argv[1:]
    rows = [r for r in ALL if r['space'] not in SKIP_SPACES]
    if only:
        rows = [r for r in rows if r['file'] in only or os.path.basename(r['source_path']) in only]
    pages = {}
    shutil.rmtree(OUT, ignore_errors=True)
    for r in rows:
        res = convert_page(r)
        if res is None:
            continue
        md, title, ctx = res
        d = OUT + r['space'] + '/'
        os.makedirs(d, exist_ok=True)
        open(d + r['file'], 'w', encoding='utf-8').write(md)
        pages[r['space'] + '/' + r['file']] = (r['space'], os.path.basename(r['source_path']))
    # includes
    for (space, name), body in INCLUDES.items():
        d = OUT + space + '/.gitbook/includes/'
        os.makedirs(d, exist_ok=True)
        open(d + name, 'w', encoding='utf-8').write(body + '\n')
    # assets
    for space, names in ASSETS.items():
        d = OUT + space + '/.gitbook/assets/'
        os.makedirs(d, exist_ok=True)
        for nme in names:
            p = SRC + 'image/' + nme
            if os.path.exists(p):
                shutil.copy(p, d + nme)
    # SUMMARY.md
    for space in sorted({r['space'] for r in rows}):
        sr = [r for r in ALL if r['space'] == space]
        lines = ['# Summary', '']
        for r in sr:
            dep = int(r['depth'])
            title = r['title'] or r['slug']
            title = title.replace('[', '\\[').replace(']', '\\]')
            lines.append('%s* [%s](%s)' % ('  ' * dep, title, r['file']))
        d = OUT + space + '/'
        os.makedirs(d + '.gitbook/assets', exist_ok=True)
        open(d + 'SUMMARY.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    json.dump({k: v for k, v in REP.items()}, open(WORK + 'report.json', 'w'), indent=1, default=list)
    json.dump(pages, open(WORK + 'pages.json', 'w'), indent=1)
    print('converted', len(pages), 'pages;', sum(len(v) for v in ASSETS.values()), 'asset refs;', len(INCLUDES), 'includes')
    for k, v in REP.items():
        print(' ', k, len(v))
