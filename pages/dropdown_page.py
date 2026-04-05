from playwright.sync_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "dropdown"


class DropdownPage(BasePage):
    def __init__(self, page: Page):
        # This calls the BasePage's __init__ to set up self.page and self.base_url
        super().__init__(page) 
        #grab all the dropdowns on the page and store them into var dropdowns
        self.dropdown_elements = page.get_by_role("combobox")
        logger.info("DropdownPage initialized with dropdown elements.")
        # self.dropdown_elements = dropdown.get_by_role("option")
        

    def open(self):
        # Uses the navigate_to method from BasePage
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the <select> element to be present, then read its options
        self.dropdown_elements.first.wait_for()
        option_locator = self.dropdown_elements.locator("option")

        options = []
        for i in range(option_locator.count()):
            options.append(option_locator.nth(i).inner_text())
        logger.info(f"Open(): Dropdown options: {options}")
        print(options)
    
    """tests to do: 
    1. start on "Please select an option", 
    2. cannot select "please select an option", 
    3.switch between option 1 and 2,  """
    def starting_option(self) -> str:
        """Returns the currently selected option's text."""
        selected_option = self.dropdown_elements.first.locator("option:checked").inner_text()
        logger.info(f"Current selected option: {selected_option}")
        return selected_option
    
    def select_option(self, option_text: str):
        """Selects an option from the dropdown based on visible text."""
        logger.info(f"Selecting option: {option_text}")
        self.dropdown_elements.first.select_option(label=option_text)
        logger.info(f"Option '{option_text}' selected.")