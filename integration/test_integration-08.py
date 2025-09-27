import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.FixeServiceAutoCPM
def test_integration_01():
    # Запуск браузера и страницы
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        file_path = "/Users/mbookpro403gmail.com/Documents/Мишки/_1052135.jpeg"

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "9147992636")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("rowseMbeRilI")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=10000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")

        # Закрываем баннер
        page.locator('//button[contains(@class,"absolute right-4 top-4 rounded-sm")]').click()

        # Поиск и отклик
        search_input = page.locator('//input[@placeholder="Поиск"]')
        search_input.wait_for(state="visible", timeout=10000)
        search_input.fill('Замена экрана в телефоне')
        expect(search_input).to_have_value('Замена экрана в телефоне')
        page.wait_for_timeout(1000)

        response_button = page.locator('//button[text()="Откликнуться"]').nth(0)
        response_button.wait_for(state="visible", timeout=10000)
        response_button.click()

        page.wait_for_timeout(1000)

        response_in_card = page.locator('//button[text()="Откликнуться"]').nth(2)
        response_in_card.scroll_into_view_if_needed()
        response_in_card.wait_for(state="visible", timeout=10000)
        response_in_card.click()
        
        page.locator(2000)

        approved_text = page.locator('//button[(text()="Ваш отклик одобрен, приступайте")]')
        approved_text.wait_for(state="visible", timeout=180000)
        print("Отклик одобрен")


        integ_tabs = page.locator('//a[text()="Интеграции"]').first
        integ_tabs.click()

        page.wait_for_timeout(5000)

        page.reload()

        page.wait_for_timeout(2000)
        
        new_tads = page.locator('//span[text()="Новая"]')
        new_tads.click()
        
        page.locator('//span[text()="Замена экрана в телефоне"]').first.click()

        start_button = page.locator('//button[text()="Начать работу"]')
        start_button.wait_for(state="visible", timeout=30000)
        start_button.click()
 
 
        # Шаг 1
        file_input_step2 = page.locator('//input[@type="file"]').first
        file_input_step2.wait_for(state="attached", timeout=20000)
        file_input_step2.scroll_into_view_if_needed()
        file_input_step2.set_input_files(file_path)

        page.locator('//div[contains(text(),"Загрузка")]').wait_for(state="detached", timeout=30000)

        page.wait_for_timeout(15000)

        print("Картинка загружена для step 1")
        button1 = page.locator('//button[contains(@class,"bg-purple text-white")]').first
        button1.wait_for(state="visible", timeout=10000)
        button1.click()

        page.wait_for_timeout(10000)


@pytest.mark.FixeServiceAutoCPM
def test_integration_04():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "9087814701")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()

        page.locator('//a[text()="Интеграции"]').click()

        page.locator('//p[text()="minicakes.ru"]').click()
     
        accept_button_one = page.locator('//button[contains(text(),"Принять")]').first
        accept_button_one.wait_for(state="visible", timeout=10000)
        accept_button_one.click()

        page.wait_for_timeout(2000)



@pytest.mark.FixeServiceAutoCPM
def test_integration_05():

    # Запуск браузера
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "9147992636")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("rowseMbeRilI")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=20000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")

        # Закрываем баннер
        close_banner = page.locator('//button[contains(@class,"absolute right-4 top-4 rounded-sm")]')
        close_banner.click()

        # Переходим в "Интеграции"
        integration = page.locator('//a[text()="Интеграции"]')
        integration.wait_for(state="visible", timeout=10000)
        integration.click()
        page.wait_for_timeout(2000)

        page.locator('//span[text()="Замена экрана в телефоне"]').click()

       # Ждем именно input по placeholder
        link_input = page.locator('//input[@placeholder="Ссылка на результат"]').first
        link_input.scroll_into_view_if_needed()
        link_input.wait_for(state="visible", timeout=20000)
        link_input.fill("https://www.instagram.com/p/DHxgYDLILJu/?img_index=1")

        submit_button = page.locator('//button[normalize-space(text())="Отправить"]').first
        submit_button.scroll_into_view_if_needed()
        submit_button.wait_for(state="visible", timeout=10000)
        submit_button.click(force=True)

        page.wait_for_timeout(3000)
      
@pytest.mark.FixeServiceAutoCPM
def test_integration_06():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "9087814701")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()
        page.locator('//a[text()="Интеграции"]').click()
        page.locator('//p[text()="minicakes.ru"]').click()

        accept_button_four = page.locator('//button[contains(text(),"Принять")]').first
        accept_button_four.scroll_into_view_if_needed()
        accept_button_four.wait_for(state="visible", timeout=10000)
        accept_button_four.click()

        completion_button = page.locator('//button[@class="inline-flex items-center justify-center text-sm ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none bg-purple text-white disabled:opacity-100 disabled:bg-slate-900/5 disabled:text-slate-900/30 h-10 rounded-2lg px-3 py-2 font-normal mt-4 w-full"]').first
        completion_button.wait_for(state="visible", timeout=10000)
        completion_button.click()

        page.wait_for_timeout(5000)
        browser.close()



@pytest.mark.FixeServiceAutoCPM
def test_integration_07():

    # Запуск браузера
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "9147992636")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("rowseMbeRilI")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=20000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")

        # Закрываем баннер
        close_banner = page.locator('//button[contains(@class,"absolute right-4 top-4 rounded-sm")]')
        close_banner.click()

        # Переходим в "Интеграции"
        integration = page.locator('//a[text()="Интеграции"]')
        integration.wait_for(state="visible", timeout=10000)
        integration.click()
        page.wait_for_timeout(2000)

        page.locator('//span[text()="Принята"]').click()

        card = page.locator('//span[text()="Замена экрана в телефоне"]').first
        card.click()

        # Нажимаем "Создать акт"
        create_act = page.locator(
            '//button[contains(text(),"Создать акт")]'
        ).first
        create_act.scroll_into_view_if_needed()
        create_act.wait_for(state="visible", timeout=180000000)
        create_act.click()
        print("Кнопка 'Создать акт' нажата")

        # Проверяем, что появилась кнопка "Подписать"
        sign_button = page.locator('//button[@class="items-center justify-center text-sm ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none bg-purple text-white disabled:opacity-100 disabled:bg-slate-900/5 disabled:text-slate-900/30 h-10 rounded-2lg px-3 py-2 font-normal flex gap-2"]').first
        sign_button.wait_for(state="visible", timeout=180000000)
        expect(sign_button).to_be_visible()
        print("Кнопка 'Подписать' появилась, но мы её НЕ нажимаем")

        page.wait_for_timeout(5000)
        browser.close()


