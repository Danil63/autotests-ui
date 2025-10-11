import pytest
from playwright.sync_api import sync_playwright
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def create_course_page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield CreateCoursePage(page)
    context.close()


@pytest.fixture(scope="function")
def courses_list_page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield CoursesListPage(page)
    context.close()