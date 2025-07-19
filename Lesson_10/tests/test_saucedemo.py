import pytest
import allure
from selenium import webdriver
from Lesson_10.pages.login_page import LoginPage


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный процесс оформления заказа")
@allure.description("Тест проверяет полный процесс оформления заказа с добавлением нескольких товаров")
def test_saucedemo_checkout(browser):
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    ITEMS_TO_ADD = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    FIRST_NAME = "Иван"
    LAST_NAME = "Петров"
    POSTAL_CODE = "123456"
    EXPECTED_TOTAL = "58.29"

    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(browser).open()
        main_page = (login_page
                     .enter_username(USERNAME)
                     .enter_password(PASSWORD)
                     .click_login())

    with allure.step("Добавление товаров в корзину"):
        for item in ITEMS_TO_ADD:
            main_page.add_item_to_cart(item)

    with allure.step("Оформление заказа"):
        cart_page = main_page.go_to_cart()
        checkout_page = cart_page.click_checkout()

        with allure.step("Заполнение данных доставки"):
            total_amount = (checkout_page
                          .fill_shipping_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
                          .click_continue()
                          .get_total_amount())

    with allure.step("Проверка итоговой суммы"):
        assert total_amount == EXPECTED_TOTAL, \
            f"Ожидалось {EXPECTED_TOTAL}, получено {total_amount}"
