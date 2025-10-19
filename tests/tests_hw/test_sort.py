import time
from pages.tables import Tables


def test_sort(browser):
    page_tables = Tables(browser)
    table_class_1 = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    table_class_2 = 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    page_tables.visit()

    for i in range(2):
        page_tables.first_name.click()
    assert page_tables.first_name.get_dom_attribute('class') == table_class_1 or table_class_2
    time.sleep(2)
