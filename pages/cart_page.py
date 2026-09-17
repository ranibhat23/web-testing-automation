from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        items = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_ITEMS
            )
        )
        return len(items)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "first-name")
            )
        )