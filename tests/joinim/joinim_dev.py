from playwright.sync_api import sync_playwright, Response, Request, expect


def response_check(response: Response):
    return('/api/auth/get-session' in response.url)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto('https://admin.joinim.ru/login', wait_until='networkidle')


    email = 'tester@example.com'
    password = 'demo-local-1234'


    email_input = page.get_by_test_id('login-email-input')
    password_input = page.get_by_test_id('login-password-input')
    auth_button = page.get_by_test_id('login-submit-button')


    email_input.focus()
    page.keyboard.type(email)
    expect(email_input).to_have_value(email)


    password_input.focus()
    page.keyboard.type(password)
    expect(password_input).to_have_value(password)


    with page.expect_response(response_check) as response_info:
        auth_button.click()
        expect(page).to_have_url('https://admin.joinim.ru/')
        context.storage_state(path='browser-path.json')


        response = response_info.value()
        expect(response).to_be_ok()
        response_body = response.json()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state='browser-path.json')
    page = context.new_page()


    page.goto('https://admin.joinim.ru/', wait_until='networkidle')


    title_page = page.locator("//h1[text()='Ваш бизнес']")
    expect(title_page).to_have_text('Ваш бизнес')


