import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


LINK_AUTH = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_positive_authorization(browser):

    exp_url = 'https://www.saucedemo.com/inventory.html'

    browser.get(LINK_AUTH)

    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(2)

    assert browser.current_url == exp_url, 'Авторизоваться не удалось!'


def test_negative_authorization(browser):

    exp_error_text = 'Epic sadface: Username and password ' \
                     'do not match any user in this service'

    browser.get(LINK_AUTH)

    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys('user')

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('user')

    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()

    error_message = browser.find_element(By.CLASS_NAME,
                                         'error-message-container').text

    time.sleep(2)

    assert error_message == exp_error_text, 'Некорректное сообщение об ошибке'
