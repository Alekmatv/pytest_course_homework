import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from data import URL, Username, Password


LINK_AUTH = URL.AUTH


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.close()


@pytest.fixture(scope='function')
def browser_with_auth(browser):

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login(Username.STANDART, Password.POSITIVE)

    yield browser
