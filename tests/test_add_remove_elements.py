import re
import pytest
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.internet_pages import AddRemovePage

@pytest.mark.parametrize("count", [1, 2, 3])
def test_add_remove_elements(page: Page, count: int) -> None:
    # navigates to heroku add elements page
    add_remove = AddRemovePage(page)
    add_remove.open()

    #add elements to page and confirms if the count matches number of elements added  
    add_remove.add_elements(count)
    expect(add_remove.delete_buttons).to_have_count(count)

    #remove all elements then checks if count is 0
    add_remove.remove_all_elements()
    expect(add_remove.delete_buttons).to_have_count(0)