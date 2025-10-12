import pytest #импортируем pytest
from selenium import webdriver #импортируем из selenium - webdriver

@pytest.fixture(scope="session") #декоратор - это функция, которая изменяет поведение другой функциии. pytest.fixture - будет изменять поведение нашей функции в браузере. Передаем в scope - session
def browser(): #пишем функцию чтобы использовать наш браузер в других тестах, и на нашу ф-и навешиваем декоратор (обертку)
    driver = webdriver.Chrome()#пишем наш драйвер
    driver.set_window_size(1000, 1000)
    yield driver #чтобы наш драйвер мог использоваться в функции мы должны написать слово yield
    driver.quit() #закрываем наш драйвер
