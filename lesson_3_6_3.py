import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.xfail
@pytest.mark.parametrize('nlink', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, language):
    link = f"https://stepik.org/lesson/{nlink}/step/1"
    browser.get(link)
    input = browser.find_element_by_class_name("textarea")
    input.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    feedback = browser.find_element_by_class_name("smart-hints__hint") 
    assert feedback.text == "Correct"

