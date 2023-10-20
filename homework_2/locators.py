from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_CONTAINER = (By.CLASS_NAME, 'error-message-container')


class HomePageLocators:
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    BURGER_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    BURGER_LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    BURGER_ABOUT_BUTTON = (By.ID, 'about_sidebar_link')
    BURGER_RESET_BUTTON = (By.ID, 'reset_sidebar_link')
    BACKPACK_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BACKPACK_IMAGE = (By.ID, 'item_4_img_link')
    BACKPACK_TITLE_LINK = (By.ID, 'item_4_title_link')
    BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    SORT_CONTAINER = (By.CLASS_NAME, 'product_sort_container')
    SORT_AZ = (By.CSS_SELECTOR, 'option[value="az"]')
    SORT_ZA = (By.CSS_SELECTOR, 'option[value="za"]')
    SORT_LOHI = (By.CSS_SELECTOR, 'option[value="lohi"]')
    SORT_HILO = (By.CSS_SELECTOR, 'option[value="hilo"]')


class CartPageLocators:
    BACKPACK_NAME = (By.CSS_SELECTOR,
                     '#item_4_title_link .inventory_item_name')
    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    BURGER_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    BURGER_ALL_ITEMS_BUTTON = (By.ID, 'inventory_sidebar_link')
    ALL_ITEMS = (By.CLASS_NAME, 'inventory_item_name')


class ProductPageLocators:
    BACKPACK_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    ADD_TO_CART = (By.CLASS_NAME, 'btn.btn_primary.btn_small.btn_inventory')
    PRODUCT_NAME = (By.CLASS_NAME, 'inventory_details_name')


class CheckoutPageLocators:
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    ZIP_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    ERROR_CONTAINER = (By.CLASS_NAME, 'error-message-container.error')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')
