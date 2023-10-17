from pages import HomePage


def test_sort_by_a_to_z(browser_with_auth):
    '''Сортировка от A до Z'''

    mode = 'az'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.sort_items_by_mode(mode)

    items_names = [item.text for item in home_page.get_all_names()]
    sorted_items = sorted(items_names)

    assert items_names == sorted_items, 'Неправильная сортировка'


def test_sort_by_z_to_a(browser_with_auth):
    '''Сортировка от Z до A'''

    mode = 'za'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.sort_items_by_mode(mode)

    items_names = [item.text for item in home_page.get_all_names()]
    sorted_items = sorted(items_names, reverse=True)

    assert items_names == sorted_items, 'Неправильная сортировка'


def test_sort_by_low_to_high(browser_with_auth):
    '''Сортировка по возрастанию цены'''

    mode = 'lohi'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.sort_items_by_mode(mode)

    items_names = [float(item.text[1:]) for item in home_page.get_all_prices()]
    sorted_items = sorted(items_names)

    assert items_names == sorted_items, 'Неправильная сортировка'


def test_sort_by_high_to_low(browser_with_auth):
    '''Сортировка по убыванию цены'''

    mode = 'hilo'

    home_page = HomePage(browser_with_auth, browser_with_auth.current_url)
    home_page.sort_items_by_mode(mode)

    items_names = [float(item.text[1:]) for item in home_page.get_all_prices()]
    sorted_items = sorted(items_names, reverse=True)

    assert items_names == sorted_items, 'Неправильная сортировка'
