# Selenium Google Open Script

This project contains a simple Python script using Selenium WebDriver to open Google.com, wait for 2 seconds, and close the browser.

## 💻 Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
time.sleep(2)
driver.quit()
