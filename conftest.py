import pytest
from utils.browser_setup import get_driver
import logging
from logging.handlers import RotatingFileHandler
import os


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Fixture to initialize and quit the WebDriver."""
    browser_name = request.param
    print(f"Initializing driver for {browser_name}...")
    try:
        driver = get_driver(browser_name)
        driver.maximize_window()
        yield driver
    except Exception as e:
        pytest.fail(f"Failed to set up {browser_name} driver: {e}")
    finally:
        driver.quit()
        print(f"Closed {browser_name} driver.")


def pytest_configure(config):
    # Ensure the logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Set up log rotation
    log_file = "logs/test_automation.log"
    log_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB per log file
        backupCount=5,  # Keep up to 5 backup log files
    )
    log_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    log_handler.setLevel(logging.INFO)

    # Add console logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    console_handler.setLevel(logging.INFO)

    # Set up the root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[log_handler, console_handler],  # File + Console
    )