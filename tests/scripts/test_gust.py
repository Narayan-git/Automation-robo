import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.keys import Keys
logger = logging.getLogger(__name__)

class TestGust(BaseTest):
    def test_gust(self):
        logger.info("test gust started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(2)

    def test_AcceleratorRegister(self):
        logger.info("test gust Accelerator register")
        self.site_navigator("signup").click()
        sleep(3)
        self.site_navigator("accelerator_program").click()
        sleep(4)
        field_list = ["first_name", "last_name", "click_location", "primary_email", "password",
                      "confirm_password", "recap", "accept", "accelerator_signup"]

        for i in field_list:
            if (i == "accelerator_signup"):
                sleep(10)
                self.site_navigator(i).click()
                sleep(2)
            elif (i == "accept" or i == "recap"):
                self.site_navigator(i).click()
                sleep(3)
            elif (i == "click_location"):
                print("gender in process")
                self.site_navigator(i).click()
                sleep(2)
                self.site_navigator("enter_location").fill()
                sleep(2)
                self.site_navigator("enter_location").send_keys(Keys.ENTER)
                sleep(5)
            else:
                self.site_navigator(i).clear()
                sleep(1)
                self.site_navigator(i).fill()
            sleep(1)
        sleep(5)
