from selene import browser, have, command
from time import sleep
import os.path


def test_add_form(browser_settings_demoqa):
    browser.open('automation-practice-form')
    browser.element('#firstName').type('Sergei')
    browser.element('#lastName').type('Chu')
    browser.element('#userEmail').type('ncrs@example.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type(1234567890)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-dropdown-container').click()
    browser.all('.react-datepicker__month-dropdown-container select option').element_by(
        have.exact_text('October')).click()
    browser.element('.react-datepicker__year-dropdown-container').click()
    browser.all('.react-datepicker__year-select option').element_by(
        have.exact_text('1983')).click()
    browser.all('.react-datepicker__day--006').first.click()
    browser.element('#dateOfBirthInput').should(have.value('06 Oct 1983'))
    browser.element('#subjectsInput').type('En')
    browser.element('#react-select-2-option-0').should(have.exact_text('English')).click()
    browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('bar-h.png'))
    browser.element('#currentAddress').type('SPB')
    browser.element('#state').click().element('#react-select-3-option-2').should(have.exact_text('Haryana')).click()
    browser.element('#city').click().element('#react-select-4-option-0').should(have.exact_text('Karnal')).click()
    # browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').press_enter()

    sleep(1)
