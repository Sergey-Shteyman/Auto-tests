from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), "$100")
    )
    book_btn = browser.find_element(By.CSS_SELECTOR, 'button#book')
    book_btn.click()

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
