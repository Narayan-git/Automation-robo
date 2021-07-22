import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestKooimo(BaseTest):
    def test_kooimo(self):
        logger.info("test kooimo started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(2)
        self.accept_cookies()
        sleep(2)

    def test_register(self):
        logger.info("test kooimo register")
        sleep(2)
        self.site_navigator("login_page").click()
        sleep(2)
        self.site_navigator("registration").click()
        sleep(2)
        field_list = ["user_name", "email", "password", "agree", "register"]
        for i in field_list:
            if (i == "agree" or i == "register"):
                self.site_navigator(i).click()
                sleep(2)
            else:
                self.site_navigator(i).fill()
            sleep(1)
        sleep(2)
    def test_Login(self):
        WebDriverWait(self.driver, 2)
        logger.info("test kooimo login")
        field_list = ["home", "login_page", "email", "login_pass", "login"]
        for i in field_list:
            if (i == "login"):
                self.site_navigator(i).click()
                sleep(2)
            elif(i == "login_page" or i == "home"):
                self.site_navigator(i).click()
                sleep(3)
            else:
                self.site_navigator(i).fill()
            sleep(1)
        sleep(5)