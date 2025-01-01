from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.set_page_load_timeout(300)
driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space(.)='Login']").click()

url=driver.current_url

if(url.__contains__("dashboard")):
    print("Login Successful")
else:
    print("Login Failed")