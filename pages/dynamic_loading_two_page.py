from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "dynamic_loading/2"


class DynamicLoadingTwoPage(BasePage):
    def __init__(self, page: Page):
        """ This calls the BasePage's __init__ to set up self.page and self.base_url"""
        super().__init__(page) 
        #grab all the dropdowns on the page and store them into var dropdowns
        self.start_button = page.get_by_role("button", name= "Start")
        self.loading_bar = page.locator("#loading")
        self.finish_text = page.locator("#finish")
        logger.info("DynamicLoadingTwoPage initialized with button elements.")
        

    def open(self):
        """ Uses the navigate_to method from BasePage"""
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the <select> element to be present, then read its options
        self.start_button.first.wait_for()

    def click_start(self):
        """Clicks the start button to trigger dynamic loading."""
        logger.info(f"Clicking button to trigger dynamic loading")
        self.start_button.click()
        logger.info("Waiting for dynamic content to load.")