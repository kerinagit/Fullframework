from selenium.webdriver.common.by import By
from Locators.locators_place import locatorscode
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException


class currency:
    def currencypage(self):
        lc = locatorscode()
        self.driver = webdriver.Chrome(lc.path)
        driver = self.driver
        driver.get(lc.url)
        driver.maximize_window()
        try:
            currency_dropdown = driver.find_element(By.XPATH, lc.currencyDropdown)
            currency_dropdown.click()
            pound = driver.find_element(By.XPATH, lc.pound)
            pound.click()
            time.sleep(5)
            ActionChains(driver).scroll(0, 0, 0, 500).perform()
            time.sleep(5)
            ActionChains(driver).scroll(0, 0, 0, -500).perform()
            time.sleep(5)
            product = driver.find_element(By.XPATH, lc.product)
            product.click()
            productitem = driver.find_element(By.XPATH, lc.productItem)
            productitem.click()
            addTocart = driver.find_element(By.XPATH, lc.addToCart)
            addTocart.click()
            time.sleep(15)
            shoppingCart = driver.find_element(By.XPATH,lc.shoppingCart)
            shoppingCart.click()
            time.sleep(5)
        except NoSuchElementException:
            print('This is no such element')
        except ElementNotInteractableException:
            print("This is in exception")

        except ElementClickInterceptedException:
            print("Element is not clickable")