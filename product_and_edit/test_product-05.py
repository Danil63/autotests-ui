import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_05(page_with_state: Page):
    page = page_with_state
    # лом меди

    print("Повторное создание товара Лом меди + редактирование через кебаб меню")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()


    file_input = page.locator('//input[@type="file"]').first
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/94897836583789.jpg")
    page.wait_for_timeout(1000)
    print("Картинка загружена")


    artic_input = page.locator('//input[@name="sku"]')
    artic_input.wait_for(state="visible", timeout=10000)
    artic_input.fill("556161")
    expect(artic_input).to_have_value("556161")

   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("Лом меди")
    expect(name_input).to_have_value("Лом меди")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill("Лом меди – это вторичное сырьё, образующееся при утилизации кабелей, проводов, труб, радиаторов и другого оборудования. Медь ценится за высокую электропроводность, теплопроводность и устойчивость к коррозии, поэтому её активно принимают и перерабатывают. Сдача медного лома выгодна: он имеет высокую стоимость на рынке цветных металлов. Переработка снижает нагрузку на добычу природных ресурсов и способствует экологичному производству.")
    expect(description_input).to_have_value("Лом меди – это вторичное сырьё, образующееся при утилизации кабелей, проводов, труб, радиаторов и другого оборудования. Медь ценится за высокую электропроводность, теплопроводность и устойчивость к коррозии, поэтому её активно принимают и перерабатывают. Сдача медного лома выгодна: он имеет высокую стоимость на рынке цветных металлов. Переработка снижает нагрузку на добычу природных ресурсов и способствует экологичному производству.")

    
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Цифровые товары")
    expect(category_dropdown).to_have_value("25")

    
    brand_input = page.locator('//input[@name="brand"]')
    brand_input.fill("Яблоня")
    expect(brand_input).to_have_value("Яблоня")

    
    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="Ozon")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "Ozon"


    price_input = page.locator('//input[@placeholder="Цена в рублях"]')
    price_input.scroll_into_view_if_needed()
    price_input.wait_for(state="visible", timeout=10000)
    price_input.fill("15")
    expect(price_input).to_have_value("15")

    product_link_input = page.locator('//input[@name="link"]')
    product_link_input.wait_for(state="visible", timeout=10000)
    product_link_input.fill("https://www.wildberries.ru/catalog/260912292/detail.aspx")
    expect(product_link_input).to_have_value("https://www.wildberries.ru/catalog/260912292/detail.aspx")
    print("Поля заполнены")

    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")
