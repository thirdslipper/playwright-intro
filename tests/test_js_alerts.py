
import re
import pytest
import random
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.js_alerts_page import JSAlertsPage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_js_alerts(page: Page, count: int) -> None:
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    assert jsalerts.get_header_text() == "JavaScript Alerts"
    jsalerts.handle_alert(count)
    expect(jsalerts.page.locator("#result")).to_have_text("You successfully clicked an alert")
    
    for i in range(count):
        random_option = random.choice([True, False])
        jsalerts.handle_confirm(random_option)
        if random_option:
            expect(jsalerts.page.locator("#result")).to_have_text("You clicked: Ok")  
        else: 
            expect(jsalerts.page.locator("#result")).to_have_text("You clicked: Cancel")

    test_prompts = [("null", True), ("", True), ("Playwright", True), ("null", False), ("テスト", True), ("テストケース9990000", True)]
    for input_text, option in test_prompts:
        jsalerts.handle_prompt(input_text, option)
        prev_text = jsalerts.page.locator("#result").inner_text()
        if option:
            expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: {input_text}")
        else:
            expect(jsalerts.page.locator("#result")).to_have_text(f"{prev_text}")