from playwright.sync_api import sync_playwright, expect, Page
from pages.login_pages import LoginPages
import pytest


users = [
    ('user.name@gmail.com', 'password'),
    ('user.name@gmail.com', '  '),
    ('  ', 'password')
] 


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', users)
def test_wrong_email_or_password_authorization(login_page: LoginPages, email: str, password: str):

    login_page.fill_email_input(email=email, password=password)
    login_page.click_login_button()





