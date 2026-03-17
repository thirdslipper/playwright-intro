import re
from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
def test_google_store(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.google.com/?zx=1773356422955&no_sw_cr=1")
    page.get_by_role("link", name="Store").click()
    page.locator("[data-test=\"nav-links\"]").get_by_role("link", name="Phones").click()
    page.get_by_role("link", name="Learn more about Pixel 10a").click()
    page.get_by_text("Google Pixel 10a").first.click()
    expect(page.get_by_text("Google Pixel 10a").first).to_be_visible()
    expect(page.get_by_text("testing failed test").first).not_to_be_visible()
    page.locator("#p10a-overview-hero").get_by_role("link", name="Buy Pixel 10a").click()
    expect(page.get_by_role("heading", name="Pixel 10a")).to_be_visible()
    page.get_by_role("link", name="Google Store home").click()

    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
