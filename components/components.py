from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By #By - обеспечивает взаимодействие с веб-элементами

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver #драйвер получаем из драйвера
        self.locator = locator #локатор получаем из локатора

    def click(self):
        self.find_element().click()

    def find_element(self):
          return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        self.find_element().is_displayed()

    def send_keys(self, text: str): #gолучает текст типа str
        self.find_element().send_keys(text)



