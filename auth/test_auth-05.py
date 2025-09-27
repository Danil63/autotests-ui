from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_05(page):

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


        password_login_input = page.locator('//input[@id=":r1:-form-item"]')
        password_login_input.wait_for(state="visible", timeout=5000)
        password_login_input.fill(password)

        expect(password_login_input).to_have_value(password)
        print("Поле пароль заполнено валидно")

        login_button = page.locator('//button[@type="submit"]')
        login_button.click()

        error_alert = page.locator('//div[@class="text-sm font-semibold"]')
        expect(error_alert).to_have_text("Произошла ошибка", timeout=5000)

        error_alert2 = page.locator('//div[@class="text-sm opacity-90"]')
        expect(error_alert2).to_have_text("Пользователь не найден", timeout=5000)
        print("Ошибки отработали верно")



    