from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.dynamic_loading_two_page import DynamicLoadingTwoPage

def test_dynamic_loading_two(page: Page) -> None:
    """
    Intent: Verify the responsiveness of dynamically loaded elements.
    Steps:
    1. Navigate to the Dynamically Loaded Page Elements page.
    2. Verify page title
    3. Click the button to trigger dynamic loading.
    4. Verify the loading indicator appears and displays the correct text.
    5. Verify the loading bar disappears and the dynamically loaded content is visible with the correct text.
    """
    dynamic_loading_two = DynamicLoadingTwoPage(page)
    dynamic_loading_two.open()
    assert dynamic_loading_two.get_header_text() == "Dynamically Loaded Page Elements"
    dynamic_loading_two.click_start()
    
    expect(dynamic_loading_two.loading_bar).to_be_visible()
    expect(dynamic_loading_two.loading_bar).to_have_text("Loading...")
    expect(dynamic_loading_two.finish_text).to_be_visible(timeout=10000)
    expect(dynamic_loading_two.finish_text).to_have_text("Hello World!")
    expect(dynamic_loading_two.loading_bar).not_to_be_visible()
