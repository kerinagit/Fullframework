from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://demoblaze.com")
LogIn = driver.find_element(By.ID,"login2")
LogIn.click()
loginUsername = WW(driver,10).until(EC.presence_of_element_located((By.ID,"loginusername")))
loginUsername.send_keys("testmorning")
loginPassword = driver.find_element(By.ID,"loginpassword")
loginPassword.send_keys("test123")
Button = driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
Button.click()