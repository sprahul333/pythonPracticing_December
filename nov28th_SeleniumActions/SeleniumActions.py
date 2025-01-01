import time
from locale import windows_locale

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)
driver.set_page_load_timeout(300)

driver.get("https://freelance-learn-automation.vercel.app/login")

txt_UserName=driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']")
txt_Password=driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']")


txt_UserName.send_keys("admin@email.com")
txt_Password.send_keys("admin@123")

btn_Submit=driver.find_element(By.CSS_SELECTOR,".submit-btn")
btn_Submit.click()

actions=ActionChains(driver)
lnk_Manage=driver.find_element(By.XPATH,"//span[text()='Manage']")
actions.move_to_element(lnk_Manage).perform()

lnk_ManageCategories=driver.find_element(By.XPATH,"//a[text()='Manage Categories']")
actions.move_to_element(lnk_ManageCategories).click().perform()

#Return type is list here for multiple window handles
handles=driver.window_handles #Gets the list of all window handles

print(handles)

#Switching to the last window opened
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

#Switching to the window based on index position

time.sleep(3)
# driver.switch_to.window(handles[0])

btn_AddNewCategory=driver.find_element(By.XPATH,"//button[normalize-space(text())='Add New Category']")
btn_AddNewCategory.click()

#Passing the data to the alert
driver.switch_to.alert.send_keys("Testing1234")

#Getting the text of the alert
print(driver.switch_to.alert.text)

time.sleep(3)
#Accepting the alert
driver.switch_to.alert.accept()

time.sleep(3)

btn_DeleteCategory=driver.find_element(By.XPATH,"//td[text()='Testing1234']/following-sibling::td[1]/button")
actions.move_to_element(btn_DeleteCategory).perform()
btn_DeleteCategory.click()

time.sleep(3)
btn_Delete=driver.find_element(By.XPATH,"//button[text()='Delete']")
actions.move_to_element(btn_Delete).perform()
btn_Delete.click()

list_Rows=driver.find_elements(By.XPATH,"//td[text()='Testing1234']")

if len(list_Rows)==0:
    print("Category Deleted Successfully")

driver.close() #Closes the current window

windows_handles=driver.window_handles
for handle in windows_handles:
    driver.switch_to.window(handle)

# driver.quit() #Closes all the windows and cannot be used in the middle of the sessions
time.sleep(30)