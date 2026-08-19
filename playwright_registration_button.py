from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', wait_until='networkidle')


    email_input = page.locator('//input[@id=":r0:"]')
    name_input = page.locator('//input[@id=":r1:"]')
    password_input = page.locator('//input[@id=":r2:"]')
    registration_button = page.get_by_test_id('registration-page-registration-button')


    expect(registration_button).to_be_disabled()


    email_input.focus()
    page.keyboard.type('user.name@gmail.com')
    expect(email_input).to_have_value('user.name@gmail.com')


    name_input.focus()
    page.keyboard.type('username')
    expect(name_input).to_have_value('username')


    password_input.focus()
    page.keyboard.type('password')
    expect(password_input).to_have_value('password')


    expect(registration_button).to_be_enabled()

    