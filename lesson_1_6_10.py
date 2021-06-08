from selenium import webdriver
import time
import unittest

class Test(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("first")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("second")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("test@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

     # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
     # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
         # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    
        browser.quit()

    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("first")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("second")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("test@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

     # Проверяем, что смогли зарегистрироваться
     # ждем загрузки страницы
        time.sleep(1)

     # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
     # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertNotEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
  unittest.main()
  unittest.main()
   
