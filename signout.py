def test_signOff(self):
    self.driver.find_element_by_xpath("//a[@href='mercurysignoff.php']").click()

def test_verifySignedOut(self):
    self.driver.find_element_by_xpath("//img[@src='/images/masts/mast_signon.gif']")
    self.signofmessage = self.driver.title
    print(self.signofmessage)
    if "Sign-on" in self.signofmessage:
        print("Test Case is Passed")
    else:
        print("Test Case is Failed")

