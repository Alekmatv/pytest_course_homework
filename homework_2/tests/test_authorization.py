from pages import LoginPage
from data import URL, Username, Password, Error


LINK_AUTH = URL.AUTH
LINK_HOME = URL.HOME


def test_positive_authorization(browser):

    exp_url = LINK_HOME
    login = Username.STANDART
    password = Password.POSITIVE

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login(login, password)

    assert browser.current_url == exp_url, 'Авторизоваться не удалось!'


def test_negative_authorization(browser):

    exp_error_text = Error.AUTH
    login = Username.NEGATIVE
    password = Username.NEGATIVE

    login_page = LoginPage(browser, LINK_AUTH)
    login_page.open()
    login_page.login(login, password)

    assert login_page.is_error(), 'Нет сообщения об ошибке'

    error_message = login_page.get_error_message()

    assert error_message == exp_error_text, 'Некорректное сообщение об ошибке'
