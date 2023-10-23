import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser

    browser.quit()


@pytest.fixture
def browser_impilicitly_wait():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)

    return wait
