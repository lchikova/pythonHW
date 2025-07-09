from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        from Lesson_7.task2.pages.main_page import MainPage
        return MainPage(self.driver)
