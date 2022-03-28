import unittest
from selenium import webdriver

class WebDriverSetup(unittest.TestCase): #test case classes will inherit from this
    #setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) #seconds
        self.driver.maximize_window()

    #tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()