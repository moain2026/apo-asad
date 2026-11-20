"""لقطات + فحوصات: python3 concepts/_build/render.py  (يحتاج playwright + Chrome)"""
import asyncio, json, os, sys
from playwright.async_api import async_playwright
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES=sys.argv[1:] or ["dana","raml","sadu"]
CHECK="""()=>{const r={overflow:document.documentElement.scrollWidth-innerWidth,small:[],tiny:[],h:document.documentElement.scrollHeight};
document.querySelectorAll('a,button,summary,input,select').forEach(e=>{const b=e.getBoundingClientRect();const cs=getComputedStyle(e);if(b.width&&b.height&&cs.visibility!=='hidden'&&!e.closest('dialog')&&!e.closest('.mbar:not(.on)')&&b.height<44)r.small.push((e.textContent||e.name||e.tagName).trim().slice(0,30)+':'+Math.round(b.height))});
document.querySelectorAll('body *').forEach(e=>{if(e.closest('dialog'))return;const t=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());if(t){const f=parseFloat(getComputedStyle(e).fontSize);if(f<13)r.tiny.push(e.tagName+':'+f)}});return r}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        out={}
        for n in NAMES:
            sd=os.path.join(ROOT,n,"screens"); os.makedirs(sd,exist_ok=True)
            for tag,w,h,m in [("mobile",390,844,True),("desktop",1440,900,False)]:
                pg=await b.new_page(viewport={"width":w,"height":h},device_scale_factor=2 if m else 1,is_mobile=m,has_touch=m)
                await pg.goto("file://"+os.path.join(ROOT,n,"index.html")); await pg.wait_for_timeout(700)
                await pg.evaluate("document.fonts.ready")
                await pg.screenshot(path=f"{sd}/{tag}-fold.png")
                await pg.screenshot(path=f"{sd}/{tag}-full.jpg",full_page=True,quality=70,type="jpeg")
                out[f"{n}-{tag}"]=await pg.evaluate(CHECK)
                await pg.close()
            for w in (320,360,768,1024):
                pg=await b.new_page(viewport={"width":w,"height":800}); await pg.goto("file://"+os.path.join(ROOT,n,"index.html")); await pg.wait_for_timeout(200)
                out[f"{n}-ovf{w}"]=await pg.evaluate("document.documentElement.scrollWidth-innerWidth"); await pg.close()
        await b.close()
        print(json.dumps(out,ensure_ascii=False,indent=0))
asyncio.run(main())
