import time

from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

print(driver) #Prints the object reference, session id, browser name, browser version

time.sleep(5) #It is used to wait for 5 seconds
print(type(driver))

# Navigate to the application home page
driver.get("http://www.google.com")

#For Chrome Browser and Edge Browser it is different
# driver = webdriver.Chrome()
# driver = webdriver.Edge()

#For all the chromium based browsers , it will close the browser automatically after the execution
#Clean up the driver instance automatically

#Only for Firefox Browser we need to close the browser

driver.quit() #It is used to close the browser

driver1 = webdriver.Chrome()

#.get() is used to navigate to the URL until the page is loaded
driver1.get("http://www.google.com")

#It is used to get the title of the page
print(f'Title of the window is: {driver1.title}')

if(driver1.title == "Google"):
    print("Title of the page is correct")

#It is used to get the current URL of the page
print(f'URL of the application launched is: {driver1.current_url}')

#It is used to get the page source of the page
print(driver1.page_source)

#It is used to get the window handle of the page
print(f'Current Window Handle is {driver1.current_window_handle}')

#Maximize the window
driver1.maximize_window()

#Minimize the window
driver1.minimize_window()

#It is used to refresh the page
driver1.refresh()

driver1.maximize_window()