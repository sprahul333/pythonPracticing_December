import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://freelance-learn-automation.vercel.app/")
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()

@pytest.mark.regression
@pytest.mark.parametrize("emailId, password",
                         [
                             ("admin@email.com","admin@123"),
                             ("admin@email.com", "admin@123")
                         ]
                         )
def test_userLogin(driver, emailId, password):
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='navbar-menu']/descendant::img[@alt='menu']").click()
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(emailId)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Sign in']").click()


