import time
import re
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(300)

driver.get("https://freelance-learn-automation.vercel.app")

assert "automation" in driver.current_url

img_Menus=driver.find_element(By.XPATH,"//img[@alt='menu']")
img_Menus.click()

btn_Login=driver.find_element(By.XPATH,"//button[text()='Log in']")
btn_Login.click()

txt_EmailAddress=driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']")
txt_EmailAddress.send_keys("admin@email.com")

txt_Password=driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']")
txt_Password.send_keys("admin@123")

btn_Submit=driver.find_element(By.XPATH,"//button[@class='submit-btn']")
btn_Submit.click()

btn_AddtoCart_Playwright=driver.find_element(By.XPATH,"//h2[text()='Playwright']/.././../descendant::button")
btn_AddtoCart_Playwright.click()

count_items=driver.find_elements(By.XPATH,"//span[@class='count']")

if len(count_items)!=0:
    print("Item added to the cart")
    print(count_items[0].text) #Prints the count of items in the cart
else:
    print("Item not added to the cart")

btn_AddtoCart_Selenium=driver.find_element(By.XPATH,"//h2[text()='Selenium']/.././../descendant::button")
btn_AddtoCart_Selenium.click()

btn_AddtoCart_Cypress=driver.find_element(By.XPATH,"//h2[text()='Cypress']/.././../descendant::button")
btn_AddtoCart_Cypress.click()

btn_Cart=driver.find_element(By.XPATH,"//button[text()='Cart']")
btn_Cart.click()

list_of_Prices=driver.find_elements(By.XPATH,"//span[normalize-space(text())='Price:']")

total = 0

for price in list_of_Prices:
    total+=int(re.sub(r"[^0-9]", "", price.text.split("\n")[1]))

btn_EnrollNow=driver.find_element(By.XPATH,"//button[text()='Enroll Now']")
btn_EnrollNow.click()

btn_EnrollCourse=driver.find_element(By.XPATH,"//button[text()='Enroll Now' and @class='action-btn']")
btn_EnrollCourse.click()

fld_AddressEmptyMessage=driver.find_elements(By.XPATH,"//div[text()='Address is empty']")

if len(fld_AddressEmptyMessage)!=0:
    print("Address is empty error is popping up")
else:
    raise Exception("Address is empty error is not popping up")

txt_Address=driver.find_element(By.XPATH,"//textarea[@id='address']")
txt_Address.send_keys("Bangalore, Karnataka")

txt_PhoneNumber=driver.find_element(By.XPATH,"//input[@id='phone']")
txt_PhoneNumber.send_keys("1234567891")

btn_EnrollCourse=driver.find_element(By.XPATH,"//button[text()='Enroll Now' and @class='action-btn']")
btn_EnrollCourse.click()

txt_UniqueID=driver.find_element(By.XPATH,"//h4[@class='uniqueId']")
print("Order ID Generated is: "+txt_UniqueID.text)

btn_Cancel=driver.find_element(By.XPATH,"//button[text()='Cancel']")
btn_Cancel.click()

try:
    img_Menus=driver.find_element(By.XPATH,"//img[@alt='menu']")
    img_Menus.click()
except ElementClickInterceptedException:
    time.sleep(5)
    img_Menus = driver.find_element(By.XPATH, "//img[@alt='menu']")
    img_Menus.click()

btn_Logout=driver.find_element(By.XPATH,"//button[text()='Sign out']")
btn_Logout.click()

time.sleep(10)