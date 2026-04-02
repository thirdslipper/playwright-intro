"""
Intent: Verify that the 'checkboxes' switches states when clicked.
Steps:
1. Navigate to the page.
2. Click checkboxes.
3. Confirm the checkboxes are checked or unchecked opposite to their initial state.
"""
import re
import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.checkboxes_page import CheckboxesPage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_checkboxes(page: Page, count: int) -> None:
    """
    Intent: Verify the interactivity of checkbox elements.
    Steps:
    1. Navigate to the Checkboxes page.
    2. Toggle the first checkbox 'count' times.
    3. Verify the state of the checkbox.
    """
    is_even = count % 2 == 0
    checkboxes = CheckboxesPage(page)
    checkboxes.open()

    checkboxValuesBefore = checkboxes.get_all_checkbox_states()
    checkboxes.click_first_checkbox(count)
    checkboxValuesAfter = checkboxes.get_all_checkbox_states()
    if is_even:
        assert checkboxValuesBefore[0] == checkboxValuesAfter[0]
    else:
        assert checkboxValuesBefore[0] != checkboxValuesAfter[0]

    checkboxValuesBefore = checkboxes.get_all_checkbox_states()
    checkboxes.click_all_checkboxes(count)
    checkboxValuesAfter = checkboxes.get_all_checkbox_states()
    for i in range(checkboxes.checkbox_count):
        if is_even:
            assert checkboxValuesBefore[i] == checkboxValuesAfter[i]
        else:
            assert checkboxValuesBefore[i] != checkboxValuesAfter[i]

    checkboxes.check_checkboxes()
    for i in range(checkboxes.checkbox_count):
        expect(checkboxes.checkbox_elements.nth(i)).to_be_checked()

    checkboxes.uncheck_checkboxes()
    for i in range(checkboxes.checkbox_count):
        expect(checkboxes.checkbox_elements.nth(i)).not_to_be_checked()