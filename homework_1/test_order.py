import time

from selenium.webdriver.common.by import By


def test_positive_make_an_order(browser_with_auth):
    '''Совершение заказа с корректными данными'''

    exp_text = 'Thank you for your order!'
    browser = browser_with_auth

    button_add_to_cart_first = browser.find_element(
        By.ID,
        'add-to-cart-sauce-labs-backpack')
    button_add_to_cart_first.click()

    button_shopping_cart = browser.find_element(By.CLASS_NAME,
                                                'shopping_cart_link')
    button_shopping_cart.click()

    button_checkout = browser.find_element(By.ID, 'checkout')
    button_checkout.click()

    # -------Ввод данных заказчика-------

    first_name_field = browser.find_element(By.ID, 'first-name')
    first_name_field.send_keys('Oksana')

    last_name_field = browser.find_element(By.ID, 'last-name')
    last_name_field.send_keys('Morozova')

    postal_code_field = browser.find_element(By.ID, 'postal-code')
    postal_code_field.send_keys('40-123')

    time.sleep(1)

    # ------------------------------------

    button_continue = browser.find_element(By.ID, 'continue')
    button_continue.click()

    button_finish = browser.find_element(By.ID, 'finish')
    button_finish.click()

    complete_header = browser.find_element(By.CLASS_NAME, 'complete-header')

    time.sleep(3)

    assert complete_header.text == exp_text, 'Некорректное сообщение об успехе'
