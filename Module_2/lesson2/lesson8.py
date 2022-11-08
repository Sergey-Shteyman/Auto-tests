from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_name_label = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name_label.send_keys("Sergey")

    last_name_label = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name_label.send_keys("Shteyman")

    email_label = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email_label.send_keys("Serega.shteiman@yandex.ru")

    insert_file = browser.find_element(By.CSS_SELECTOR, 'input#file')
    # current_dir = os.path.abspath(os.path.dirname(__file__)) # Еще один способо узнать абсолютный путь
                                                               # до текущей директории
    current_dir = os.path.abspath(os.path.join("..", "lesson2"))
    file_path = os.path.join(current_dir, 'file.txt')
    insert_file.send_keys(file_path)

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
