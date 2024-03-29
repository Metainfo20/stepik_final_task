import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

languages = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr",
             "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk",
             "zh-hans"]


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help=f"Choose language. Supporting languages: \n{languages}",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()

