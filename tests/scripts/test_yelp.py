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


class TestYelp(BaseTest):

    def test_Yelp(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        self.site_navigator("sign up").click()
        field_list = ["first_name","last_name", "email", "password", "city", "month", "day","year"]
        for i in field_list:
            if(i=="month"):
                self.site_navigator(i, opt=True).click()

            elif (i == "day"):
                self.site_navigator(i, opt=True).click()

            elif (i == "year"):
                self.site_navigator(i, opt=True).click()

            else:
                self.site_navigator(i).fill()

                sleep(2)

                self.site_navigator("submit").click()

                sleep(2)
                logger.info("Finished!!")


