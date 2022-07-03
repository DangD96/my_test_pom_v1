# Good practice to name class after file name
# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1")

# from selenium.webdriver.common.by import By
from Src.Locators import HomePageLocators


# Capitalize class name
class HomePage(object):
    # Locators for page elements
    def __init__(self, driver):
        # The * here unpacks the contents of the tuple and removes any commas or quotes
        self.company_tab = driver.find_element(*HomePageLocators.COMPANY_TAB)
        self.contact_us = driver.find_element(*HomePageLocators.CONTACT_US_LINK)

    # Methods for this page
    def clickCompanyTab(self):
        self.company_tab.click()

    def clickContactUs(self):
        self.contact_us.click()
