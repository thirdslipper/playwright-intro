import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # slow_mo makes it human-speed to help avoid robot detection
        browser = await p.chromium.launch(headless=True, slow_mo=1000)
        page = await browser.new_page()
        
        await page.goto("https://www.google.com")
        
        # SMART WAIT: Playwright waits for the textarea to exist before typing
        search_box = page.get_by_role("combobox") 
        await search_box.fill("Google Operations Center Jobs")
        await search_box.press("Enter")
        
        # SMART WAIT: Instead of 2000ms, wait until the "Results" div is visible
        await page.wait_for_selector("#search")
        
        print("Page loaded successfully without fixed timers.")
        
        # Manual intervention for CAPTCHAs
        print("Pausing... solve CAPTCHA and click 'Resume' in the Inspector window.")
        # await page.pause() 
        try:
            await page.wait_for_selector("#search", state="visible", timeout=30000)
            print("Results detected. Continuing...")
        except:
            print("Timed out. You might need to solve a CAPTCHA manually.")        
        await browser.close()

asyncio.run(run())