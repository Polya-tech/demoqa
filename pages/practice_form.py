from components.components import WebElement
from pages.base_page import BasePage

class PracticeForm(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.btn_submit_pf = WebElement(driver, '#submit')
        self.validated_form = WebElement(driver, '#userForm')

        self.element_state_and_city = WebElement(driver, '#stateCity-label')
        self.state_container = WebElement(driver, '#state')
        self.state_input = WebElement(driver, "input[id^='react-select-'][id$='-input']")
        self.city_container = WebElement(driver, '#city') #div.css-1hwfws3
        self.city_input = WebElement(driver, "input#react-select-4-input")
