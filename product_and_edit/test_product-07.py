import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_06(page_with_state: Page):
    page = page_with_state
    # штангель циркуль

    print("Повторное создание товара + редактирование через кебаб меню")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()


    file_input = page.locator('//input[@type="file"]').first
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/8af6c99503e43ef4c4df01b4c29475f7.jpg")
    page.wait_for_timeout(1000)
    print("Картинка загружена")


    artic_input = page.locator('//input[@name="sku"]')
    artic_input.wait_for(state="visible", timeout=10000)
    artic_input.fill("556161")
    expect(artic_input).to_have_value("556161")

   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("штангель циркуль")
    expect(name_input).to_have_value("штангель циркуль")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill("Штангенциркуль — универсальный измерительный инструмент для точного определения наружных и внутренних размеров, глубины и шагов деталей. Оснащён губками, глубиномером и шкалой (нониусной или цифровой). Обеспечивает высокую точность до 0,02 мм, применяется в машиностроении и быту.")
    expect(description_input).to_have_value("Штангенциркуль — универсальный измерительный инструмент для точного определения наружных и внутренних размеров, глубины и шагов деталей. Оснащён губками, глубиномером и шкалой (нониусной или цифровой). Обеспечивает высокую точность до 0,02 мм, применяется в машиностроении и быту.")
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Строительство и ремонт")
    expect(category_dropdown).to_have_value("18")

    
    brand_input = page.locator('//input[@name="brand"]')
    brand_input.fill("Инструменты")
    expect(brand_input).to_have_value("Инструменты")

    
    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="ВсеИнструменты")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "ВсеИнструменты"


    price_input = page.locator('//input[@placeholder="Цена в рублях"]')
    price_input.scroll_into_view_if_needed()
    price_input.wait_for(state="visible", timeout=10000)
    price_input.fill("10")
    expect(price_input).to_have_value("10")

    product_link_input = page.locator('//input[@name="link"]')
    product_link_input.wait_for(state="visible", timeout=10000)
    product_link_input.fill("https://www.wildberries.ru/catalog/437026734/detail.aspx")
    expect(product_link_input).to_have_value("https://www.wildberries.ru/catalog/437026734/detail.aspx")
    print("Поля заполнены")

    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")
    
