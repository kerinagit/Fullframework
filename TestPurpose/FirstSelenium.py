from selenium import webdriver

driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://demoblaze.com")
driver.quit()