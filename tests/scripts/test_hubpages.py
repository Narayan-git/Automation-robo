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


class TestHubpages(BaseTest):

    def test_hubpages(self):

        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        self.site_navigator("join").click()

        field_list = ["username", "email", "password", "reenter_password"]
        for i in field_list:
            self.site_navigator(i).fill()

        self.site_navigator("term_&_condition").click()
        self.site_navigator("recaptcha").click()
        sleep(150)
        self.site_navigator("sign_up").click()

        sleep(2)
        logger.info("Finished!!")

    def test_VerifyEmail(self):
        logger.info("test kennstDuEinen email Verify")
        verification_link = self.mail_verification()
        # Window opened in new tab
        # self.driver.execute_script('''window.open("", "_blank)''')
        # self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get(verification_link)
        sleep(12)
        self.driver.close()
        # self.driver.switch_to_window(self.driver.window_handles[0])