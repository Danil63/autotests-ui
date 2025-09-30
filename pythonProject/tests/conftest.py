import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }


@pytest.fixture(scope="session")
def base_url():
    # URL должен быть без пути, без слеша в конце, без #.
    return 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course'


@pytest.fixture(scope="session")
def chromium_page_with_state(browser, base_url) -> Page:

    VALID_EMAIL = "valikl.ct@gmail.com"
    VALID_PASSWORD = "89087814701"
    VALID_USERNAME = "DANIK"


    context = browser.new_context()
    page = context.new_page()
    print(f"\n[SETUP] Performing login for: {VALID_EMAIL}")

    login_page = LoginPage(page)

    login_page.visit(f'{base_url}/#/auth/login')
    login_page.fill_login_form(VALID_EMAIL, VALID_PASSWORD)
    login_page.click_login_button()
    page.wait_for_url(f'{base_url}/#/', timeout=15000)
    yield page
    context.close()


@pytest.fixture(scope="function")
def chromium_page(page: Page) -> Page:
    return page