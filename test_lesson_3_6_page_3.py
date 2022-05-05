import pytest
from selenium import webdriver
import time
import math

@pytest.mark.parametrize(
        'page_list',
        ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"])
class TestPages:
    def test_open_page(self, browser, page_list):
        try:
            answer = math.log(int(time.time()))
            link = page_list
            browser.get(link)
            browser.find_element_by_css_selector(".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(answer)
            browser.find_element_by_css_selector(".submit-submission").click()
            check = browser.find_element_by_css_selector('.smart-hints__hint').text
            result = check
            assert 'Correct!' in check, f"Результат отличается от Correct! {result}"
        finally:
            browser.quit()