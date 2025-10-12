from pages.demoqa import DemoQa
import time

def test_size_demo(browser):
    demo_qa_page = DemoQa(browser) #созждем объект от класса DemoQa и передаем браузер

    demo_qa_page.visit()
    browser.set_window_size(1000, 300) #обращаемся к браузеру и устанавливаем размер окна
    time.sleep(2)
    browser.set_window_size(1000, 1000)
