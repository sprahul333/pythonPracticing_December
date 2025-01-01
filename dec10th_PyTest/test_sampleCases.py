from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(300)
    driver.implicitly_wait(10)
    driver.get("https://freelance-learn-automation.vercel.app/login")
    txt_Email=driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']")
    wait=WebDriverWait(driver,timeout=10)
    wait.until(EC.element_to_be_clickable(txt_Email))
    assert txt_Email.is_displayed()
    txt_Email.send_keys("admin@email.com")
    txt_Password=driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']")
    wait=WebDriverWait(driver,timeout=10,poll_frequency=1)
    wait.until(lambda e:txt_Password.send_keys("admin@123") or True)
    driver.quit() #Closes the browser



def test_logout():
    print("Logout Test")