import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.js_alerts_page import JSAlertsPage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_js_alerts(page: Page, count: int) -> None:
    """
    Intent: Verify the interactivity of the javascript alert.
    Steps:
    1. Navigate to the javascript alerts page.
    2. Verify page title
    3. Click the alert button to trigger the alert and accept it 'count' times.
    4. Verify the result text reflects the successful interaction with the alert.
    """
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    assert jsalerts.get_header_text() == "JavaScript Alerts"
    jsalerts.handle_alert(count)
    expect(jsalerts.page.locator("#result")).to_have_text("You successfully clicked an alert")
    
@pytest.mark.parametrize("choice", [True, False])
def test_js_confirm_dismiss(page: Page, choice: bool) -> None:
    """
    Intent: Verify the interactivity of the javascript confirm.
    Steps:
    1. Navigate to the javascript alerts page.
    2. Click the confirm button to trigger the confirm alert and accept it with the specified choice.
    4. Verify the result text reflects the successful interaction with the alert.
    """
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    jsalerts.handle_confirm(choice)
    expected_text = "You clicked: Ok" if choice else "You clicked: Cancel"
    expect(jsalerts.page.locator("#result")).to_have_text(expected_text)

@pytest.mark.parametrize("test_prompts", [("null", True), ("", True), ("Playwright", True), ("null", False), ("テスト", True), ("テストケース9990000", True)])
def test_js_prompt(page: Page, test_prompts: tuple[str, bool]) -> None:
    """
    Intent: Verify the interactivity of the javascript prompt.
    Steps:
    1. Click the prompt button to trigger the prompt and enter the specified text.
    2. Accept or dismiss the prompt based on the 'option' parameter.
    3. Verify the result text reflects the successful interaction with the prompt.
    """
    jsalerts = JSAlertsPage(page)
    jsalerts.open()
    input_text, option = test_prompts
    jsalerts.handle_prompt(input_text, option)
    if option:
        expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: {input_text}")
    else:
        expect(jsalerts.page.locator("#result")).to_have_text(f"You entered: null")