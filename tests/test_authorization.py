from playwright.sync_api import sync_playwright, expect, Page
import pytest

users = [
    ('user.name@gmail.com', 'password'),
    ('user.name@gmail.com', '  '),
    ('  ', 'password')
] 


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', users)
def test_wrong_email_or_password_authorization(chromium_page_with_state: Page, email: str, password: str):


    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until='networkidle')


    email_input = chromium_page_with_state.get_by_test_id('login-form-email-input').locator('div').locator('input')
    password_input = chromium_page_with_state.get_by_test_id('login-form-password-input').locator('div').locator('input')
    authorizations_button = chromium_page_with_state.get_by_test_id('login-page-login-button')
    error_notification = chromium_page_with_state.locator("//div[text()='Wrong email or password']")


    email_input.fill(email)
    password_input.fill(password)
    authorizations_button.click()
    expect(error_notification).to_have_text('Wrong email or password')







