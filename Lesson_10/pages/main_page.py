from selenium.webdriver.common.by import By
import allure
from .cart_page import CartPage


class MainPage:
    def __init__(self, driver):
        """Инициализация главной страницы.

              Args:
                  driver: WebDriver экземпляр браузера
              """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.item_locator = ("//div[text()='{}']"
                             "/ancestor::div[@class='inventory_item']//button")

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name):
        """Добавляет товар в корзину.

                Args:
                    item_name (str): название товара

                Returns:
                    MainPage: текущий экземпляр страницы
                """
        item_xpath = (By.XPATH, self.item_locator.format(item_name))
        self.driver.find_element(*item_xpath).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Переходит на страницу корзины.

               Returns:
                   CartPage: экземпляр страницы корзины
               """
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)
