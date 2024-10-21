import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFIndElementByXPath():
    def locate_by_xpath_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_xpath("//input[@id='login-input]").send_keys("test@test.com")
        time.sleep(4)
    