from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    magic_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    magic_btn.click()

    windows = browser.window_handles
    browser.switch_to.window(windows[1])

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
