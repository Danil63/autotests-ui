from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_10(page):

        page.goto("https://app.rizz.market/auth/sign-in")

        Home_url = "https://app.rizz.market/app/creator/market"
        login = "+79087810000"
        password = "Gub89087814701"

        one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
        one_log_button.wait_for(state="visible", timeout=5000)
        one_log_button.click()

        phone_login_input = page.locator('//input[@id=":r0:-form-item"]')
        phone_login_input.wait_for(state="visible", timeout=5000)
        phone_login_input.fill(login)
        phone_login_input.click()

        phone_login_input.focus()
        page.keyboard.press("ControlOrMeta+A")
        page.keyboard.press("Backspace")

        expect(phone_login_input).to_have_value("")
        print("Поле login пустое")


        password_login_input = page.locator('//input[@id=":r1:-form-item"]')
        password_login_input.wait_for(state="visible", timeout=5000)
        password_login_input.fill(password)

        password_login_input.focus()
        page.keyboard.press("ControlOrMeta+A")
        page.keyboard.press("Backspace")

        expect(password_login_input).to_have_value("")
        print("Поле password пустое")



