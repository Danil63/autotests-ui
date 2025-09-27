from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_08(page):

        page.goto("https://app.rizz.market/auth/sign-in")

        Home_url = "https://app.rizz.market/app/creator/market"
        login = "79087814701"

        one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
        one_log_button.wait_for(state="visible", timeout=5000)
        one_log_button.click()

        phone_login_input = page.locator('//input[@id=":r0:-form-item"]')
        phone_login_input.wait_for(state="visible", timeout=5000)
        phone_login_input.fill(login)
        phone_login_input.click()

        login_button = page.locator('//button[@type="submit"]')
        login_button.click()

        error_alert = page.locator('//p[@id=":r1:-form-item-message"]')
        expect(error_alert).to_have_text("Обязательное поле", timeout=5000)
        print("Ошибка отработала верно")




