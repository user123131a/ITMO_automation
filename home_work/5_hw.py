from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID,"user-name")

password_field = driver.find_element(By.ID, "password")

submit_button = driver.find_element(By.CSS_SELECTOR, ".btn_action")

if username_field and password_field and submit_button is None:
    print('элементы не найдены')
else:
    print('элементы найдены')
