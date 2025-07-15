import pytest
import allure
from selenium import webdriver
from Lesson_10.pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Тесты калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверка работы калькулятора "
                    "с установленной задержкой вычислений")
def test_calculator_with_delay(browser):
    with allure.step("Открыть калькулятор и установить задержку"):
        calculator = CalculatorPage(browser).open()
        calculator.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        (calculator
         .click_button("7")
         .click_button("+")
         .click_button("8")
         .click_button("="))

    with allure.step("Проверить результат"):
        result = calculator.get_result("15")
        assert result == "15", f"Ожидаемый результат 15, но получили {result}"
