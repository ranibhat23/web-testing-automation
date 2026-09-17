from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):

    BACKPACK_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    BACKPACK_REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)

    def remove_backpack_from_cart(self):
        self.click(self.BACKPACK_REMOVE_BUTTON)

    def open_cart(self):
        self.click(self.CART_LINK)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)