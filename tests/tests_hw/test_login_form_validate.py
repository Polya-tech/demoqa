from pages.practice_form import PracticeForm
import time
from selenium.webdriver.common.keys import Keys

def test_practice_form(browser):
    test_pf = PracticeForm(browser)

    test_pf.visit()


    assert test_pf.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_pf.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_pf.email.get_dom_attribute('placeholder') == 'name@example.com'
    assert test_pf.email.get_dom_attribute('pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    time.sleep(1)

    test_pf.btn_submit_pf.click_force()
    time.sleep(1)

    assert test_pf.validated_form.get_dom_attribute('class') == 'was-validated'

def test_click_state_and_city(browser):
    state_and_city = PracticeForm(browser)

    state_and_city.visit()


    assert state_and_city.element_state_and_city.exist()

    state_and_city.element_state_and_city.scroll_to_elements()
    state_and_city.state_container.click()
    state_and_city.state_input.send_keys("Haryana")
    state_and_city.state_input.send_keys(Keys.ENTER)

    time.sleep(3)
    state_and_city.city_container.click()
    time.sleep(2)
    state_and_city.city_input.send_keys('Karnal')
    state_and_city.state_input.send_keys(Keys.ENTER)
    time.sleep(2)






    # относится к def test_practice_form
    # first_name_placeholder = test_pf.first_name.get_dom_attribute('placeholder')
    # email_pattern = test_pf.email.get_dom_attribute('pattern')
    
    # print("First name placeholder:", first_name_placeholder)
    # print("Email_pattern:", email_pattern)
    
    # assert first_name_placeholder == 'First Name'
    # assert email_pattern == 'First Name'




    


