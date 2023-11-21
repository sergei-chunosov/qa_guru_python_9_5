from selene import browser, have, command
from time import sleep
import pyautogui

from selenium.webdriver import Keys


def upload_by_os():
    pyautogui.hotkey('ctrl', 'L')
    pyautogui.typewrite('/home/necros/bar-h.png', interval=0)
    pyautogui.press('enter')


def test_add_form(browser_settings_qaguru):
    browser.open('automation-practice-form/')
    browser.element('.MuiBox-root .css-1vpe9z').click()
    browser.element('#\:r0\:').type('Sergei')
    browser.element('#\:r1\:').type('Chu')
    browser.element('#\:r2\:').type('ncrs@example.com')
    browser.element('#\:r3\:').type('9111111111')
    browser.all('.MuiFormControl-root').element_by(have.exact_text('Language')).click()
    browser.element('[data-value=Chines]').hover().click()
    browser.element('#\:r4\:').click().type('10061983')
    # sleep(100)
    browser.element('#\:r4\:').should(have.value('10/06/1983'))
    browser.all('[data-testid=gender]').element_by(have.value('Male')).click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Sports')).click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Reading')).click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Music')).click()
    browser.all('[role=button]')[1].click()
    browser.element('[data-value=Dance]').click()
    browser.element('[data-value=Music]').click().press_escape()
    browser.all('[role=button]')[4].click()
    browser.element('[data-value=Florida]').click()
    browser.all('[role=button]')[5].perform(command.js.scroll_into_view).click()
    browser.element('[data-value=Miami]').click()

    for i in range(1, 5):
        browser.element('.MuiSlider-thumb').element('input').type(Keys.ARROW_RIGHT)

    browser.element('#\:r7\:').type('SPB')
    browser.element('[role=presentation]').click()
    #TODO тут я нифига не придумал как загрузить файл, тащу из гуйни оси
    upload_by_os()
    browser.element('[type = submit]').click()

    sleep(1)
