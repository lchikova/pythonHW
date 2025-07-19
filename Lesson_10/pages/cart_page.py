from selenium.webdriver.common.by import By
import allure
from .checkout_page import CheckoutPage


class CartPage:
    def __init__(self, driver):
        """Инициализация страницы корзины.

               Args:
                   driver: WebDriver экземпляр браузера
               """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Начать оформление заказа")
    def click_checkout(self):
        """Начинает процесс оформления заказа.

               Returns:
                   CheckoutPage: экземпляр страницы оформления заказа
               """
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)
