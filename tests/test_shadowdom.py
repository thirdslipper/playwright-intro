from playwright.sync_api import expect, Page
import pytest #Playwright, sync_playwright, 
from pages.shadowdom_page import ShadowdomPage

header = "Simple template"
test_text = "Let's have some different text!"
test_text_list = "In a list!"


def test_shadowdom(page: Page) -> None:
    """Intent: Verify elements are present with shadowdom elements on the page.
    Navigates to the shadowdom page
    Verifies title header name is 'Simple Template'
    Verifies the first shadowdom text in a span is "Let's have some different text!"
    """
    shadowdom = ShadowdomPage(page)
    shadowdom.open()
    assert(shadowdom.get_header_text() == header)
    assert(shadowdom.get_span_slot_text() == test_text)

def test_span_slot(page: Page) -> None:
    """Intent: Validate the shadowdom elements in the list
    Navigates to the shadowdom page
    Verifies the first list-item of the shadowdom is 'Let's have some different text!/
    Verifies the second list-item of the shadowdom is 'In a list!'"""
    shadowdom = ShadowdomPage(page)
    shadowdom.open()
    dom_list = shadowdom.get_list_text()
    assert(dom_list[0] == test_text)
    assert(dom_list[1] == test_text_list)