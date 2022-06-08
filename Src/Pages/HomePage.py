# good practice to name class after file name
# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1")

# from selenium.webdriver.common.by import By
from Src.Locators import HomePageLocators


# capitalize class name
class HomePage(object): # removing object here doesn't seem to functionally change anything
    # locators for page elements
    def __init__(self, driver):
        # self.driver = driver --> not needed here
        self.company_tab = driver.find_element(*HomePageLocators.COMPANY_TAB)
        self.contact_us = driver.find_element(*HomePageLocators.CONTACT_US_LINK)
        # the * here unpacks the contents of the tuple and removes any commas or quotes - not sure why
        # this works with find_element

    # methods for this page
    def clickCompanyTab(self):
        self.company_tab.click()

    def clickContactUs(self):
        self.contact_us.click()
