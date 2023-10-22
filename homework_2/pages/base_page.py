from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_exist(self, by, path):
        return bool(self.browser.find_elements(by, path))

    def find_element(self, by, path):
        return self.browser.find_element(by, path)

    def find_element_and_click(self, by, path):
        self.find_element(by, path).click()

    def find_element_and_send_keys(self, by, path, keys):
        self.find_element(by, path).send_keys(keys)

    def wait_and_click(self, by, path, timeout=1):
        wait = WebDriverWait(self.browser, timeout=timeout)

        element = wait.until(EC.element_to_be_clickable((by, path)))

        element.click()
