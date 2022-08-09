import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
URL = "http://demo.automationtesting.in/Alerts.html"
driver.maximize_window()
driver.get(URL)
AlertWithOk = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
AlertWithOk.click()
Button = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
Button.click()
time.sleep(5)
driver.switch_to.alert.send_keys("Usha")
driver.switch_to.alert.accept()