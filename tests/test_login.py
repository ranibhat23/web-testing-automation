from pages.login_page import LoginPage
from utils.config import (
    BASE_URL,
    STANDARD_USER,
    PASSWORD,
    LOCKED_OUT_USER
)


def test_valid_login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        STANDARD_USER,
        PASSWORD
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        STANDARD_USER,
        "wrong_password"
    )

    assert "Username and password do not match" in (
        login_page.get_error_message()
    )


def test_locked_out_user(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        LOCKED_OUT_USER,
        PASSWORD
    )

    assert "locked out" in (
        login_page.get_error_message()
    )