import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage  # Убедитесь, что импортируете класс DashboardPage

@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
      "username, email, password",
    [
        ("TestUser", "user.name@gmail.com", "password"),
    ]
)

def test_successful_registration(chromium_page: Page, base_url: str, username: str, email: str, password: str):
    registration_page = RegistrationPage(page=chromium_page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(username, email, password)
    registration_page.click_registration_button()


    dashboard_page = DashboardPage(page=chromium_page)
    dashboard_page.check_dashboard_title_visibility()