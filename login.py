import time
from selenium.webdriver.support.ui import Select

def test_loginIntoWebsite(self):
    self.driver.find_element_by_name("userName").send_keys("test2282")
    self.driver.find_element_by_name("password").send_keys("test2282")
    self.driver.find_element_by_name("login").click()
    self.driver.find_element_by_xpath("//a[@href='mercuryreservation.php']").click()
    time.sleep(2)
    self.driver.find_element_by_xpath("//input[@type='radio' and @name='tripType' and @value='oneway']").click()
    self.passenger = Select(self.driver.find_element_by_name("passCount"))
    self.passenger.select_by_index(2)
    time.sleep(2)
    departfrom = Select(self.driver.find_element_by_name("fromPort"))
    departfrom.select_by_visible_text("Frankfurt")
    time.sleep(2)
    self.driver.find_element_by_name("findFlights").click()
    time.sleep(4)
    


