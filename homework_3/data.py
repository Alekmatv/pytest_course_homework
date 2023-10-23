from selenium.webdriver.common.by import By
from faker import Faker


class URL:
    URL_REGISTRATION = "https://victoretc.github.io/selenium_waits/"


class Locator:
    START_BUTTON = (By.ID, 'startTest')
    REGISTER_BUTTON = (By.ID, 'register')
    HEADER = (By.CSS_SELECTOR, 'h1')
    LOGIN_FIELD = (By.ID, 'login')
    PASSWORD_FIELD = (By.ID, 'password')
    CHECKBOX_AGREE = (By.ID, 'agree')
    SUCCESS_MESSAGE = (By.ID, 'successMessage')
    LOADER = (By.ID, 'loader')


class Text:
    HEADER_TEXT = 'Практика с ожиданиями в Selenium'
    SUCCESSFUL_REGISTRATION = 'Вы успешно зарегистрированы!'


class User:
    FAKER = Faker()

    @classmethod
    def get_username(cls):
        return cls.FAKER.first_name()

    @classmethod
    def get_password(cls):
        return cls.FAKER.password()
