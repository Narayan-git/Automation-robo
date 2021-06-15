"""
This is simple test suit. The test suit must be start with "test" or end with "test".
It must be annoted with pytest fixture.
"""

import logging
import os
from posixpath import basename
from typing import List
import glob
import time
import re
import pytest
from pathlib import Path
import inspect

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.data_utils import DataUtils



# uses the root logger - automatically will be enabled
logger = logging.getLogger(__name__)
cur_path = os.path.dirname(__file__)


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    """
    Base Test class.
    """


    def lunch_site(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        site_name = os.path.basename(filename).replace(".py","").split("test_")[1]
        print(site_name)

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
            self.driver.find_element_by_xpath(self.navigator_data["cookies"]).click()
        except:
            logger.info("No cookies found")
            pass








