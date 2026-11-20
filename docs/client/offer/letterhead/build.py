"""Build letterhead variants. The page frame is drawn in a position:fixed layer
(WeasyPrint places @page backgrounds inside the content box, so we avoid them)."""
from weasyprint import HTML

M = dict(top=46, right=20, bottom=32, left=20)   # page margins (mm)
CONTENT = open('content.html', encoding='utf-8').read()

def layer(inner):
    return (f'<div class="frame" style="top:-{M["top"]}mm; left:-{M["left"]}mm">'
            f'{inner}</div>')

VARIANTS = {
# A — classic: logo right, gold double rule, dark footer band
'a': ('''
.frame .logo { position:absolute; top:13mm; right:20mm; width:14mm; height:14mm; }
.frame .name { position:absolute; top:12.5mm; right:37mm; width:80mm; text-align:right; }
.frame .who  { position:absolute; top:14mm; left:20mm; width:70mm; text-align:left; font-size:9pt; color:var(--soft); line-height:1.6; }
.frame .who b { color:var(--gold); font-weight:600; font-size:10pt; }
.frame .rule1 { position:absolute; top:34mm; right:20mm; left:20mm; height:0.7mm; background:var(--gold); }
.frame .rule2 { position:absolute; top:35.4mm; right:20mm; left:20mm; height:0.25mm; background:var(--gold); }
.frame .band { position:absolute; bottom:0; left:0; right:0; height:16mm; background:var(--navy); border-top:0.8mm solid var(--gold); }
.frame .f1 { position:absolute; bottom:5.5mm; right:20mm; width:90mm; text-align:right; color:#e9e1cd; font-size:8.8pt; }
.frame .f2 { position:absolute; bottom:5.5mm; left:20mm; width:90mm; text-align:left; color:#e9e1cd; font-size:8.8pt; }
.n1 { font-family:"Taj"; font-weight:800; font-size:19pt; color:var(--navy); line-height:1.15; }
.n2 { font-size:9pt; color:var(--soft); line-height:1.5; }
''', '''
<img class="logo" src="mark.svg">
<div class="name"><div class="n1">MoTech</div><div class="n2">تطوير المواقع والهوية الرقمية</div></div>
<div class="who"><b>م. معين العباسي</b><br>مهندس تطوير وتصميم</div>
<div class="rule1"></div><div class="rule2"></div>
<div class="band"></div>
<div class="f1">MoTech — حلول رقمية للأعمال</div>
<div class="f2">الجوال: ــــــــــ &nbsp;&nbsp;|&nbsp;&nbsp; البريد: ــــــــــ</div>
'''),
# B — modern: full navy header band, light footer line
'b': ('''
.frame .band { position:absolute; top:0; left:0; right:0; height:32mm; background:var(--navy); border-bottom:1.2mm solid var(--gold); }
.frame .logo { position:absolute; top:9mm; right:20mm; width:14mm; height:14mm; }
.frame .name { position:absolute; top:8.5mm; right:37mm; width:80mm; text-align:right; }
.frame .who  { position:absolute; top:10mm; left:20mm; width:70mm; text-align:left; font-size:9pt; color:#c9d1db; line-height:1.6; }
.frame .who b { color:#fff; font-weight:600; font-size:10pt; }
.frame .rule { position:absolute; bottom:16mm; right:20mm; left:20mm; height:0.3mm; background:var(--gold); }
.frame .f1 { position:absolute; bottom:9mm; right:20mm; width:90mm; text-align:right; color:var(--soft); font-size:8.8pt; }
.frame .f1 b { color:var(--gold); font-weight:600; }
.frame .f2 { position:absolute; bottom:9mm; left:20mm; width:90mm; text-align:left; color:var(--soft); font-size:8.8pt; }
.n1 { font-family:"Taj"; font-weight:800; font-size:19pt; color:#fff; line-height:1.15; }
.n2 { font-size:9pt; color:#d8c79c; line-height:1.5; }
''', '''
<div class="band"></div>
<img class="logo" src="mark-light.svg">
<div class="name"><div class="n1">MoTech</div><div class="n2">تطوير المواقع والهوية الرقمية</div></div>
<div class="who"><b>م. معين العباسي</b><br>مهندس تطوير وتصميم</div>
<div class="rule"></div>
<div class="f1"><b>MoTech</b> — حلول رقمية للأعمال</div>
<div class="f2">الجوال: ــــــــــ &nbsp;&nbsp;|&nbsp;&nbsp; البريد: ــــــــــ</div>
'''),
# C — minimal: navy side strip, wordmark, thin rules
'c': ('''
.frame .strip { position:absolute; top:0; bottom:0; right:0; width:8mm; background:var(--navy); border-left:1.2mm solid var(--gold); }
.frame .name { position:absolute; top:12mm; right:20mm; width:90mm; text-align:right; }
.frame .who  { position:absolute; top:16mm; left:20mm; width:70mm; text-align:left; font-size:9pt; color:var(--soft); line-height:1.6; }
.frame .who b { color:var(--navy); font-weight:600; font-size:10pt; }
.frame .r1 { position:absolute; top:33mm; right:20mm; left:20mm; height:0.3mm; background:#d9ccb0; }
.frame .r2 { position:absolute; bottom:16mm; right:20mm; left:20mm; height:0.3mm; background:#d9ccb0; }
.frame .f1 { position:absolute; bottom:9mm; right:20mm; width:90mm; text-align:right; color:var(--soft); font-size:8.8pt; }
.frame .f2 { position:absolute; bottom:9mm; left:20mm; width:90mm; text-align:left; color:var(--soft); font-size:8.8pt; }
.n1 { font-family:"Taj"; font-weight:800; font-size:23pt; color:var(--navy); line-height:1.1; }
.n1 .t { color:var(--gold); }
.n2 { font-size:9pt; color:var(--soft); line-height:1.5; }
''', '''
<div class="strip"></div>
<div class="name"><div class="n1"><span dir="ltr">Mo<span class="t">Tech</span></span></div><div class="n2">تطوير المواقع والهوية الرقمية</div></div>
<div class="who"><b>م. معين العباسي</b><br>مهندس تطوير وتصميم</div>
<div class="r1"></div><div class="r2"></div>
<div class="f1">MoTech — حلول رقمية للأعمال</div>
<div class="f2">الجوال: ــــــــــ &nbsp;&nbsp;|&nbsp;&nbsp; البريد: ــــــــــ</div>
'''),
}

PAGE = f'''
@page {{ size: A4; margin: {M["top"]}mm {M["right"]}mm {M["bottom"]}mm {M["left"]}mm; }}
.frame {{ position: fixed; width: 210mm; height: 297mm; z-index: -1; }}
'''

for key, (css, frame) in VARIANTS.items():
    html = (f'<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="base.css"><style>{PAGE}{css}</style></head>'
            f'<body>{layer(frame)}{CONTENT}</body></html>')
    open(f'letterhead-{key}.html', 'w', encoding='utf-8').write(html)
    HTML(f'letterhead-{key}.html').write_pdf(f'letterhead-{key}.pdf')
    print('built', key)
