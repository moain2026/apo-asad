"""قالب عروض العباسي تك: python3 render.py tayf"""
import sys, importlib
from weasyprint import HTML
D = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'tayf')
AR = '٠١٢٣٤٥٦٧٨٩'
ar = lambda n: ''.join(AR[int(c)] for c in str(n))
GRAD = 'linear-gradient(100deg,#7CF5E0 0%,#3DE6C8 35%,#4A86FF 100%)'
F = '../fonts/'

css = f'''
@font-face{{font-family:R;src:url({F}ReadexPro-400.ttf);font-weight:400}}
@font-face{{font-family:R;src:url({F}ReadexPro-500.ttf);font-weight:500}}
@font-face{{font-family:R;src:url({F}ReadexPro-600.ttf);font-weight:600}}
@font-face{{font-family:C;src:url({F}camel-700.ttf);font-weight:700}}
@font-face{{font-family:C;src:url({F}camel-900.ttf);font-weight:900}}
@page{{size:A4;margin:44mm 22mm 30mm 22mm;
  @bottom-left{{content:counter(page) " / " counter(pages);font-family:R;font-size:8pt;color:#9AA2BC;margin-bottom:21mm}} }}
@page:first{{@bottom-left{{content:none}}}}
*{{box-sizing:border-box}}
html{{direction:rtl}}
body{{margin:0;font-family:R;font-size:10.2pt;line-height:1.7;color:#0A1030}}
.frame{{position:fixed;top:-44mm;left:-22mm;width:210mm;height:297mm;z-index:-1}}
.frame>*{{position:absolute}}
.logo{{top:12mm;right:22mm;width:14mm;height:14mm}}
.nm{{top:11.4mm;right:39mm;width:80mm;text-align:right}}
.n1{{font-family:C;font-weight:900;font-size:19pt;line-height:1.15;color:#0A1030}}
.n2{{font-weight:500;font-size:7pt;letter-spacing:2.2px;color:#08705F;direction:ltr;text-align:right}}
.who{{top:13.2mm;left:22mm;width:70mm;text-align:left;font-size:8.6pt;line-height:1.6;color:#4B5578}}
.who b{{color:#0A1030;font-weight:600;font-size:9.4pt}}
.g1{{top:32mm;right:22mm;left:22mm;height:0.8mm;border-radius:1mm;background:{GRAD}}}
.band{{bottom:0;left:0;right:0;height:14mm;background:#040820}}
.g2{{bottom:14mm;left:0;right:0;height:0.7mm;background:{GRAD}}}
.f1,.f2{{bottom:4.6mm;width:110mm;font-size:8.2pt;color:#D5DAE8}}
.f1{{right:22mm;text-align:right}} .f1 b{{color:#7CF5E0;font-weight:600}}
.f2{{left:22mm;text-align:left}}

.kick{{font-size:9pt;font-weight:500;color:#08705F;letter-spacing:.3px;margin:0}}
.kick span{{float:left;color:#7A84A3;font-weight:400}}
h1{{font-family:C;font-weight:900;font-size:24pt;line-height:1.35;margin:1mm 0 0}}
.tline{{width:24mm;height:1mm;border-radius:1mm;background:{GRAD};margin:3.5mm 0 7mm}}

.sec{{margin:0 0 6.5mm}} .sec.keep{{break-inside:avoid}}
.sh{{break-after:avoid;margin:0 0 3.2mm;padding-bottom:2.4mm;border-bottom:0.3mm solid #DDE2EF}}
.sh .no{{font-family:C;font-weight:900;font-size:15pt;color:#3DE6C8;margin-left:2.5mm}}
.sh .t{{font-family:C;font-weight:700;font-size:15pt}}
.sh .s{{display:block;font-size:9pt;color:#7A84A3;margin-top:.3mm}}
.its{{width:100%;border-collapse:collapse}}
.its tr{{break-inside:avoid}}
.its td{{vertical-align:top;padding:0 0 1.7mm;text-align:right}}
.its td.n{{width:9mm;padding-top:.75mm}}
.its td.n span{{display:block;width:6.5mm;font-size:8.4pt;font-weight:500;color:#08705F;text-align:center;
  border:0.3mm solid #BFE9DF;border-radius:3mm;line-height:1.55}}
.its b{{font-weight:600}}
.its .d{{color:#3C4566}}

.end{{break-inside:avoid;margin-top:4mm}} .end .tline{{margin:0 0 4mm}}
.et{{font-family:C;font-weight:700;font-size:15pt;margin-bottom:1.5mm}}
.end p{{margin:0;font-size:10.8pt;line-height:1.9;color:#3C4566;text-align:justify}}
table{{width:100%;border-collapse:collapse}}
.pt td{{padding:2.6mm 0;border-bottom:0.3mm solid #DDE2EF;font-size:10.6pt}}
.pt .w{{color:#7A84A3;font-size:9pt}}
.pt .a{{text-align:left;font-weight:600;white-space:nowrap}}
.pt .a small{{font-family:R;font-weight:400;color:#7A84A3;font-size:8.6pt;margin-right:1mm}}
.pt tr.tot td{{border-bottom:none;border-top:0.6mm solid #0A1030;padding-top:3.4mm}}
.pt tr.tot .l{{font-family:C;font-weight:700;font-size:14pt}}
.pt tr.tot .a{{font-family:C;font-weight:900;font-size:17pt;color:#08705F}}
.sg{{margin-top:12mm}} .sg td{{width:50%;padding:0 0 0 10mm;font-size:9pt;color:#7A84A3;vertical-align:top}}
.sg td+td{{padding:0 10mm 0 0}}
.sg .ln{{border-bottom:0.3mm solid #0A1030;height:12mm;margin-bottom:1.6mm}}
'''

frame = f'''<div class="frame">
<img class="logo" src="../brand/alabbasi-mark.png">
<div class="nm"><div class="n1">العباسي تك</div><div class="n2">ALABBASI TECH</div></div>
<div class="who"><b>م. معين العباسي</b><br>مواقع وتطبيقات وأنظمة</div>
<div class="g1"></div><div class="g2"></div><div class="band"></div>
<div class="f1"><b>العباسي تك</b> · مواقع، تطبيقات، أنظمة</div>
<div class="f2"><span dir="ltr">+967 770 941 666</span> &nbsp;·&nbsp; <span dir="ltr">moain.learn@gmail.com</span> &nbsp;·&nbsp; <span dir="ltr">alabbasi.uk</span></div>
</div>'''

body, k = [], 0
for i, (t, s, items) in enumerate(D.SECTIONS, 1):
    rows = []
    for lead, det in items:
        k += 1
        rows.append(f'<tr><td class="n"><span>{ar(k)}</span></td><td><b>{lead}</b><span class="d">: {det}</span></td></tr>')
    body.append(f'<div class="sec{" keep" if len(items) <= 5 else ""}"><div class="sh"><span class="no">{ar(i)}</span><span class="t">{t}</span>'
                f'<span class="s">{s}</span></div><table class="its">{"".join(rows)}</table></div>')

closing = ''
if getattr(D, 'CLOSING', None):
    closing = f'<div class="end"><div class="tline"></div><div class="et">{D.CLOSING[0]}</div><p>{D.CLOSING[1]}</p></div>'

html = f'''<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{frame}
<p class="kick"><span>{D.DATE}</span>&nbsp;</p><h1>{D.TITLE}</h1><div class="tline"></div>
{"".join(body)}{closing}</body></html>'''
open('offer.html', 'w', encoding='utf-8').write(html)
HTML(string=html, base_url='.').write_pdf(D.OUT)
print('built', D.OUT, k, 'items')
