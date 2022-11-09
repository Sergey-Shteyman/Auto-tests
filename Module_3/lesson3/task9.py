import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/registration1.html")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


def test_exception2():
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/registration2.html")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
