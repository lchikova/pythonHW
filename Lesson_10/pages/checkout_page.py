from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """Инициализация страницы оформления заказа.

               Args:
                   driver: WebDriver экземпляр браузера
               """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию о доставке")
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Заполняет данные для доставки.

                Args:
                    first_name (str): имя
                    last_name (str): фамилия
                    postal_code (str): почтовый индекс

                Returns:
                    CheckoutPage: текущий экземпляр страницы
                """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        (self.driver.find_element(*self.postal_code_field).
         send_keys(postal_code))
        return self

    @allure.step("Продолжить оформление заказа")
    def click_continue(self):
        """Переходит к следующему шагу оформления.

               Returns:
                   CheckoutPage: текущий экземпляр страницы
               """
        self.driver.find_element(*self.continue_button).click()
        return self

    @allure.step("Получить итоговую сумму")
    def get_total_amount(self):
        """Получает итоговую сумму заказа.

                Returns:
                    str: итоговая сумма (только число)
                """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        return total_element.text.split("$")[1]
