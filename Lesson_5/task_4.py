from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

geckodriver_path = r'C:\geckodriver.exe'

firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

options = Options()
options.binary_location = firefox_binary_path

service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get('http://the-internet.herokuapp.com/login')

username = driver.find_element(By.ID, 'username')
username.send_keys('tomsmith')

password = driver.find_element(By.ID, 'password')
password.send_keys('SuperSecretPassword!')

login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()
sleep(2)

flash_message = driver.find_element(By.ID, 'flash').text
print("Сообщение системы:", flash_message.split('\n')[0])

driver.quit()
