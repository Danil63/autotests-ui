from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_11(page):

        page.goto("https://app.rizz.market/auth/sign-in")

        Home_url = "https://app.rizz.market/app/creator/market"
        login = "+79087810000"
        password = "Gub89087814701"

        one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
        one_log_button.wait_for(state="visible", timeout=5000)
        one_log_button.click()

        phone_login_input = page.locator('//input[@id=":r0:-form-item"]')
        phone_login_input.wait_for(state="visible", timeout=5000)

        expect(phone_login_input).to_have_attribute("placeholder", "+7", timeout=5000)
        print("placeholder в поле телефон отображается валидно")

        password_login_input = page.locator('//input[@id=":r1:-form-item"]')
        password_login_input.wait_for(state="visible", timeout=5000)

        expect(password_login_input).to_have_attribute("placeholder", "Пароль", timeout=5000)
        print("placeholder в поле пароль отображается валидно")





