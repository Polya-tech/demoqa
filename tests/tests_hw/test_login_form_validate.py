from pages.practice_form import PracticeForm
import time

def test_practice_form(browser):
    test_pf = PracticeForm(browser)

    test_pf.visit()

    assert test_pf.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_pf.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_pf.email.get_dom_attribute('placeholder') == 'name@example.com'


 first_name_placeholder = test_pf.first_name.get_dom_attribute('placeholder')
    last_name_placeholder = test_pf.last_name.get_dom_attribute('placeholder')
    email_placeholder = test_pf.email.get_dom_attribute('placeholder')

    print("First name placeholder:", first_name_placeholder)
    print("Last name placeholder:", last_name_placeholder)
    print("Email placeholder:", email_placeholder)

    assert first_name_placeholder == 'First Name'
    assert last_name_placeholder == 'Last Name'
    assert email_placeholder == 'name@example.com'

