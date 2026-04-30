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
        self.shadow_host = page.locator("my-paragraph")
        self.ul_slot = page.get_by_role("list")
        self.page = page
        logger.info("DropdownPage initialized with shadowdom elements.")
        # self.dropdown_elements = dropdown.get_by_role("option")
        

    def get_header_text(self) -> str:
        "Returns h1 title header of the page."
        return self.page.locator("h1").first.inner_text()

    def open(self):
        """ Uses the navigate_to method from BasePage"""
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the <select> element to be present, then read its options
        self.shadow_host.first.wait_for()
        self.ul_slot.first.wait_for()
    
    def get_span_slot_text(self) -> str:
        """Returns the text of the shadowdom element"""
        span_var = self.shadow_host.locator('span[slot="my-text"]').first
        logger.debug(f"span_slot text is: {span_var.inner_text()}")
        return span_var.inner_text()
    
    def get_list_text(self) -> list:
        """Returns a text list of items contained in a list on the website."""
        list_res = []
        list_var = self.ul_slot.get_by_role("listitem")
        for i, item in enumerate(list_var.all()):
            logger.debug(f"item : {i} has contents: {item.inner_text()}")
            list_res.append(item.inner_text())
        return list_res