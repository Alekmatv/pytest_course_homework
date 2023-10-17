from pages import LoginPage


LINK_AUTH = 'https://www.saucedemo.com/'


def test_positive_authorization(browser):

    exp_url = 'https://www.saucedemo.com/inventory.html'
    login = 'standard_user'
    password = 'secret_sauce'

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login(login, password)

    assert browser.current_url == exp_url, 'Авторизоваться не удалось!'


def test_negative_authorization(browser):

    exp_error_text = 'Epic sadface: Username and password ' \
                     'do not match any user in this service'
    login = 'user'
    password = 'user'

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login(login, password)

    assert login_page.is_error(), 'Нет сообщения об ошибке'

    error_message = login_page.get_error_message()

    assert error_message == exp_error_text, 'Некорректное сообщение об ошибке'
