from os import truncate
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from actions import click, is_element_present, select_by_value, send_keys, wait_for_element_present
from selenium import webdriver



option = Options()
option.add_experimental_option("debuggerAddress" , "localhost:9015")
driver = webdriver.Chrome("drivers/chromedriver" , options= option)

# driver.get("https://www.unternehmensverzeichnis.org")
# click(driver , locator_value="cookieModalAccept" , locator_name="" , id = True)

click(driver , locator_value="Registration_Legal" , locator_name="Terms and Cond Check box" , id = True)






