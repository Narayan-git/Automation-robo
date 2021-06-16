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

    def site_navigator(self,locator=None, id=False, name=False, xpath=True, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
        driver = self.driver
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]
        sleep(2)
        obj = Element_Action(driver,site_name=site_name,locator=locator, id=id, name=name, xpath=xpath, link_text=link_text, partial_link_text=partial_link_text, tag_name=tag_name, class_name=class_name, css_selector=css_selector)
        return obj











