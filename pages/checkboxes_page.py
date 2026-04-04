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

    @property
    def checkbox_count(self) -> int:
        """Returns the number of checkboxes found on the page."""
        return self.checkbox_elements.count()

    def click_first_checkbox(self, count: int):
        """Clicking first checkbox {count} times"""
        for _ in range(count):
            self.checkbox_elements.first.click()
            logger.info(f"Clicked first checkbox - Iteration {_+1}")

    def click_all_checkboxes(self, count: int):
        """Clicking all checkboxes {count} times"""
        logger.info(f"Clicking each checkbox_elements {count} times.")
        for i, checkbox in enumerate(self.checkbox_elements.all()):
            for _ in range(count):
                checkbox.click()
                logger.debug(f"Clicked checkbox{i+1} - Iteration {_+1}")

    def get_all_checkbox_states(self) -> list[bool]:
        """Returns a list of booleans representing the checked state of all boxes."""
        checkboxValues = []
        for i, checkbox in enumerate(self.checkbox_elements.all()):
            checkboxValues.append(checkbox.is_checked())
            logger.debug(f"Appending checkbox{i+1} to list")
        return checkboxValues
    
    def uncheck_checkboxes(self):
        """Setting all checkboxes to false/unchecked state."""
        logger.info(f"Setting all checkboxes to false(unchecked).")
        for i, checkbox in enumerate(self.checkbox_elements.all()):
            checkbox.set_checked(False)
            logger.debug(f"checkbox {i+1} set to false")
    
    def check_checkboxes(self):
        """Setting all checkboxes to true/checked state."""
        logger.info(f"Setting all checkboxes to true(checked).")
        for i, checkbox in enumerate(self.checkbox_elements.all()):
            checkbox.set_checked(True)
            logger.debug(f"checkbox {i+1} set to true")