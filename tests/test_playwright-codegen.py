import re
from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
def test_google_store(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://www.google.com/?zx=1773356422955&no_sw_cr=1")
    page.get_by_role("link", name="Store").click()
    page.locator("[data-test=\"nav-links\"]").get_by_role("link", name="Phones").click()
    page.locator("[data-test=\"nav-links\"]").get_by_role("link", name="Phones").press("ControlOrMeta+-")
    page.get_by_role("link", name="Learn more about Pixel 10a").click()
    page.get_by_text("Google Pixel 10a").first.click()
    expect(page.get_by_text("Google Pixel 10a").first).to_be_visible()
    expect(page.get_by_text("testing failed test").first).to_be_visible()
    page.locator("#p10a-overview-hero").get_by_role("link", name="Buy Pixel 10a").click()
    page.get_by_role("main").press("ControlOrMeta+-")
    page.get_by_role("main").press("ControlOrMeta+-")
    page.get_by_role("main").press("ControlOrMeta+-")
    page.get_by_role("main").press("ControlOrMeta+-")
    expect(page.get_by_role("heading", name="Pixel 10a")).to_be_visible()
    page.get_by_role("link", name="Google Store home").click()
    page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dtest%2Bancestral%2Bnavigation%2Band%2Bstore%26sca_esv%3D0969567df9557e92%26source%3Dhp%26ei%3D7EWzafabLuGrur8PnaexmA0%26iflsig%3DAFdpzrgAAAAAabNT_A0xLMayhK8zXI6UHargMuvdq7X-%26ved%3D0ahUKEwj2wd_tu5uTAxXhle4BHZ1TDNMQ4dUDCBY%26uact%3D5%26oq%3D%26gs_lp%3DEgdnd3Mtd2l6IgBIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEAmAIAoAIAmAMAkgcAoAcAsgcAuAcAwgcAyAcAgAgA%26sclient%3Dgws-wiz%26sei%3D-EWzaZTgGcz7kPIP9p2TiQU&q=EgSsdv5fGPiLzc0GIjAqfVbO_8fRZpnSaM4LHxQxEHy8zXyhpCf1HK4tDWyOblAyZfvRTatZdf6-wrpAYmkyAVJaAUM")
    page.locator("iframe[name=\"a-bv5879i4lwcz\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("div:nth-child(2) > div").first.click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
