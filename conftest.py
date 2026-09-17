import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SCREENSHOT_DIR = os.path.join("reports", "screenshots")


@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


def pytest_sessionstart(session):
    """Create the screenshot directory before tests start."""

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_path = os.path.join(
                SCREENSHOT_DIR,
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)