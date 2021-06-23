from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from logging import log
from src.base_test import BaseTest
from tools.inbox import get_message_by_subject_mail
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import logging

logger = logging.getLogger(__name__)


class TestProvenexpert(BaseTest):

    def test_provenexpert(self):

        options = Options()
        options.add_argument("window-size=1200x600")
        wait = WebDriverWait(self.driver, 3)
        logger.info("Step 1 : Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        # logger.info("Clear Cookies")
        # #Accept cookies if any occurrence.
        # self.accept_cookies()

        logger.info("Step 2: Open registration")
        #self.open_registration()
        button = self.driver.find_element_by_xpath(u"//A[@class='peButton ctaRegister small'][text()='Start']/self::A")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

        # logger.info("Step 3: Fill required mail and go for sign up")
        # #Fill with mail id to sign up
        # self.site_navigator('email').fill()

        # #Click on sign up
        # self.site_navigator("sign_up").click()


        # ###Below list of registration field
        # field_list = ["email","user_name","password","repeat_password","place_name"]
        # for i in field_list:
        #     self.site_navigator(i).fill()

        # self.site_navigator("gender",opt = True).click()

        # #Click on Registration
        # logger.info("Click on Registration")
        # assert self.site_navigator("register-and-active").click()

        sleep(2)
        logger.info("Finished!!")