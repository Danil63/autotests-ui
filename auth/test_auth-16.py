from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_16(page):

        page.goto("https://app.rizz.market/auth/sign-in")

        Home_url = "https://app.rizz.market/app/creator/market"

        one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
        one_log_button.wait_for(state="visible", timeout=5000)
        one_log_button.click()

        Create_account = page.locator('//a[@class="mt-2 text-sm font-light underline"]')
        Create_account.click()

        expect(page).to_have_url('https://app.rizz.market/auth/recover-password')
        print("Пользователь перешел на страницу востановления пароля")

