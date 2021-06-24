from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.base_test import BaseTest
from utilities.customLogger import LogGen
import time

class TestWebwiki(BaseTest):
    logger = LogGen.loggen()
    def test_webwiki(self):
        self.logger.debug("Test webwiki started")
        WebDriverWait(self.driver, 2)
        self.driver.maximize_window()
        self.lunch_site()
        title = self.home_title()
        print("Home Title : ", title)
        time.sleep(2)
        self.lang_english()

    def test_AcceptCookies(self):
        self.logger.debug("Test webwiki cookie accepted started")
        WebDriverWait(self.driver, 2)
        self.accept_cookies()

    def test_search(self):
        self.logger.debug("Test webwiki search started")
        WebDriverWait(self.driver, 2)
        self.search_info()
        time.sleep(2)

    def test_register(self):
        self.logger.debug("Test webwiki register started")
        self.open_registration()
        time.sleep(2)
        self.test_AcceptCookies()
        field_list = ["domain", "addUrl", "category", "title", "description", "email", "operator", "address", "zip", "city", "country", "phone", "fax", "website", "agree"]
        for i in field_list:
            if(i == "category"):
                print("select Catagory")
                self.select_category(i)
            elif(i== "country"):
                print("Select Country")
                self.select_category(i)
            elif (i == "agree"):
                print("Checked agree")
                self.agree_checked()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)

    def test_submit(self):
        self.logger.debug("Test webwiki submit started")
        self.driver.save_screenshot(".\\screenshorts\\"+"test_webwiki_register.png")
        self.form_submit()
        time.sleep(5)
        self.driver.close()





