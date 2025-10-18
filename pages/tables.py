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
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.new_note = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(3) > div')
        self.pencil = WebElement(driver, '#edit-record-4')
        self.btn_delete = WebElement(driver, '#delete-record-4')


