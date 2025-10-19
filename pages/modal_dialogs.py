from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_three_element = WebElement(self.driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > span')
        self.btns_three_menu = WebElement(self.driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(self.driver, '#app > header > a > img')
        self.small_modal = WebElement(self.driver, '#showSmallModal')
        self.large_modal = WebElement(self.driver, '#showLargeModal')
        self.close_small_modal = WebElement(self.driver, '#closeSmallModal')
        self.close_large_modal = WebElement(self.driver, '#closeLargeModal')
