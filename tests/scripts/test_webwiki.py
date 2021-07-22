from selenium.webdriver.support.ui import WebDriverWait
from src.base_test import BaseTest
import logging
from time import sleep
logger = logging.getLogger(__name__)
class TestWebwiki(BaseTest):
    def test_webwiki(self):
        logger.debug("Test webwiki started")
        WebDriverWait(self.driver, 2)
        self.driver.maximize_window()
        self.lunch_site()
        print("Home Title : ", self.driver.title)
        sleep(2)
        self.lang_english()

    def test_AcceptCookies(self):
        logger.debug("Test webwiki cookie accepted started")
        WebDriverWait(self.driver, 2)
        self.accept_cookies()

    # def test_search(self):
    #     logger.debug("Test webwiki search started")
    #     WebDriverWait(self.driver, 2)
    #     self.search_info()
    #     time.sleep(2)

    def test_register(self):
        logger.debug("Test webwiki register started")
        self.open_registration()
        sleep(2)
        self.test_AcceptCookies()
        field_list = ["domain", "addUrl", "category", "title", "description", "email", "operator", "address", "zip", "city", "country", "phone", "fax", "website", "agree"]
        for i in field_list:
            if(i == "category"):
                print("select Catagory")
                self.select_tag(i)
            elif(i== "country"):
                print("Select Country")
                self.select_tag(i)
            elif (i == "agree"):
                print("Checked agree")
                self.site_navigator(i).click()
                # self.agree_checked()
            else:
                self.site_navigator(i).fill()
            sleep(1)

    def test_submit(self):
        logger.debug("Test webwiki submit started")
        self.driver.save_screenshot(".\\screenshorts\\"+"test_webwiki_register.png")
        self.site_navigator('submit').click()
        sleep(5)
        # self.driver.close()





