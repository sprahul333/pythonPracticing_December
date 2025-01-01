import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://freelance-learn-automation.vercel.app/signup")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.regression
@pytest.mark.parametrize("name,email,password,interest,statename,hobbiesname",
                         [
                             # ("laks","laks@gmail.com","laks@123","Selenium","Karnataka","Reading"),
                             # ("pravar","pravar@gmail.com","laks@123","Selenium","Andhra Pradesh","Reading"),
                             ("havish1", "havish1@gmail.com", "laks@123", "Selenium", "Karnataka", "Reading")
                         ])
def test_createuser(driver, name, email, password, interest, statename, hobbiesname):
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//label[normalize-space()='" + interest + "']").click()
    state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
    state.select_by_visible_text(statename)
    hobbies = Select(driver.find_element(By.XPATH, "//select[@id='hobbies']"))
    hobbies.select_by_visible_text(hobbiesname)
    actions=ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH, "//button[@type='submit']")).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)
    str1 = driver.find_element(By.XPATH, "//div[text()='Signup successfully, Please login!']").is_displayed()
    assert str1, "Create User Failed"
