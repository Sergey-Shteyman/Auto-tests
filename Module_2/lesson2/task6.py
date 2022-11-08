from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    x_value = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    result = calc(x_value)

    input_label = browser.find_element(By.CSS_SELECTOR, "input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_label)
    input_label.send_keys(result)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robot_radio_btn = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio_btn)
    robot_radio_btn.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
