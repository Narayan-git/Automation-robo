import string
import selenium
from random import randint
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException

def click(driver: WebDriver, locator_value: string, locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False,
          ):
    """This Function will click on a web elemen

    Args:
        driver (WebDriver): [Current Instance of the web Driver]
        locator_value (string) : [Value of the search query]
        locator_name (string): [Name of the locator for loggin purpose]
        id (bool, optional): [True if find by ID]. Defaults to False.
        name (bool, optional): [True if find by NAME]. Defaults to False.
        xpath (bool, optional): [True if find by XPATH]. Defaults to False.
        link_text (bool, optional): [True if find by LINK_TEXT]. Defaults to False.
        partial_link_text (bool, optional): [True if find by PARTIAL_LINK_TEXT]. Defaults to False.
        tag_name (bool, optional): [True if find by TAG_NAME]. Defaults to False.
        class_name (bool, optional): [True if find by CLASS_NAME]. Defaults to False.
        css_selector (bool, optional): [True if find by CSS_SELECTOR]. Defaults to False.
    """
    try:
        if id == True:
            driver.find_element(By.ID, locator_value).click()
        elif xpath == True:
            driver.find_element(By.XPATH, locator_value).click()
        elif name == True:
            driver.find_element(By.NAME, locator_value).click()
        elif link_text == True:
            driver.find_element(By.LINK_TEXT, locator_value).click()
        elif partial_link_text == True:
            driver.find_element(By.PARTIAL_LINK_TEXT, locator_value).click()
        elif tag_name == True:
            driver.find_element(By.TAG_NAME, locator_value).click()
        elif class_name == True:
            driver.find_element(By.CLASS_NAME, locator_value).click()
        elif css_selector == True:
            driver.find_element(By.CSS_SELECTOR, locator_value).click()
    except Exception as e : 
        print(e)


def send_keys(driver: WebDriver, locator_value: string, text : string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
    """This Function will send keys to a web elemen

    Args:
        driver (WebDriver): [Current Instance of the web Driver]
        locator_value (string) : [Value of the search query]
        text (string) : [Value to be added in input field]
        locator_name (string): [Name of the locator for loggin purpose]
        id (bool, optional): [True if find by ID]. Defaults to False.
        name (bool, optional): [True if find by NAME]. Defaults to False.
        xpath (bool, optional): [True if find by XPATH]. Defaults to False.
        link_text (bool, optional): [True if find by LINK_TEXT]. Defaults to False.
        partial_link_text (bool, optional): [True if find by PARTIAL_LINK_TEXT]. Defaults to False.
        tag_name (bool, optional): [True if find by TAG_NAME]. Defaults to False.
        class_name (bool, optional): [True if find by CLASS_NAME]. Defaults to False.
        css_selector (bool, optional): [True if find by CSS_SELECTOR]. Defaults to False.
    """
    try:
        if id == True:
            driver.find_element(By.ID, locator_value).clear()
            driver.find_element(By.ID, locator_value).send_keys(text)
        elif xpath == True:
            driver.find_element(By.XPATH, locator_value).clear()
            driver.find_element(By.XPATH, locator_value).send_keys(text)
        elif name == True:
            driver.find_element(By.NAME, locator_value).clear()
            driver.find_element(By.NAME, locator_value).send_keys(text)
        elif link_text == True:
            driver.find_element(By.LINK_TEXT, locator_value).clear()
            driver.find_element(By.LINK_TEXT, locator_value).send_keys(text)
        elif partial_link_text == True:
            driver.find_element(By.PARTIAL_LINK_TEXT, locator_value).clear()
            driver.find_element(By.PARTIAL_LINK_TEXT, locator_value).send_keys(text)
        elif tag_name == True:
            driver.find_element(By.TAG_NAME, locator_value).clear()
            driver.find_element(By.TAG_NAME, locator_value).send_keys(text)
        elif class_name == True:
            driver.find_element(By.CLASS_NAME, locator_value).clear()
            driver.find_element(By.CLASS_NAME, locator_value).send_keys(text)
        elif css_selector == True:
            driver.find_element(By.CSS_SELECTOR, locator_value).clear()
            driver.find_element(By.CSS_SELECTOR, locator_value).send_keys(text)
    except Exception as e : 
        print(e)

def wait_for_element_present(driver: WebDriver, locator_value: string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False,):
    """[This function will wait for the element to be present ]

    Args:
        driver (WebDriver): [description]
        locator_value (string): [description]
        text (string): [description]
        locator_name (string): [description]
        id (bool, optional): [description]. Defaults to False.
        name (bool, optional): [description]. Defaults to False.
        xpath (bool, optional): [description]. Defaults to False.
        link_text (bool, optional): [description]. Defaults to False.
        partial_link_text (bool, optional): [description]. Defaults to False.
        tag_name (bool, optional): [description]. Defaults to False.
        class_name (bool, optional): [description]. Defaults to False.
        css_selector (bool, optional): [description]. Defaults to False.
    """
    try:
        web_driver_wait = WebDriverWait(driver , 10)

        if id == True:
            web_driver_wait.until(EC.presence_of_element_located((By.ID, locator_value)))
        elif xpath == True:
            web_driver_wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        elif name == True:
            web_driver_wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
        elif link_text == True:
            web_driver_wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
        elif partial_link_text == True:
            web_driver_wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator_value)))
        elif tag_name == True:
            web_driver_wait.until(EC.presence_of_element_located((By.TAG_NAME, locator_value)))
        elif class_name == True:
            web_driver_wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
        elif css_selector == True:
            web_driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
    except Exception as e : 
        print(e)

def wait_for_element_clickable(driver: WebDriver, locator_value: string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False,):
    """[This function will wait for the element to be clickable ]

    Args:
        driver (WebDriver): [description]
        locator_value (string): [description]
        text (string): [description]
        locator_name (string): [description]
        id (bool, optional): [description]. Defaults to False.
        name (bool, optional): [description]. Defaults to False.
        xpath (bool, optional): [description]. Defaults to False.
        link_text (bool, optional): [description]. Defaults to False.
        partial_link_text (bool, optional): [description]. Defaults to False.
        tag_name (bool, optional): [description]. Defaults to False.
        class_name (bool, optional): [description]. Defaults to False.
        css_selector (bool, optional): [description]. Defaults to False.
    """
    try:
        web_driver_wait = WebDriverWait(driver , 10)

        if id == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif xpath == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        elif name == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.NAME, locator_value)))
        elif link_text == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
        elif partial_link_text == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator_value)))
        elif tag_name == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.TAG_NAME, locator_value)))
        elif class_name == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
        elif css_selector == True:
            web_driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
    except Exception as e : 
        print(e)

def select_by_visible_text(driver: WebDriver, locator_value: string, visible_text : string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
    """This Function will select from dropdown using visible text

    Args:
        driver (WebDriver): [Current Instance of the web Driver]
        locator_value (string) : [Value of the search query]
        text (string) : [Value to be added in input field]
        locator_name (string): [Name of the locator for loggin purpose]
        id (bool, optional): [True if find by ID]. Defaults to False.
        name (bool, optional): [True if find by NAME]. Defaults to False.
        xpath (bool, optional): [True if find by XPATH]. Defaults to False.
        link_text (bool, optional): [True if find by LINK_TEXT]. Defaults to False.
        partial_link_text (bool, optional): [True if find by PARTIAL_LINK_TEXT]. Defaults to False.
        tag_name (bool, optional): [True if find by TAG_NAME]. Defaults to False.
        class_name (bool, optional): [True if find by CLASS_NAME]. Defaults to False.
        css_selector (bool, optional): [True if find by CSS_SELECTOR]. Defaults to False.
    """
    try:
        if id == True:
            select = Select(driver.find_element(By.ID, locator_value))
        elif xpath == True:
            select = Select(driver.find_element(By.XPATH, locator_value))
        elif name == True:
            select = Select(driver.find_element(By.NAME, locator_value))
        elif link_text == True:
            select = Select(driver.find_element(By.LINK_TEXT, locator_value))
        elif partial_link_text == True:
            select = Select(driver.find_element(By.PARTIAL_LINK_TEXT, locator_value))
        elif tag_name == True:
            select = Select(driver.find_element(By.TAG_NAME, locator_value))
        elif class_name == True:
            select = Select(driver.find_element(By.CLASS_NAME, locator_value))
        elif css_selector == True:
            select = Select(driver.find_element(By.CSS_SELECTOR, locator_value))
        
        select.select_by_visible_text(visible_text)
    except Exception as e : 
        print(e)

def select_by_value(driver: WebDriver, locator_value: string, select_value : string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
    """This Function will select from dropdown using value

    Args:
        driver (WebDriver): [Current Instance of the web Driver]
        locator_value (string) : [Value of the search query]
        select_value (string) : [Value to be added in input field]
        locator_name (string): [Name of the locator for loggin purpose]
        id (bool, optional): [True if find by ID]. Defaults to False.
        name (bool, optional): [True if find by NAME]. Defaults to False.
        xpath (bool, optional): [True if find by XPATH]. Defaults to False.
        link_text (bool, optional): [True if find by LINK_TEXT]. Defaults to False.
        partial_link_text (bool, optional): [True if find by PARTIAL_LINK_TEXT]. Defaults to False.
        tag_name (bool, optional): [True if find by TAG_NAME]. Defaults to False.
        class_name (bool, optional): [True if find by CLASS_NAME]. Defaults to False.
        css_selector (bool, optional): [True if find by CSS_SELECTOR]. Defaults to False.
    """
    try:
        if id == True:
            select = Select(driver.find_element(By.ID, locator_value))
        elif xpath == True:
            select = Select(driver.find_element(By.XPATH, locator_value))
        elif name == True:
            select = Select(driver.find_element(By.NAME, locator_value))
        elif link_text == True:
            select = Select(driver.find_element(By.LINK_TEXT, locator_value))
        elif partial_link_text == True:
            select = Select(driver.find_element(By.PARTIAL_LINK_TEXT, locator_value))
        elif tag_name == True:
            select = Select(driver.find_element(By.TAG_NAME, locator_value))
        elif class_name == True:
            select = Select(driver.find_element(By.CLASS_NAME, locator_value))
        elif css_selector == True:
            select = Select(driver.find_element(By.CSS_SELECTOR, locator_value))
        
        select.select_by_value(select_value)
    except Exception as e : 
        print(e)


def is_element_present(driver: WebDriver, locator_value: string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
    try:
        if id == True:
            driver.find_element(By.ID, locator_value)
        elif xpath == True:
            driver.find_element(By.XPATH, locator_value)
        elif name == True:
            driver.find_element(By.NAME, locator_value)
        elif link_text == True:
            driver.find_element(By.LINK_TEXT, locator_value)
        elif partial_link_text == True:
            driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif tag_name == True:
            driver.find_element(By.TAG_NAME, locator_value)
        elif class_name == True:
            driver.find_element(By.CLASS_NAME, locator_value)
        elif css_selector == True:
            driver.find_element(By.CSS_SELECTOR, locator_value)
        return True
    except NoSuchElementException as e : 
        print("Element" + locator_name + " not found")
        return False
    except InvalidElementStateException as e:
        print("Element" + locator_name + " state is invalid")
        return False    

def JS_click(driver: WebDriver, locator_value: string , locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False):
    try:
        if id == True:
            element = driver.find_element(By.ID, locator_value)
        elif xpath == True:
            element = driver.find_element(By.XPATH, locator_value)
        elif name == True:
            element = driver.find_element(By.NAME, locator_value)
        elif link_text == True:
            element = driver.find_element(By.LINK_TEXT, locator_value)
        elif partial_link_text == True:
            element = driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif tag_name == True:
            element = driver.find_element(By.TAG_NAME, locator_value)
        elif class_name == True:
            element = driver.find_element(By.CLASS_NAME, locator_value)
        elif css_selector == True:
            element = driver.find_element(By.CSS_SELECTOR, locator_value)

        driver.execute_script("arguments[0].click();", element)

    except Exception as e:
        print(e)

def delay():
    time.sleep(randint(2,5))
