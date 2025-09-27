from playwright.sync_api import expect
import pytest

@pytest.mark.auth
def test_auth_01(page): 
    page.goto("https://app.rizz.market/auth/sign-in")

    
    one_log_button = page.locator('//span[@class="text-sm text-gray-500 underline"]')
    one_log_button.click()

   
    phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
    phone_login_input.fill("79087814701")

    password_login_input = page.locator('//input[@aria-describedby=":r1:-form-item-description"]')
    password_login_input.fill("89087814701")

    
    login_button = page.locator('//button[@type="submit"]')
    login_button.click()

    
    Home_url = "https://app.rizz.market/app/creator/market"
    expect(page).to_have_url(Home_url, timeout=10000)

    print("Пользователь на главной странице")
