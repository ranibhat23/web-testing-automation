from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product_to_cart():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        inventory_page = InventoryPage(driver)

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_count() == "1"

    finally:
        driver.quit()