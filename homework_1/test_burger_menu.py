import time

from selenium.webdriver.common.by import By


LINK_AUTH = 'https://www.saucedemo.com/'


def test_logout(browser_with_auth):
    '''Выход из аккаунта через бургер меню'''

    exp_url = 'https://www.saucedemo.com/'
    browser = browser_with_auth

    button_burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    button_burger_menu.click()

    time.sleep(2)

    button_logout = browser.find_element(By.ID, 'logout_sidebar_link')
    button_logout.click()

    assert browser.current_url == exp_url, 'Не удалось выйти из системы'


def test_about(browser_with_auth):
    '''Переход на страницу About из бургер меню'''

    exp_url = 'https://saucelabs.com/'
    browser = browser_with_auth

    button_burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    button_burger_menu.click()

    time.sleep(2)

    button_about = browser.find_element(By.ID, 'about_sidebar_link')
    button_about.click()

    assert browser.current_url == exp_url, 'Не удалось открыть About'


def test_reset_app_state(browser_with_auth):
    '''Сбросить все состояние'''

    browser = browser_with_auth

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
