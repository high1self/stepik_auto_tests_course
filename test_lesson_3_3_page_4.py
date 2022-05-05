from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
import pytest


def test_reg1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        # Ваш код, который заполняет обязательные поля
        required_elements = browser.find_elements_by_css_selector('input[required]')
        for element in required_elements:
            element.send_keys('required')
        #first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
        #    "First" + Keys.ENTER)
        #last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(
        #    "Last" + Keys.ENTER)
        #email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
        #    "mail@mail.com" + Keys.ENTER)

        # Отправляем заполненную форму

        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert 'Congratulations! You have successfully registered!' in welcome_text_elt

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_reg2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        #required_elements = browser.find_elements_by_css_selector('input[required]')
        #for element in required_elements:
        #    element.send_keys('required')

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
            "First" + Keys.ENTER)
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(
           "Last" + Keys.ENTER)
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
           "mail@mail.com" + Keys.ENTER)

        # Отправляем заполненную форму

        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert 'Congratulations! You have successfully registered!' in welcome_text_elt
    finally:
        browser.quit()

if __name__ == "__main__":
   pytest.main()


