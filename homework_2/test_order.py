from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from locators import HomePageLocators as HL


def test_positive_make_an_order(browser_with_auth):
    '''Совершение заказа с корректными данными'''

    exp_text = 'Thank you for your order!'
    info = ('Оксана', 'Михальчук', '40-123')

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
