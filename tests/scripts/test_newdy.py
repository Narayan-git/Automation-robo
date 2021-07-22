import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestNewdy(BaseTest):
    def test_newdy(self):
        logger.info("test newdy started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(4)
        self.accept_cookies()
        sleep(2)

    def test_submitWebpage(self):
        logger.info("test newdy register webpage")
        self.site_navigator("free_web").click()
        sleep(2)
        field_list = ["category", "url", "title", "description", "email", "submit"]
        for i in field_list:
            if (i == "submit"):
                sleep(10)
                self.site_navigator(i).click()
                sleep(2)
            elif (i == "category"):
                self.site_navigator(i, opt=True).click()
                sleep(3)
            else:
                self.site_navigator(i).clear()
                sleep(1)
                self.site_navigator(i).fill()
            sleep(1)
        self.site_navigator('back').click()
        sleep(3)
    def test_submitPicture(self):
        logger.info("test newdy login")
        self.site_navigator("free_image").click()
        sleep(2)
        field_list = ["url", "title", "description", "email", "submit"]
        for i in field_list:
            if (i == "submit"):
                sleep(10)
                self.site_navigator(i).click()
                sleep(2)
            else:
                self.site_navigator(i).clear()
                sleep(1)
                self.site_navigator(i).fill()
            sleep(1)
        self.site_navigator('back').click()
        sleep(3)