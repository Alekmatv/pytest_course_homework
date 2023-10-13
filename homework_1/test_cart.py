import time

from selenium.webdriver.common.by import By


def test_adding_product_catalog(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога'''

    exp_text = 'Sauce Labs Backpack'
    browser = browser_with_auth

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


def test_removing_product_catalog(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога и удалить'''

    browser = browser_with_auth

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


def test_adding_product_page(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из карточки товара'''

    exp_text = 'Sauce Labs Backpack'
    browser = browser_with_auth

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


def test_removing_product_page(browser_with_auth):

    """Добавить товар (Sauce Labs Backpack) в корзину
       из карточки товара и удалить"""

    browser = browser_with_auth

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
