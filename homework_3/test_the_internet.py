from selenium.webdriver.common.by import By


def test_add_remove_element(browser):

    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button = browser.find_element(
        By.CSS_SELECTOR, '.example > button')
    add_button.click()

    delete_button = browser.find_element(By.CLASS_NAME, 'added-manually')
    delete_button.click()

    delete_buttons = browser.find_elements(By.CLASS_NAME, 'added-manually')

    assert len(delete_buttons) == 0, 'Количество кнопок Delete не равно 0'


def test_basic_auth(browser):

    exp_text = "Congratulations! You must have " \
               "the proper credentials."

    browser.get("https://the-internet.herokuapp.com/basic_auth")

    login = "admin"
    password = "admin"
    link = f"https://{login}:{password}@the-internet.herokuapp.com/basic_auth"

    browser.get(link)

    message = browser.find_element(By.CSS_SELECTOR, "p").text

    assert (
        message == exp_text
    ), "Некорректное сообщение об успешной авторизации"


def test_broken_images_links(browser):

    start = 'https://the-internet.herokuapp.com/img/'

    browser.get('https://the-internet.herokuapp.com/broken_images')

    images = browser.find_elements(By.CSS_SELECTOR, '.example > img')

    for image in images:
        src = image.get_attribute('src')

        assert src.startswith(start), 'Некорректная ссылка на изображение'


def test_broken_images(browser):

    browser.get('https://the-internet.herokuapp.com/broken_images')

    images = browser.find_elements(By.CSS_SELECTOR, '.example img')
    images_links = [image.get_attribute('src') for image in images]

    for src in images_links:
        browser.get(src)

        img = browser.find_elements(By.CSS_SELECTOR, 'img')

        assert img, 'Изображение сломано'


def test_checkboxes(browser):

    browser.get('https://the-internet.herokuapp.com/checkboxes')

    checkbox_1, checkbox_2 = browser.find_elements(
        By.CSS_SELECTOR,
        '#checkboxes > input')

    checkbox_1.click()
    checkbox_2.click()

    is_checked_1 = checkbox_1.get_attribute('checked')
    is_checked_2 = checkbox_2.get_attribute('checked')

    assert is_checked_1 == 'true', 'Не удалось пометить 1ый чекбокс'

    assert is_checked_2 is None, 'Не удалось убрать отметку со 2го чекбокса'
