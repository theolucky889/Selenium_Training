import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import by


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://myedit.online/en/photo-editor")
# driver.find_element_by_id('Sign_In_Button').click()
# driver.find_element_by_id('mui-4').send_keys('myedit_premium_credits@cyberlink.com')
driver.find_element(by.ID, 'Sign_In_Button').click()
time.sleep(10)
        
