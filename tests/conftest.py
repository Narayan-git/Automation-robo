from selenium import webdriver
import pytest


# creds
API_KEY = ''
API_SECRET = ''



### BlazeGrid capabilites
desired_capabilities = {
    'browserName': 'chrome',
}


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome("drivers/chromedriver")
    request.cls.driver = web_driver
    yield
    web_driver.close()






