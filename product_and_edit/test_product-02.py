import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_02(page_with_state: Page):
    page = page_with_state
    # заклепки

    print("Повторное создание товара + редактирование через кебаб меню")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()


    file_input = page.locator('//input[@type="file"]').first
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/Без названия (2).jpeg")
   
    print("Картинка загружена")


    artic_input = page.locator('//input[@name="sku"]')
    artic_input.wait_for(state="visible", timeout=10000)
    artic_input.fill("556161")
    expect(artic_input).to_have_value("556161")

   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("заклепки")
    expect(name_input).to_have_value("заклепки")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill("заклепки")
    expect(description_input).to_have_value("заклепки")

    
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Детские товары")
    expect(category_dropdown).to_have_value("3")

    
    brand_input = page.locator('//input[@name="brand"]')
    brand_input.fill("ТукТук")
    expect(brand_input).to_have_value("ТукТук")

    
    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="ВсеИнструменты")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "ВсеИнструменты"

    
    price_input = page.locator('//input[@placeholder="Цена в рублях"]')
    price_input.scroll_into_view_if_needed()
    price_input.wait_for(state="visible", timeout=10000)
    price_input.fill("15")
    expect(price_input).to_have_value("15")

    product_link_input = page.locator('//input[@name="link"]')
    product_link_input.wait_for(state="visible", timeout=10000)
    product_link_input.fill("https://market.yandex.ru/card/6-kolesnyy-vnedorozhnik-4-wd-na-pulte-du-radioupravlyayemaya-mashinka-polnyy-privod---chernyy/103002821313?do-waremd5=pSmgNDD5ovrd48GCSh0XjA&cpc=TVViUX1alipQEEZSl5XgrH4O8LpR4h-GZXzZrO1RypVKk4BufWHiFzjrVOfezXR_VD1iPR44mpBWVgQQ5hK0VOiUNgVi6j_tuBbiV5x_pGU5_PgeyyBAN2xr7iERyM00sbg3oamnEjGQ0yaNHWOEJaTmWEavbjx9hj3Hv85jR3jjFXm1NP-tGpV7-FswZg-HM_6I-dBlNPCE7DtXnuvBe4oFLW2wGtmddEY4-sv5UZbfYZbV8ETp9DMKvBphZHtOiYu_uKPl0FYritSwAOVl0x0mQE-ELy7UKn0-Q6fDuzuViRoxQg7-Fmw2MWKlvsngcrW-pEls9t8liiOi_SM6iJ9ihM9v-0oSYBUeb5rUxFs_lyg0m5UKCYKtesU_daUemJwNbrzXljM0XKIo6UtXFCvXn5eulhCvCA6ko_pXxyx8blOwfxJmm827Xw6dR4fmR2iH1aQG3r4G50IfCizaZc3Fje_egPRTZ_QPYqlD_ps%2C&ogV=-3")
    expect(product_link_input).to_have_value("https://market.yandex.ru/card/6-kolesnyy-vnedorozhnik-4-wd-na-pulte-du-radioupravlyayemaya-mashinka-polnyy-privod---chernyy/103002821313?do-waremd5=pSmgNDD5ovrd48GCSh0XjA&cpc=TVViUX1alipQEEZSl5XgrH4O8LpR4h-GZXzZrO1RypVKk4BufWHiFzjrVOfezXR_VD1iPR44mpBWVgQQ5hK0VOiUNgVi6j_tuBbiV5x_pGU5_PgeyyBAN2xr7iERyM00sbg3oamnEjGQ0yaNHWOEJaTmWEavbjx9hj3Hv85jR3jjFXm1NP-tGpV7-FswZg-HM_6I-dBlNPCE7DtXnuvBe4oFLW2wGtmddEY4-sv5UZbfYZbV8ETp9DMKvBphZHtOiYu_uKPl0FYritSwAOVl0x0mQE-ELy7UKn0-Q6fDuzuViRoxQg7-Fmw2MWKlvsngcrW-pEls9t8liiOi_SM6iJ9ihM9v-0oSYBUeb5rUxFs_lyg0m5UKCYKtesU_daUemJwNbrzXljM0XKIo6UtXFCvXn5eulhCvCA6ko_pXxyx8blOwfxJmm827Xw6dR4fmR2iH1aQG3r4G50IfCizaZc3Fje_egPRTZ_QPYqlD_ps%2C&ogV=-3")
    print("Поля заполнены")

    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")
