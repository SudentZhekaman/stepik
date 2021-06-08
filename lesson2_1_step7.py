from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_css_selector("[id='answer']")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    