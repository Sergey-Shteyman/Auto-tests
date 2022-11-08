from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    confirm_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    confirm_btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    value_x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    result = calc(value_x)

    input_label = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_label.send_keys(result)

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn')
    submit_btn.click()
finally:
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    browser.quit()
