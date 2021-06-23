from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from logging import log
from src.base_test import BaseTest

import logging

logger = logging.getLogger(__name__)


class TestGolocal(BaseTest):

    def test_golocal(self):


        
        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        logger.info("Clear Cookies")
        #Accept cookies if any occurrence.
        self.accept_cookies()

        logger.info("Open registration")
        self.open_registration()

        #Register by using mail id
        self.site_navigator('register_per_email').click()

        ###Below list of registration field
        field_list = ["email","user_name","password","repeat_password","place_name"]
        for i in field_list:
            self.site_navigator(i).fill()

        self.site_navigator("gender",opt = True).click()

        #Click on Registration
        logger.info("Click on Registration")
        assert self.site_navigator("register-and-active").click()

        sleep(2)
        logger.info("Finished!!")