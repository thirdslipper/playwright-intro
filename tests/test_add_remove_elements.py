import re
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.internet_pages import AddRemovePage

def test_add_remove_elements(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    # expect(page.get_by_text("Add Element")).first.to_be_visible()
    for i in range(3):
        page.get_by_role("button", name="Add Element").first.click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(3)
    for i in range(3):
        page.get_by_role("button", name="Delete").first.click()
    expect(page.get_by_role("button", name="Delete")).not_to_be_visible()
