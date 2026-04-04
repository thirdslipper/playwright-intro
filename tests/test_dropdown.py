"""
Intent: Verify that the 'dropdown' selector switches states when selecting different values.
Steps:
1. Navigate to the page.
2. Click dropdown list to expand options.
3. Select one of the dropdown list options.
4. Confirm the dropdown field now reflects the selected dropdown list option.
"""
import re
import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.dropdown_page import DropdownPage

@pytest.mark.parametrize("count", [1])#, 2, 3])
def test_checkboxes(page: Page, count: int) -> None:
    """
    Intent: Verify the interactivity of dropdown elements.
    Steps:
    1. Navigate to the Checkboxes page.
    2. Toggle the first checkbox 'count' times.
    3. Verify the state of the checkbox.
    """
    dropdown = DropdownPage(page)
    dropdown.open()
    assert dropdown.get_header_text() == "Dropdown List"