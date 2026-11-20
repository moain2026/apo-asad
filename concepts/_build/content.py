# -*- coding: utf-8 -*-
"""محتوى مشترك لتصورات طيف الضيافة. كل ما هنا من كلام أبو سعد أو مؤقت مُعلَّم.
لا ادعاءات: لا سنوات خبرة، لا أعداد مناسبات، لا شعارات جهات، لا طاقم نسائي (DEC-13)."""

ICONS = {
 "dallah": '<path d="M14 6h4M16 6v3M11 13c0-2.2 2.2-4 5-4s5 1.8 5 4l1 9H10l1-9Z"/><path d="M21 14l5-4M10 22h12M9 26h14"/>',
 "cup": '<path d="M7 12h16l-2 9a4 4 0 0 1-4 3h-4a4 4 0 0 1-4-3l-2-9Z"/><path d="M5 27h20M12 7c0-2 2-2 2-4M17 7c0-2 2-2 2-4"/>',
 "tea": '<path d="M10 9h12l-1.5 15a2 2 0 0 1-2 2h-5a2 2 0 0 1-2-2L10 9Z"/><path d="M11 15h10M8 28h16"/>',
 "tray": '<path d="M4 22h24M6 22a10 10 0 0 1 20 0M16 9v3M14 9h4"/><path d="M8 26h16"/>',
 "rings": '<circle cx="12" cy="18" r="6"/><circle cx="20" cy="18" r="6"/><path d="M10 8l2 3 2-3"/>',
 "majlis": '<path d="M4 24V14a3 3 0 0 1 3-3h18a3 3 0 0 1 3 3v10M4 24h24M4 19h24M9 11V8M23 11V8"/>',
 "building": '<path d="M7 27V7h12v20M19 13h6v14M4 27h24M11 11h4M11 15h4M11 19h4"/>',
 "door": '<path d="M9 27V8a7 7 0 0 1 14 0v19M5 27h22M19 18h.01"/>',
 "wa": '<path d="M5 27l1.6-5A11 11 0 1 1 11 26.4L5 27Z"/><path d="M12 11c0 5 4 9 9 9l1.5-2.5-3-1.5-1.5 1.5c-1.5-.5-3-2-3.5-3.5L16 12l-1.5-3L12 11Z"/>',
 "phone": '<path d="M8 4h4l2 6-3 2a14 14 0 0 0 9 9l2-3 6 2v4a3 3 0 0 1-3 3C14 27 5 18 5 7a3 3 0 0 1 3-3Z"/>',
 "check": '<path d="M6 16l6 6 14-14"/>',
 "pin": '<path d="M16 28s9-8 9-15a9 9 0 0 0-18 0c0 7 9 15 9 15Z"/><circle cx="16" cy="13" r="3"/>',
 "shield": '<path d="M16 4l10 4v7c0 6-4 11-10 13C10 26 6 21 6 15V8l10-4Z"/><path d="M11 16l3 3 7-7"/>',
 "image": '<rect x="4" y="6" width="24" height="20" rx="2"/><path d="M4 22l7-7 6 6 4-4 7 7"/><circle cx="21" cy="12" r="2"/>',
 "arrow": '<path d="M26 16H6M13 9l-7 7 7 7"/>',
}
def icon(n, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

SERVICES = [
 ("dallah","قهوجيين وصبابين","قهوة سعودية تُجهَّز في المكان، وصبّاب يخدم المجلس من أول ضيف إلى آخره."),
 ("tray","ركن الضيافة","الدلال والفناجين والتمر مرتّبة في ركن واحد يليق بمدخل مناسبتك."),
 ("tea","الشاي والمشروبات","شاي ونعناع ومشروبات الشتاء الساخنة، حسب موسم مناسبتك ووقتها."),
 ("cup","التقديمات","تمر وحلا ومعجنات تُقدَّم مع القهوة، وتحدّدها معنا قبل الموعد."),
]
OCCASIONS = [
 ("rings","أعراس وملكات","wedding"),
 ("majlis","مجالس وعزاء","majlis"),
 ("building","مناسبات الشركات","corp"),
 ("door","استقبالات وغبقات","recv"),
]
STEPS = [
 ("أرسل التفاصيل","المدينة والتاريخ والوقت وعدد الضيوف، من النموذج أو واتساب."),
 ("يوصلك العرض","نرتّب معك الطاقم والتقديمات، ويوصلك السعر قبل أي تأكيد."),
 ("نخدم ضيوفك","يحضر الطاقم قبل الموعد، ويرتّب الركن، ويخدم حتى آخر ضيف."),
]
GALLERY = [
 ("القهوجي يصب لضيف، لقطة قريبة بإضاءة المناسبة","wide"),
 ("ركن الضيافة كامل: الدلال والفناجين والتمر",""),
 ("الطاقم واقف بالزي قبل بداية المناسبة",""),
 ("التقديمات: تمر وحلا ومعجنات",""),
 ("الشاي والمشروبات الشتوية",""),
]
FAQ = [
 ("هل تخدمون الدمام والخبر فقط؟","نبدأ بالدمام والخبر. اكتب مدينتك في الطلب ونرد عليك بإمكانية التغطية. <em>(نص مؤقت: يؤكده أبو سعد)</em>"),
 ("كيف أعرف السعر؟","أرسل المدينة والتاريخ وعدد الضيوف، ويوصلك السعر على واتساب قبل أي تأكيد."),
 ("وش يشمل الطلب؟","يحدد حسب مناسبتك: الطاقم، القهوة والشاي، والتقديمات. <em>(القائمة النهائية من أبو سعد، س١–س٢)</em>"),
 ("كم قبل المناسبة أحجز؟","كل ما بكّرت كان أضمن، خصوصًا في المواسم. <em>(سياسة الطلب في نفس اليوم: س٦)</em>"),
]
CITIES = ["الدمام","الخبر"]
TYPES = ["زواج أو ملكة","مجلس أو عزاء","مناسبة شركة","استقبال أو غبقة","أخرى"]

def form_html(prefix=""):
    cities = "".join(f"<option>{c}</option>" for c in CITIES) + "<option>مدينة أخرى</option>"
    types = "".join(f"<option>{t}</option>" for t in TYPES)
    return f'''<form class="order" data-order novalidate>
  <div class="f"><label for="{prefix}c">المدينة</label><select id="{prefix}c" name="city">{cities}</select></div>
  <div class="f"><label for="{prefix}t">نوع المناسبة</label><select id="{prefix}t" name="type">{types}</select></div>
  <div class="f"><label for="{prefix}d">التاريخ</label><input id="{prefix}d" name="date" type="date"></div>
  <div class="f"><label for="{prefix}h">الوقت</label><input id="{prefix}h" name="time" type="time"></div>
  <div class="f full"><label for="{prefix}g">عدد الضيوف تقريبًا</label><input id="{prefix}g" name="guests" type="number" inputmode="numeric" min="1" placeholder="مثال: 80"></div>
  <button class="btn wa full" type="submit">{icon("wa")}<span>جهّز رسالة واتساب</span></button>
  <p class="fine full">{icon("shield","ic sm")}لا نحفظ أي بيانات. الرسالة تفتح في واتساب وتعدّلها قبل الإرسال.</p>
</form>'''

def faq_html():
    return "".join(f'<details data-faq{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(FAQ))

DIALOG = '''<dialog id="waPreview" aria-labelledby="waT"><h3 id="waT">رسالة طلب عرض السعر</h3><pre id="waText"></pre><p id="waNote" class="fine"></p><div class="dl-act"><a id="waGo" class="btn wa" target="_blank" rel="noopener">فتح واتساب</a><button class="btn ghost" data-close type="button">رجوع</button></div></dialog>'''

def head(title, css_rel):
    return f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><title>{title}</title><link rel="stylesheet" href="../_fonts/fonts.css"><link rel="stylesheet" href="../_shared/base.css"><link rel="stylesheet" href="{css_rel}"></head>'''

PROTO_BAR = '<div class="proto">تصوّر تصميمي داخلي · النصوص والصور مؤقتة ويعتمدها أبو سعد</div>'
