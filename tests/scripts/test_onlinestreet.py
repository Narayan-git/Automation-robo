import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestOnlinestreet(BaseTest):
    def test_onlinestreet(self):
        logger.info("test onlinestreet started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        self.site_navigator("entercompany").click()
        sleep(2)

    def test_register(self):
        logger.info("test onlinestreet register company Step 1")
        sleep(2)
        field_list = ["website", "next1", "role", "first_name", "sur_name", "email",
                      "title", "description", "road", "house_number", "zip", "place", "telephone",
                      "main_catagory1", "main_catagory2", "send"]
        for i in field_list:
            if (i == "next1" or i == "send" or i == "role"):
                self.site_navigator(i).click()
                sleep(5)
            else:
                self.site_navigator(i).fill()
            sleep(2)