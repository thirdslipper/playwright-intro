from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "javascript_alerts"


class JSAlertsPage(BasePage):
    def __init__(self, page: Page):
        """ This calls the BasePage's __init__ to set up self.page and self.base_url"""
        super().__init__(page) 
        #grab all the dropdowns on the page and store them into var dropdowns
        self.js_elements = page.get_by_role("button")
        logger.info("JSAlertsPage initialized with button elements.")
        # self.dropdown_elements = dropdown.get_by_role("option")
        

    def open(self):
        """ Uses the navigate_to method from BasePage"""
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the <select> element to be present, then read its options
        self.js_elements.first.wait_for()
    
    def handle_alert(self, count: int):
        """Handles JavaScript alerts by accepting them."""
        logger.info(f"Clicking button to trigger alert")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.js_elements.get_by_text("Click for JS Alert").click()
        logger.info("Waiting for alert to appear.")

    def handle_confirm(self, option: bool):
        """Handles JavaScript confirm dialogs by accepting or dismissing them based on the 'option' parameter."""
        logger.info(f"Clicking button to trigger confirm dialog with option: {option}")
        if option:
            logger.debug(f"Will accept the confirm dialog.")
            self.page.once("dialog", lambda dialog: dialog.accept())
        else:
            logger.debug(f"Will dismiss the confirm dialog.")
            self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.js_elements.get_by_text("Click for JS Confirm").click()

    def handle_prompt(self, input_text: str, option: bool):
        """Handles JavaScript prompt dialogs by entering text and accepting or dismissing them."""
        logger.info(f"Clicking button to trigger prompt dialog with input: {input_text}")
        if option:
            logger.debug(f"Will accept the prompt dialog with dialogue input: {input_text}")
            self.page.once("dialog", lambda dialog: dialog.accept(input_text))
        else:
            logger.debug(f"Will dismiss the prompt dialog with dialogue input: {input_text}")
            self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.js_elements.get_by_text("Click for JS Prompt").click()