import time
import unittest
from Pages.contact import Contacts
from Pages.loginpage import Login
from Locators.Drivers import drivers
from Locators.locators import Base


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        dr = drivers()
        base = Base()
        self.driver = dr.newdriver
        driver = self.driver
        driver.maximize_window()
        driver.get(base.URL)

    def test_something(self):
        lp = Login(self.driver)
        lp.login("testmorning", "test123")
        time.sleep(5)
        cc = Contacts(self.driver)
        cc.contactpage("test@test.com","test","next message")

    def test_contact(self):
        Contacts(self.driver).contactpage("test@test.com","test","next message")



if __name__ == '__main__':
    unittest.main()
