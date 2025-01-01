import time

from selenium import webdriver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver1=driver.Chrome()

driver1.maximize_window()

driver1.implicitly_wait(10)
driver1.set_page_load_timeout(300)

driver1.get("https://demo.automationtesting.in/Register.html")

txt_FirstName=driver1.find_element(By.XPATH,"//input[@placeholder='First Name']")
txt_FirstName.send_keys("Selenium")

txt_LastName=driver1.find_element(By.XPATH,"//input[@ng-model='LastName']")
txt_LastName.send_keys("Python")

txt_Address=driver1.find_element(By.XPATH,"//textarea[@ng-model='Adress']")
txt_Address.send_keys("Bangalore, Karnataka")

txt_EmailAddress=driver1.find_element(By.XPATH,"//input[@ng-model='EmailAdress']")
txt_EmailAddress.send_keys("abc@abc.com")

txt_PhoneNumber=driver1.find_element(By.XPATH,"//input[@ng-model='Phone']")
txt_PhoneNumber.send_keys("1234567891")

rbn_Male=driver1.find_element(By.XPATH,"//label[normalize-space(.)='Male']")
rbn_Male.click()

cbx_Hobbies=driver1.find_elements(By.XPATH,"//input[@type='checkbox']")
# cbx_Hobbies[0].click() #Clicks on the first checkbox
#
# cbx_Hobbies[1].click() #Clicks on the second checkbox
#
# cbx_Hobbies[len(cbx_Hobbies)-1].click() #Clicks on the last checkbox

for x in cbx_Hobbies:
    x.click()
    time.sleep(1)

#Scroll Page Down:
#.execute_script ---> Executing the JS Code
driver1.execute_script("window.scrollBy(0,300)")

ddl_Skills=driver1.find_element(By.ID,"Skills")
select=Select (ddl_Skills) #Select is a class in Selenium that is used to handle the libraries using the select function

#Finding the Drop Down Option on the basis of visible text
select.select_by_visible_text("Java")
select.select_by_visible_text("Linux")
time.sleep(2)

#Finding the Drop Down Option on the basis of index
select.select_by_index(3)
time.sleep(2)

#Finding the Drop Down Option on the basis of value
select.select_by_value("Python")
time.sleep(2)

ddl_Year=driver1.find_element(By.ID,"yearbox")
select=Select(ddl_Year)
listOfOptions=select.options

#Get a random option from the list of options

import random
randomIndex=random.randint(0,len(listOfOptions)-1)

listOfOptions[randomIndex].click()

ddl_Month=driver1.find_element(By.XPATH,"//select[@placeholder='Month']")
select=Select(ddl_Month)

#Finding the Drop Down Option on the basis of visible text
select.select_by_visible_text("May")

ddl_Date=driver1.find_element(By.XPATH,"//select[@placeholder='Day']")
select=Select(ddl_Date)

#Finding the Drop Down Option on the basis of visible text
listOfDates=select.options

randomNumber=random.randint(0,len(listOfDates)-1)

listOfDates[randomNumber].click()

txt_Password=driver1.find_element(By.ID,"firstpassword")

#Generating a random string:

randomString=""

for x in range(0,8):
    randomString=randomString+chr(random.randint(65,90))
    

txt_Password.send_keys(randomString)


time.sleep(20)
