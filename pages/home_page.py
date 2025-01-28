from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logger = logging.getLogger(__name__)
class HomePage:
    """Page Object Model for the Insider homepage."""

    URL = "https://useinsider.com/"
    # Locators
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(),'Company')]")
    CAREERS_OPTION = (By.XPATH, "//a[@href='https://useinsider.com/careers/']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """Open the Insider homepage."""
        self.driver.get(self.URL)

    def navigate_to_careers_page(self):
        """Navigate to the Careers page via the Company dropdown."""
        try:
            # Wait for the Company dropdown to be clickable and click it
            company_menu = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COMPANY_MENU)
            )
            company_menu.click()

            # Wait for the dropdown menu to be visible
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdown-menu"))
            )

            # Wait for and click the Careers link
            careers_option = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.CAREERS_OPTION)
            )
            careers_option.click()
        except Exception as e:
            # Capture screenshot on failure
            self.driver.save_screenshot("error_navigate_to_careers.png")
            raise e
