
from pages.demoqa import DemoQa
from pages.elements_page import ElementPage
import time


def test_text_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_text_body_height(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementPage(browser)
    demo_qa_page.visit()
    time.sleep(3)
    # assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    time.sleep(3)
  
    assert elements_page.get_center_text.get_text() == 'Please select an item from left to start practice.'





