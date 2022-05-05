from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # Нажать на кнопку когда цена будет 100 долларов
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    btn = browser.find_element(By.ID, "book")
    btn.click()


    # решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer").send_keys(calc(x))

    # Нажать на кнопку "Submit".
    submit = browser.find_element(By.ID,"solve")
    submit.click()

finally:
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
