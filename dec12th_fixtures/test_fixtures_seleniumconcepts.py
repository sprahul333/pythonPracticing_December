import pytest

from selenium import webdriver

#Fixtures are used to setup and teardown the test environment

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#setup is the fixture name which is passed as an argument to the test method
#setup fixture will be executed before the test method
#yield driver is used as a return statement and passes the driver object to the test method
#After the test method is executed, the teardown activity will be performed
def test_googleTitle(setup):
    setup.get("https://www.google.com")
    print(setup.title)
    assert setup.title=="Google"

def test_facebookTitle(setup):
    setup.get("https://www.facebook.com")
    print(setup.title)
    assert setup.title.lower()=="Facebook - Log In or Sign Up".lower()