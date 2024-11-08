import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "100.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    browser.config.driver_name = "chrome"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
