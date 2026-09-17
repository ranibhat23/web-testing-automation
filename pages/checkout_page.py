from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    COMPLETE_MESSAGE = (
        By.CLASS_NAME,
        "complete-header"
    )

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def complete_order(self):
        self.wait.until(
            EC.url_contains("/checkout-step-two.html")
        )

        finish_button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        finish_button.click()

        self.wait.until(
            EC.presence_of_element_located(
                self.COMPLETE_MESSAGE
            )
        )

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_MESSAGE)