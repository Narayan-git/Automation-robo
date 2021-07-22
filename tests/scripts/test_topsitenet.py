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


class TestTopsitenet(BaseTest):

    def test_topsitenet(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        self.site_navigator("register").click()

        field_list = ["display_name", "email", "username", "password", "confirmation"]
        for i in field_list:
            self.site_navigator(i).fill()

        sleep(30)

        self.site_navigator("submit").click()

        sleep(20)
        logger.info("Finished!!")
