import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default='en', help="Set a locale.")


@pytest.fixture(scope="function")
def browser(request):
    locale = request.config.getoption("language")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': locale})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
