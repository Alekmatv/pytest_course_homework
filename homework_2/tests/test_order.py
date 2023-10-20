from pages import HomePage, CartPage, CheckoutPage
from locators import HomePageLocators as HL
from data import Info, Text, Error


def test_positive_make_an_order(browser_with_auth):
    '''Совершение заказа с корректными данными'''

    exp_text = Text.SUCCESSFUL_ORDER
    info = Info.get_positive_cyrillic_info()

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.add_to_cart(*HL.BACKPACK_ADD_TO_CART)
    home_page.open_cart()

    cart_page = CartPage(home_page.browser, home_page.browser.current_url)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(cart_page.browser,
                                 cart_page.browser.current_url)
    checkout_page.fill_in_the_informations(*info)
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.get_complete_text(
                ) == exp_text, 'Некорректное сообщение об успехе'


def test_negative_post_code_make_an_order(browser_with_auth):
    '''Совершение заказа с некорректными данными'''

    exp_error_text = Error.POSTAL_CODE
    info = Info.get_negative_post_code_cyrillic_info()

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.add_to_cart(*HL.BACKPACK_ADD_TO_CART)
    home_page.open_cart()

    cart_page = CartPage(home_page.browser, home_page.browser.current_url)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(cart_page.browser,
                                 cart_page.browser.current_url)
    checkout_page.fill_in_the_informations(*info)
    checkout_page.click_continue()

    assert checkout_page.is_error(), 'Нет сообщения об ошибке'

    assert checkout_page.get_error_message(
                ) == exp_error_text, 'Некорректное сообщение об ошибке'
