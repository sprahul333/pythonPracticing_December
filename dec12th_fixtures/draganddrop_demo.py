from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-automation"]) #Disables the automation info bar
options.add_argument("--start-maximized")

driver2=webdriver.Chrome(options)

driver2.maximize_window()
driver2.implicitly_wait(10)
driver2.set_page_load_timeout(300)

driver2.get("https://jqueryui.com/droppable/")

driver2.switch_to.frame(driver2.find_element(By.XPATH,"//iframe[@class='demo-frame']"))

source=driver2.find_element(By.ID,"draggable")
destination=driver2.find_element(By.ID,"droppable")

actions=ActionChains(driver2)
actions.drag_and_drop(source,destination).perform()

driver2.save_screenshot("DragAndDrop.png")