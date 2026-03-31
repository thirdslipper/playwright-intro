"""
Intent: Verify that the 'Add Element' button dynamically creates a 'Delete' button.
Steps:
1. Navigate to the page.
2. Click checkboxes.
3. Confirm the checkboxes are checked or unchecked opposite to their initial state.
"""
import re
import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.checkboxes_page import CheckboxesPage

@pytest.mark.parametrize("count", [1])#, 2, 3])
def test_checkboxes(page: Page, count: int) -> None:
    """
    Intent: Verify the interactivity of checkbox elements.
    Steps:
    1. Navigate to the Checkboxes page.
    2. Toggle the first checkbox 'count' times.
    3. Verify the state of the checkbox.
    """
    checkboxes = CheckboxesPage(page)
    checkboxes.open()

    checkboxes.click_first_checkbox(count)
    expect(checkboxes.checkbox_elements.first).to_be_checked()