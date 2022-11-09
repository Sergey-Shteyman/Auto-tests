from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def test_site() -> str:
    link = "http://suninjuly.github.io/registration2.html"
    # link = "link = http://suninjuly.github.io/registration1.html"
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


class TestAbs(unittest.TestCase):

    def test_test(self):
        welcome_text = test_site()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
