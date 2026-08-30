from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPages(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('')
        self.password_input = page.get_by_test_id('')
        self.login_button = page.get_by_test_id('')


    def fill_email_input(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()




