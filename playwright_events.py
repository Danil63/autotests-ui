from playwright.sync_api import sync_playwright, expect, Request, Response


def is_registration_response(response: Response):
    return('/api/auth/register' in response.url 
           and response.request.method == "POST")




with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', wait_until='networkidle')



    with page.expect_response(is_registration_response) as response_info:


    response = response_info.value

    expect(response).to_be_ok()

    response_body = response.json()

    assert response_body["email"] == email
    assert response_body["username"] == username
    assert response_body["id"]