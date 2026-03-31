"""
Intent: Verify that the 'Add Element' button dynamically creates a 'Delete' button.
Steps:
1. Navigate to the page.
2. Click 'Add Element'.
3. Confirm a 'Delete' button appears in the list.
4. Click 'Delete Element' to remove all elements. 
5. Confirm all added elements are deleted.
"""
import re
import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.add_remove_page import AddRemovePage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_add_remove_elements(page: Page, count: int) -> None:
    """
    Verify the dynamic creation and deletion of elements.
    Validates that clicking 'Add' produces the correct number of buttons,
    'Delete' deletes the correct number of buttons.
    """
    # navigates to heroku add elements page
    add_remove = AddRemovePage(page)
    add_remove.open()

    #add elements to page and confirms if the count matches number of elements added  
    add_remove.add_elements(count)
    expect(add_remove.delete_buttons).to_have_count(count)

    #remove all elements then checks if count is 0
    add_remove.remove_all_elements()
    expect(add_remove.delete_buttons).to_have_count(0)