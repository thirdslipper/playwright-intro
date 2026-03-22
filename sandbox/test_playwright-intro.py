import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=True, slow_mo=1000) # headless=False lets you see it work
        page = await browser.new_page()
        
        # 1. Logic: Our list of things to search for
        search_terms = ["Python Playwright", "Software QA Jobs 2026", "Scorpion Santa Clarita"]
        
        # 2. Loop: Iterate through the list
        for term in search_terms:
            print(f"Searching for: {term}")
            await page.goto("https://www.google.com")
            await page.fill('textarea[name="q"]', term) # 'textarea' is the modern Google search box
            await page.press('textarea[name="q"]', "Enter")
            await page.wait_for_timeout(2000) # Wait 2 seconds to see the results
            await page.pause()
        await browser.close()
        print("Success! Your logic and automation are talking to each other.")

asyncio.run(run())