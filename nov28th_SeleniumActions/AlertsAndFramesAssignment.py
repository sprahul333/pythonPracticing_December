import os
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
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

actions=ActionChains(driver)
lnk_Manage=driver.find_element(By.XPATH,"//span[text()='Manage']")
actions.move_to_element(lnk_Manage).perform()

lnk_ManageCategories=driver.find_element(By.XPATH,"//a[text()='Manage Courses']")
actions.move_to_element(lnk_ManageCategories).click().perform()

time.sleep(3)

btn_AddNewCourse=driver.find_element(By.XPATH,"//button[normalize-space(text())='Add New Course']")
btn_AddNewCourse.click()

fld_Image=driver.find_element(By.XPATH,"//input[@id='thumbnail']")

#os.getcwd() will give the current working directory
fld_Image.send_keys(os.getcwd()+"//GIT-Workflow.png")

txt_CourseName=driver.find_element(By.XPATH,"//h3[text()='Course Name']/following-sibling::input")
txt_CourseName.send_keys("Selenium Automation")

txt_CourseDescription=driver.find_element(By.XPATH,"//h3[text()='Description']/following-sibling::textarea")
txt_CourseDescription.send_keys("This is a Selenium Automation Course")

txt_CourseInstructor=driver.find_element(By.XPATH,"//h3[text()='Instructor']/following-sibling::input")
txt_CourseInstructor.send_keys("Mukesh")

txt_CoursePrice=driver.find_element(By.XPATH,"//h3[text()='Price']/following-sibling::input")
txt_CoursePrice.clear()
txt_CoursePrice.send_keys("500")

txt_CourseStartDate=driver.find_element(By.NAME,"startDate")
txt_CourseStartDate.clear()
txt_CourseStartDate.send_keys("05-01-2025")

txt_CourseEndDate=driver.find_element(By.NAME,"endDate")
txt_CourseEndDate.clear()
txt_CourseEndDate.send_keys("05-01-2026")

btn_SelectCategory=driver.find_element(By.XPATH,"//div[text()='Select Category']")
btn_SelectCategory.click()

time.sleep(3)

btn_Selnium=driver.find_element(By.XPATH,"//button[text()='Selenium']")
btn_Selnium.click()

btn_Save=driver.find_element(By.XPATH,"//button[text()='Save']")
btn_Save.click()

assert len(driver.find_elements(By.XPATH,"//td[text()='Selenium Automation']"))!=0

cbx_Course=driver.find_element(By.XPATH,"//td[text()='Selenium Automation']/preceding-sibling::td/descendant::input")
cbx_Course.click()

btn_DeleteCourse=driver.find_element(By.XPATH,"//td[text()='Selenium Automation']/following-sibling::td/descendant::button[text()='Delete']")
btn_DeleteCourse.click()

try:
    img_Menus=driver.find_element(By.XPATH,"//img[@alt='menu']")
    img_Menus.click()
except ElementClickInterceptedException:
    time.sleep(5)
    img_Menus = driver.find_element(By.XPATH, "//img[@alt='menu']")
    img_Menus.click()

while len(driver.find_elements(By.XPATH,"//button[text()='Sign out']"))==0:
    time.sleep(4)

btn_Logout=driver.find_element(By.XPATH,"//button[text()='Sign out']")
btn_Logout.click()

time.sleep(2)

print(driver.current_url)
assert "login" in driver.current_url

time.sleep(10)