import os
from selenium import webdriver
import time


try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    firstname = browser.find_element_by_xpath("//input[@name='firstname']").send_keys("First")
    lastname = browser.find_element_by_xpath("//input[@name='lastname']").send_keys("Last")
    email = browser.find_element_by_xpath("//input[@name='email']").send_keys("first@gmail.com")

    # создание файла
    open("test.txt", 'a').close()

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    load_click = browser.find_element_by_css_selector("#file").send_keys(file_path)

    # удаляем файл
    os.remove("test.txt")  # удаляем

    # Нажать кнопку "Submit"
    btn = browser.find_element_by_css_selector(".btn.btn-primary")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
