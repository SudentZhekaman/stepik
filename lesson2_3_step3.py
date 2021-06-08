from selenium import webdriver
import math
import time 

def calc(x1):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    x1 = int(x)
    y = calc(x1)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла