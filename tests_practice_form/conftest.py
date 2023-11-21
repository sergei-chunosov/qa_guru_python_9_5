import pytest
from selene import browser



# @pytest.fixture(scope='function', autouse=True)
@pytest.fixture()
def browser_settings_demoqa():
    browser.config.base_url = "https://demoqa.com/"
    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = 4


# @pytest.fixture(scope='function', autouse=True)
@pytest.fixture()
def browser_settings_qaguru():
    browser.config.base_url = "https://app.qa.guru/"
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.timeout = 4