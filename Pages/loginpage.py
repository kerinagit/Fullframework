from selenium.webdriver.common.by import By
from Locators.locators import locate
from Locators.Drivers import drivers
import logging
class Login:
    def __init__(self, driver):
        self.d = drivers
        self.driver = driver



    def login(self, username, password):
        lc = locate()
        driver = self.driver
        login = driver.find_element(By.ID,lc.LogIn)
        login.click()
        driver.implicitly_wait(10)
        Username = driver.find_element(By.ID, lc.Username)
        Username.send_keys(username)
        logging.info("This is entering username")
        Password = driver.find_element(By.ID, lc.Password)
        Password.send_keys(password)
        Button = driver.find_element(By.XPATH, lc.Button)
        Button.click()

