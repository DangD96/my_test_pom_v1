# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1")

from selenium.webdriver.common.by import By
from Src.Locators import ContactUsPageLocators


class ContactUsPage(object):
    # Locators for this page
    def __init__(self, driver):
        # The * here unpacks the contents of the tuple and removes any commas or quotes
        self.contact_info = driver.find_element(*ContactUsPageLocators.CONTACT_INFO_SECTION) 

    # Methods for this page
    def getContactInfo(self):
        return self.contact_info.text
