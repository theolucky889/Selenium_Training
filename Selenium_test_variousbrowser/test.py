import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

# Define service and options
# service = Service("E:\Github\Selenium_Training\BrowserDrivers\geckodriver.exe")
service = Service("E:\Github\Selenium_Training\BrowserDrivers\msedgedriver.exe")
options = Options()
# options.add_argument("--headless")  # Run in headless mode (Operates in the background without opening a window)
# driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Firefox(service=service, options=options)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
time.sleep(5)
driver.close()