from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_name = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[1]/input')
    input_name.send_keys("Sergey")
    input_last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    input_last_name.send_keys("Shteyman")

    input_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    input_email.send_keys("Serega.shteiman@yandex.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
