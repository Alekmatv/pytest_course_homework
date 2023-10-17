import pytest

from pages.home_page import HomePage
from locators import HomePageLocators as HL


LINK_AUTH = 'https://www.saucedemo.com/'


def test_logout(browser_with_auth):
    '''Выход из аккаунта через бургер меню'''

    exp_url = 'https://www.saucedemo.com/'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.open_burger_menu()
    home_page.click_logout()

    act_url = home_page.browser.current_url

    assert act_url == exp_url, 'Не удалось выйти из системы'


def test_about(browser_with_auth):
    '''Переход на страницу About из бургер меню'''

    exp_url = 'https://saucelabs.com/'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.open_burger_menu()
    home_page.click_about()

    act_url = home_page.browser.current_url

    assert act_url == exp_url, 'Не удалось открыть About'


@pytest.mark.xfail
def test_reset_app_state(browser_with_auth):
    '''Сбросить все состояние'''

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.add_to_cart(*HL.BACKPACK_ADD_TO_CART)
    home_page.open_burger_menu()
    home_page.click_reset()

    assert not home_page.is_badge(), 'Счетчик корзины не исчез'

    assert home_page.is_exist(*HL.BACKPACK_ADD_TO_CART), \
        'Не появилась кнопка Add to cart'
