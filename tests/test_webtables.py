import time
from pages.tables import Tables


def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
#     assert not page_tables.no_data.exist()
#
#     while page_tables.btn_delete_row.exists():
#         page_tables.btn_delete_row.click()
#
#     time.sleep(2)
#     assert page_tables.no_data.exist()

    assert page_tables.btn_add.exist()
    page_tables.btn_add.click()
    time.sleep(1)
    # assert page_tables.modal_content.visible()
    page_tables.btn_submit.click()
    assert page_tables.modal_content.visible()
    time.sleep(1)
    page_tables.first_name.send_keys('vasya')
    page_tables.last_name.send_keys('testirovich')
    page_tables.email.send_keys('mail@mail.com')
    page_tables.age.send_keys('17')
    page_tables.salary.send_keys('55')
    page_tables.department.send_keys('Department')
    time.sleep(5)
    page_tables.btn_submit.click()
    time.sleep(3)

    page_tables.pencil.click()
    page_tables.new_note.exist()
    page_tables.first_name.send_keys('tester')
    page_tables.btn_submit.click()
    time.sleep(1)
    page_tables.btn_delete.click()
    time.sleep(3)
















