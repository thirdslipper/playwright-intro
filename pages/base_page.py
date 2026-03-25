from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://the-internet.herokuapp.com"
        # Common elements across ALL pages
        self.footer_link = page.get_by_role("link", name="Elemental Selenium")

    def navigate_to(self, endpoint: str):
        """Centralized navigation logic."""
        self.page.goto(f"{self.base_url}/{endpoint}")

    def get_header_text(self):
        """Generic helper to get the H3 header most of these pages use."""
        return self.page.locator("h3").inner_text()

    def wait_for_load(self):
        """A common place to put 'wait' logic if the site is slow."""
        self.page.wait_for_load_state("networkidle")