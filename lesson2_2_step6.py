from selenium import webdriver
import math
import time

def calc(x1):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    x1 = int(x)
    y = calc(x1)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    