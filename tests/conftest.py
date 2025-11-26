import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_configure(config):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    if not os.path.exists("reports"):
        os.makedirs("reports")