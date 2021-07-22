import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestAdresse(BaseTest):

    def test_adresse(self):
        logger.info("test adresse started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(5)
        self.accept_cookies()

    def test_register(self):
        logger.info("test register started")
        WebDriverWait(self.driver, 2)
        self.open_registration()
        sleep(5)
        self.site_navigator("clickregister").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        field_list = ["zip", "company_name", "street", "house_number", "contact_type",
                      "phone_number", "email", "url"]
        for i in field_list:
            if (i == "contact_type"):
                self.select_tag(i)
                sleep(2)
            else:
                self.site_navigator(i).fill()
                sleep(2)
        try:
            sleep(2)
            self.site_navigator("next").click()
            print("next successfully")
        except:
            logger.info("No Deny found")
            print("next failure")
        sleep(10)
        self.driver.quit()

