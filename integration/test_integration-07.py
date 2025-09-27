import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.Cpm
def test_integration_01():
    # Запуск браузера и страницы
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "79938854791")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=10000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")

        # Поиск и отклик
        search_input = page.locator('//input[@placeholder="Поиск"]')
        search_input.wait_for(state="visible", timeout=10000)
        search_input.fill('штангель циркуль')
        expect(search_input).to_have_value('штангель циркуль')
        page.wait_for_timeout(1000)

        response_button = page.locator('//button[text()="Откликнуться"]').nth(0)
        response_button.wait_for(state="visible", timeout=10000)
        response_button.click()

        page.wait_for_timeout(1000)

        response_in_card = page.locator('//button[text()="Откликнуться"]').nth(1)
        response_in_card.scroll_into_view_if_needed()
        response_in_card.wait_for(state="visible", timeout=10000)
        response_in_card.click()
        
        page.locator(2000)

        approved_text = page.locator('//button[(text()="Ваш отклик одобрен, приступайте")]')
        approved_text.wait_for(state="visible", timeout=180000)
        print("Отклик одобрен")

        page.wait_for_timeout(1000)


def retry_if_error(page, button, timeout=5000):
    """
    Проверяет наличие текста 'ошибка' и кликает по кнопке повторно.
    Если ошибки нет, просто идём дальше.
    """
    try:
        error = page.locator("//*[contains(text(),'ошибка')]")
        error.wait_for(state="visible", timeout=timeout)
        print("вылезла ошибка")
        page.wait_for_timeout(2000)
        button.click()
        page.wait_for_timeout(2000)
    except:
        # Ошибка не появилась за timeout → продолжаем
        pass        



@pytest.mark.Cpm
def test_integration_02():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        file_path = "/Users/mbookpro403gmail.com/Documents/Мишки/_1052135.jpeg"

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "79938854791")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_timeout(1000)
        attempt = 1
        while True:
            new_integration = page.locator('//span[text()="Новая"]').first
            new_integration.wait_for(state="visible", timeout=10000)
            new_integration.click()

            try:
                card_company_integration = page.locator('//span[text()="штангель циркуль"]')
                card_company_integration.wait_for(state="visible", timeout=5000)
                print(f"Элемент найден на {attempt}-й попытке ✅")
                card_company_integration.click()
                break
            except:
                print(f"С {attempt}-го раза не прогрузилось ❌ — обновляем страницу")
                attempt += 1
                page.reload()
                page.wait_for_timeout(2000)
        
        start_button = page.locator('//button[text()="Товар выкуплен"]')
        start_button.wait_for(state="visible", timeout=30000)
        start_button.click()
 
        # === Шаг 1 ===
        file_input_step1 = page.locator('//input[@type="file"]').first
        file_input_step1.wait_for(state="attached", timeout=20000)
        file_input_step1.scroll_into_view_if_needed()
        file_input_step1.set_input_files(file_path)
        page.wait_for_timeout(10000)
        print("Картинка загружена для step 1")

        button1 = page.locator('//button[contains(@class,"bg-purple text-white")]').first
        button1.wait_for(state="visible", timeout=10000)
        button1.click()
        page.wait_for_timeout(2000)
        retry_if_error(page, button1)

        # === Шаг 2 ===
        file_input_step2 = page.locator('//input[@type="file"]').first
        file_input_step2.wait_for(state="attached", timeout=20000)
        file_input_step2.scroll_into_view_if_needed()
        file_input_step2.set_input_files(file_path)
        page.wait_for_timeout(5000)
        print("Картинка загружена для step 2")

        button2 = page.locator('//button[contains(@class,"bg-purple text-white")]').first
        button2.wait_for(state="visible", timeout=10000)
        button2.click()
        retry_if_error(page, button2)

        # === Шаг 3 ===
        file_input_step3 = page.locator('//input[@type="file"]').first
        file_input_step3.wait_for(state="attached", timeout=20000)
        file_input_step3.scroll_into_view_if_needed()
        file_input_step3.set_input_files(file_path)
        page.wait_for_timeout(5000)
        print("Картинка загружена для step 3")

        button3 = page.locator('//button[contains(@class,"bg-purple text-white")]').first
        button3.wait_for(state="visible", timeout=10000)
        button3.click()
        retry_if_error(page, button3)
        

@pytest.mark.Cpm
def test_integration_03():
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
        retry_if_error(page, accept_button_one)

        page.wait_for_timeout(2000)

        accept_button_two = page.locator('//button[contains(text(),"Принять")]').first
        accept_button_two.wait_for(state="visible", timeout=10000)
        accept_button_two.click()
        retry_if_error(page, accept_button_two)

        page.wait_for_timeout(2000)

        accept_button_three = page.locator('//button[contains(text(),"Принять")]').first
        accept_button_three.wait_for(state="visible", timeout=10000)
        accept_button_three.click()
        retry_if_error(page, accept_button_three)

        page.wait_for_timeout(2000)



@pytest.mark.Cpm
def test_integration_04():

    # Запуск браузера
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "79938854791")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=20000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")

        # Переходим в "Интеграции"
        integration = page.locator('//a[text()="Интеграции"]')
        integration.wait_for(state="visible", timeout=10000)
        integration.click()
        page.wait_for_timeout(2000)

        page.locator('//span[text()="штангель циркуль"]').click()

       # Ждем именно input по placeholder
        link_input = page.locator('//input[@placeholder="Ссылка на результат"]').first
        link_input.scroll_into_view_if_needed()
        link_input.wait_for(state="visible", timeout=20000)
        link_input.fill("https://www.instagram.com/p/DHxgYDLILJu/?img_index=1")

        submit_button = page.locator('//button[normalize-space(text())="Отправить"]').first
        submit_button.scroll_into_view_if_needed()
        submit_button.wait_for(state="visible", timeout=10000)
        submit_button.click(force=True)

        confirmation = page.locator("//*[contains(text(),'отправлен')]")
        confirmation.wait_for(state="visible", timeout=30000)  # ждём до 30 секунд
        print("Сообщение 'отправлен' появилось!")

        page.wait_for_timeout(2000)


@pytest.mark.Cpm
def test_integration_05():
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
        accept_button_four.click(force=True)

        completion_button = page.locator('//button[@class="inline-flex items-center justify-center text-sm ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none bg-purple text-white disabled:opacity-100 disabled:bg-slate-900/5 disabled:text-slate-900/30 h-10 rounded-2lg px-3 py-2 font-normal mt-4 w-full"]').first
        completion_button.wait_for(state="visible", timeout=10000)
        completion_button.click()

        page.wait_for_timeout(5000)
        browser.close()



@pytest.mark.Cpm
def test_integration_06():

    # Запуск браузера
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Авторизация
        page.goto("https://app.rizz.market/auth/sign-in")
        page.locator('//span[@class="text-sm text-gray-500 underline"]').click()

        phone_login_input = page.locator('//input[@aria-describedby=":r0:-form-item-description"]')
        phone_login_input.click()
        page.evaluate("""text => navigator.clipboard.writeText(text)""", "79938854791")
        page.keyboard.press("Meta+V")

        page.locator('//input[@aria-describedby=":r1:-form-item-description"]').fill("89087814701")
        page.locator('//button[@type="submit"]').click()

        page.wait_for_url("https://app.rizz.market/app/creator/market", timeout=20000)
        expect(page).to_have_url("https://app.rizz.market/app/creator/market")
        print("Пользователь на главной странице")


        # Переходим в "Интеграции"
        integration = page.locator('//a[text()="Интеграции"]')
        integration.wait_for(state="visible", timeout=10000)
        integration.click()
        page.wait_for_timeout(2000)

        page.locator('//span[text()="Принята"]').click()

        card = page.locator('//span[text()="штангель циркуль"]').first
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
        browser.close()




        

