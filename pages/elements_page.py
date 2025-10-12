from components.components import WebElement
from pages.base_page import BasePage



class ElementPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.get_center_text = WebElement(self.driver, ".col-12.mt-4.col-md-6")
        self.text_elements = WebElement(self.driver, '.col-12.mt-4.col-md-6')
        self.icon = WebElement(self.driver, '#app > header > a > img')
        self.btn_sidebar_first = WebElement(self.driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(self.driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(self.driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WebElement(self.driver, 'div:nth-child(1) > div > ul > li')
