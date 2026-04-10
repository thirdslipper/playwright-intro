import pytest
from playwright.sync_api import Page

@pytest.mark.infrastructure
def test_screenshot_on_failure_verification(page: Page):
    """
    INTENT: Force a failure to verify that conftest.py correctly 
    captures a screenshot and names it after this test function.
    """
    page.goto("https://google.com")
    # This assertion is designed to fail
    assert False, "Verification failure: Check if 'FAIL_test_screenshot_on_failure_verification.png' exists."