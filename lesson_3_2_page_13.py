from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By

### ГОВНОЗАДАЧА НЕ ПАШЕТ НИХУЯ БЛЯТЬ.###

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(2)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
                "First" + Keys.ENTER)
            last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(
                "Last" + Keys.ENTER)
            email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
                "mail@mail.com" + Keys.ENTER)

            # Отправляем заполненную форму

            button = browser.find_element(By.XPATH, "button[type='submit']")
            button.click()

            self.assertEqual(browser.current_url, 'http://suninjuly.github.io/registration_result.html?')

            # находим элемент, содержащий текст
            # welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1").text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # self.assertEqual(welcome_text_elt, 'Congratulations! You have successfully registered!')

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(2)
            browser.get(link)
            # Ваш код, который заполняет обязательные поля
            required_elements = browser.find_elements_by_css_selector('input[required]')
            for element in required_elements:
                element.send_keys('required')

            # Отправляем заполненную форму

            button = browser.find_element(By.XPATH, "button[type='submit']")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1").text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text_elt, 'Congratulations! You have successfully registered!')
        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()


