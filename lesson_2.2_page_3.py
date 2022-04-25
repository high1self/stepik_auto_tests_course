from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

try:

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим х y
    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    x = int(x)
    y = int(y)

    # получаем сумму
    def sum(x, y):
        return str(x + y)
    # выбираем из списка значение = sum
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum(x,y))

    submit = browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
