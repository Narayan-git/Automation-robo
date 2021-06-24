from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.base_test import BaseTest
from utilities.customLogger import LogGen
import time

class TestSachsische(BaseTest):
    logger = LogGen.loggen()
    def test_sachsische(self):
        self.logger.info("Test sachische started")
        WebDriverWait(self.driver, 3)
        self.driver.maximize_window()
        self.lunch_site()
        title = self.home_title()
        print("Home Title : ", title)
        time.sleep(2)

    def test_AcceptCookies(self):
        WebDriverWait(self.driver, 2)
        self.accept_cookies()
        time.sleep(2)
        self.option_deny()

    # def test_search(self):
    #     WebDriverWait(self.driver, 2)
    #     self.search_info()
    #     time.sleep(5)

    # def test_register(self):
    #     self.open_registration()
    #     time.sleep(5)
    #     self.test_AcceptCookies()
    #     field_list = ["domain", "addUrl", "category", "title", "description", "email", "operator", "address", "zip",
    #                   "city", "country", "phone", "fax", "website", "agree"]
    #     for i in field_list:
    #         if (i == "category"):
    #
    #      print("select Catagory")
    #             self.select_category(i)
    #         elif(i== "country"):
    #             print("Select Country")
    #             self.select_category(i)
    #         elif (i == "agree"):
    #             print("Checked agree")
    #             self.agree_checked()
    #         else:
    #             self.site_navigator(i).fill()
    #         time.sleep(1)
    #
    # def test_submit(self):
    #     self.form_submit()
    #     time.sleep(10)
    #     self.driver.close()





