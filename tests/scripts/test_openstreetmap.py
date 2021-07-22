import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestOpenstreetmap(BaseTest):
    def test_openstreetmap(self):
        logger.info("test openstreetmap started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(5)

    def test_register(self):
        logger.info("test register started")
        WebDriverWait(self.driver, 2)
        self.open_registration()
        sleep(2)
        field_list = ["email", "email_confirmation", "display_name", "password", "confirm_password", "signup"]
        for i in field_list:
            if (i == "signup"):
                self.site_navigator(i).click()
                sleep(2)
            else:
                self.site_navigator(i).fill()
                sleep(2)
        sleep(5)
    def test_register_2(self):
        WebDriverWait(self.driver, 2)
        sleep(2)
        field_list = ["country", "contributor_terms", "agree", "public_domain", "continue"]
        for i in field_list:
            if(i == "country"):
                self.site_navigator(i, opt=True).click()
            else:
                self.site_navigator(i).click()
            sleep(2)
        sleep(5)

