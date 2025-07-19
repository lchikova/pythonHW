from selenium.webdriver.common.by import By
import allure
from .main_page import MainPage


class LoginPage:
    def __init__(self, driver):
        """Инициализация страницы входа.

                Args:
                    driver: WebDriver экземпляр браузера
                """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу входа")
    def open(self):
        """Открывает страницу входа.

               Returns:
                   LoginPage: текущий экземпляр страницы
               """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести логин '{username}'")
    def enter_username(self, username):
        """Вводит имя пользователя.

                Args:
                    username (str): имя пользователя

                Returns:
                    LoginPage: текущий экземпляр страницы
                """
        self.driver.find_element(*self.username_field).send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Вводит пароль.

        Args:
            password (str): пароль

        Returns:
            LoginPage: текущий экземпляр страницы
        """
        self.driver.find_element(*self.password_field).send_keys(password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self):
        """Выполняет вход в систему.

               Returns:
                   MainPage: экземпляр главной страницы
               """
        self.driver.find_element(*self.login_button).click()
        return MainPage(self.driver)
