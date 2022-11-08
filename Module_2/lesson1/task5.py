from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value")
    x = x_element.text
    result = calc(x)

    input_label = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_label.send_keys(result)

    checkbox_the_robot = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotCheckbox"]')
    checkbox_the_robot.click()

    radio_btn_the_robot = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotsRule"]')
    radio_btn_the_robot.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
