import sys
sys.path.append("/Users/daviddang/python/my_test_pom_v1") #add my prj directory path to PATH so I can import stuff

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.Pages.HomePage import HomePage
from Src.Locators import HomePageLocators

class DemoHomePage(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")
        time.sleep(3)
        
        # Create an instance of the class so you can make use of the methods in the class
        home = HomePage(driver)

        #I guess checks can go in the main test file
        assert home.contact_us.is_displayed() == False

        #hover over company tab
        actions = ActionChains(driver) #need to create ActionChains object first
        actions.move_to_element(home.company_tab) #queue up action or actions
        actions.perform()
        time.sleep(1.5)

        #wait until contact us link is present
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(HomePageLocators.CONTACT_US_LINK), message = "Element doesn't exist") 
        #i guess this needs a tuple
        #if element really isn't there then an error will be thrown (NoSuchElementException)
        
        #check innerText (python)
        assert "Contact Us" in home.contact_us.get_attribute("innerText")

        #check innerText (javascript)
        #seems to need this format for argument[0]
        assert driver.execute_script("return arguments[0].innerText.includes('Contact Us');", home.contact_us) == True
        #return statement can only be used in a function so it guess .execute_script's argument is treated like a function
        
        #click contact us
        home.clickContactUs()
        time.sleep(3)

        #verify the URL (python)
        assert driver.current_url == "https://phptravels.com/contact-us/"

        #verify the URL (javascript)
        assert driver.execute_script("return window.location.href;") == "https://phptravels.com/contact-us/"
        time.sleep(1.5)

#runs the test case
if __name__ == '__main__':
    unittest.main()