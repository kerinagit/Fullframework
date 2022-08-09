from selenium import webdriver
from Locators.locators import Base
class drivers:
    lb = Base()
    newdriver = webdriver.Chrome(lb.path)