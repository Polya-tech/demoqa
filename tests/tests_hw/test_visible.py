from pages.demoqa import DemoQa
from pages.elements_page import ElementPage
import time

def test_visible_btn_sidebar(browser):
    elements_page = ElementPage(browser)

    elements_page.visit()
    # elements_page.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements_page.btn_sidebar_first_textbox.exist()
    assert elements_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()



