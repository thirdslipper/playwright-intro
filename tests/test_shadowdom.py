from playwright.sync_api import expect, Page
import pytest #Playwright, sync_playwright, 
from pages.shadowdom_page import ShadowdomPage

test_text = "Let's have some different text!"
test_text_list = "In a list!"


def test_shadowdom(page: Page) -> None:
    """Intent: Verify elements are present with shadowdom elements on the page.
    """
    shadowdom = ShadowdomPage(page)
    shadowdom.open()
    assert(shadowdom.get_span_slot_text() == test_text)

def test_span_slot(page: Page) -> None:
    shadowdom = ShadowdomPage(page)
    shadowdom.open()
    dom_list = shadowdom.get_list_text()
    assert(dom_list[0] == test_text)
    assert(dom_list[1] == test_text_list)