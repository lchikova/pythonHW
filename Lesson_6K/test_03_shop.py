import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_saucedemo_checkout(browser):
    browser.get("https://www.saucedemo.com/")

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = (f"//div[text()='{item_name}']"
                      f"/ancestor::div[@class='inventory_item']//button")
        browser.find_element(By.XPATH, item_xpath).click()

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    browser.find_element(By.ID, "checkout").click()

    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    browser.find_element(By.ID, "continue").click()

    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    total_amount = total_text.split("$")[1]

    assert total_amount == "58.29", \
        f"Ожидалась сумма $58.29, получено ${total_amount}"
