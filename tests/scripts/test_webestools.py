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


class TestWebestools(BaseTest):

    def test_webestools(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        self.site_navigator("sign in").click()

        self.site_navigator("create_account").click()

        sleep(10)

        field_list = ["username", "password", "repassword", "email"]
        for i in field_list:
            self.site_navigator(i).fill()

        sleep(2)

        self.site_navigator("create").click()

        sleep(2)
        logger.info("Finished!!")
