from playwright.sync_api import expect, Page
import pytest #Playwright, sync_playwright, 
from pages.shadowdom_page import ShadowdomPage

# @pytest.mark.parametrize("target", [[("B", "A"), ("A", "B"), ("B", "A")]])
def test_shadowdom(page: Page) -> None:
    """Intent: 
    """
    shadowdom = ShadowdomPage(page)
    shadowdom.open()
    # assert shadowdom.get_header_text() == "Simple template"