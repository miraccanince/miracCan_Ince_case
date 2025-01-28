import pytest
from pages.home_page import HomePage
from selenium.common.exceptions import WebDriverException
import logging
logger = logging.getLogger(__name__)

def test_home_page_title(driver):
    """
    Test to verify the homepage is opened and the title contains 'Insider'.
    Fulfills Requirement 1.
    """
    home_page = HomePage(driver)
    try:
        home_page.load()
        assert "Insider" in home_page.get_title(), "Title does not contain 'Insider'"
    except WebDriverException as e:
        # Handle browser-related errors gracefully
        driver.save_screenshot("screenshots/test_home_page_title_failure.png")
        raise e
