from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.base_test import BaseTest


class TestBooking(BaseTest):

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 3)
        self.lunch_site()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()



