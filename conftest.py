import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_dir = os.path.join(
                "reports",
                "screenshots"
            )

            os.makedirs(
                screenshot_dir,
                exist_ok=True
            )

            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)