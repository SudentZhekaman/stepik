from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='num1']")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("[id='num2']")
    y = y_element.text

    x1 = int(x)
    y1 = int(y)
    xy = x1 + y1
    summa = str(xy) 

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    