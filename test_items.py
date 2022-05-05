import pytest
from selenium import webdriver
import time

def test_items(browser):
    try:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(10)
        assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
            'Кнопка добавления товара в корзину отсутствует'
    finally:
        browser.quit()