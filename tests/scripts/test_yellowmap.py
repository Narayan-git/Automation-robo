import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestYellowmap(BaseTest):
    def test_yellowmap(self):
        logger.info("test yellowmap started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(3)
        self.accept_cookies()
        sleep(5)

    def test_open_register(self):
        logger.info("test register started")
        WebDriverWait(self.driver, 2)
        self.site_navigator("dropdown").click()
        sleep(2)
        self.open_registration()
        sleep(2)
        self.site_navigator("find_company").fill()
        self.site_navigator("find_city").fill()
        self.site_navigator("find").click()
        sleep(3)

    def test_register(self):
        WebDriverWait(self.driver, 3)
        self.accept_cookies()
        sleep(3)
        self.site_navigator("company_register").click()
        sleep(2)
        self.site_navigator("gender").select_by_value('Frau')
        sleep(2)
        field_list = ["title", "first_name", "sur_name", "department", "function", "telephone",
                      "cellphone", "company", "additive", "street", "house_number", "country", "zip",
                      "place", "phone", "homepage", "vat", "mail", "password", "repeat_password",
                      "legal", "news_letter", "register"]
        for i in field_list:
            if(i == "country"):
                self.site_navigator(i).select_by_value('DE')
            elif(i == "legal" or i == "news_letter" or i == "register"):
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            sleep(2)



