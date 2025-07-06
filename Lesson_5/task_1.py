from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver_path = r'C:\chromedriver\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get('http://uitestingplayground.com/classattr')

blue_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
blue_button.click()
sleep(5)
alert = Alert(driver)
sleep(2)
alert.accept()
sleep(2)
driver.quit()