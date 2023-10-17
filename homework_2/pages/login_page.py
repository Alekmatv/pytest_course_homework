from pages.base_page import BasePage
from locators import LoginPageLocators as LL


class LoginPage(BasePage):
    def login(self, username, password):
        self.find_element_and_send_keys(*LL.USERNAME_FIELD, username)
        self.find_element_and_send_keys(*LL.PASSWORD_FIELD, password)

        self.find_element_and_click(*LL.LOGIN_BUTTON)

    def is_error(self):
        return self.is_exist(*LL.ERROR_CONTAINER)

    def get_error_message(self):
        return self.browser.find_element(*LL.ERROR_CONTAINER).text
