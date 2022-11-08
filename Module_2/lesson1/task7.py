from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    treasure_value = treasure.get_attribute("valuex")
    result = calc(treasure_value)

    input_label = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_label.send_keys(result)

    checkbox_the_robot = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox_the_robot.click()

    radio_btn_the_robot = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radio_btn_the_robot.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()