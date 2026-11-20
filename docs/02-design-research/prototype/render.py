"""Render prototype screens: python3 render.py  (needs playwright + chromium)"""
import asyncio, pathlib
from playwright.async_api import async_playwright
HERE=pathlib.Path(__file__).parent.resolve()
URL=(HERE/'index.html').as_uri()
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for name,(w,h,m,dsf) in {'mobile':(390,844,True,2),'desktop':(1440,900,False,1)}.items():
      c=await b.new_context(viewport={'width':w,'height':h},is_mobile=m,device_scale_factor=dsf,locale='ar-SA')
      pg=await c.new_page(); await pg.goto(URL); await pg.wait_for_timeout(800)
      await pg.evaluate('document.fonts.ready')
      await pg.screenshot(path=str(HERE/f'screens/tayf-{name}-fold.png'))
      await pg.screenshot(path=str(HERE/f'screens/tayf-{name}-full.jpg'),full_page=True,type='jpeg',quality=82)
      await c.close()
    await b.close()
asyncio.run(main())
