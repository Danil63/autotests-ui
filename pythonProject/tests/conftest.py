import pytest
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.fixture
def dashboard_page_with_state(page):
    """Создает объект DashboardPage, используя стандартную фикстуру page"""
    return DashboardPage(page)


@pytest.fixture
def courses_list_page(page):
    """Создает объект CoursesListPage"""
    return CoursesListPage(page)


@pytest.fixture
def create_course_page(page):
    """Создает объект CreateCoursePage"""
    return CreateCoursePage(page)