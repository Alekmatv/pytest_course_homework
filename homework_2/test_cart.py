from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from locators import HomePageLocators as HL, CartPageLocators as CL


def test_adding_product_catalog(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога'''

    exp_text = 'Sauce Labs Backpack'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.add_to_cart(*HL.BACKPACK_ADD_TO_CART)
    home_page.open_cart()

    cart_page = CartPage(home_page.browser, home_page.browser.current_url)
    item_name = cart_page.get_item_name(*CL.BACKPACK_NAME)

    assert item_name == exp_text, 'Товар не был добавлен в корзину'

    assert len(cart_page.get_all_items()) == 1, 'Количество товаров не равно 1'


def test_removing_product_catalog(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из каталога и удалить'''

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.add_to_cart(*HL.BACKPACK_ADD_TO_CART)
    home_page.open_cart()

    cart_page = CartPage(home_page.browser, home_page.browser.current_url)
    cart_page.remove_item(*CL.REMOVE_BACKPACK)

    assert len(cart_page.get_all_items()
               ) == 0, 'Товар не был удален из корзины'


def test_adding_product_page(browser_with_auth):
    '''Добавить товар (Sauce Labs Backpack) в корзину из карточки товара'''

    exp_text = 'Sauce Labs Backpack'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.click_on_image(*HL.BACKPACK_IMAGE)

    product_page = ProductPage(home_page.browser,
                               home_page.browser.current_url)
    product_page.add_to_cart()
    product_page.open_cart()

    cart_page = CartPage(product_page.browser,
                         product_page.browser.current_url)
    item_name = cart_page.get_item_name(*CL.BACKPACK_NAME)

    assert item_name == exp_text, 'Товар не был добавлен в корзину'

    assert len(cart_page.get_all_items()) == 1, 'Количество товаров не равно 1'


def test_removing_product_page(browser_with_auth):
    """Добавить товар (Sauce Labs Backpack) в корзину
       из карточки товара и удалить"""

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.click_on_image(*HL.BACKPACK_IMAGE)

    product_page = ProductPage(home_page.browser,
                               home_page.browser.current_url)
    product_page.add_to_cart()
    product_page.open_cart()

    cart_page = CartPage(product_page.browser,
                         product_page.browser.current_url)
    cart_page.remove_item(*CL.REMOVE_BACKPACK)

    assert len(cart_page.get_all_items()
               ) == 0, 'Товар не был удален из корзины'
