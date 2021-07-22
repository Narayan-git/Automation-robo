import logging
from selenium.webdriver.support.ui import WebDriverWait
from src.base_test import BaseTest
from time import sleep
# create logger
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
class TestEuropages(BaseTest):
    def test_europages(self):
        logger.info("Test Europage started")
        WebDriverWait(self.driver, 3)
        self.driver.maximize_window()
        # lunch the website
        self.lunch_site()
        # get the home page title
        print("Home Title : ", self.driver.title)
        self.accept_cookies()
        logger.info(" Cookies Accepted")

    # def test_search(self):
    #     WebDriverWait(self.driver, 3)
    #     self.search_info()

    def test_register(self):
        self.site_navigator("clickRegister").click()
        self.accept_cookies()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.accept_cookies()
        self.site_navigator('entry').click()
        self.accept_cookies()
        field_list1 = ["companyName", "country", "zip", "edit", "website", "gender", "firstName",
                       "lastName", "email", "mobile", "agree", "send"]
        for i in field_list1:
            if (i == "country"):
                print("select Country")
                self.site_navigator(i).click()
                sleep(2)
                self.site_navigator('select_country').click()
            elif (i == "edit"):
                print("edit in process")
                self.site_navigator(i).click()
                sleep(5)
                self.site_navigator('webtype').click()
            elif (i == "gender"):
                print("in process")
                self.site_navigator(i, opt=True).click()
            elif (i == "send"):
                # self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_Europage_Register1.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            sleep(1)
        sleep(5)
        self.driver.quit()

    # def test_register_other(self):
    #     self.driver.back()
    #     self.driver.back()
    #     self.site_navigator('medium').click()
    #     self.test_register()
    #     self.driver.back()
    #     self.driver.back()
    #     self.site_navigator('premium').click()
    #     self.test_register()




