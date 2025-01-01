from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://freelance-learn-automation.vercel.app/")

driver.set_page_load_timeout(300)
driver.implicitly_wait(10)

title=driver.title

if(title.__contains__("Automation")):
    print("Passed")

else:
    print("Failed")