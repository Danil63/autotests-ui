from playwright.sync_api import expect

class SidebarComponent:
    def __init__(self, page):
        self.page = page
        self.sidebar = page.get_by_test_id("sidebar")
        self.logo = page.get_by_test_id("sidebar-logo")

    def check_visible(self):
        expect(self.sidebar).to_be_visible()
        expect(self.logo).to_be_visible()
        print("✅ Sidebar отображается корректно")