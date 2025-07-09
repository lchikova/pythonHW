from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.item_locator = ("//div[text()='{}']"
                             "/ancestor::div[@class='inventory_item']//button")

    def add_item_to_cart(self, item_name):
        item_xpath = (By.XPATH, self.item_locator.format(item_name))
        self.driver.find_element(*item_xpath).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        from Lesson_7.task2.pages.cart_page import CartPage
        return CartPage(self.driver)
