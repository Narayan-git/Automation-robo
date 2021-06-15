# import selenium
# from selenium import webdriver
# import time

# driver = webdriver.Chrome("drivers/chromedriver")

# #open the browser
# time.sleep(5)

# driver.get("https://web.whatsapp.com/")
# time.sleep(5)

# element = driver.find_element_by_name("Chuinn")
# element.click()
# #/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div[1]/span/span

# #close the browser
# #driver.quit()


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
  
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('drivers/chromedriver')
  
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
  
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Friend\'s Name"'
  
# Replace the below string with your own message
string = "I love you"
  
x_arg = '//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)