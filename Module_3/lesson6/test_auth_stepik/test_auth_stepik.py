import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestTaskOnsStepik:

    urls = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('links', urls)
    def test_auth_stepik(self, browser, links):
        """
        Метод, который по очереди открывает ссылки,
        проходит аутентификацию, рассчитывает формулу и воодит правильный ответ.
        Для запуска необходимо ввести логин и пароль от степика.
        По итогу в фале остается фидбек с посланием.
        :param browser: принимает браузер из фикстуры
        :param links: ссылки на сайт
        """
        print("\nstart browser for test suite..")
        browser.get(links)

        browser.implicitly_wait(5)
        btn = browser.find_element(By.CSS_SELECTOR,
                                   "a.ember-view.navbar__auth.navbar__auth_login")
        btn.click()

        browser.implicitly_wait(3)
        login_label = browser.find_element(By.CSS_SELECTOR,
                                           'input[name="login"].ember-text-field.ember-view')
        login_label.send_keys("")  # Your login

        password_label = browser.find_element(By.CSS_SELECTOR,
                                              'input[name="password"].ember-text-field.ember-view')
        password_label.send_keys("")  # Your password

        password_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        password_button.click()

        WebDriverWait(browser, 10).until_not(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.light-tabs.ember-view"))
        )

        text_label = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        text_label.send_keys(str(math.log(int(time.time()))))

        send_answer_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        send_answer_button.click()

        feed_back_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        ).text
        if "Correct!" != feed_back_text:
            with open("feed_backs.txt", "a", encoding='utf-8') as file:
                file.write(feed_back_text)

            decide_again_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
            )
            decide_again_button.click()
        else:
            decide_again_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
            )
            decide_again_button.click()

        time.sleep(5)

# Второе решение. Не смог настроить параметризацию для класса. Пришлось решать в один метод.
# Решил оставить, так как в нем соблюдается принцип единой ответственности, а это круто

# import time
# import math
# import pytest
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
#
#
# class TestAuthStepik:
#
#     # urls = ["https://stepik.org/lesson/236895/step/1",
#     #         "https://stepik.org/lesson/236896/step/1"]
#
#     @classmethod
#     @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
#                                        "https://stepik.org/lesson/236896/step/1"])
#     def setup_class(self, links):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.Chrome()
#         self.browser.get(links)
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()
#
#     def test_visible_login_btn(self):
#         self.browser.implicitly_wait(5)
#         btn = self.browser.find_element(By.CSS_SELECTOR, "#ember32")
#         btn.click()
#
#     def test_input_email(self):
#         self.browser.implicitly_wait(3)
#         login_label = self.browser.find_element(By.ID, "id_login_email")
#         login_label.send_keys("Serega.shteiman@yandex.ru")
#
#     def test_input_password(self):
#         password_label = self.browser.find_element(By.ID, "id_login_password")
#         password_label.send_keys("Shteyman.Sergey1999")
#
#     def test_click_submit_button(self):
#         password_button = self.browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
#         password_button.click()
#
#     def test_pop_ap_disappear(self):
#         WebDriverWait(self.browser, 5).until_not(
#             EC.visibility_of_element_located((By.ID, "ember91"))
#         )
#
#     def test_input_answer_in_text_label(self):
#         text_label = WebDriverWait(self.browser, 5).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
#         )
#         text_label.send_keys(str(math.log(int(time.time()))))
#
#     def test_click_send_answer_button(self):
#         send_answer_button = WebDriverWait(self.browser, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
#         )
#         send_answer_button.click()
#
#     def test_is_correct_answer(self):
#         feed_back_text = WebDriverWait(self.browser, 5).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
#         ).text
#         if "Correct!" != feed_back_text:
#             with open("feed_backs.txt", "a", encoding='utf-8') as file:
#                 file.write(feed_back_text)
#
#             decide_again_button = WebDriverWait(self.browser, 5).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
#             )
#             decide_again_button.click()
#
#             submit_button = WebDriverWait(self.browser, 5).until(
#                 EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.modal-popup__footer :nth-child(1)"))
#             )
#             submit_button.click()
#
#             WebDriverWait(self.browser, 5).until_not(
#                 EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-popup__title"))
#             )
#         else:
#             decide_again_button = WebDriverWait(self.browser, 5).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
#             )
#             decide_again_button.click()
#
#     def test_sleep(self):
#         time.sleep(5)
