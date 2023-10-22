from pages.base_page import BasePage
from locators import CartPageLocators as CL


class CartPage(BasePage):
    def get_item_name(self, by, path):
        item = self.browser.find_element(by, path)

        return item.text

    def remove_item(self, by, path):
        self.find_element_and_click(by, path)

    def get_all_items(self):
        items = self.browser.find_elements(*CL.ALL_ITEMS)

        return items

    def go_to_checkout(self):
        self.find_element_and_click(*CL.CHECKOUT_BUTTON)

    def open_burger_menu(self):
        self.find_element_and_click(*CL.BURGER_MENU_BUTTON)

    def click_all_items(self):
        self.wait_and_click(*CL.BURGER_ALL_ITEMS_BUTTON)
