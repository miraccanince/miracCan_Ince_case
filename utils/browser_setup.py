from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

def get_driver(browser_name="chrome"):
    """Set up the WebDriver for Chrome or Firefox using local drivers."""
    # Define paths to the drivers
    project_root = os.path.dirname(os.path.abspath(__file__))
    chrome_driver_path = os.path.join(project_root, "../chromedriver.exe")
    firefox_driver_path = os.path.join(project_root, "../geckodriver.exe")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(chrome_driver_path))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(firefox_driver_path))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    return driver
