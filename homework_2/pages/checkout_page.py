from pages.base_page import BasePage
from locators import CheckoutPageLocators as CheckL


class CheckoutPage(BasePage):
    def fill_in_the_informations(self, name, surname, postal_code):
        self.find_element_and_send_keys(*CheckL.FIRST_NAME_FIELD, name)
        self.find_element_and_send_keys(*CheckL.LAST_NAME_FIELD, surname)
        self.find_element_and_send_keys(*CheckL.ZIP_CODE_FIELD, postal_code)

    def is_error(self):
        return self.is_exist(*CheckL.ERROR_CONTAINER)

    def get_error_message(self):
        return self.browser.find_element(*CheckL.ERROR_CONTAINER).text

    def click_continue(self):
        self.find_element_and_click(*CheckL.CONTINUE_BUTTON)

    def click_finish(self):
        self.find_element_and_click(*CheckL.FINISH_BUTTON)

    def get_complete_text(self):
        return self.browser.find_element(*CheckL.COMPLETE_HEADER).text
