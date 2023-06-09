import time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price_check = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100"))

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "book")
    button.click()

    browser.implicitly_wait(5)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)

    # Отправляем заполненную форму
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(f'{y}')


    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()