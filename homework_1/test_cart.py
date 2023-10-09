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

    browser.close()


def test_adding_product_catalog(browser):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога'''

    exp_text = 'Sauce Labs Backpack'

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_shopping_cart = browser.find_element(By.CLASS_NAME,
                                                'shopping_cart_link')
    button_shopping_cart.click()

    first_product = browser.find_element(By.CLASS_NAME, 'inventory_item_name')

    time.sleep(2)

    assert first_product.text == exp_text, 'Товар не был добавлен в корзину'


def test_removing_product_catalog(browser):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога и удалить'''

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_shopping_cart = browser.find_element(By.CLASS_NAME,
                                                'shopping_cart_link')
    button_shopping_cart.click()

    remove_button = browser.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_button.click()

    product = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')

    time.sleep(2)

    assert len(product) == 0, 'Товар не был удален из корзины'


def test_adding_product_page(browser):
    '''Добавить товар (Sauce Labs Backpack) в корзину из карточки товара'''

    exp_text = 'Sauce Labs Backpack'

    to_product_page = browser.find_element(By.ID, 'item_4_title_link')
    to_product_page.click()

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_shopping_cart = browser.find_element(By.CLASS_NAME,
                                                'shopping_cart_link')
    button_shopping_cart.click()

    first_product = browser.find_element(By.CLASS_NAME, 'inventory_item_name')

    time.sleep(2)

    assert first_product.text == exp_text, 'Товар не был добавлен в корзину'


def test_removing_product_page(browser):

    """Добавить товар (Sauce Labs Backpack) в корзину
       из карточки товара и удалить"""

    to_product_page = browser.find_element(By.ID, 'item_4_title_link')
    to_product_page.click()

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_shopping_cart = browser.find_element(By.CLASS_NAME,
                                                'shopping_cart_link')
    button_shopping_cart.click()

    remove_button = browser.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_button.click()

    product = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')

    time.sleep(2)

    assert len(product) == 0, 'Товар не был удален из корзины'
