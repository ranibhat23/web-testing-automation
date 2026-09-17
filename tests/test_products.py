from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, STANDARD_USER, PASSWORD


def login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        STANDARD_USER,
        PASSWORD
    )


def test_add_backpack_to_cart(driver):

    login(driver)

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_remove_backpack_from_cart(driver):

    login(driver)

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    inventory_page.remove_backpack_from_cart()

    assert not driver.find_elements(
        *inventory_page.CART_BADGE
    )