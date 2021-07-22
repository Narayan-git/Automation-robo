import logging
from selenium.webdriver.support.ui import WebDriverWait
from src.base_test import BaseTest
from time import sleep

logger = logging.getLogger(__name__)

class TestPrima(BaseTest):

    def test_prima(self):
        WebDriverWait(self.driver, 3)
        logger.info("lunch site")
        self.lunch_site()
        self.driver.maximize_window()

    def test_AcceptCookies(self):
        WebDriverWait(self.driver, 2)
        self.accept_cookies()
        self.site_navigator('home').click()
        self.accept_cookies()

        field_list = ["yourname","email","phoneno","subject","loadingpoint","unloadingpoint","message"]
        for i in field_list:
            self.site_navigator(i).fill()
            sleep(2)

        sleep(2)
        logger.info("Finished!!")
        self.site_navigator('send').click()