import time
from pages.tables import Tables

def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()

    assert page_tables.btn_add.exist()
    page_tables.btn_add.click()
    time.sleep(1)

    assert page_tables.modal_content.visible()
    time.sleep(1)

    page_tables.reg_form_btn_submit.click()
    time.sleep(2)
    page_tables.modal_content.get_dom_attribute('class') != 'novalidate'
