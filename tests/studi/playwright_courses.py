from playwright.sync_api import sync_playwright, expect, Request, Response


# def responce_check(response: Response):
#     return ('auth/url/me' in response.url
#         and response.request.method=='POST')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', 
    wait_until='networkidle')


    email = 'user.name@gmail.com'
    name = 'username'
    password = '1343295'


    title = page.get_by_test_id('authentication-ui-course-title-text')
    email_input = page.get_by_test_id('registration-form-email-input').locator('div').locator('input')
    name_input = page.get_by_test_id('registration-form-username-input').locator('div').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('div').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')


    expect(registration_button).to_be_disabled()

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
    registration_button.click()
    expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')


    # with page.expect_response(responce_check) as response_info:
    #     registration_button.click()

    #     response = response_info.value()
    #     expect(response).to_be_ok()
    #     response_body = response.json()

    #     assert response_body["id"]

    #     expected_body = {
    #         "id": response_body["id"],
    #         "email": email,
    #         "name": name,
    #         "role": "student",
    #         "isActive": True,
    #     }
 
    #     assert response_body == expected_body 
    
    context.storage_state(path='browser-stage.json')



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-stage.json')
    page = context.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', 
    wait_until='networkidle')

    text_title = 'Courses'
    text_results = 'There is no results'
    text = 'Results from the load test pipeline will be displayed here'


    button_courses = page.get_by_test_id('courses-drawer-list-item-button')
    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    icon_courses_page = page.get_by_test_id('courses-list-empty-view-icon')
    title_h4_result_courses_page = page.get_by_test_id('courses-list-empty-view-title-text')
    title_h6_courses_page = page.get_by_test_id('courses-list-empty-view-description-text')


    button_courses.click()
    expect(title_courses).to_have_text('Courses')
    expect(title_h4_result_courses_page).to_have_text(text_results)
    expect(icon_courses_page).to_be_visible()
    expect(title_h6_courses_page).to_have_text(text)