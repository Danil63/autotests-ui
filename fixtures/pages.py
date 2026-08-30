import pytest
from playwright.sync_api import Page
from pages.login_pages import LoginPage
from pages.registration_page import RegistrationPage

@pytest.fixture
def login_pages(chromium_page_with_state: Page) -> LoginPage:
    return LoginPage(page=chromium_page_with_state)

@pytest.fixture
def registration_pages(chromium_page_with_state: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page_with_state)