import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser

    browser.quit()


@pytest.fixture
def browser_headless():
    options = Options()
    options.add_argument('--headless')

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


@pytest.fixture
def browser_implicitly_wait():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)

    return wait
