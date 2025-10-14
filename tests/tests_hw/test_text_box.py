from pages.text_box_clear import TextBox
import time

def test_clear(browser):
    text_box = TextBox(browser)

    full_name_text = "Иван"   # Переменные с тестовыми данными
    address_text = "г. Москва, ул. Пушкина, д. 10"

    text_box.visit()
    text_box.full_name.send_keys(full_name_text)
    text_box.current_address.send_keys(address_text)
    text_box.btn_submit.click()
    time.sleep(3)

    assert text_box.output_full_name.get_text() == 'Name:Иван'
    assert text_box.output_current_address.get_text() == 'Current Address :г. Москва, ул. Пушкина, д. 10'
