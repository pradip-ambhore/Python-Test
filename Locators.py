import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Pradip")
time.sleep(3)
driver.find_element(By.NAME,"email").send_keys("Hello@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
time.sleep(3)
driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(3)
driver.find_element(By.ID,"inlineRadio1").click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(3)
dropdown.select_by_visible_text("Female")
dropdown.
time.sleep(3)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message


