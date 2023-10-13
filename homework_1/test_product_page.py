import time

from selenium.webdriver.common.by import By


def test_page_product_from_image(browser_with_auth):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по картинке'''

    exp_name = 'Sauce Labs Backpack'
    browser = browser_with_auth

    image = browser.find_element(By.ID, 'item_4_img_link')
    image.click()

    time.sleep(2)

    product_name = browser.find_element(By.CLASS_NAME,
                                        'inventory_details_name')

    assert product_name.text == exp_name, 'Некорректное имя товара'


def test_page_product_from_name(browser_with_auth):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по названию'''

    exp_name = 'Sauce Labs Backpack'
    browser = browser_with_auth

    image = browser.find_element(By.ID, 'item_4_title_link')
    image.click()

    time.sleep(2)

    product_name = browser.find_element(By.CLASS_NAME,
                                        'inventory_details_name')

    assert product_name.text == exp_name, 'Некорректное имя товара'
