from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    CART_ITEMS = (
        By.CLASS_NAME,
        "cart_item"
    )

    def get_number_of_items(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)