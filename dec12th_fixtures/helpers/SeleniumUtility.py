from selenium.webdriver.common.by import By


class SeleniumUtility:

    def __init__(self,driver):
        self.driver=driver

    def clickOnElement(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()

    def enterText(self,xpath,data):
        self.driver.find_element(By.XPATH,xpath).send_keys(data)