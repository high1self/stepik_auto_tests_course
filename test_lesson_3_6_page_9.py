import pytest
from selenium import webdriver
import time

def test_items(browser):
    try:
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        browser.get(link)
        add_btn = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket").text
        time.sleep(10)
        assert 'Добавить в корзину' in add_btn, f"Результат отличается | {add_btn}"
    finally:
        browser.quit()