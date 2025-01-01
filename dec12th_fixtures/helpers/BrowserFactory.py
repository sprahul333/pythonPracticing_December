from selenium import webdriver
class BrowserFactory:

    #Return the driver object based on the parameter passed

    def getDriver(self,browserName):
        if browserName.lower()=="chrome":
            driver=webdriver.Chrome()
        elif browserName.lower()=="firefox":
            driver=webdriver.Firefox()
        elif browserName.lower()=="ie":
            driver=webdriver.Ie()
        else:
            driver=webdriver.Edge()

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(300)
        driver.maximize_window()
        return driver