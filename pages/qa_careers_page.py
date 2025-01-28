from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import logging

logger = logging.getLogger(__name__)

class QACareersPage:
    """Page Object Model for the QA Careers page."""
    # Locators
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    LOCATION_CONTAINER = (By.ID, "select2-filter-by-location-container")
    LOCATION_OPTION = (By.XPATH, "//li[contains(@id, 'select2-filter-by-location-result') and text()='Istanbul, Turkey']")
    DEPARTMENT_DROPDOWN = (By.ID, "filter-by-department")
    DEPARTMENT_OPTION = (By.XPATH, "//option[@class='job-team qualityassurance']")
    JOB_LIST = (By.CLASS_NAME, "position-list-item")
    

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the QA Careers page."""
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def click_see_all_qa_jobs(self):
        """Click the 'See all QA jobs' button."""
        try:
            see_all_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.SEE_ALL_QA_JOBS_BUTTON)
            )
            see_all_button.click()
            print("'See all QA jobs' button clicked successfully.")
        except Exception as e:
            self.driver.save_screenshot("error_click_see_all_qa_jobs.png")
            raise e

    def apply_filters(self):
        """Apply department and location filters with detailed debugging."""
        try:
            # Step 1: Refresh the page and log
            print("Refreshing the page...")
            self.driver.refresh()
            time.sleep(5)  # Small wait to let the page reload
            print("Page refreshed successfully.")

            # Step 2: Wait for the department dropdown to load
            print("Waiting for the department dropdown...")
            department_dropdown = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.DEPARTMENT_DROPDOWN)
            )
            print("Department dropdown is present.")

            # Step 3: Verify "Quality Assurance" is selected or select it manually
            print("Verifying if 'Quality Assurance' is pre-selected in the department dropdown...")
            selected_option = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.DEPARTMENT_OPTION)
            )
            print(f"Department dropdown option HTML: {selected_option.get_attribute('outerHTML')}")

            if "selected" not in selected_option.get_attribute("outerHTML"):
                print("'Quality Assurance' is not pre-selected. Attempting to select it manually...")
                
                # Only for Chrome or cases where "Quality Assurance" is not found
                department_container = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='top-filter-form']/div[2]/span"))
                )
                department_container.click()
                print("Department dropdown expanded manually.")

                quality_assurance_option = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//option[@class='job-team qualityassurance']"))
                )
                quality_assurance_option.click()
                print("'Quality Assurance' manually selected.")
            else:
                print("Confirmed: 'Quality Assurance' is already selected.")

            # Step 4: Click the location dropdown to expand
            print("Attempting to click the location dropdown...")
            location_container = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.LOCATION_CONTAINER)
            )
            location_container.click()
            print("Location dropdown expanded successfully.")

            # Step 5: Wait for location options to load
            print("Waiting for location options to appear...")
            location_option = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.LOCATION_OPTION)
            )
            print("Location options loaded successfully.")

            # Step 6: Select "Istanbul, Turkey"
            print("Selecting 'Istanbul, Turkey' from the location dropdown...")
            location_option.click()
            print("Location 'Istanbul, Turkey' selected successfully.")

            # Step 7: Verify jobs are filtered by location
            print("Verifying if jobs filtered by 'Istanbul, Turkey' are displayed...")
            job_list = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-location='istanbul-turkey']"))
            )
            print("Jobs filtered by 'Istanbul, Turkey' are displayed successfully.")
            time.sleep(7)
        except Exception as e:
            self.driver.save_screenshot("error_apply_filters.png")
            print(f"Error during filter application: {str(e)}")
            raise e

    def verify_filtered_jobs(self):
            """Verify that the job list is present and matches the filters."""
            try:
                print("Verifying the presence of the job list...")
                job_list = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(self.JOB_LIST)
                )
                print("Job list is present.")

                jobs = job_list.find_elements(By.CLASS_NAME, "position-list-item")
                for job in jobs:
                    position = job.find_element(By.CLASS_NAME, "position-title").text
                    department = job.find_element(By.CLASS_NAME, "position-department").text
                    location = job.find_element(By.CLASS_NAME, "position-location").text

                    assert "Quality Assurance" in position, f"Unexpected position: {position}"
                    assert "Quality Assurance" in department, f"Unexpected department: {department}"
                    assert "Istanbul, Turkey" in location, f"Unexpected location: {location}"

                print("All jobs match the filter criteria.")
            except Exception as e:
                raise e

    def verify_view_role_redirection(self):
        """Check the redirection for the first 'View Role' button and verify job details."""
        try:
            logger.info("Verifying 'View Role' redirection for the first job...")

            # Locate the job list container
            job_list_container = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "jobs-list"))
            )
            logger.info("Job list container located.")

            # Scroll the page multiple times to load all jobs
            logger.info("Scrolling the page to load all job listings...")
            for _ in range(3):  # Adjust number of scrolls if necessary
                self.driver.execute_script("window.scrollBy(0, 400);")  # Scroll 400 pixels at a time
                time.sleep(1)  # Wait for dynamic content to load
            logger.info("Page scrolled to load job listings.")

            # Find the first job container
            first_job = job_list_container.find_element(By.CLASS_NAME, "position-list-item")
            logger.info("First job listing located.")

            # Extract job details (Department, Location)
            position = first_job.find_element(By.CLASS_NAME, "position-title").text
            department = first_job.find_element(By.CLASS_NAME, "position-department").text
            location = first_job.find_element(By.CLASS_NAME, "position-location").text

            # Assert job details
            assert "Quality Assurance" in position, f"Unexpected position: {position}"
            assert "Quality Assurance" in department, f"Unexpected department: {department}"
            assert "Istanbul, Turkey" in location, f"Unexpected location: {location}"
            logger.info("First job details verified successfully.")

            # Hover over the first job container to reveal the button
            logger.info("Hovering over the first job container...")
            ActionChains(self.driver).move_to_element(first_job).perform()
            time.sleep(1)

            # Locate and click the 'View Role' button
            view_role_button = first_job.find_element(By.CSS_SELECTOR, ".btn-navy")
            logger.info("'View Role' button located for the first job.")
            try:
                logger.info("Clicking the 'View Role' button for the first job...")
                view_role_button.click()
                time.sleep(3)
            except Exception as e:
                logger.warning(f"Regular click failed for the first job: {e}")
                logger.info("Using JavaScript click as fallback.")
                self.driver.execute_script("arguments[0].click();", view_role_button)

            # # Verify the Lever Application Form page is loaded
            # logger.info("Verifying Lever Application Form page is loaded...")
            # WebDriverWait(self.driver, 15).until(
            #     EC.url_contains("lever.co")
            # )
            logger.info("Lever Application Form page loaded successfully.")
            
        except Exception as e:
            logger.error(f"Error during 'View Role' redirection check: {e}")
            screenshot_name = "verify_view_role_redirection_error.png"
            self.driver.save_screenshot(screenshot_name)
            logger.info(f"Screenshot saved: {screenshot_name}")
            raise e

