from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.config import BASE_URL, STANDARD_USER, PASSWORD

def test_cart_contains_selected_product(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        STANDARD_USER,
        PASSWORD
    )

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    print("Cart badge:", inventory_page.get_cart_count())

    inventory_page.open_cart()

    print("Current URL:", driver.current_url)

    cart_page = CartPage(driver)

    print("Cart items:", cart_page.get_number_of_items())

    assert cart_page.get_number_of_items() == 1