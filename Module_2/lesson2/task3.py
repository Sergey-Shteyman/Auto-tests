from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_summand = browser.find_element(By.CSS_SELECTOR, 'span#num1')
    second_summand = browser.find_element(By.CSS_SELECTOR, 'span#num2')
    result = str(int(first_summand.text) + int(second_summand.text))

    input_list = Select(browser.find_element(By.TAG_NAME, 'select'))
    input_list.select_by_value(result)

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()