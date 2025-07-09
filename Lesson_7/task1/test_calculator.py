import pytest
from selenium import webdriver
from Lesson_7.task1.pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_with_delay(browser):
    calculator = CalculatorPage(browser).open()

    (calculator
     .set_delay(45)
     .click_button("7")
     .click_button("+")
     .click_button("8")
     .click_button("="))

    result = calculator.get_result()
    assert result == "15", f"Ожидаемый результат 15, но получили {result}"
