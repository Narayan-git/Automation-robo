from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.base_test import BaseTest
import time

class TestWebwiki(BaseTest):
    def test_dastelefonbuch(self):
        WebDriverWait(self.driver, 3)
        self.driver.maximize_window()
        self.lunch_site()
        title = self.home_title()
        print("Home Title : ", title)
        time.sleep(2)

    def test_AcceptCookies(self):
        WebDriverWait(self.driver, 2)
        self.accept_cookies()


    def test_search(self):
        WebDriverWait(self.driver, 2)
        self.search_info()
        time.sleep(10)
        self.driver.close()






