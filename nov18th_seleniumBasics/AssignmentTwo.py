from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://freelance-learn-automation.vercel.app/login")

driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

error_msg=driver.find_element(By.CLASS_NAME,"errorMessage").text

if(error_msg == "Email and Password is required"):
    print("Passed")

else:
    print("Failed")