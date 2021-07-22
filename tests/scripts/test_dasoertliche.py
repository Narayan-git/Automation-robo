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


class TestDasoertliche(BaseTest):

    def test_dasoertliche(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        logger.info("Clear Cookies")
    # Accept cookies if any occurrence.
        self.accept_cookies()

        self.site_navigator('service').click()

        field_list = ["companyname", "road", "houseno", "postcode", "place", "prefix", "number", "prefixfax", "fax", "website", "email"]
        for i in field_list:
            self.site_navigator(i).fill()


        self.site_navigator("start").click()

        sleep(2)
        logger.info("Finished!!")
