import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)

def switchToFirstWindow(driver):
    allWindows=driver.window_handles
    driver.switch_to.window(allWindows[0])

def switchToLastWindow(driver):
    allWindows=driver.window_handles
    driver.switch_to.window(allWindows[-1])

driver.get("https://www.cricbuzz.com")

driver.save_screenshot("Cricbuzz.png")

# Scroll down the page
driver.execute_script("window.scrollBy(0, 1000)")

#Scroll up the page
driver.execute_script("window.scrollBy(0, -1000)")

action1=ActionChains(driver)
#Use of Mouse Hover and click
action1.move_to_element(driver.find_element(By.LINK_TEXT,"AUS vs IND - Live")).click().perform()

#Double click
action1.double_click(driver.find_element(By.LINK_TEXT,"Scorecard")).perform()

driver.save_screenshot("Scorecard.png")

listOfPlayers=driver.find_elements(By.XPATH,"//div[contains(@class,'cb-scrd-itms')]/descendant::a[contains(@title,'View profile')]")

for i in range(len(listOfPlayers)):
    try :
        player=driver.find_elements(By.XPATH,"//div[contains(@class,'cb-scrd-itms')]/descendant::a[contains(@title,'View profile')]")[i]
        playerName=player.text
        action1.move_to_element(player).key_down(Keys.CONTROL).click().perform()
        switchToLastWindow(driver)
        driver.save_screenshot(f'{playerName}.png')
        time.sleep(5)
        switchToFirstWindow(driver)
        listOfPlayers = driver.find_elements(By.XPATH,"//div[contains(@class,'cb-scrd-itms')]/descendant::a[contains(@title,'View profile')]")

    except StaleElementReferenceException as e:
        print("Element is not attached to the page document")





time.sleep(10)
