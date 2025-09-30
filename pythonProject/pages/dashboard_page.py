from playwright.sync_api import Page, expect
from .base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title_text = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_title_visibility(self):
        expect(self.dashboard_title_text).to_be_visible()
        expect(self.dashboard_title_text).to_have_text("Dashboard")