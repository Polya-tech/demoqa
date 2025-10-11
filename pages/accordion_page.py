from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_content1 = WebElement(self.driver, '#section1Content > p')
        self.section_heading1 = WebElement(self.driver, '#section1Heading')
        self.section_content2 = WebElement(self.driver, '#section2Content > p:nth-child(1)')
        self.section_heading2 = WebElement(self.driver, '#section2Heading')
        self.section_content3 = WebElement(self.driver, '#section2Content > p:nth-child(2)')
        self.section_content4 = WebElement(self.driver, '#section3Content > p')
        self.section_heading4 = WebElement(self.driver, '#section3Heading')
