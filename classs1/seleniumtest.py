from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
time.sleep(2)
driver.quit()
