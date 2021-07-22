import pytest
import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestWlw(BaseTest):
    def test_wlw(self):
        sleep(2)
        logger.info("test wlw started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(2)
        self.accept_cookies()
        sleep(2)

    def test_register(self):
        WebDriverWait(self.driver, 2)
        logger.info("test register free")
        self.site_navigator('registeration').click()
        sleep(2)
        self.site_navigator('register_free').click()
        sleep(2)
        field_list = ["company_name", "url", "street", "house_number", "zip", "city", "phone_number", "company_email", "next1"]
        for i in field_list:
            if(i == "next1"):
                sleep(1)
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_free_register_wlw.png")
                sleep(1)
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            sleep(2)
        sleep(5)

    def test_register_buyer(self):
        logger.info("register for buyer")
        WebDriverWait(self.driver, 2)
        self.site_navigator("register_buyer").click()
        sleep(2)
        field_list = ["gender", "first_name", "last_name", "user_email", "password", "agree", "submit"]
        for i in field_list:
            if(i == 'gender'):
                # self.select_category(i)
                self.site_navigator(i).select_by_value('mrs')
            elif(i == 'agree'):
                self.site_navigator(i).click()
            elif(i == 'submit'):
                sleep(1)
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_buyer_register_wlw.png")
                sleep(1)
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            sleep(2)
        sleep(5)

