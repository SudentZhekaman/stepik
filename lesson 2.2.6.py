from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button1 = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button1)



option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

   
time.sleep(30)
   
browser.quit()

