from selenium.webdriver.common.by import By


def clickOnElement(driver,xpath):
    driver.find_element(By.XPATH,xpath).click()

def enterText(driver,xpath,data):
    driver.find_element(By.XPATH,xpath).send_keys(data)
