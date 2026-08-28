import pytest
from playwright.sync_api import sync_playwright, Page, expect, Playwright


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', wait_until='networkidle')


    EMAIL = 'user@gmail.com'
    NAME = 'Dani'
    PASSWORD = '1111'
    dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'


    email_input = page.get_by_test_id('registration-form-email-input').locator('div').locator('input')
    name_input = page.get_by_test_id('registration-form-username-input').locator('div').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('div').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')


    email_input.fill(EMAIL)
    name_input.fill(NAME)
    password_input.fill(PASSWORD)
    registration_button.click()


    expect(page).to_have_url(dashboard_url)
    context.storage_state(path='test_data/browser-stage.json')

    
    context.close()
    browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='test_data/browser-stage.json')
    page = context.new_page()


    yield page


    context.close()
    browser.close()

   