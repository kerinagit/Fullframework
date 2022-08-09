import time
import unittest
from Locators.Drivers import drivers
from Locators.locators import Base
from Pages.loginpage import Login
from ddt import ddt,data, unpack
from Utilities.datadriventesting import Utils

@ddt

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        dr = drivers()
        base = Base()
        self.driver = dr.newdriver
        driver = self.driver
        driver.maximize_window()
        driver.get(base.URL)

    @data(*Utils.read_data_from_excel("D:\\PythonCourse\\eveningautomation\\testdata\\Username_data.xlsx","Sheet1"))
    @unpack
    def test_login(self,Username,Password):
        lp = Login(self.driver)
        lp.login(Username,Password)
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()

