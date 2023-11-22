import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(3)
email = driver.find_element(By.XPATH,"//form/div[1]/input")
email.clear()
email.send_keys("pradipambhore85@gmail.com")
time.sleep(3)
password = driver.find_element(By.XPATH,"//form/div[2]/input")
password.clear()
password.send_keys("Pradip@321")
time.sleep(3)
confirmpass = driver.find_element(By.XPATH,"//form/div[3]/input")
confirmpass.clear()
confirmpass.send_keys("Pradip@321")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']")
time.sleep(3)

