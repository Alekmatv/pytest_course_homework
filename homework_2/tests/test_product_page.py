from pages import HomePage, ProductPage
from locators import HomePageLocators as HL
from data import ProductName


def test_page_product_from_image(browser_with_auth):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по картинке'''

    exp_name = ProductName.BACKPACK

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.click_on_image(*HL.BACKPACK_IMAGE)

    product_page = ProductPage(home_page.browser,
                               home_page.browser.current_url)
    product_name = product_page.get_product_name()

    assert product_name == exp_name, 'Некорректное имя товара'


def test_page_product_from_name(browser_with_auth):
    '''Открытие страницы товара (Sauce Labs Backpack) кликом по названию'''

    exp_name = ProductName.BACKPACK

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.click_on_title(*HL.BACKPACK_TITLE_LINK)

    product_page = ProductPage(home_page.browser,
                               home_page.browser.current_url)
    product_name = product_page.get_product_name()

    assert product_name == exp_name, 'Некорректное имя товара'
