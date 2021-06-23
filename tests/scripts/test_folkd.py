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


class TestFolkd(BaseTest):

    def test_folkd(self):

        options = Options()
        options.add_argument("window-size=1200x600")
        wait = WebDriverWait(self.driver, 3)
        logger.info("Step 1 : Lunch site")
        self.lunch_site()

        #Mazimize current window
        self.driver.maximize_window()

        logger.info("Open registration")
        self.open_registration()

        ###Below list of registration field
        field_list = ["user_name","email","password","repeat_password"]
        for i in field_list:
            self.site_navigator(i).fill()

        #######
        # Put here captch api
        #######
        
        #Finished with registration
        self.site_navigator("register").click()
        