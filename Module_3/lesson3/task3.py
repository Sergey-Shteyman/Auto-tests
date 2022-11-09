from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def registration_site(link: str) -> str:
    browser = webdriver.Chrome()

    browser.get(link)

    input_name = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[1]/input')
    input_name.send_keys("Sergey")

    input_last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    input_last_name.send_keys("Shteyman")

    input_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    input_email.send_keys("Serega.shteiman@yandex.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    time.sleep(5)
    browser.quit()
    return welcome_text


def test_1():
    welcome_text = registration_site("http://suninjuly.github.io/registration1.html")
    assert "Congratulations! You have successfully registered!" == welcome_text, "Error: registration failure"


def test_2():
    welcome_text = registration_site("http://suninjuly.github.io/registration2.html")
    assert "Congratulations! You have successfully registered!" == welcome_text, "Error: registration failure"


if __name__ == "__main__":
    pytest.main()
