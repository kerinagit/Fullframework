import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://demoblaze.com")
LogIn = driver.find_element(By.ID,"login2")
LogIn.click()
# time.sleep(5)
driver.implicitly_wait(10)
loginUsername = driver.find_element(By.ID,"loginusername")
loginUsername.send_keys("testmorning")
loginPassword = driver.find_element(By.ID,"loginpassword")
loginPassword.send_keys("test123")
Button = driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
Button.click()