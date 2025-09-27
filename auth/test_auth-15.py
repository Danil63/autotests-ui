from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.auth
def test_auth_15(page):

        # Открываем страницу входа
        page.goto("https://app.rizz.market/auth/sign-in", wait_until="load")

        # Кликаем по кнопке "Войти одним кликом"
        one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
        one_log_button.wait_for(state="visible", timeout=5000)
        one_log_button.click()

        # Кликаем по ссылке "Создать аккаунт"
        create_account = page.locator('//a[@class="text-purple underline"]')
        create_account.wait_for(state="visible", timeout=5000)
        create_account.click()

        # Проверяем, что перешли на страницу регистрации
        expect(page).to_have_url("https://app.rizz.market/auth/sign-up")
        print("Пользователь перешел на страницу создания аккаунта")