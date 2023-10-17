import time

from pages.base_page import BasePage
from locators import HomePageLocators as HL


class HomePage(BasePage):
    def open_cart(self):
        self.find_element_and_click(*HL.CART_BUTTON)

    def add_to_cart(self, by, path):
        self.find_element_and_click(by, path)

    def click_on_image(self, by, path):
        self.find_element_and_click(by, path)

    def click_on_title(self, by, path):
        self.find_element_and_click(by, path)

    def open_sort_menu(self):
        self.find_element_and_click(*HL.SORT_CONTAINER)

    def sort_items_by_mode(self, mode):
        selectors = {
            'az': HL.SORT_AZ,
            'za': HL.SORT_ZA,
            'hilo': HL.SORT_HILO,
            'lohi': HL.SORT_LOHI
        }

        self.open_sort_menu()
        self.find_element_and_click(*selectors[mode])

    def get_all_names(self):
        return self.browser.find_elements(*HL.ITEM_NAME)

    def get_all_prices(self):
        return self.browser.find_elements(*HL.ITEM_PRICE)

    def open_burger_menu(self):
        self.find_element_and_click(*HL.BURGER_MENU_BUTTON)

        time.sleep(1)

    def click_about(self):
        self.find_element_and_click(*HL.BURGER_ABOUT_BUTTON)

    def click_logout(self):
        self.find_element_and_click(*HL.BURGER_LOGOUT_BUTTON)

    def click_reset(self):
        self.find_element_and_click(*HL.BURGER_RESET_BUTTON)

    def is_badge(self):
        return self.is_exist(*HL.BADGE)

    def get_number_of_cart_badge(self):
        return self.browser.find_element(*HL.BADGE).text
