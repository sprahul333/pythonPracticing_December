from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver2=wd.Chrome()

driver2.get("https://www.cricbuzz.com")

driver2.maximize_window()
driver2.implicitly_wait(10)
driver2.set_page_load_timeout(300)

listOfLinks=driver2.find_elements(By.TAG_NAME,"a")

for ele in listOfLinks:
    if(ele.text != ''):
        print(ele.text)