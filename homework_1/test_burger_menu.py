import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


LINK_AUTH = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()

    browser.get(LINK_AUTH)

    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()

    yield browser


def test_logout(browser):
    '''Выход из аккаунта через бургер меню'''

    exp_url = 'https://www.saucedemo.com/'

    button_burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    button_burger_menu.click()

    time.sleep(2)

    button_logout = browser.find_element(By.ID, 'logout_sidebar_link')
    button_logout.click()

    assert browser.current_url == exp_url, 'Не удалось выйти из системы'


def test_about(browser):
    '''Переход на страницу About из бургер меню'''

    exp_url = 'https://saucelabs.com/'

    button_burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    button_burger_menu.click()

    time.sleep(2)

    button_about = browser.find_element(By.ID, 'about_sidebar_link')
    button_about.click()

    assert browser.current_url == exp_url, 'Не удалось открыть About'


def test_reset_app_state(browser):
    '''Сбросить все состояние'''

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    button_burger_menu.click()

    time.sleep(2)

    button_reset = browser.find_element(By.ID, 'reset_sidebar_link')
    button_reset.click()

    shopping_cart_badge = browser.find_elements(
        By.CLASS_NAME, 'shopping_cart_badge')

    assert len(shopping_cart_badge) == 0, \
        'Значок количества товаров в корзине не исчез'

    add_to_cart_button = browser.find_elements(
        By.ID, 'add-to-cart-sauce-labs-backpack')

    assert len(add_to_cart_button) != 0, \
        'Кнопка Add to cart не появилась обратно'
