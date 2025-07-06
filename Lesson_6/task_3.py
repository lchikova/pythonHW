from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 20).until(
    lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
)

def images_loaded(d):
    images = d.find_elements(By.CSS_SELECTOR, "#image-container img")
    if len(images) != 4:
        return False
    return all(img.get_attribute("complete") == "true" for img in images)

WebDriverWait(driver, 20).until(images_loaded)

images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
if len(images) >= 3:
    print(images[2].get_attribute("src"))

driver.quit()