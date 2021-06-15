from selenium.webdriver.firefox.webdriver import WebDriver
from actions import click, send_keys
from selenium import webdriver

driver = webdriver.Chrome("drivers/chromedriver")

# link : https://www.marktplatz-mittelstand.de/Firmeneintrag
# author : Manthan 
def marktplatz_auaotmation(driver : WebDriver):
    #  Xpath
    first_name_xpath = "//input[@id = 'firstname']"
    
    # Data
    first_name_data = "baap"
    
    # Action
    driver.get("https://www.marktplatz-mittelstand.de/Firmeneintrag")
    send_keys(driver = driver , text=first_name_data , locator_value=first_name_xpath , locator_name= "First Name Input field" , xpath=True)
    

marktplatz_auaotmation(driver)




