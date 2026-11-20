# -*- coding: utf-8 -*-
"""يبني التصورات الثلاثة: python3 concepts/_build/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ph(caption, cls="", tag="figure"):
    return f'<{tag} class="ph {cls}" role="img" aria-label="مكان صورة: {caption}">{icon("image","ic ph-ic")}<figcaption><b>صورة من شغل أبو سعد</b>{caption}</figcaption></{tag}>'

def header(logo, nav=True):
    links = '<a href="#services">الخدمات</a><a href="#occasions">المناسبات</a><a href="#work">من شغلنا</a><a href="#order">اطلب عرض</a>' if nav else ""
    return f'''<header class="hdr"><div class="wrap hdr-in"><a class="brand" href="#" aria-label="طيف الضيافة، الرئيسية">{logo}<span class="bt"><b>طيف الضيافة</b><small>الدمام · الخبر</small></span></a><nav class="nav" aria-label="الأقسام">{links}</nav><a class="btn call sm" href="#" data-call>{icon("phone")}<span>اتصل</span></a></div></header>'''

MBAR = f'<div class="mbar" aria-label="تواصل سريع"><a class="btn wa" href="#" data-wa>{icon("wa")}<span>اطلب على واتساب</span></a><a class="btn call" href="#" data-call>{icon("phone")}<span>اتصل</span></a></div>'

def services(cls="svc"):
    items = "".join(f'<article class="{cls}-it"><span class="{cls}-ic">{icon(i)}</span><h3>{t}</h3><p>{d}</p></article>' for i,t,d in SERVICES)
    return items

def occasions():
    return "".join(f'<a class="occ-it" href="#order" data-wa="السلام عليكم طيف الضيافة، أرغب في عرض سعر لـ{t}.">{icon(i)}<span>{t}</span>{icon("arrow","ic arr")}</a>' for i,t,_ in OCCASIONS)

def steps():
    nums = "١٢٣"
    return "".join(f'<li><span class="n">{nums[k]}</span><h3>{t}</h3><p>{d}</p></li>' for k,(t,d) in enumerate(STEPS))

def gallery():
    return "".join(ph(c, f"g {w}") for c,w in GALLERY)

def footer():
    return f'''<footer class="ftr"><div class="wrap ftr-in"><div><b class="ftr-b">طيف الضيافة</b><p>قهوجيين وصبابين وضيافة مناسبات في الدمام والخبر.</p></div><nav aria-label="صفحات"><a href="#">قهوجيين الدمام</a><a href="#">قهوجيين الخبر</a><a href="#">ضيافة الأعراس</a><a href="#">ضيافة الشركات</a></nav><p class="fine">© <span id="yr"></span> طيف الضيافة · tayfaldiafa.com</p></div></footer>'''

def page(name, title, logo, hero, body_cls):
    sec = f'''
<section id="services" class="sec svc-sec"><div class="wrap"><div class="sh"><span class="eb">خدماتنا</span><h2>كل اللي تحتاجه ضيافة مناسبتك</h2><p>من تجهيز القهوة إلى آخر فنجان، بطاقم واحد ينسق معك.</p></div><div class="svc">{services()}</div></div></section>
<section id="occasions" class="sec occ-sec"><div class="wrap"><div class="sh"><span class="eb">المناسبات</span><h2>لأي مناسبة تخدمها؟</h2></div><div class="occ">{occasions()}</div></div></section>
<section id="how" class="sec how-sec"><div class="wrap"><div class="sh"><span class="eb">طريقة الطلب</span><h2>ثلاث خطوات وتوصلك التفاصيل</h2></div><ol class="steps">{steps()}</ol></div></section>
<section id="work" class="sec work-sec"><div class="wrap"><div class="sh"><span class="eb">من شغلنا</span><h2>ضيافة تبان بالصور</h2><p>هذه المساحات مخصصة لصور أبو سعد الأصلية، بعد إذن النشر.</p></div><div class="gal">{gallery()}</div></div></section>
<section id="order" class="sec order-sec"><div class="wrap order-in"><div class="sh"><span class="eb">اطلب عرض سعر</span><h2>متى مناسبتك؟</h2><p>خمس معلومات تكفي، ويوصلك العرض على واتساب.</p><ul class="ticks"><li>{icon("check","ic sm")}السعر قبل أي تأكيد</li><li>{icon("check","ic sm")}تواصل مباشر مع صاحب الخدمة</li><li>{icon("check","ic sm")}الدمام والخبر</li></ul></div><div class="panel">{form_html(name)}</div></div></section>
<section id="faq" class="sec faq-sec"><div class="wrap faq-in"><div class="sh"><span class="eb">أسئلة شائعة</span><h2>قبل ما تطلب</h2></div><div class="faq">{faq_html()}</div></div></section>
'''
    html = head(title, "style.css") + f'<body class="{body_cls}">' + PROTO_BAR + header(logo) + f'<main>{hero}{sec}</main>' + footer() + MBAR + DIALOG + '<script src="../_shared/order.js" defer></script></body></html>'
    d = os.path.join(ROOT, name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(html)

HERO_CTA = f'<div class="cta" data-hero-cta><a class="btn wa lg" href="#order" data-wa>{icon("wa")}<span>اطلب عرض سعر على واتساب</span></a><a class="btn call lg" href="#" data-call>{icon("phone")}<span>اتصل الآن</span></a></div><p class="assure">{icon("shield","ic sm")}أرسل التاريخ وعدد الضيوف، ويوصلك السعر قبل أي تأكيد.</p>'

# ── A: دانة — كحلي الخليج + لؤلؤ (فاخر داكن، غير ذهبي)
LOGO_A = '<svg class="mk" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22.5" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".5"/><path d="M12 27c4-7 20-7 24 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M15 31c3 4 15 4 18 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="24" cy="17" r="3.4" fill="currentColor"/></svg>'
HERO_A = f'''<section class="hero"><div class="wrap hero-in"><div class="hero-txt"><span class="chip"><i></i>ضيافة سعودية · المنطقة الشرقية</span><h1>قهوجيين وصبابين<br><em>في الدمام والخبر</em></h1><p class="lead">قهوة سعودية وشاي وتقديمات لمناسبتك، بطاقم يخدم ضيوفك من أول فنجان إلى آخر ضيف.</p>{HERO_CTA}</div><div class="hero-media">{ph("القهوجي يصب لضيف، لقطة قريبة بإضاءة دافئة","hero-ph")}<ul class="facts"><li><b>الدمام والخبر</b><span>نغطي مناسباتك</span></li><li><b>السعر أولًا</b><span>قبل أي تأكيد</span></li><li><b>تواصل مباشر</b><span>مع صاحب الخدمة</span></li></ul></div></div></section>'''

# ── B: رَمل — تحريري فاتح (ورق رملي + حبر + زعفران)
LOGO_B = '<svg class="mk" viewBox="0 0 48 48" aria-hidden="true"><rect x="1" y="1" width="46" height="46" rx="12" fill="currentColor"/><path d="M14 22h20l-2.5 10a5 5 0 0 1-4.9 4h-5.2a5 5 0 0 1-4.9-4L14 22Z" fill="none" stroke="var(--paper)" stroke-width="2.2" stroke-linejoin="round"/><path d="M20 17c0-2.5 3-2.5 3-5M26 17c0-2.5 3-2.5 3-5" fill="none" stroke="var(--paper)" stroke-width="2.2" stroke-linecap="round"/></svg>'
HERO_B = f'''<section class="hero"><div class="wrap"><div class="hero-head"><span class="eb">ضيافة المناسبات · الشرقية</span><h1>قهوجيين وصبابين <em>في الدمام والخبر</em></h1><div class="hero-row"><p class="lead">قهوة سعودية وشاي وتقديمات لمناسبتك، بطاقم يخدم ضيوفك من أول فنجان إلى آخر ضيف.</p><div>{HERO_CTA}</div></div></div>{ph("ركن الضيافة كامل قبل دخول الضيوف، لقطة عريضة","hero-ph")}<ul class="facts"><li><b>٠١</b><span>الدمام والخبر أولًا</span></li><li><b>٠٢</b><span>السعر قبل أي تأكيد</span></li><li><b>٠٣</b><span>تواصل مباشر مع صاحب الخدمة</span></li></ul></div></section>'''

# ── C: سدو — تراثي جريء (عنابي التمر + زعفران + نقش السدو)
LOGO_C = '<svg class="mk" viewBox="0 0 48 48" aria-hidden="true"><path d="M24 2l22 22-22 22L2 24Z" fill="currentColor"/><path d="M24 11l13 13-13 13-13-13Z" fill="none" stroke="var(--ink)" stroke-width="2"/><path d="M24 19l5 5-5 5-5-5Z" fill="var(--ink)"/></svg>'
SADU = '<div class="sadu" aria-hidden="true"></div>'
HERO_C = f'''<section class="hero">{ph("الطاقم بالزي يستقبل الضيوف عند مدخل المجلس","hero-ph")}<div class="hero-veil"></div><div class="wrap hero-in"><div class="hero-card"><span class="chip">ضيافة سعودية · المنطقة الشرقية</span><h1>قهوجيين وصبابين <em>في الدمام والخبر</em></h1><p class="lead">قهوة سعودية وشاي وتقديمات لمناسبتك، بطاقم يخدم ضيوفك من أول فنجان إلى آخر ضيف.</p>{HERO_CTA}</div></div></section>{SADU}'''

page("dana", "دانة | تصوّر طيف الضيافة A", LOGO_A, HERO_A, "c-dana")
page("raml", "رمل | تصوّر طيف الضيافة B", LOGO_B, HERO_B, "c-raml")
page("sadu", "سدو | تصوّر طيف الضيافة C", LOGO_C, HERO_C, "c-sadu")
print("built")
