/* طيف الضيافة — منطق مشترك للتصورات (بدون مكتبات).
   R-02: الرقم في مصدر واحد. فارغ = وضع المعاينة (لا يُفتح واتساب ولا تُرسل بيانات). */
window.TAYF = { wa: "", tel: "" }; // يُملأ بالرقم المعتمد (DEC-03) بالصيغة الدولية بدون + مثل 9665XXXXXXXX

(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  function buildMsg(form) {
    const v = (n) => (form.elements[n] && form.elements[n].value.trim()) || "…";
    return [
      "السلام عليكم طيف الضيافة، أرغب في عرض سعر:",
      "المدينة: " + v("city"),
      "نوع المناسبة: " + v("type"),
      "التاريخ: " + v("date"),
      "الوقت: " + v("time"),
      "عدد الضيوف تقريبًا: " + v("guests"),
    ].join("\n");
  }

  function openPreview(text) {
    const d = $("#waPreview");
    if (!d) return;
    $("#waText", d).textContent = text;
    const go = $("#waGo", d);
    if (TAYF.wa) {
      go.href = "https://wa.me/" + TAYF.wa + "?text=" + encodeURIComponent(text);
      go.removeAttribute("aria-disabled");
      $("#waNote", d).textContent = "تفتح الرسالة في واتساب وتقدر تعدّلها قبل الإرسال.";
    } else {
      go.removeAttribute("href");
      go.setAttribute("aria-disabled", "true");
      $("#waNote", d).textContent = "معاينة فقط: الرقم المعتمد لم يُضف بعد، ولا تُرسل أي بيانات.";
    }
    d.showModal();
  }

  document.addEventListener("submit", (e) => {
    if (!e.target.matches("[data-order]")) return;
    e.preventDefault();
    openPreview(buildMsg(e.target));
  });

  document.addEventListener("click", (e) => {
    const t = e.target.closest("[data-wa]");
    if (t) {
      e.preventDefault();
      openPreview(t.dataset.wa || "السلام عليكم طيف الضيافة، أرغب في عرض سعر لمناسبة.");
    }
    const c = e.target.closest("[data-close]");
    if (c) c.closest("dialog").close();
    const call = e.target.closest("[data-call]");
    if (call && !TAYF.tel) { e.preventDefault(); openPreview("(زر الاتصال يعمل بعد إضافة الرقم المعتمد)"); }
  });

  // الشريط السفلي: يختفي ما دامت أزرار الهيرو ظاهرة
  const bar = $(".mbar"), heroCta = $("[data-hero-cta]");
  if (bar && heroCta && "IntersectionObserver" in window) {
    new IntersectionObserver(([en]) => bar.classList.toggle("on", !en.isIntersecting)).observe(heroCta);
  } else if (bar) bar.classList.add("on");

  // الأسئلة: سؤال واحد مفتوح
  $$("details[data-faq]").forEach((d) =>
    d.addEventListener("toggle", () => {
      if (d.open) $$("details[data-faq]").forEach((o) => o !== d && (o.open = false));
    })
  );

  const y = $("#yr"); if (y) y.textContent = new Date().getFullYear();
})();
