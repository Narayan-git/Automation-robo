import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestUnsplash(BaseTest):
    def test_unsplash(self):
        logger.info("test unsplash started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(2)

    def test_register(self):
        logger.info("test unsplash register ")
        sleep(2)
        field_list = ["join", "first_name", "last_name", "user_name", "email", "password", "register"]
        for i in field_list:
            if (i == "join" or i == "register"):
                self.site_navigator(i).click()
                sleep(5)
            else:
                self.site_navigator(i).fill()
            sleep(2)
        sleep(3)

    # def test_Login(self):
    #     logger.info("test unsplash login")
    #     field_list = ["login_page", "email", "password", "login"]
    #     for i in field_list:
    #         if (i == "login_page" or i == "login"):
    #             self.site_navigator(i).click()
    #             sleep(3)
    #         else:
    #             self.site_navigator(i).fill()
    #         sleep(1)
    #     sleep(5)