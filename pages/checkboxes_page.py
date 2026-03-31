from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "checkboxes"


class CheckboxesPage(BasePage):
    def __init__(self, page: Page):
        # This calls the BasePage's __init__ to set up self.page and self.base_url
        super().__init__(page) 
        #should grab all the checkboxes on the page and store them into var checkboxes
        #better than hardcoding grabbing checkbox 1 and checkbox 2
        self.checkbox_elements = page.get_by_role("checkbox")

    def open(self):
        # Uses the navigate_to method from BasePage
        self.navigate_to(PAGE_PATH)
        logger.info(f"Adding Navigating to page {PAGE_PATH}")
        self.checkbox_elements.first.wait_for()
    def click_first_checkbox(self, count: int):
        logger.info(f"Clicking first checkbox {count} times.")
        for _ in range(count):
            self.checkbox_elements.first.click()
            logger.info(f"Clicked {self.checkbox_elements.first.inner_text()} - Iteration {_+1}")

    """untested below"""
    def click__all_checkboxes(self, count: int):
        logger.info(f"Clicking each checkbox_elements {count} times.")
        for checkbox in self.checkbox_elements.all():
            for i in range(count):
                self.checkbox.click()
                logger.debug(f"Clicked {checkbox.inner_text()} - Iteration {i+1}")
        
    def uncheck_checkboxes(self, count: int):
        logger.info(f"Unchecking all checkboxes {count} times.")
        for checkbox in self.checkbox_elements.all():
            for i in range(count):
                checkbox.set_checked(False)
                logger.debug(f"{checkbox.inner_text()} set to false - Iteration {i+1}")
    
    def check_checkboxes(self, count: int):
        logger.info(f"Checking all checkboxes {count} times.")
        for checkbox in self.checkbox_elements.all():
            for i in range(count):
                checkbox.set_checked(True)
                logger.debug(f"{checkbox.inner_text()} set to true - Iteration {i+1}")


    # def add_elements(self, count: int):
    #     logger.info(f"Adding {count} elements to the page.")
    #     for _ in range(count):
    #         self.add_button.click()
    #         logger.debug(f"Clicked 'Add' - Iteration {_+1}")

    # def remove_all_elements(self):
    #     del_Count = self.delete_buttons.count()
    #     logger.info(f"Deleting {del_Count} elements to the page.")
    #     # Clicks the first "Delete" button until none are left
    #     for _ in range(del_Count):
    #         self.delete_buttons.first.click()
    #         logger.debug(f"Clicked 'Delete' - Iteration {_+1}")