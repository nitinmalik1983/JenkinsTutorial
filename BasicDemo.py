from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.ui import Select
import unittest
import pytest

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(6)
        cls.driver.maximize_window()

    def test_launchWebsite(self):
        self.driver.get("http://newtours.demoaut.com/")

    from login import test_loginIntoWebsite
    from signout import test_signOff
    from signout import test_verifySignedOut


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



if __name__ == '__main__':
    unittest.main()
