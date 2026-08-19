from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    BASE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"



    title_main = page.get_by_test_id('registration-form-email-input')
    expect(title_main).to_be_visible

    email_input = page.locator('//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall css-i12hqd"]//input[@id=":r0:"]')

    name_input = page.locator('//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall css-i12hqd"]//input[@id=":r1:"]')

    password_input = page.locator('//div[@class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall css-i12hqd"]//input[@id=":r1:"]')

    registration_button = page.get_by_test_id('registration-page-registration-button')


    expect(password_input).to_be_disabled



    email_input.fill('user.name@gmail.com')
    name_input.fill('имя пользователя')
    password_input.fill('пароль')


    expect(password_input).to_be_attached

   




    