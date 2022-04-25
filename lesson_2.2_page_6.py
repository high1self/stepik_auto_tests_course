from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import math

try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим х
    x = browser.find_element_by_css_selector("#input_value").text

    # считаем
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # скроллим вниз

    browser.execute_script("window.scrollBy(0, 200);")
    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    # Выбрать radiobutton "Robots rule!".
    radiobtn = browser.find_element_by_css_selector("#robotsRule").click()
    # Нажать на кнопку "Submit".
    btn = browser.find_element_by_css_selector(".btn.btn-primary")
    btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
