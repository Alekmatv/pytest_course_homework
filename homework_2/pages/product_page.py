from pages.base_page import BasePage
from locators import ProductPageLocators as PL


class ProductPage(BasePage):
    def open_cart(self):
        self.find_element_and_click(*PL.CART_BUTTON)

    def add_to_cart_backpack(self):
        self.find_element_and_click(*PL.BACKPACK_ADD_TO_CART)

    def add_to_cart(self):
        self.find_element_and_click(*PL.ADD_TO_CART)

    def get_product_name(self):
        return self.browser.find_element(*PL.PRODUCT_NAME).text
