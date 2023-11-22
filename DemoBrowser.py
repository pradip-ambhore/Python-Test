import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# --- for chrome
# service_obj = Service(r"C:\Users\Pradip Ambhore\Documents\chromedriver.exe")
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver = webdriver.Edge()


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()


