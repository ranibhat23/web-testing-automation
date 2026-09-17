from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.config import BASE_URL, STANDARD_USER, PASSWORD


def test_complete_checkout(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        STANDARD_USER,
        PASSWORD
    )

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.enter_customer_details(
        "Rani",
        "Raviraj",
        "2000"
    )

    checkout_page.continue_checkout()
    checkout_page.complete_order()

    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )