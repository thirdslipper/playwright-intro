
import re
import pytest
import random
from playwright.sync_api import expect, Page #Playwright, sync_playwright, 
from pages.js_alerts_page import JSAlertsPage

@pytest.mark.parametrize("count", [1])#, 2, 3])
def test_js_alerts(page: Page, count: int) -> None:
    jsalerts = JSAlertsPage(page)
    jsalerts.open()