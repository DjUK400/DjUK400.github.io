import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from skin import apply, HUB
H = '/home/claude/'
ALL = (HUB, '← Sve aplikacije')

# ---------- 1. Rješavač inverznih funkcija (uzor) ----------
apply(H+'Rje-ava-a-inverznih-funkcija/index.html', '', [ALL], '1080px', fonts=False)

# ---------- 2. Limesi nizova ----------
LIM = """
:root:root:root{--bg:var(--fk-bg);--card:var(--fk-paper);--ink:var(--fk-ink);--mute:var(--fk-ink2);--line:var(--fk-rule);
  --acc:var(--fk-blue);--acc-soft:var(--fk-blue-bg);--ok:var(--fk-ok);--ok-soft:var(--fk-ok-bg);--bad:var(--fk-err);--bad-soft:var(--fk-err-bg);
  --warn:var(--fk-warn);--warn-soft:var(--fk-warn-bg);--why:var(--fk-chip);--why-line:var(--fk-blue)}
html body,html{font:16px/1.5 var(--fk-body)}
html .wrap{max-width:var(--fk-w);padding:22px max(16px,env(safe-area-inset-right,0px)) 56px max(16px,env(safe-area-inset-left,0px))}
html header.fk-head{display:block;margin:0}
html .card,html .step,html .form{border-radius:4px}
html .card{border-color:var(--fk-rule)}
html select,html input[type=text]{border-radius:4px;border:1.5px solid var(--fk-ink2)}
html .btn{background:var(--fk-ink);color:var(--fk-paper);border:1.5px solid var(--fk-ink);border-radius:4px;font:600 16px var(--fk-body);padding:8px 16px}
html .btn.ghost{background:transparent;color:var(--fk-ink)}
html .btn.small{font-size:14px;padding:6px 11px}
html .chip{border:1px dashed var(--fk-ink2);background:transparent;color:var(--fk-ink);font-size:14px}
html .chip:hover{border-color:var(--fk-ink);color:var(--fk-ink)}
html .step h3{font:700 18px/1.25 var(--fk-head)}
html .step h3:before{background:transparent;color:var(--fk-ink);border:1.5px solid var(--fk-ink);border-radius:50%;min-width:22px;height:22px;display:inline-grid;place-items:center;padding:0;font-size:13px}
html .why{border-radius:4px}
html .result{border:1.5px solid var(--fk-ink);background:var(--fk-paper);border-radius:3px}
html .result .lab{color:var(--fk-ink2)}
html .toast{border-radius:4px;border:1px solid var(--fk-rule);border-left:5px solid var(--fk-err)}
html .toast.warn{border-left-color:var(--fk-warn)}
html .sw{background:var(--fk-rule)}
html .rules h2,html .rules h3{font-family:var(--fk-head);font-weight:700}
html .rules h2{font-size:22px}
html details summary{color:var(--fk-blue)}
html footer{text-align:left;margin-top:40px;padding:12px 0 0;border-top:1px solid var(--fk-rule);font-size:13.5px;color:var(--fk-ink2)}
"""
p = pathlib.Path(H+'Rjesavanje-Limes-Niza/index.html'); s = p.read_text()
old = re.search(r'<header>.*?</header>', s, re.S)
if old and 'fk-head' not in old.group(0):
    s = s.replace(old.group(0), '''<header class="fk-head">
  <p class="fk-eyebrow">Matematika · limesi nizova</p>
  <h1 class="fk-h1">Limesi nizova</h1>
  <p class="fk-lede">Rješavač s postupkom, hintovima i objašnjenjima. Izaberi tip zadatka, upiši niz i dobićeš svaki korak, uz „Zašto?“ za razlog.</p>
  <nav class="tabs fk-tabs" role="tablist">
    <button class="on" data-tab="solve">Rješavač</button>
    <button data-tab="rules">Pravila i pojmovi</button>
  </nav>
  <button id="theme" hidden></button>
</header>''')
    p.write_text(s)
apply(str(p), LIM, [ALL], '860px')

# ---------- 3. Rješavač ortogonalnih projekcija ----------
ORT = """
:root:root:root{--paper:var(--fk-bg);--panel:var(--fk-paper);--ink:var(--fk-ink);--muted:var(--fk-ink2);--line:var(--fk-rule);--soft:var(--fk-chip);
  --grid:var(--fk-grid5);--h:var(--fk-h);--f:var(--fk-f);--p:var(--fk-p);--warn-bg:var(--fk-warn-bg);--warn-fg:var(--fk-warn);
  --f-body:var(--fk-body);--r:4px}
html body{font-size:16px}
html .wrap{padding-top:22px}
html header.top{display:block;margin-bottom:18px}
html textarea#postava{border-radius:4px;border:1.5px solid var(--fk-ink2);background:var(--fk-bg)}
html select{border-radius:4px}
html .keys button,html .zoom button,html .stepbar .navb{border-radius:4px}
html .btn{font:600 16px var(--fk-body);letter-spacing:0;border-radius:4px;border:1.5px solid var(--fk-ink);background:transparent;color:var(--fk-ink)}
html .btn.primary{background:var(--fk-ink);color:var(--fk-paper)}
html .lbl{font-size:13px;letter-spacing:.09em}
html .notice{border-radius:4px}
html .caption h2{font-size:22px}
html footer.foot{margin-top:40px;padding-top:12px;border-top:1px solid var(--fk-rule);font-size:13.5px}
"""
p = pathlib.Path(H+'Aplikacija-Za-Nacrtnu-Geometriju/index.html'); s = p.read_text()
old = re.search(r'<header class="top">.*?</header>', s, re.S)
if old and 'fk-h1' not in old.group(0):
    s = s.replace(old.group(0), '''<header class="top">
    <p class="fk-eyebrow">Nacrtna geometrija · rješavač</p>
    <h1 class="fk-h1">Rješavač ortogonalnih projekcija</h1>
    <p class="sub fk-lede">Upiši postavu zadatka iz nacrtne geometrije. Stranica prepozna tačke, prave i ravni, i riješi zadatak u prvoj i drugoj projekciji, korak po korak.</p>
  </header>''')
    p.write_text(s)
apply(str(p), ORT, [ALL], '1320px')

# ---------- 4. MM Rješavač (LAAG) — mijenja se src, pa build.py ----------
LAAG = """
:root:root:root{--bg:var(--fk-bg);--card:var(--fk-paper);--ink:var(--fk-ink);--mute:var(--fk-ink2);--line:var(--fk-rule);--soft:var(--fk-chip);
  --acc:var(--fk-blue);--acc-ink:var(--fk-paper);--ok:var(--fk-ok);--ok-bg:var(--fk-ok-bg);--no:var(--fk-err);--no-bg:var(--fk-err-bg);--warn:var(--fk-warn);
  --sans:var(--fk-body)}
html header.top{max-width:var(--fk-w);padding:22px max(16px,env(safe-area-inset-right,0px)) 0 max(16px,env(safe-area-inset-left,0px))}
html nav.tabs{position:sticky;top:0;z-index:5;background:var(--fk-bg);border:0;margin-top:0;padding-top:6px}
html nav.tabs .inner.fk-tabs{max-width:var(--fk-w);margin:0 auto;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding:0 max(16px,env(safe-area-inset-right,0px)) 0 max(16px,env(safe-area-inset-left,0px));
  box-shadow:none;background:linear-gradient(var(--fk-ink),var(--fk-ink)) bottom/calc(100% - 32px) 1.5px no-repeat}
html nav.tabs .inner.fk-tabs>button{border-bottom:0;padding:8px 12px}
html main,html footer{max-width:var(--fk-w)}
html .card{border-radius:4px;border-color:var(--fk-rule)}
html .card h2{font:700 22px/1.2 var(--fk-head)}
html .card h3{font:700 18px/1.25 var(--fk-head)}
html input[type=text],html input:not([type]),html input[type=number],html textarea,html select{border-radius:4px;border:1.5px solid var(--fk-ink2)}
html button{border-radius:4px;font-family:var(--fk-body)}
html button.primary{background:var(--fk-ink);border-color:var(--fk-ink);color:var(--fk-paper);font-size:16px;padding:8px 16px}
html button.ex{border:1px dashed var(--fk-ink2);border-radius:999px}
html .subtabs{top:52px}
html .subtabs button{border-radius:999px}
html .eq,html details.theory,html .verdict{border-radius:4px}
html .toast{border-radius:4px}
html footer{padding:12px max(16px,env(safe-area-inset-right,0px)) 30px max(16px,env(safe-area-inset-left,0px));border-top:1px solid var(--fk-rule);font-size:13.5px;color:var(--fk-ink2)}
"""
L = pathlib.Path(H+'LAAG-Rjesavanje-Zadataka')
sh = (L/'src/shell.html').read_text()
old = re.search(r'<header class="top">.*?</header>\s*<nav class="tabs"><div class="inner">', sh, re.S)
if old:
    sh = sh.replace(old.group(0), '''<!--fk-head--><header class="top">
  <p class="fk-eyebrow">Matematika · prvi kolokvijum</p>
  <h1 class="fk-h1">MM Rješavač</h1>
  <p class="fk-lede">Postavi zadatak, dobij rješenje sa postupkom. U svakom tabu su pravila i teorija tog poglavlja: logika, skupovi, relacije, funkcije i indukcija.</p>
  <button id="theme" hidden></button>
</header>
<nav class="tabs"><div class="inner fk-tabs">''')
    (L/'src/shell.html').write_text(sh)
mj = (L/'src/main.js').read_text().replace('"mm-theme"', '"fk-theme"')
(L/'src/main.js').write_text(mj)
apply(str(L/'src/shell.html'), LAAG, [ALL], '1000px')

# ---------- 5. Nacrtna – zadaci sa vježbi ----------
N = H+'Nacrtna-Geometrija-Zadaci-Sa-Vijezbi/'
NAC = """
:root:root:root{--bg:var(--fk-bg);--paper:var(--fk-paper);--ink:var(--fk-ink);--ink-2:var(--fk-ink2);--rule:var(--fk-rule);
  --grid-1:var(--fk-grid);--grid-2:var(--fk-grid5);--h:var(--fk-h);--f:var(--fk-f);--p:var(--fk-p);--n:var(--fk-n);--o:var(--fk-o);
  --f-head:var(--fk-head);--f-body:var(--fk-body);--f-lab:var(--fk-math)}
html body{font-size:16px}
html .eyebrow{font-weight:600;letter-spacing:.09em}
"""
NIDX = NAC + """
html body{background-image:none}
html .page{padding-top:22px}
html .lede{font-size:16px}
html .body h2{font-size:18px}
html footer{margin-top:40px;padding-top:12px;border-top:1px solid var(--fk-rule);font-size:13.5px}
"""
apply(N+'index.html', NIDX, [ALL], '880px')
VJ = (ALL, (N.replace(H, '') and '../', 'Nacrtna – vježbe'))
VJ = (ALL, ('../', 'Nacrtna – vježbe'))
OLD_BACK = re.compile(r'<a href="\.\./" style="[^"]*">&larr; Sve vježbe</a>\n?')
for v in ['vjezba-2.1', 'vjezba-3', 'vjezba-4']:
    f = pathlib.Path(N+v+'/index.html'); f.write_text(OLD_BACK.sub('', f.read_text()))
    apply(str(f), NAC, list(VJ), '1120px')
V22 = """
:root:root:root{--bg:var(--fk-bg);--sheet:var(--fk-paper);--ink:var(--fk-ink);--muted:var(--fk-ink2);--rule:var(--fk-rule);--grid:var(--fk-grid5);
  --chip:var(--fk-ink);--on-chip:var(--fk-paper);--sans:var(--fk-body);--serif:var(--fk-head)}
html .eyebrow{font:600 13px/1.3 var(--fk-head);letter-spacing:.09em;margin:0 0 4px}
html .page>h1{font-family:var(--fk-head);font-weight:700;font-size:clamp(28px,7vw,42px);line-height:1.05;margin:0 0 8px}
html .sheet{border-radius:4px}
"""
f = pathlib.Path(N+'vjezba-2.2/index.html'); f.write_text(OLD_BACK.sub('', f.read_text()))
apply(str(f), V22, list(VJ), '720px')
