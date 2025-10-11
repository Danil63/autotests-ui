from playwright.sync_api import expect

class NavbarComponent:
    def __init__(self, page):
        self.page = page
        self.navbar = page.get_by_test_id("navbar")
        self.username_label = page.get_by_test_id("navbar-username")

    def check_visible(self, username: str):
        expect(self.navbar).to_be_visible()
        expect(self.username_label).to_have_text(username)
        print(f"✅ Navbar отображается с пользователем: {username}")