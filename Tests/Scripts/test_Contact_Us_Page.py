# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1") #add my prj directory path to PATH so I can import stuff

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.Pages.ContactUsPage import ContactUsPage
from Src.Locators import ContactUsPageLocators


class DemoContactPage(WebDriverSetup):

    def test_contact_page(self):
        driver = self.driver
        driver.get("https://phptravels.com/contact-us/")
        time.sleep(3)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ContactUsPageLocators.CONTACT_INFO_SECTION),
                                       message = "Element doesn't exist")
        
        contact = ContactUsPage(driver)
        
        try:
            assert "Email" and "Skype" in contact.getContactInfo()
            # assert "Email" in ContactUsPage(driver).getContactInfo() --> also works if you don't want to instantiate
        except AssertionError:
            print("Assertion failed.")


if __name__ == '__main__':
    unittest.main()