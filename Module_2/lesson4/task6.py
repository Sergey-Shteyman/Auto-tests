from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "button")

finally:
    time.sleep(1)
    browser.quit()
