import pytest
from playwright.sync_api import expect

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state):
    page = dashboard_page_with_state

    page.sidebar.check_visible()

    page.navbar.check_visible("username")

    page.check_visible_dashboard_title()

    print("✅ Тест Dashboard прошёл успешно")