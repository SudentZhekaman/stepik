import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(20)
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('nlink', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, nlink):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{nlink}/step/1"
    browser.get(link)
    input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    input.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    feedback = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))) 
    assert feedback.text == "Correct!"

