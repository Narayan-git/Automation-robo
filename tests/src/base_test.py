"""
This is simple test suit. The test suit must be start with "test" or end with "test".
It must be annoted with pytest fixture.
"""

import logging
import os
from posixpath import basename
from typing import List
import glob
from time import sleep
import re
import pytest
from pathlib import Path
import inspect
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.data_utils import DataUtils
from src.element_action import Element_Action




# uses the root logger - automatically will be enabled
logger = logging.getLogger(__name__)
cur_path = os.path.dirname(__file__)

@pytest.mark.usefixtures("intial_call")
@pytest.mark.usefixtures("driver_init")
class BaseTest:
    """
    Base Test class.
    """
    @pytest.fixture
    def intial_call(self):
        self.name = "satyanhojnroj"
        #self.site_navigator = Element_Action()
        pass


    def lunch_site(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]
        print(site_name)
        sleep(2)
        #Collect data with map
        self.site_data = DataUtils.site_map_data(self,site_name)
        print(self.site_data["name"])
        self.driver.get(self.site_data["name"])

    def accept_cookies(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]

        self.navigator_data = DataUtils.data_navigator(self,site_name)
        try:
            sleep(2)
            self.driver.find_element_by_xpath(self.navigator_data["cookies"]).click()
            print("{0} Cookies Accepted Successfully".format(site_name))
        except:
            logger.info("No cookies found")
            pass


    def open_registration(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]

        self.navigator_data = DataUtils.data_navigator(self,site_name)
        sleep(2)
        self.driver.find_element_by_xpath(self.navigator_data["registration"]).click(),"No registation page found"

    def site_navigator(self,locator=None,opt = False, id=False, name=False, xpath=True, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
        driver = self.driver
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]
        sleep(2)
        obj = Element_Action(driver,site_name=site_name,locator=locator,opt = opt, id=id, name=name, xpath=xpath, link_text=link_text, partial_link_text=partial_link_text, tag_name=tag_name, class_name=class_name, css_selector=css_selector)
        return obj

    def select_tag(self, optn):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)
        self.site_data = DataUtils.site_map_data(self, site_name)
        sel = Select(self.driver.find_element_by_xpath(self.navigator_data[optn]))
        sel.select_by_visible_text(self.site_data[optn])
        # sleep(5)

    def lang_english(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)
        # click on choose language option
        self.driver.find_element_by_xpath(self.navigator_data["lang"]).click()
        sleep(2)
        # select the language as english
        self.driver.find_element_by_xpath(self.navigator_data["langeng"]).click()
        sleep(3)

    def select_country_a(self, optn):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)
        self.site_data = DataUtils.site_map_data(self, site_name)
        sel = self.driver.find_element_by_class('selectBox')
        sel.select_by_visible_text(self.site_data[optn])
        # sleep(5)

    def option_deny(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)

        try:
            sleep(2)
            self.driver.find_element_by_xpath(self.navigator_data['deny']).click()
            print("Deny successfully")
        except:
            logger.info("No Deny found")
            pass

    def marketing_goals(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]

        self.navigator_data = DataUtils.data_navigator(self, site_name)
        try:
            sleep(2)
            self.driver.find_element_by_xpath(self.navigator_data["shutdown"]).click()
            print("{0} Marketing Goals shutdown".format(site_name))
        except:
            logger.info("No Marketing Goals shutdown found")
            pass

    def funEdit(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)
        self.driver.find_element_by_xpath(self.navigator_data['edit']).click()
        self.select_category("webtype")

    def search_info(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]
        sleep(2)
        self.navigator_data = DataUtils.data_navigator(self, site_name)
        self.site_data = DataUtils.site_map_data(self, site_name)
        self.driver.find_element_by_xpath(self.navigator_data["searchinp"]).send_keys(self.site_data['searchinp'])
        sleep(2)
        self.driver.find_element_by_xpath(self.navigator_data['search']).click()

    def mail_verification(self):
        from tools.inbox import get_mail_verification_link
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py", "").split("test_")[1]

        self.navigator_data = DataUtils.data_navigator(self, site_name)
        self.site_data = DataUtils.site_map_data(self, site_name)

        email_id = self.site_data["email"]
        # subject = self.site_data["subject"]
        hrf_link = get_mail_verification_link(email_id = email_id)
        return hrf_link













