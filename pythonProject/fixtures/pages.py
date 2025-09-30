import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


pytest_plugins = (
    "fixtures.pages",
    "fixtures.browsers"
)

def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    login_page = LoginPage(page=chromium_page)
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")


def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

