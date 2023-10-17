import pytest
from selenium import webdriver

from pages.login_page import LoginPage


LINK_AUTH = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.close()


@pytest.fixture(scope='function')
def browser_with_auth(browser):

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')

    yield browser
