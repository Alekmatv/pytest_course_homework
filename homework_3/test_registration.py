import time

from selenium.webdriver.support import expected_conditions as EC
import pytest

from data import URL, Text, User, Locator as LC


def test_registration_with_expected_conditions(browser, wait):
    browser.get(URL.URL_REGISTRATION)

    header = browser.find_element(*LC.HEADER)

    assert header.text == Text.HEADER_TEXT, "Некорректный текст в заголовке"

    start_button = wait.until(EC.element_to_be_clickable(LC.START_BUTTON))
    start_button.click()

    login_field = browser.find_element(*LC.LOGIN_FIELD)
    login_field.send_keys(User.get_username())

    password_field = browser.find_element(*LC.PASSWORD_FIELD)
    password_field.send_keys(User.get_password())

    checkbox = browser.find_element(*LC.CHECKBOX_AGREE)
    checkbox.click()

    register_button = browser.find_element(*LC.REGISTER_BUTTON)
    register_button.click()

    loader = browser.find_elements(*LC.LOADER)

    assert len(loader) > 0, "Индикатор загрузки не появился"

    successful_message = wait.until(
        EC.visibility_of_element_located(LC.SUCCESS_MESSAGE))

    assert (
        successful_message.text == Text.SUCCESSFUL_REGISTRATION
    ), "Некорректное сообщение об успешной регистрации"


@pytest.mark.xfail
def test_registration_with_impilicitly_wait(browser_impilicitly_wait):
    browser = browser_impilicitly_wait

    browser.get(URL.URL_REGISTRATION)

    header = browser.find_element(*LC.HEADER)

    assert header.text == Text.HEADER_TEXT, "Некорректный текст в заголовке"

    start_button = browser.find_element(*LC.START_BUTTON)
    start_button.click()

    login_field = browser.find_element(*LC.LOGIN_FIELD)
    login_field.send_keys(User.get_username())

    password_field = browser.find_element(*LC.PASSWORD_FIELD)
    password_field.send_keys(User.get_password())

    checkbox = browser.find_element(*LC.CHECKBOX_AGREE)
    checkbox.click()

    register_button = browser.find_element(*LC.REGISTER_BUTTON)
    register_button.click()

    loader = browser.find_elements(*LC.LOADER)

    assert len(loader) > 0, "Индикатор загрузки не появился"

    successful_message = browser.find_element(*LC.SUCCESS_MESSAGE)

    assert (
        successful_message.text == Text.SUCCESSFUL_REGISTRATION
    ), "Некорректное сообщение об успешной регистрации"


def test_registration_with_sleep(browser):
    browser.get(URL.URL_REGISTRATION)

    header = browser.find_element(*LC.HEADER)

    assert header.text == Text.HEADER_TEXT, "Некорректный текст в заголовке"

    time.sleep(10)

    start_button = browser.find_element(*LC.START_BUTTON)
    start_button.click()

    login_field = browser.find_element(*LC.LOGIN_FIELD)
    login_field.send_keys(User.get_username())

    password_field = browser.find_element(*LC.PASSWORD_FIELD)
    password_field.send_keys(User.get_password())

    checkbox = browser.find_element(*LC.CHECKBOX_AGREE)
    checkbox.click()

    register_button = browser.find_element(*LC.REGISTER_BUTTON)
    register_button.click()

    loader = browser.find_elements(*LC.LOADER)

    assert len(loader) > 0, "Индикатор загрузки не появился"

    time.sleep(10)

    successful_message = browser.find_element(*LC.SUCCESS_MESSAGE)

    assert (
        successful_message.text == Text.SUCCESSFUL_REGISTRATION
    ), "Некорректное сообщение об успешной регистрации"
