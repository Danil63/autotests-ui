from playwright.sync_api import sync_playwright, expect, Request, Response

def response_check(response: Response):
    return ('url' in response.url 
        and response.request.method=='POST')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('url', wait_until='networkidle')

    email = 'mail@gmal.com'
    name = 'Oleg'
    password = '1111'

    email_input = page.get_by_test_id('locator').locator('input')

    with page.expect_response(response_check) as response_info:
        response = response_info.value
        expect(response).to_be_ok()
        response_body = response.json()

        assert response_body['email'] == email