#importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from scrapy import Selector
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

#path,driver and url
PATH = "/Users/hasanzeynalov/Desktop/for_github/scraping/selenium/chromedriver"

service = Service("/Users/hasanzeynalov/Desktop/for_github/scraping/selenium/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://turbo.az/")

car_prices = driver.find_elements(By.XPATH,'//div[@class="product-price"]')
SCROLL_PAUSE_TIME = 2.0

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script('window.scrollBy(0,10000)','')
time.sleep(100.0)

for i in range(0,100):
    print(car_prices[i].text)
print(len(car_prices))
print(car_prices)



# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height





#driver.find_element(By.XPATH,"//button[@name='commit']").click()

# #car_prices = driver.find_elements(By.XPATH,"//div[@class='product-price']")
# dictioanry = {}
# for i in range(415):
#     driver.find_element(By.XPATH,"//a[@rel='next']")
#     car_prices = driver.find_element(By.XPATH,"//div[@class='product-price']")

#     car_price = car_prices[r].text
#         dictioanry['car_name'] =car_price
# print(len(dictioanry))

driver.quit()