from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
page_url = 'https://www.saucedemo.com/'

driver.get(page_url)

username = 'standard_user'
password = 'secret_sauce'

driver.find_element(By.ID, 'user-name').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'login-button').click()