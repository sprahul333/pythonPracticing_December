import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors") #Ignores the SSL Certificate Errors
chrome_options.add_argument("--disable-popup-blocking") #Disables the Pop Up Blocking

#Headless Browser
#Headless Browser is a browser that runs without a GUI
#It runs in the background

#chrome_options.add_argument("--headless=new")

prefs={"profile.default_content_setting_values.notifications":2, #Disables the notifications
       "profile.default_content_setting_values.geolocation":2, #Disables the geolocation
        "profile.default_content_setting_values.media_stream":2, #Disables the media stream
        "profile.default_content_setting_values.automatic_downloads":2} #Disables the automatic downloads

chrome_options.add_experimental_option("prefs",prefs)

chrome_options.add_experimental_option("excludeSwitches",["enable-automation"]) #Disables the automation info bar

driver=webdriver.Chrome(chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)

driver.get("https://freelance-learn-automation.vercel.app/login")

action3=ActionChains(driver)

driver.find_element(By.ID,"email1").send_keys("admin@email.com")

action3.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

action3.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

action3.send_keys(Keys.TAB).perform()

action3.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

action3.send_keys(Keys.ENTER).perform()



time.sleep(30)