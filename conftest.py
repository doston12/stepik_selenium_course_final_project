import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test...")
    language = request.config.getoption("language")
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": str(language)})
    browser = webdriver.Chrome(options=chrome_options)

    yield browser
    print("\nquit browser...")
    browser.quit()
