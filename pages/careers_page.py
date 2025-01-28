from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logger = logging.getLogger(__name__)

class CareersPage:
    """Page Object Model for the Careers page."""
    # Locators
    LOCATIONS_SECTION = (By.ID, "career-our-location")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LIFE_SECTION = (By.XPATH, "//h2[text()='Life at Insider']")  # Use text-based locator for clarity

    def __init__(self, driver):
        self.driver = driver

    def is_section_visible(self, locator, screenshot_name):
        """Check if a section is visible on the page and take a screenshot if not."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            # Capture screenshot if the section is not visible
            self.driver.save_screenshot(screenshot_name)
            print(f"Error: {e}")
            return False

    def is_locations_section_present(self):
        """Check if the Locations section is present."""
        return self.is_section_visible(self.LOCATIONS_SECTION, "error_locations_section.png")

    def is_teams_section_present(self):
        """Check if the Teams section is present."""
        return self.is_section_visible(self.TEAMS_SECTION, "error_teams_section.png")

    def is_life_section_present(self):
        """Check if the Life at Insider section is present."""
        return self.is_section_visible(self.LIFE_SECTION, "error_life_section.png")
