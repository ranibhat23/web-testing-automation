from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def create_driver():
    options = Options()
    options.add_argument("--headless")

    return webdriver.Chrome(options=options)


def test_valid_login():

    driver = create_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        assert "inventory" in driver.current_url

    finally:
        driver.quit()


def test_invalid_login():

    driver = create_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)

        login_page.login(
            "standard_user",
            "wrong_password"
        )

        error_message = driver.find_element(
            By.CSS_SELECTOR,
            "[data-test='error']"
        )

        assert "Username and password do not match" in error_message.text

    finally:
        driver.quit()