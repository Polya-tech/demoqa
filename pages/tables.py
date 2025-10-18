import time

from components.components import WebElement
from pages.base_page import BasePage

class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '//span[@title="Delete"]', 'xpath')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_content = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.reg_form_btn_submit = WebElement(driver, '#submit')


