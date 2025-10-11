from pages.accordion_page import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit() #создала объект страницы accordion_page
    assert accordion_page.section_content1.visible()
    time.sleep(2)
    accordion_page.section_heading1.click()
    time.sleep(2)
    assert not accordion_page.section_content1.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    accordion_page.section_heading2.click()

    time.sleep(2)
    assert accordion_page.section_content2.visible()
    assert accordion_page.section_content3.visible()
    time.sleep(2)
    accordion_page.section_heading2.click()
    time.sleep(2)
    assert not accordion_page.section_content2.visible()
    assert not accordion_page.section_content3.visible()
    time.sleep(2)


    accordion_page.section_heading4.click()
    assert accordion_page.section_content4.visible()
    time.sleep(2)
    accordion_page.section_heading4.click()
    time.sleep(2)
    assert not accordion_page.section_content4.visible()


