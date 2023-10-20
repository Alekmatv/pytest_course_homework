from faker import Faker


class URL:
    AUTH = 'https://www.saucedemo.com/'
    HOME = 'https://www.saucedemo.com/inventory.html'
    ABOUT = 'https://saucelabs.com/'


class Username:
    STANDART = 'standard_user'
    NEGATIVE = 'user'
    LOCKED = 'locked_out_user'
    PROBLEM = 'problem_user'
    PERFORMANCE_GLITCH = 'performance_glitch_user'
    ERROR = 'error_user'
    VISUAL = 'visual_user'


class Password:
    POSITIVE = 'secret_sauce'
    NEGATIVE = 'wrong_password'


class Text:
    SUCCESSFUL_ORDER = 'Thank you for your order!'


class ProductName:
    BACKPACK = 'Sauce Labs Backpack'


class Error:
    AUTH = 'Epic sadface: Username and password ' \
                     'do not match any user in this service'
    POSTAL_CODE = 'Error: Postal Code is required'


class Info:
    @staticmethod
    def _get_info(locale=None):
        fake = Faker(locale=locale)

        name = fake.first_name()
        surname = fake.last_name()
        post_code = fake.postcode()

        return name, surname, post_code

    @classmethod
    def get_positive_cyrillic_info(cls):
        return cls._get_info('ru_RU')

    @classmethod
    def get_positive_english_info(cls):
        return cls._get_info('en')

    @classmethod
    def get_negative_post_code_cyrillic_info(cls):
        name, surname, _ = cls.get_positive_cyrillic_info()

        return name, surname, ''

    @classmethod
    def get_negative_post_code_english_info(cls):
        name, surname, _ = cls.get_positive_english_info()

        return name, surname, ''
