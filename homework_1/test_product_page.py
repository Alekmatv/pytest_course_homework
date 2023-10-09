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


def test_page_product_from_image(browser):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по картинке'''

    exp_name = 'Sauce Labs Backpack'

    image = browser.find_element(By.ID, 'item_4_img_link')
    image.click()

    time.sleep(2)

    product_name = browser.find_element(By.CLASS_NAME,
                                        'inventory_details_name')

    assert product_name.text == exp_name, 'Некорректное имя товара'


def test_page_product_from_name(browser):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по названию'''

    exp_name = 'Sauce Labs Backpack'

    image = browser.find_element(By.ID, 'item_4_title_link')
    image.click()

    time.sleep(2)

    product_name = browser.find_element(By.CLASS_NAME,
                                        'inventory_details_name')

    assert product_name.text == exp_name, 'Некорректное имя товара'
