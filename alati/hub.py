import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from skin import FONTS, CORE, THEME_JS

# Svaka aplikacija: (grupa, oznaka na kartici, boja, naslov, opis, oznake, link)
APPS = [
 ("Matematika (MM)", "f⁻¹", "--fk-blue", "Rješavač inverznih funkcija",
  "Skiciranje arcus funkcije i njenog inverza, korak po korak, uz vježbu i osnovna pravila.",
  ["1. zadatak K1", "arcsin · arccos · arctg · arcctg"], "/Rje-ava-a-inverznih-funkcija/"),
 ("Matematika (MM)", "lim", "--fk-red", "Limesi nizova",
  "Limesi nizova sa postupkom, hintovima, objašnjenjem „zašto“ i svim pravilima i neodređenim oblicima.",
  ["∞/∞", "0·∞", "1^∞"], "/Rjesavanje-Limes-Niza/"),
 ("Matematika (MM)", "∧∨", "--fk-ok", "MM Rješavač · prvi kolokvijum",
  "Logika (tablica istinitosti), skupovi, relacije, funkcije i indukcija. Svako poglavlje u svom tabu, sa teorijom.",
  ["logika", "skupovi", "relacije", "funkcije", "indukcija"], "/LAAG-Rjesavanje-Zadataka/"),
 ("Nacrtna geometrija", "⊥", "--fk-n", "Rješavač ortogonalnih projekcija",
  "Upišeš postavu sa lista, sajt riješi zadatak u Mongeovoj projekciji, korak po korak, sa crtežom.",
  ["prava", "ravan", "presjek", "prava veličina"], "/Aplikacija-Za-Nacrtnu-Geometriju/"),
 ("Nacrtna geometrija", "O₁", "--fk-o", "Zadaci sa vježbi",
  "Riješeni zadaci sa vježbi 2–4, svaki crtež korak po korak ili odmah gotov.",
  ["vježba 2.1", "2.2", "3", "4"], "/Nacrtna-Geometrija-Zadaci-Sa-Vijezbi/"),
]

CSS = """
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
body{margin:0;background:var(--fk-bg);color:var(--fk-ink);font:16px/1.5 var(--fk-body)}
.page{box-sizing:border-box;max-width:var(--fk-w);margin:0 auto;padding:22px max(16px,env(safe-area-inset-right,0px)) 56px max(16px,env(safe-area-inset-left,0px))}
.search{display:flex;gap:8px;margin:0 0 26px;max-width:520px}
.search input{flex:1;min-width:0;font:17px var(--fk-body);color:var(--fk-ink);background:var(--fk-paper);border:1.5px solid var(--fk-ink2);border-radius:4px;padding:9px 12px}
.search input:focus-visible{outline:2px solid var(--fk-blue);outline-offset:2px}
.grp{margin:0 0 30px}
.grp h2{font:700 22px/1.2 var(--fk-head);margin:0 0 12px;padding-bottom:6px;border-bottom:1.5px solid var(--fk-ink);display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.grp h2 small{font:600 13px var(--fk-head);letter-spacing:.09em;text-transform:uppercase;color:var(--fk-ink2)}
.list{display:grid;gap:14px;grid-template-columns:minmax(0,1fr);margin:0;padding:0;list-style:none}
@media (min-width:760px){.list{grid-template-columns:repeat(2,minmax(0,1fr))}}
.card{height:100%;box-sizing:border-box;display:grid;grid-template-columns:auto minmax(0,1fr);text-decoration:none;color:inherit;background:var(--fk-paper);border:1.5px solid var(--fk-ink);transition:transform .15s,box-shadow .15s}
.card:hover,.card:focus-visible{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--a);outline:none}
.mark{display:grid;place-items:center;width:86px;border-right:1px solid var(--fk-ink);border-left:6px solid var(--a);font:400 30px/1 var(--fk-math);color:var(--fk-ink)}
.body{padding:12px 14px;min-width:0;display:flex;flex-direction:column}
.body h3{font:700 19px/1.2 var(--fk-head);margin:0 0 4px}
.body p{margin:0;font-size:15px;color:var(--fk-ink2)}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin-top:auto;padding-top:10px}
.tags span{font:600 12.5px var(--fk-head);letter-spacing:.02em;padding:1px 7px;border:1px solid var(--fk-rule);border-radius:3px;color:var(--fk-ink2)}
.go{font:600 13px var(--fk-head);letter-spacing:.09em;text-transform:uppercase;color:var(--fk-ink);margin-top:10px}
.none{color:var(--fk-ink2)}
.foot{margin-top:40px;padding-top:12px;border-top:1px solid var(--fk-rule);font-size:13.5px;color:var(--fk-ink2);max-width:80ch}
@media (prefers-reduced-motion:reduce){.card{transition:none}.card:hover{transform:none}}
"""

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;')

groups = []
for a in APPS:
    if a[0] not in groups: groups.append(a[0])
sections = []
for g in groups:
    items = [a for a in APPS if a[0] == g]
    lis = []
    for _, mark, col, title, desc, tags, href in items:
        key = ' '.join([title, desc] + tags).lower()
        lis.append(f'''      <li data-k="{esc(key)}"><a class="card" href="{href}" style="--a:var({col})">
        <span class="mark" aria-hidden="true">{mark}</span>
        <span class="body"><h3>{esc(title)}</h3><p>{esc(desc)}</p>
          <span class="tags">{''.join('<span>%s</span>' % esc(t) for t in tags)}</span>
          <span class="go">Otvori →</span></span></a></li>''')
    n = len(items)
    sections.append(f'''  <section class="grp">
    <h2>{esc(g)} <small>{n} {"aplikacija" if n != 1 else "aplikacija"}</small></h2>
    <ul class="list">
{chr(10).join(lis)}
    </ul>
  </section>''')

html = f'''<!doctype html>
<html lang="sr-Latn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Aplikacije za fakultet</title>
<meta name="description" content="Besplatni rješavači i riješeni zadaci za prvu godinu Građevinskog fakulteta u Banjoj Luci: inverzne funkcije, limesi nizova, MM prvi kolokvijum, nacrtna geometrija.">
{FONTS}
<style>{CORE}:root{{--fk-w:1080px}}
{CSS}</style>
{THEME_JS}
</head>
<body>
<nav class="fk-bar" aria-label="Navigacija"><div class="fk-crumbs"><a href="/" aria-current="page">Sve aplikacije</a></div><button type="button" id="fk-theme" aria-label="Svijetla ili tamna tema"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.7a6.3 6.3 0 0 1 0 12.6z" fill="currentColor"/></svg>Tema</button></nav>
<main class="page">
  <p class="fk-eyebrow">Građevinski fakultet · prva godina</p>
  <h1 class="fk-h1">Aplikacije za fakultet</h1>
  <p class="fk-lede">Rješavači i riješeni zadaci iz matematike i nacrtne geometrije. Izaberi šta ti treba; sve radi u browseru na telefonu i računaru, bez instalacije i naloga.</p>
  <div class="search"><input id="q" type="search" placeholder="Traži, npr. limes, ravan, indukcija" aria-label="Traži aplikaciju" autocomplete="off"></div>
{chr(10).join(sections)}
  <p class="none" id="none" hidden>Ništa ne odgovara pretrazi.</p>
  <p class="foot">Stefan Đukić · Građevinski fakultet, Univerzitet u Banjoj Luci. Aplikacije služe za vježbu i provjeru; na kolokvijumu postupak piši sam.</p>
</main>
<script>
(function(){{var q=document.getElementById('q'),none=document.getElementById('none');
q.addEventListener('input',function(){{var v=q.value.trim().toLowerCase(),any=false;
document.querySelectorAll('.grp').forEach(function(g){{var vis=0;g.querySelectorAll('li').forEach(function(li){{var ok=!v||li.dataset.k.indexOf(v)>=0;li.hidden=!ok;if(ok)vis++}});g.hidden=!vis;if(vis)any=true}});
none.hidden=any;}});}})();
</script>
</body>
</html>
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'index.html'; out.write_text(html); print('hub', len(html))
