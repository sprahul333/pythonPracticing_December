import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

driver.maximize_window()

#Page Load Timeout --> The time that the script will wait for the page to load
driver.set_page_load_timeout(300)

#Script Timeout --> The time that the script will wait for the script to execute
driver.set_script_timeout(30)

#Checks if the element is present on the page or not
#Checks if element.is_displayed() is true or false
#Default polling time is 0.25 seconds
#Default Polling time in explicit wait is 0.5 seconds
driver.implicitly_wait(10)

#Prints the capabilities of the browser
print(driver.capabilities)

driver.get("https://freelance-learn-automation.vercel.app/login")

txt_Email=driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']");
#Explicit Wait
#Explicit Wait is used to wait for a particular condition to be met
wait=WebDriverWait(driver,timeout=10)
#Smart Wait and not global
#Applied at an element level
wait.until(EC.element_to_be_clickable(txt_Email))

print(txt_Email.is_displayed())

txt_Email.send_keys("admin@email.com")

#Fluent wait:
#It is a type of explicit wait
#It is used to wait for a particular condition to be met
#Fluent Wait is used for the web elements

txt_Password=driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']")
wait=WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=[ElementClickInterceptedException,NoSuchElementException])
wait.until(lambda e:txt_Password.send_keys("admin@123") or True)

#Chrome Options
#Chrome Options is a class in Selenium
#It is used to set the properties of the Chrome Browser
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors") #Ignores the SSL Certificate Errors
chrome_options.add_argument("--disable-popup-blocking") #Disables the Pop Up Blocking

#Headless Browser
#Headless Browser is a browser that runs without a GUI
#It runs in the background

chrome_options.add_argument("--headless=new")

prefs={"profile.default_content_setting_values.notifications":2, #Disables the notifications
       "profile.default_content_setting_values.geolocation":2, #Disables the geolocation
        "profile.default_content_setting_values.media_stream":2, #Disables the media stream
        "profile.default_content_setting_values.automatic_downloads":2} #Disables the automatic downloads

chrome_options.add_experimental_option("prefs",prefs)

chrome_options.add_experimental_option("excludeSwitches",["enable-automation"]) #Disables the automation info bar

driver=webdriver.Chrome(chrome_options)

driver.get("https://freelance-learn-automation.vercel.app/login")

time.sleep(10)
