# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1")

from selenium.webdriver.common.by import By
from Src.Locators import ContactUsPageLocators


class ContactUsPage(object):
    # locators for this page
    def __init__(self, driver):
        self.contact_info = driver.find_element(*ContactUsPageLocators.CONTACT_INFO_SECTION) 
        # the * here unpacks the contents of the tuple and removes any commas or quotes

    # methods for this page
    def getContactInfo(self):
        return self.contact_info.text