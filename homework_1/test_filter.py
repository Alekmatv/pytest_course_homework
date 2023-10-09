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


def test_sort_by_a_to_z(browser):
    '''Сортировка от A до Z'''

    sort_container = browser.find_element(By.CLASS_NAME,
                                          'product_sort_container')
    sort_container.click()

    option_az = browser.find_element(By.CSS_SELECTOR, 'option[value="az"]')
    option_az.click()

    time.sleep(2)

    # -----------Первые 3 элемента, которые вернул сайт-----------

    items = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    items_names = [item.text for item in items[:3]]

    # -------------------------------------------------------------

    sorted_items = sorted(items_names)

    assert items_names == sorted_items, 'Неправильная сортировка'


def test_sort_by_z_to_a(browser):
    '''Сортировка от Z до A'''

    sort_container = browser.find_element(By.CLASS_NAME,
                                          'product_sort_container')
    sort_container.click()

    option_za = browser.find_element(By.CSS_SELECTOR, 'option[value="za"]')
    option_za.click()

    time.sleep(2)

    # -----------Первые 3 элемента, которые вернул сайт-----------

    items = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    items_names = [item.text for item in items[:3]]

    # -------------------------------------------------------------

    sorted_items = sorted(items_names, reverse=True)

    assert items_names == sorted_items, 'Неправильная сортировка'


def test_sort_by_low_to_high(browser):
    '''Сортировка по возрастанию цены'''

    sort_container = browser.find_element(By.CLASS_NAME,
                                          'product_sort_container')
    sort_container.click()

    option_za = browser.find_element(By.CSS_SELECTOR, 'option[value="lohi"]')
    option_za.click()

    time.sleep(2)

    # -----------Первые 3 элемента, которые вернул сайт-----------

    items = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    items_prices = [float(item.text[1:]) for item in items[:3]]

    # -------------------------------------------------------------

    sorted_items = sorted(items_prices)

    assert items_prices == sorted_items, 'Неправильная сортировка'


def test_sort_by_high_to_low(browser):
    '''Сортировка по убыванию цены'''

    sort_container = browser.find_element(By.CLASS_NAME,
                                          'product_sort_container')
    sort_container.click()

    option_za = browser.find_element(By.CSS_SELECTOR, 'option[value="hilo"]')
    option_za.click()

    time.sleep(2)

    # -----------Первые 3 элемента, которые вернул сайт-----------

    items = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    items_prices = [float(item.text[1:]) for item in items[:3]]

    # -------------------------------------------------------------

    sorted_items = sorted(items_prices, reverse=True)

    assert items_prices == sorted_items, 'Неправильная сортировка'
