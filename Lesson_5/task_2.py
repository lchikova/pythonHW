from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r'C:\chromedriver\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get('http://uitestingplayground.com/dynamicid')

blue_button = driver.find_element(By.CSS_SELECTOR,
                                  'button.btn-primary[type="button"]')
blue_button.click()
button_id = blue_button.get_attribute('id')
print(f"Текущий ID кнопки: {button_id}")

driver.quit()
