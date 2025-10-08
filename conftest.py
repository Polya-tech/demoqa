import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome() #создаем драйвер
    yield driver #yield - нужен чтобы драйвер мог использоваться в функции
    driver.quit()
