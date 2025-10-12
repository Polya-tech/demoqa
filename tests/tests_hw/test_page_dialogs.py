from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa
import time

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    # modal_dialogs.btn_three_element.click()
    # time.sleep(2)
    assert modal_dialogs.btns_three_menu.check_count_elements(count=5) #доступ к btns_three_menu получаем через объект modal_dialogs, там где и находится атрибут btns_three_menu



def test_navigation_modal(browser):
    modal_dialogs_new = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)
    modal_dialogs_new.visit()
    modal_dialogs_new.refresh()
    browser.refresh()
    modal_dialogs_new.icon.click()
    browser.back()
    browser.set_window_size(900, 400)  # обращаемся к браузеру и устанавливаем размер окна
    time.sleep(2)
    browser.forward()

    assert demo_qa_page.equal_url()
    # time.sleep(2)
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
