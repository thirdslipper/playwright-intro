from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "shadowdom"


class ShadowdomPage(BasePage):
    def __init__(self, page: Page):
        """ This calls the BasePage's __init__ to set up self.page and self.base_url"""
        super().__init__(page) 
        #grab all the dropdowns on the page and store them into var dropdowns
        # self.shadowdom = page.get_by_role("combobox")
        logger.info("DropdownPage initialized with shadowdom elements.")
        # self.dropdown_elements = dropdown.get_by_role("option")
        

    def open(self):
        """ Uses the navigate_to method from BasePage"""
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the <select> element to be present, then read its options
        # self.dropdown_elements.first.wait_for()
        