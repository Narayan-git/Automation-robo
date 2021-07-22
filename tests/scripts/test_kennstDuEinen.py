import logging
from src.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
logger = logging.getLogger(__name__)

class TestKennstDuEinen(BaseTest):
    def test_kennstDuEinen(self):
        logger.info("test kennstDuEinen started")
        self.driver.maximize_window()
        logger.info("site lunched")
        self.lunch_site()
        WebDriverWait(self.driver, 2)
        print("[ HOME PAGE ] : ", self.driver.title)
        sleep(2)
        self.accept_cookies()
        sleep(2)

    def test_register(self):
        logger.info("test kennstDuEinen register")
        sleep(2)
        self.site_navigator("registration").click()
        sleep(2)

        field_list = ["first_name", "sur_name", "zip", "city", "email", "password",
                      "confirm_password", "agree1", "agree2", "register"]
        for i in field_list:
            if (i == "agree1" or i == "agree2" or i == "register"):
                self.site_navigator(i).click()
                sleep(2)
            else:
                self.site_navigator(i).fill()
            sleep(1)
        sleep(3)
    # def test_VerifyEmail(self):
    #     logger.info("test kennstDuEinen email Verify")
    #     verification_link = self.mail_verification()
    #     Window opened in new tab
    #     self.driver.execute_script('''window.open("", "_blank)''')
    #     self.driver.switch_to_window(self.driver.window_handles[1])
    #     self.driver.get(verification_link)
    #     sleep(12)
    #     self.driver.close()
    #     self.driver.switch_to_window(self.driver.window_handles[0])

    # def test_Login(self):
    #     logger.info("test kennstDuEinen login")
    #     field_list = ["home", "login_page", "email", "password", "login"]
    #     for i in field_list:
    #         if (i == "login"):
    #             self.site_navigator(i).click()
    #             sleep(2)
    #         elif(i == "login_page" or i == "home"):
    #             self.site_navigator(i).click()
    #             sleep(3)
    #         else:
    #             self.site_navigator(i).fill()
    #         sleep(1)
    #     sleep(5)
