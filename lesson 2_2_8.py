import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname("__file__"))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)

    # Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
input1.send_keys("first")
input2 = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
input2.send_keys("second")
input3 = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
input3.send_keys("test@mail.ru")



element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

   
button = browser.find_element_by_css_selector("button.btn")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(20)
    # закрываем браузер после всех манипуляций
browser.quit()
