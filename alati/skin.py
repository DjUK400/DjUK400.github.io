# Zajednicki dizajn (po uzoru na Rjesavac inverznih funkcija) za sve Stefanove aplikacije.
# Idempotentno: blok izmedju markera se zamjenjuje pri svakom pokretanju.
import re, sys, pathlib

HUB = "https://djuk400.github.io/"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500;600;700'
         '&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=STIX+Two+Text:ital,wght@0,400;0,600;1,400&display=swap">')

LIGHT = ("--fk-bg:#e9edeb;--fk-paper:#fbfcfa;--fk-ink:#16202a;--fk-ink2:#4b5761;--fk-rule:#c8d1ce;--fk-chip:#eef2f0;"
         "--fk-grid:#e4eae7;--fk-grid5:#ccd7d3;--fk-blue:#1c5aa8;--fk-blue-bg:#e6eef8;--fk-red:#b33a28;"
         "--fk-ok:#1f6e44;--fk-ok-bg:#e6f2ea;--fk-warn:#8a5a00;--fk-warn-bg:#fbf1dc;--fk-err:#a8261c;--fk-err-bg:#fbecea;"
         "--fk-h:#1d5fae;--fk-f:#bb3a2b;--fk-p:#1f774a;--fk-n:#b86e00;--fk-o:#7a40b8")
DARK = ("--fk-bg:#0e1215;--fk-paper:#151a1e;--fk-ink:#e2e7e5;--fk-ink2:#a1acb1;--fk-rule:#2b353a;--fk-chip:#1c2327;"
        "--fk-grid:#1b2226;--fk-grid5:#263035;--fk-blue:#7cb0f2;--fk-blue-bg:#172333;--fk-red:#f2907b;"
        "--fk-ok:#6fcf98;--fk-ok-bg:#15291e;--fk-warn:#f0b75a;--fk-warn-bg:#2e2412;--fk-err:#ff8f80;--fk-err-bg:#2c1714;"
        "--fk-h:#72aaf1;--fk-f:#f08574;--fk-p:#63c590;--fk-n:#f0b04f;--fk-o:#c39bf2;color-scheme:dark")

CORE = """
:root{%s;
  --fk-head:"Barlow Semi Condensed","Arial Narrow",system-ui,sans-serif;
  --fk-body:"Source Sans 3",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  --fk-math:"STIX Two Text","Times New Roman",Times,serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){%s}}
:root[data-theme="dark"]{%s}
/* gornja traka: povratak na sve aplikacije + tema */
.fk-bar{box-sizing:border-box;max-width:var(--fk-w,1080px);margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;
  padding:10px max(16px,env(safe-area-inset-right,0px)) 0 max(16px,env(safe-area-inset-left,0px));
  font:600 13px/1.2 var(--fk-head);letter-spacing:.07em;text-transform:uppercase}
.fk-crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:2px 8px;min-width:0}
.fk-crumbs a{color:var(--fk-ink2);text-decoration:none;padding:6px 0}
.fk-crumbs a:hover{color:var(--fk-ink);text-decoration:underline;text-underline-offset:3px}
.fk-crumbs span{color:var(--fk-rule)}
.fk-bar button{flex:none;display:inline-flex;align-items:center;gap:6px;font:inherit;letter-spacing:inherit;text-transform:inherit;color:var(--fk-ink2);background:transparent;
  border:1px solid var(--fk-rule);border-radius:4px;padding:5px 10px;min-height:32px;cursor:pointer}
.fk-bar button:hover{color:var(--fk-ink);border-color:var(--fk-ink2)}
.fk-bar a:focus-visible,.fk-bar button:focus-visible{outline:2px solid var(--fk-blue);outline-offset:2px}
/* zaglavlje */
:root body .fk-eyebrow{font:600 13px/1.3 var(--fk-head);letter-spacing:.09em;text-transform:uppercase;color:var(--fk-ink2);margin:0 0 4px}
:root body .fk-h1{font-family:var(--fk-head);font-weight:700;font-size:clamp(28px,7vw,42px);line-height:1.05;letter-spacing:0;margin:0 0 8px;color:var(--fk-ink);text-wrap:balance}
:root body .fk-lede{display:block;margin:0 0 18px;max-width:64ch;color:var(--fk-ink2);font:400 16px/1.5 var(--fk-body)}
/* tabovi kao kartoteka */
:root body .fk-tabs{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px;padding:0;background:transparent;border:0;border-radius:0;box-shadow:inset 0 -1.5px 0 var(--fk-ink)}
:root body .fk-tabs>button,:root body .fk-tabs>a{flex:0 0 auto;font:600 16px/1.3 var(--fk-head);letter-spacing:.02em;color:var(--fk-ink2);background:transparent;
  padding:8px 12px 8px;border:1.5px solid transparent;border-bottom:0;border-radius:6px 6px 0 0;cursor:pointer;white-space:nowrap;text-decoration:none}
:root body .fk-tabs>button:hover{color:var(--fk-ink);border-color:transparent}
:root body .fk-tabs>.on,:root body .fk-tabs>[aria-selected="true"]{color:var(--fk-ink);background:var(--fk-paper);border-color:var(--fk-ink);font-weight:600}
""" % (LIGHT, DARK, DARK)

THEME_JS = ("<script>(function(){var r=document.documentElement,k='fk-theme';"
            "try{var t=localStorage.getItem(k);if(t)r.dataset.theme=t}catch(e){}"
            "document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('#fk-theme');if(!b)return;"
            "var d=r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;"
            "r.dataset.theme=d?'light':'dark';try{localStorage.setItem(k,r.dataset.theme)}catch(e){}});})();</script>")

def bar(crumbs):
    links = '<span aria-hidden="true">/</span>'.join('<a href="%s">%s</a>' % c for c in crumbs)
    return ('<!--fk-bar:start--><nav class="fk-bar" aria-label="Navigacija"><div class="fk-crumbs">%s</div>'
            '<button type="button" id="fk-theme" aria-label="Svijetla ili tamna tema"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.7a6.3 6.3 0 0 1 0 12.6z" fill="currentColor"/></svg>Tema</button></nav><!--fk-bar:end-->' % links)

def apply(path, site_css, crumbs, width, fonts=True):
    p = pathlib.Path(path); s = p.read_text()
    head = ('<!--fk-dizajn:start-->\n' + (FONTS + '\n' if fonts else '') +
            '<style id="fk-dizajn">/* Zajednički dizajn svih aplikacija (izvor: djuk400.github.io/dizajn) */' + CORE +
            ':root{--fk-w:%s}\n' % width + site_css + '</style>\n' + THEME_JS + '\n<!--fk-dizajn:end-->')
    if '<!--fk-dizajn:start-->' in s:
        s = re.sub(r'<!--fk-dizajn:start-->.*?<!--fk-dizajn:end-->', lambda m: head, s, count=1, flags=re.S)
    else:
        i = s.index('</head>'); s = s[:i] + head + '\n' + s[i:]
    b = bar(crumbs)
    if '<!--fk-bar:start-->' in s:
        s = re.sub(r'<!--fk-bar:start-->.*?<!--fk-bar:end-->', lambda m: b, s, count=1, flags=re.S)
    else:
        m = re.search(r'<body[^>]*>', s); s = s[:m.end()] + '\n' + b + s[m.end():]
    p.write_text(s)
    print('ok', path)
