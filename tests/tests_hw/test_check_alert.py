import time
from pages.alerts import Alerts

def test_timer(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_timer.exist()
    time.sleep(1)
    alert_page.btn_timer.click_force()
    time.sleep(6)
    assert alert_page.alert()
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'
