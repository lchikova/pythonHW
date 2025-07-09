from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[text()='{}']"

    def open(self):
        self.driver.get("https://bonigarcia.dev"
                        "/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    def click_button(self, button_text):
        button_locator = (By.XPATH, self.button_locator.format(button_text))
        self.driver.find_element(*button_locator).click()
        return self

    def get_result(self, timeout=46):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text
