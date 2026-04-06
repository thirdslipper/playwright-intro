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
import random
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.dropdown_page import DropdownPage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_dropboxes(page: Page, count: int) -> None:
    """
    Intent: Verify the interactivity of dropdown elements.
    Steps:
    1. Navigate to the Dropdown page.
    2. Verify page title
    3. Verify the state of the dropbox.
    4. Select a random option from the dropdown 'count' times.
    5. Verify the state of the dropdown reflects the selected option.
    6. Verify the placeholder option is disabled.
    """
    dropdown = DropdownPage(page)
    dropdown.open()
    #get list of options from dropdown and store them into var options
    """[Please select an option, Option 1, Option 2]"""
    options = dropdown.get_options()
    dropdown_bar = dropdown.dropdown_elements.first.locator("option:checked")

    assert dropdown.get_header_text() == "Dropdown List"
    assert dropdown.starting_option() == options[0]
    
    for i in range(count):
        random_option = random.choice(options[1:])
        dropdown.select_option(random_option)
        expect(dropdown_bar).to_have_text(random_option)

    placeholder = dropdown.dropdown_elements.locator("option").first
    expect(placeholder).to_be_disabled()