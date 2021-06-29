import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

options = Options() 
options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) 
browser = webdriver.Chrome(options=options) 

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: russian or english")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "edge":
        print("\nstart firefox browser for test..")
        browser = Edge(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    yield browser
    print("\nquit browser..")
    browser.quit()