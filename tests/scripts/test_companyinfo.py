from selenium.webdriver.support.ui import WebDriverWait
from src.base_test import BaseTest
import logging
import time
logger = logging.getLogger(__name__)
class TestCompanyinfo(BaseTest):
    def test_companyinfo(self):
        logger.info("Test companyinfo started")
        WebDriverWait(self.driver, 2)
        self.driver.maximize_window()
        self.lunch_site()
        print("Home Title : ", self.driver.title)
        time.sleep(2)

    def test_AcceptCookies(self):
        WebDriverWait(self.driver, 2)
        self.accept_cookies()

    def test_free_register(self):
        self.open_registration()
        time.sleep(2)
        self.site_navigator('freeEntry').click()
        self.test_AcceptCookies()
        field_list1 = ["freeCompanyName", "freeStreet", "freeZip", "freeCity", "freeState", "freeAreaCode", "freePhoneNumber", "freeRegisterSubmit1"]
        for i in field_list1:
            if(i == "freeState"):
                print("select State")
                self.select_tag(i)
            elif (i == "freeRegisterSubmit1"):
                self.driver.save_screenshot(".\\screenshorts\\" + "test_companyinfo1_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)

        field_list2 = ["freeAreaCodeFax", "freeFaxNumber", "freeAreaCodeService", "freeServiceNumber",
                       "freeEmail1","freeContact" ,"freeWebsite" ,"freeDesc" ,"freeIndustry1" ,"freeIndustry2",
                       "freeIndustry3", "freeAddinput", "freeAdd", "freeName", "freeEmail2", "freeRobot", "freeAgree"]
        for i in field_list2:
            if (i == "freeAdd"):
                self.site_navigator(i).click()
            elif (i == "freeAgree"):
                print("Checked agree")
                self.site_navigator(i).click()
            elif (i == "freeRobot"):
                print("Checked robot")
                # self.robot_free_companyinfo()
                pass
            elif (i == "freeRegisterSubmit2"):
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_companyinfo2_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)
        self.driver.back()
        self.driver.back()
        self.driver.back()

    '''
    def test_base_register(self):
        self.open_registration()
        time.sleep(2)
        self.site_navigator('baseEntry').click()
        self.test_AcceptCookies()
        field_list1 = ["freeCompanyName", "freeStreet", "freeZip", "freeCity", "freeState", "freeAreaCode",
                       "freePhoneNumber", "freeRegisterSubmit1"]
        for i in field_list1:
            if (i == "freeState"):
                print("select State")
                self.select_category(i)
            elif (i == "freeRegisterSubmit1"):
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_companyinfo1_Base_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)
        field_list2 = ["freeAreaCodeFax", "freeFaxNumber", "freeAreaCodeService", "freeServiceNumber", "freeEmail1",
                       "freeContact", "freeWebsite", "freeDesc", "freeIndustry1", "freeIndustry2",
                       "freeIndustry3", "baseIndustry4", "baseIndustry5", "freeAddinput", "freeAdd", "freeName", "freeEmail2", "baseDesired", "freeRobot", "freeAgree", "freeRegisterSubmit2"]
        for i in field_list2:
            if (i == "freeAdd"):
                print("Add")
                self.site_navigator(i).click()
            elif (i == "baseDesired"):
                print("Select Desired Length")
                self.select_category(i)
            elif (i == "freeAgree"):
                print("Checked agree")
                self.site_navigator(i).click()
            elif (i == "freeRobot"):
                print("Checked robot")
                # self.robot_free_companyinfo()
                pass
            elif (i == "freeRegisterSubmit2"):
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_companyinfo2_Base_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)

        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()

    def test_pemium_register(self):
        self.open_registration()
        time.sleep(2)
        self.site_navigator('premiumEntry').click()
        self.test_AcceptCookies()
        field_list1 = ["freeCompanyName", "freeStreet", "freeZip", "freeCity", "freeState", "freeAreaCode",
                       "freePhoneNumber", "freeRegisterSubmit1"]
        for i in field_list1:
            if (i == "freeState"):
                print("select State")
                self.select_category(i)
            elif (i == "freeRegisterSubmit1"):
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_companyinfo1_Premium_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)
        field_list2 = ["freeAreaCodeFax", "freeFaxNumber", "freeAreaCodeService", "freeServiceNumber", "freeEmail1",
                       "freeContact", "freeWebsite", "freeDesc", "freeIndustry1", "freeIndustry2",
                       "freeIndustry3", "baseIndustry4", "baseIndustry5", "premiumIndustry6", "premiumIndustry7",
                       "premiumIndustry8", "premiumIndustry9", "premiumIndustry10", "freeAddinput", "freeAdd", "freeName",
                       "freeEmail2", "baseDesired", "freeRobot", "freeAgree", "freeRegisterSubmit2"]
        for i in field_list2:
            if (i == "freeAdd"):
                print("Add")
                self.site_navigator(i).click()
            elif (i == "baseDesired"):
                print("Select Desired Length")
                self.select_category(i)
            elif (i == "freeAgree"):
                print("Checked agree")
                self.site_navigator(i).click()
            elif (i == "freeRobot"):
                print("Checked robot")
                # self.robot_free_companyinfo()
                pass
            elif (i == "freeRegisterSubmit2"):
                self.driver.save_screenshot(".\\tests\\screenshorts\\" + "test_companyinfo2_Premium_register.png")
                self.site_navigator(i).click()
            else:
                self.site_navigator(i).fill()
            time.sleep(1)
    '''

    # def test_close(self):
    #     time.sleep(5)
    #     self.driver.close()





