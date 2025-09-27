from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_03(page):

        page.goto("https://app.rizz.market/auth/sign-in")

        Home_url = "https://app.rizz.market/app/creator/market"
        login = "79087814701"
        password = "89087814701"

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

        #Проверки на поле password
        expect(password_login_input).to_have_value(password)
        print("Поле пароль заполнено валидно")

        login_button = page.locator('//button[@type="submit"]')
        login_button.click()

        # Проверки на кнопку Login
        expect(page).to_have_url(Home_url, timeout=5000)
        print("Пользователь на главной странице")

        page.reload()
    
        expect(page).to_have_url(Home_url, timeout=5000)
        print("После обновления страницы пользователь находиться на главной странице")



    