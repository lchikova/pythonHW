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

driver.get('http://the-internet.herokuapp.com/inputs')

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

input_field.send_keys("Sky")
sleep(1)

input_field.clear()
sleep(1)

input_field.send_keys("Pro")
sleep(5)

driver.quit()
