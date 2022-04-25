from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math

try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считаем х
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # находим х
    x_element = browser.find_element_by_css_selector("#treasure")
    # получаем значение х
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ввести ответ в текстовое поле.
    put_text = browser.find_element_by_css_selector("#answer").send_keys(y)
    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    # Выбрать radiobutton "Robots rule!".
    radiobtn = browser.find_element_by_css_selector("#robotsRule").click()
    # Нажать на кнопку Submit.
    submit = browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()