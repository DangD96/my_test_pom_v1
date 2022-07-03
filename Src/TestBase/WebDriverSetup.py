import unittest
from selenium import webdriver


# Test case classes will inherit from this
class WebDriverSetup(unittest.TestCase):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10) #seconds
        self.driver.maximize_window()

    # Tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()
