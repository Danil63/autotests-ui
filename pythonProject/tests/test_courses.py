import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title).to_have_text('Courses')

    icons = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icons).to_be_visible()

    text1 = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text1).to_have_text("There is no results")

    text2 = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text2).to_have_text("Results from the load test pipeline will be displayed here")