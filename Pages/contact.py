import time

from selenium.webdriver.common.by import By

from Locators.Drivers import drivers
from Locators.locators import locate


class Contacts:
    def __init__(self,driver):
        self.d = drivers
        self.driver = driver

    def contactpage(self,email,name,message,):
        lc = locate()
        driver = self.driver
        contact = driver.find_element(By.XPATH, lc.ContactURL)
        contact.click()
        time.sleep(5)
        Email = driver.find_element(By.ID, lc.EmailID)
        Email.send_keys(email)
        Name = driver.find_element(By.ID,lc.ContactName)
        Name.send_keys(name)
        Message = driver.find_element(By.ID,lc.Message)
        Message.send_keys(message)
        Button = driver.find_element(By.XPATH,lc.Button1)
        Button.click()
