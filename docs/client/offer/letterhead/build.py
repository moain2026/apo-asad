"""ترويسة العباسي تك — خياران على هوية alabbasi.uk (الشعار، Readex Pro + The Year of The Camel، الكحلي والتدرج الفيروزي/الأزرق).
الإطار يُرسم في طبقة position:fixed لأن WeasyPrint يضع خلفية @page داخل منطقة المحتوى."""
from weasyprint import HTML

M = dict(top=46, right=20, bottom=32, left=20)
CONTENT = open('content.html', encoding='utf-8').read()
LOGO = '../brand/alabbasi-mark.png'
GRAD = 'linear-gradient(100deg, #7CF5E0 0%, #3DE6C8 35%, #4A86FF 100%)'
CONTACT = ('<span dir="ltr">+967 770 941 666</span> &nbsp;·&nbsp; '
           '<span dir="ltr">moain.learn@gmail.com</span> &nbsp;·&nbsp; '
           '<span dir="ltr">alabbasi.uk</span>')

COMMON = '''
.frame .logo { position:absolute; width:15mm; height:15mm; }
.frame .name { position:absolute; width:90mm; text-align:right; }
.n1 { font-family:"Camel"; font-weight:900; font-size:21pt; line-height:1.15; }
.n2 { font-family:"Readex"; font-weight:500; font-size:7.6pt; letter-spacing:2.2px; direction:ltr; text-align:right; }
.frame .who { position:absolute; width:75mm; text-align:left; font-size:9pt; line-height:1.65; }
.frame .f1, .frame .f2 { position:absolute; width:110mm; font-size:8.6pt; }
.frame .f1 { text-align:right; } .frame .f2 { text-align:left; }
'''

VARIANTS = {
# أ — داكن: شريط كحلي بلون الموقع + خط متدرج
'a': (COMMON + f'''
.frame .band {{ position:absolute; top:0; left:0; right:0; height:31mm; background:var(--night); }}
.frame .grad {{ position:absolute; top:31mm; left:0; right:0; height:1.3mm; background:{GRAD}; }}
.frame .logo {{ top:8mm; right:20mm; }}
.frame .name {{ top:7.2mm; right:39mm; }}
.n1 {{ color:#fff; }} .n2 {{ color:var(--mint); }}
.frame .who {{ top:9.5mm; left:20mm; color:#AEB6CF; }}
.frame .who b {{ color:#fff; font-weight:600; font-size:10pt; }}
.frame .rule {{ position:absolute; bottom:17mm; right:20mm; left:20mm; height:0.3mm; background:var(--line); }}
.frame .f1 {{ bottom:9.5mm; right:20mm; color:var(--muted); }}
.frame .f1 b {{ color:var(--deep-teal); font-weight:600; }}
.frame .f2 {{ bottom:9.5mm; left:20mm; color:var(--muted); }}
''', f'''
<div class="band"></div><div class="grad"></div>
<img class="logo" src="{LOGO}">
<div class="name"><div class="n1">العباسي تك</div><div class="n2">ALABBASI TECH</div></div>
<div class="who"><b>م. معين العباسي</b><br>مؤسسة حلول رقمية</div>
<div class="rule"></div>
<div class="f1"><b>العباسي تك</b> — أنظمة، مواقع، تطبيقات، بيانات</div>
<div class="f2">{CONTACT}</div>
'''),
# ب — فاتح: خلفية بيضاء + خط متدرج تحت الترويسة + تذييل كحلي
'b': (COMMON + f'''
.frame .logo {{ top:12mm; right:20mm; }}
.frame .name {{ top:11.2mm; right:39mm; }}
.n1 {{ color:var(--ink); }} .n2 {{ color:var(--deep-teal); }}
.frame .who {{ top:13.5mm; left:20mm; color:var(--muted); }}
.frame .who b {{ color:var(--ink); font-weight:600; font-size:10pt; }}
.frame .grad {{ position:absolute; top:33.5mm; right:20mm; left:20mm; height:0.9mm; border-radius:1mm; background:{GRAD}; }}
.frame .band {{ position:absolute; bottom:0; left:0; right:0; height:15mm; background:var(--night); }}
.frame .grad2 {{ position:absolute; bottom:15mm; left:0; right:0; height:0.8mm; background:{GRAD}; }}
.frame .f1 {{ bottom:5.2mm; right:20mm; color:#D5DAE8; }}
.frame .f1 b {{ color:var(--mint); font-weight:600; }}
.frame .f2 {{ bottom:5.2mm; left:20mm; color:#D5DAE8; }}
''', f'''
<img class="logo" src="{LOGO}">
<div class="name"><div class="n1">العباسي تك</div><div class="n2">ALABBASI TECH</div></div>
<div class="who"><b>م. معين العباسي</b><br>مؤسسة حلول رقمية</div>
<div class="grad"></div>
<div class="grad2"></div><div class="band"></div>
<div class="f1"><b>العباسي تك</b> — أنظمة، مواقع، تطبيقات، بيانات</div>
<div class="f2">{CONTACT}</div>
'''),
}

PAGE = f'''
@page {{ size: A4; margin: {M["top"]}mm {M["right"]}mm {M["bottom"]}mm {M["left"]}mm; }}
.frame {{ position: fixed; top: -{M["top"]}mm; left: -{M["left"]}mm; width: 210mm; height: 297mm; z-index: -1; }}
'''

files = []
for key, (css, frame) in VARIANTS.items():
    html = (f'<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="base.css"><style>{PAGE}{css}</style></head>'
            f'<body><div class="frame">{frame}</div>{CONTENT}</body></html>')
    HTML(string=html, base_url='.').write_pdf(f'letterhead-{key}.pdf')
    files.append(f'letterhead-{key}.pdf'); print('built', key)
