from pages.practice_form import PracticeForm
import time

def test_practice_form(browser):
    test_pf = PracticeForm(browser)

    test_pf.visit()

    assert test_pf.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_pf.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_pf.email.get_dom_attribute('placeholder') == 'name@example.com'
