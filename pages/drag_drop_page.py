from _pytest import mark
from playwright.sync_api import Page
import pytest
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)
PAGE_PATH = "drag_and_drop"


class DragdropPage(BasePage):
    def __init__(self, page: Page):
        """ This calls the BasePage's __init__ to set up self.page and self.base_url"""
        super().__init__(page) 
        # The page uses plain <header> elements inside .column divs
        # use a CSS locator instead of ARIA role 'columnheader'.
        self.drag_drop_elements = page.locator(".column")
        logger.info("DragdropPage initialized with drag and drop elements.")
        

    def open(self):
        """ Uses the navigate_to method from BasePage"""
        self.navigate_to(PAGE_PATH)
        logger.info(f"Navigating to page {PAGE_PATH}")
        # wait for the draggable elements to be present, then read its options
        self.drag_drop_elements.first.wait_for()

    def getState(self, elemnt: str) -> str:
        """Returns the current header text of the specified element."""
        header_text = self.drag_drop_elements.get_by_text(elemnt).locator("header").inner_text()
        logger.info(f"Current state of element '{elemnt}': {header_text}")
        return header_text

    def drag_and_drop(self, source: str, target: str):
        """Drags an element from source to target."""
        logger.info(f"Dragging element from {source} to {target}")
        source_element = self.drag_drop_elements.get_by_text(source)
        target_element = self.drag_drop_elements.get_by_text(target)
        source_element.drag_to(target_element)
        logger.info(f"Drag and drop action completed from {source} to {target}.")

    def drag_and_drop_setdist(self, source: str, target: str, dist_from_target_edge: float):
        """Moves source towards target but stops 49% of the way."""
        # 1. Get locators
        source_element = self.drag_drop_elements.get_by_text(source)
        target_element = self.drag_drop_elements.get_by_text(target)

        # 2. Get bounding boxes
        sb = source_element.bounding_box()
        tb = target_element.bounding_box()

        if not sb or not tb:
            logger.error("Could not find bounding boxes.")
            return

        # 3. Calculate Centers
        source_center = {"x": sb["x"] + sb["width"] / 2, "y": sb["y"] + sb["height"] / 2}
        target_center = {"x": tb["x"] + tb["width"] / 2, "y": tb["y"] + tb["height"] / 2}

        # 4. Calculate the '49% Point' along the vector
        # New Point = Start + (Distance * Percentage)
        # One issue that may not be accounted for is the "white space" where its past 50%~59% of the 
        # square but doesn't trigger coluimn over to allow drag and drop
        dest_x = source_center["x"] + (target_center["x"] - source_center["x"]) * dist_from_target_edge
        dest_y = source_center["y"] + (target_center["y"] - source_center["y"]) * dist_from_target_edge

        # 5. Perform the Mouse Actions
        self.page.mouse.move(source_center["x"], source_center["y"])
        self.page.mouse.down()
        
        # Adding 'steps' makes the movement visible in headed mode
        self.page.mouse.move(dest_x, dest_y) 
        
        # Optional: A tiny sleep here lets you see the 'held' state during debugging
        # self.page.wait_for_timeout(500) 
        
        self.page.mouse.up()
        logger.info(f"Partial drag from {source} completed at {dist_from_target_edge * 100:.0f} path.")