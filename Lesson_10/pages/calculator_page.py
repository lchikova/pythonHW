from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """Инициализация страницы калькулятора.

                Args:
                    driver: WebDriver экземпляр браузера
                """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[text()='{}']"

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора.

               Returns:
                   CalculatorPage: текущий экземпляр страницы
               """
        self.driver.get("https://bonigarcia.dev"
                        "/selenium-webdriver-java/slow-calculator.html")
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds):
        """Устанавливает задержку вычислений.

                Args:
                    seconds (int/str): количество секунд задержки

                Returns:
                    CalculatorPage: текущий экземпляр страницы
                """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text):
        """Нажимает указанную кнопку калькулятора.

             Args:
                 button_text (str): текст на кнопке (например, '1', '+', '=')

             Returns:
                 CalculatorPage: текущий экземпляр страницы
             """
        button_locator = (By.XPATH, self.button_locator.format(button_text))
        self.driver.find_element(*button_locator).click()
        return self

    @allure.step("Получить результат вычислений")
    def get_result(self, expected_result, timeout=46):
        """Ожидает и возвращает результат вычислений.

                Args:
                    expected_result (str): ожидаемый результат
                    timeout (int): максимальное время ожидания в секундах

                Returns:
                    str: текст результата на экране калькулятора
                """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen,
                                             str(expected_result)))
        return self.driver.find_element(*self.screen).text
