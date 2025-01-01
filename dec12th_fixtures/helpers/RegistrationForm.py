import time

from selenium import webdriver

from dec12th_fixtures.helpers.BrowserFactory import BrowserFactory
from dec12th_fixtures.helpers.SeleniumHelper import clickOnElement, enterText
from dec12th_fixtures.helpers.SeleniumUtility import SeleniumUtility

driver=BrowserFactory().getDriver("chrome")

driver.get("https://freelance-learn-automation.vercel.app/login")

#Using encapsulation concept to call the methods from SeleniumHelper class
#as the data is passed as arguments to the methods
seleniumUtility=SeleniumUtility(driver)

seleniumUtility.enterText("//input[@id='email1']","admin@email.com")
seleniumUtility.enterText("//input[@id='password1']","admin@123")
seleniumUtility.clickOnElement("//button[normalize-space(text())='Sign in']")

#Using abstraction concept to call the methods from SeleniumHelper class
# enterText(driver,"//input[@id='email1']","admin1@email.com")
# enterText(driver,"//input[@id='password1']","admin@123")
# clickOnElement(driver,"//button[normalize-space(text())='Submit']")

time.sleep(10)