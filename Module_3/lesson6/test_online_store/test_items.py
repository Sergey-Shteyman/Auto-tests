import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_basket_button(browser):
    """
    Метод, проверяющий наличие кнопки добавить в корзину для сайта.
    Использовать pytest --language=fr test_items.py для запуска теста.
    """
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements(
        By.CSS_SELECTOR,
        'button[type="submit"].btn.btn-lg.btn-primary'), "ERROR: Basket button not found"
    time.sleep(2)
