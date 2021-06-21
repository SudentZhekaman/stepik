import pytest
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
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