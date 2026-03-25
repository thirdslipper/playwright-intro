from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class AddRemovePage(BasePage):
    def __init__(self, page: Page):
        # This calls the BasePage's __init__ to set up self.page and self.base_url
        super().__init__(page) 
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_buttons = page.locator("button.added-manually")


    def open(self):
        # Uses the navigate_to method from BasePage
        self.navigate_to("add_remove_elements/")

    def add_elements(self, count: int):
        logger.info(f"Adding {count} elements to the page.")
        for _ in range(count):
            self.add_button.click()
            logger.debug(f"Clicked 'Add' - Iteration {_+1}")

    def remove_all_elements(self):
        del_Count = self.delete_buttons.count()
        logger.info(f"Deleting {del_Count} elements to the page.")
        # Clicks the first "Delete" button until none are left
        for _ in range(del_Count):
            self.delete_buttons.first.click()
            logger.debug(f"Clicked 'Delete' - Iteration {_+1}")