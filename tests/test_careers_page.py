import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_careers_page import QACareersPage
import logging

logger = logging.getLogger(__name__)

def test_careers_page_sections(driver):
    """
    Test to navigate to the Careers page and verify its sections.
    """
    # Navigate to the Careers page
    logging.info("Navigating to HomePage")
    home_page = HomePage(driver)
    home_page.load()
    logging.info("Navigating to Careers Page")
    home_page.navigate_to_careers_page()
    
    # Verify the Careers page sections
    careers_page = CareersPage(driver)
    assert careers_page.is_locations_section_present(), "Locations section is missing."
    assert careers_page.is_teams_section_present(), "Teams section is missing."
    assert careers_page.is_life_section_present(), "Life at Insider section is missing."
    logging.info("Careers Page is loaded successfully")

def test_filter_qa_jobs(driver):
    """Test to apply filters, verify jobs, and check 'View Role' redirection."""
    try:
        # Initialize the QA Careers page
        logging.info("Initializing the QA Careers page object...")
        qa_careers_page = QACareersPage(driver)

        # Step 1: Open the QA Careers page
        logging.info("Opening the QA Careers page...")
        qa_careers_page.open()

        # Step 2: Click the 'See all QA jobs' button
        logging.info("Clicking 'See all QA jobs' button...")
        qa_careers_page.click_see_all_qa_jobs()

        # Step 3: Apply department and location filters
        logging.info("Applying department and location filters...")
        qa_careers_page.apply_filters()

        # Step 4: Verify the filtered jobs
        logging.info("Verifying filtered jobs...")
        qa_careers_page.verify_filtered_jobs()

        # Step 5: Check 'View Role' redirection
        logging.info("Checking 'View Role' redirection for all jobs...")
        qa_careers_page.verify_view_role_redirection()

        logging.info("Test completed successfully.")

    except Exception as e:
        # Log failure and capture a screenshot
        logging.error(f"Test failed: {e}")
        raise e
