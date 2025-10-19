from pages.modal_dialogs import ModalDialogs
import time

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

    modal_dialogs.small_modal.click()
    modal_dialogs.close_small_modal.click()
    time.sleep(2)
    modal_dialogs.large_modal.click()
    modal_dialogs.close_large_modal.click()

