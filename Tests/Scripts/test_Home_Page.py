#When chromdriver is out of date, have to download a new version of it and stick it in PATH.
#To figure out PATH varible, type this in command prompt: echo $PATH
#That command returns places where I can put chromedriver (colon delimited). I think the first spot is where python 
# checks first. If it finds an old chromedriver in the first location, it'll try to use it. Coincidentally the first
# hit from echo $PATH is where all the python config files are located too, so maybe it's supposed to go there
#I put my chromedriver in /Library/Frameworks/Python.framework/Versions/3.8/bin 
#Go to directory chromedriver downloaded to and then: sudo mv chromedriver /Library/Frameworks/Python.framework/Versions/3.8/bin
#Do sudo so you don't get denied permission
#Have to Cmd+Space to search for the location

import sys
sys.path.append("/Users/daviddang/python/my_test_pom_v1") #add my prj directory path to PATH so I can import stuff

import unittest
from selenium.webdriver.support.ui import WebDriverWait #using python interpreter /usr/local/bin/python3 --> 3.8.5 64-bit
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.Pages.HomePage import HomePage

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

        #wait until contact us link is present (v1) - relies on referencing Locator file
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located(HomePageLocators.CONTACT_US_LINK), message = "Element doesn't exist")
        #i guess this version needs a tuple
       

        #wait until (v2) - doesn't need to rely on referencing Locator file
        #this is better than v1 IMO because element_to_be_clickable can take a WebElement while presence_of_element_located can't
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(home.contact_us), message = "Did not find element.")
        #if element really isn't there then an error will be thrown (NoSuchElementException)

        #check innerText (python)
        assert "Contact Us" in home.contact_us.get_attribute("innerText")

        #check innerText (javascript)
        #seems to need this format for arguments[0]
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