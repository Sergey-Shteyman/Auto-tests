from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

required_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, str(required_text))
    button.click()
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()