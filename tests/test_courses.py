from playwright.sync_api import sync_playwright, expect, Request, Response, Page
import pytest


@pytest.mark.ui
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):


        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', wait_until='networkidle')


        text_title = 'Courses'
        text_results = 'There is no results'
        text = 'Results from the load test pipeline will be displayed here'

        
        title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        icon_courses_page = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        title_h4_result_courses_page = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        title_h6_courses_page = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        
        
        expect(title_courses).to_have_text(text_title)
        expect(title_h4_result_courses_page).to_have_text(text_results)
        expect(icon_courses_page).to_be_visible()
        expect(title_h6_courses_page).to_have_text(text)