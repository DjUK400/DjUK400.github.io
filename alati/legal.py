import re, sys, pathlib
URL = "https://github.com/DjUK400/djuk400.github.io/issues"
TEXT = ('<b>Odricanje od odgovornosti.</b> Sadržaj ovog sajta služi isključivo za vježbu i ličnu pripremu i nije zvanični materijal fakulteta ni predmetnih nastavnika. '
 'Sajt nije povezan sa Univerzitetom u Banjoj Luci ni sa Građevinskim fakultetom. Autor ne garantuje tačnost, potpunost ni aktuelnost pitanja, odgovora, rješenja i postupaka, '
 'niti da će se bilo koje pitanje ili tip zadatka pojaviti na kolokvijumu ili ispitu. Sajt se koristi na sopstvenu odgovornost: autor ne odgovara za rezultate na kolokvijumima i ispitima, '
 'za odluke donesene na osnovu sadržaja, niti za bilo kakvu direktnu ili indirektnu štetu nastalu korištenjem sajta. Za tačne informacije mjerodavni su zvanični materijali i predmetni nastavnici. '
 'Greške, pitanja i zahtjeve za uklanjanje sadržaja (npr. ako smatrate da je nešto objavljeno bez dozvole nosioca autorskih prava) pošaljite preko '
 '<a href="%s" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline">kontakt stranice na GitHubu</a>.' % URL)
BLOCK = ('<!--fk-legal:start--><div class="fk-legal" style="box-sizing:border-box;max-width:var(--fk-w,1080px);margin:28px auto 0;'
 'padding:12px max(16px,env(safe-area-inset-right,0px)) 28px max(16px,env(safe-area-inset-left,0px))">'
 '<p style="margin:0;padding-top:10px;border-top:1px solid var(--fk-rule,#c8d1ce);font:11.5px/1.45 var(--fk-body,system-ui,sans-serif);'
 'color:var(--fk-ink2,#4b5761);max-width:90ch;opacity:.85">' + TEXT + '</p></div><!--fk-legal:end-->')
def add(path):
    p = pathlib.Path(path); s = p.read_text(encoding='utf-8')
    if '<!--fk-legal:start-->' in s:
        s = re.sub(r'<!--fk-legal:start-->.*?<!--fk-legal:end-->', lambda m: BLOCK, s, count=1, flags=re.S)
    else:
        i = s.rindex('</body>'); s = s[:i] + BLOCK + '\n' + s[i:]
    p.write_text(s, encoding='utf-8'); print('legal', path)
if __name__ == '__main__':
    for a in sys.argv[1:]: add(a)
