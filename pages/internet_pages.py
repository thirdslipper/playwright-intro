from playwright.sync_api import Page

class AddRemovePage:
    def __init__(self, page: Page):
        self.page = page
        # Define locators here
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_buttons = page.locator("button.added-manually")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    def add_elements(self, count: int):
        for _ in range(count):
            self.add_button.click()

    def remove_all_elements(self):
        # Clicks the first "Delete" button until none are left
        while self.delete_buttons.count() > 0:
            self.delete_buttons.first.click()