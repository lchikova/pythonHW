from selenium.webdriver.common.by import By
import allure
from .main_page import MainPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу входа")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести логин '{username}'")
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        return MainPage(self.driver)
