
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
    
    # for input_text, option in test_prompts:
    #     jsalerts.handle_prompt(input_text, option)
    #     prev_text = jsalerts.page.locator("#result").inner_text()
    #     if option:
    #         expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: {input_text}")
    #     else:
    #         expect(jsalerts.page.locator("#result")).to_have_text(f"{prev_text}")

@pytest.mark.parametrize("choice", [True, False])
def test_js_confirm_dismiss(page: Page, choice: bool) -> None:
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    jsalerts.handle_confirm(choice)
    expected_text = "You clicked: Ok" if choice else "You clicked: Cancel"
    expect(jsalerts.page.locator("#result")).to_have_text(expected_text)

@pytest.mark.parametrize("test_prompts", [("null", True), ("", True), ("Playwright", True), ("null", False), ("テスト", True), ("テストケース9990000", True)])
def test_js_prompt(page: Page, test_prompts: tuple[str, bool]) -> None:
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    input_text, option = test_prompts
    jsalerts.handle_prompt(input_text, option)
    if option:
        expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: {input_text}")
    else:
        expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: null")