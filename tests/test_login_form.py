import time
from pages.form_page import FormPage


def test_login_form(browser):
    from_page = FormPage(browser)

    from_page.visit()
    assert not from_page.modal_dialog.exist() #проверяем что окно сейчас не существует и недоступно
    time.sleep(2)
    from_page.first_name.send_keys('tester')
    from_page.last_name.send_keys('testirovich')
    from_page.user_email.send_keys('mail@mail.com')
    from_page.gender_radio.click()
    from_page.user_number.send_keys('1234567891')
    time.sleep(2)
    from_page.btn_submit.click()
    time.sleep(2)
