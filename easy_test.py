from playwright.sync_api import sync_playwright, expect, Request, Response


def response_check(response: Response):
    return('/#/auth/registration' in response.url and 
        response.request.method=='POST')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', wait_until='networkidle')


    email = 'user.name@gmail.com'
    name = 'username'
    password = 'password'


    title = page.get_by_test_id('authentication-ui-course-title-text').locator('font').locator('font')
    email_input = page.get_by_test_id('registration-form-email-input').locator('div').locator('input')
    name_input = page.get_by_test_id('registration-form-name-input').locator('div').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('div').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')


    expect(registration_button).not_to_be_disabled()


    email_input.focus()
    page.keyboard.type(email)
    expect(email_input).to_have_value(email)


    name_input.focus()
    page.keyboard.type(name)
    expect(name_input).to_have_value(name)


    password_input.focus()
    page.keyboard.type(password)
    expect(password_input).to_have_value(password)


    expect(registration_button).to_be_enabled()


    with page.expect_response(response_check) as response_info:

        response = response_info.value

        expect(response_info).to_be_ok()

        response_body = response.json

        assert response_body['email'] == email
        assert response_body['name'] == name
        assert response_body['password'] == password



    








