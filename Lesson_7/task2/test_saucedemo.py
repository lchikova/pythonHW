import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


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

    login_page = LoginPage(browser).open()
    main_page = (login_page
                 .enter_username(USERNAME)
                 .enter_password(PASSWORD)
                 .click_login())

    for item in ITEMS_TO_ADD:
        main_page.add_item_to_cart(item)

    cart_page = main_page.go_to_cart()
    checkout_page = cart_page.click_checkout()

    total_amount = (checkout_page
                    .fill_shipping_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
                    .click_continue()
                    .get_total_amount())

    assert total_amount == EXPECTED_TOTAL, \
        f"Ожидалось {EXPECTED_TOTAL}, получено {total_amount}"
