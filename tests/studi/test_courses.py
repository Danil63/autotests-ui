from playwright.sync_api import sync_playwright, expect, Request, Response


def test_empty_courses_list():
    with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
    
    
            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', wait_until='networkidle')
    
    
            email_input = page.get_by_test_id('registration-form-email-input').locator('div').locator('input')
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
            registration_button.click()

            expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
            context.storage_state(path='browser_path_two.json')


    with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(storage_state='browser_path_two.json')
            page = context.new_page()


            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', wait_until='networkidle')


            text_title = 'Courses'
            text_results = 'There is no results'
            text = 'Results from the load test pipeline will be displayed here'
        
            title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
            icon_courses_page = page.get_by_test_id('courses-list-empty-view-icon')
            title_h4_result_courses_page = page.get_by_test_id('courses-list-empty-view-title-text')
            title_h6_courses_page = page.get_by_test_id('courses-list-empty-view-description-text')
        
        
            expect(title_courses).to_have_text(text_title)
            expect(title_h4_result_courses_page).to_have_text(text_results)
            expect(icon_courses_page).to_be_visible()
            expect(title_h6_courses_page).to_have_text(text)
            
    
    
