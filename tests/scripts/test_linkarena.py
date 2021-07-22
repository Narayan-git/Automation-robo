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


class TestLinkarena(BaseTest):

    def test_linlarena(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

    def test_AcceptCookies(self):
        WebDriverWait(self.driver, 2)
        self.accept_cookies()

        self.site_navigator("register").click()

        field_list = ["username", "email", "password", "repassword", "pin", "know about"]
        for i in field_list:
            self.site_navigator(i).fill()

        sleep(2)

        self.site_navigator("submit").click()

        sleep(2)
        logger.info("Finished!!")
