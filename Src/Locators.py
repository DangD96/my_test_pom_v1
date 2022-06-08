from selenium.webdriver.common.by import By


class HomePageLocators(object):
    COMPANY_TAB = (By.CSS_SELECTOR, "div[class*='lvl-0 dropdown headerLang']")
    CONTACT_US_LINK = (By.CSS_SELECTOR, "a[href='https://phptravels.com/contact-us/']")


class ContactUsPageLocators(object):
    CONTACT_INFO_SECTION = (By.CSS_SELECTOR, "div.panel-body")