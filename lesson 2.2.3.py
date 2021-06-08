from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

num1 = browser.find_element_by_id("num1")
num1_text = num1.text
x = int(num1_text)

num2 = browser.find_element_by_id("num2")
num2_text = num2.text
y = int(num2_text)

sum_el = x + y
sum_el_text = str(sum_el)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum_el_text)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(30)
   
browser.quit()
