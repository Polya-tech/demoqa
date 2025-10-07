from pages.base_page import BasePage


class ElementPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)


        self.get_center_text = WebElement(self.driver, ".col-12.mt-4.col-md-6")
       

