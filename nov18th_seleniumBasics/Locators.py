import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://www.google.com")

'''
    Locator is a way to locate the element on the web page.
    
    There are 8 types of locators:
    1. ID
    2. Name
    3. Link Text
    4. Partial Link Text
    5. Tag Name
    6. Class Name
    7. CSS Selector
    8. XPath
    
    Selenium 4 has introduced a new locator called Relative Locators
'''

search_bar=driver.find_element(By.NAME, "q")
print(type(search_bar))
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.ENTER)
data=search_bar.text

#Using contains keyword
print(data.__contains__("Selenium"))

#Alternate way is:
print("Selenium" in data)

time.sleep(20)