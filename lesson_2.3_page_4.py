import os
from selenium import webdriver
import time
import math



try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    btn = browser.find_element_by_css_selector(".btn.btn-primary").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

   # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_css_selector("#input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_css_selector("#answer").send_keys(calc(x))

    # Нажать на кнопку "Submit".
    btn = browser.find_element_by_css_selector(".btn.btn-primary")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
