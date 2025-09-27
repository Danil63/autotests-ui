import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.mark.product
def test_product_01(page_with_state: Page):
    page = page_with_state
    # гвозди 

    print("Создание товара с заполнением всех обязательных полей")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    
    file_input = page.locator('//input[@type="file"]').first
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/_1052135.jpeg")
    page.wait_for_timeout(1000)
    print("Картинка загружена")
    
    
    product_card_image = page.locator("//img[contains(@src, 'rizz.market')]")
    product_card_image.wait_for(state="visible", timeout=10000)
    expect(product_card_image).to_be_visible()

    
    src_value = product_card_image.get_attribute("src")
    assert src_value and "rizz.market" in src_value


    artic_input = page.locator('//input[@name="sku"]')
    artic_input.wait_for(state="visible", timeout=10000)
    artic_input.fill("556161")
    expect(artic_input).to_have_value("556161")

   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("Гвоздь для пистолета")
    expect(name_input).to_have_value("Гвоздь для пистолета")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill("Гвозди Startul Profi для нейлера пневмостеплера тип 18GA 30 мм - это надежные и высококачественные гвозди, предназначенные для использования с пневмостеплерами. Изготовлены из закаленной углеродистой стали Q235, имеют оцинкованнное покрытие. Сечение 1,25х1,00 мм. Размер шляпки - 2 мм. Они идеально подходят для различных задач, связанных с монтажом и креплением материалов. Эти гвозди типа 18GA обладают идеальной длиной 30 мм, что позволяет легко проникать в поверхности различной толщины. Благодаря большому количеству - 5000 штук в упаковке, вы получаете долговечное решение для вашего проекта. Преимущества использования гвоздей для нейлера типа 18GA включают их высокую прочность и надежность. Они быстро и точно крепят материалы вместе, обеспечивая долговечное и надежное соединение. Благодаря тщательному изготовлению и использованию высококачественных материалов, эти гвозди отличаются своей стабильностью и устойчивостью к коррозии.")
    expect(description_input).to_have_value("Гвозди Startul Profi для нейлера пневмостеплера тип 18GA 30 мм - это надежные и высококачественные гвозди, предназначенные для использования с пневмостеплерами. Изготовлены из закаленной углеродистой стали Q235, имеют оцинкованнное покрытие. Сечение 1,25х1,00 мм. Размер шляпки - 2 мм. Они идеально подходят для различных задач, связанных с монтажом и креплением материалов. Эти гвозди типа 18GA обладают идеальной длиной 30 мм, что позволяет легко проникать в поверхности различной толщины. Благодаря большому количеству - 5000 штук в упаковке, вы получаете долговечное решение для вашего проекта. Преимущества использования гвоздей для нейлера типа 18GA включают их высокую прочность и надежность. Они быстро и точно крепят материалы вместе, обеспечивая долговечное и надежное соединение. Благодаря тщательному изготовлению и использованию высококачественных материалов, эти гвозди отличаются своей стабильностью и устойчивостью к коррозии.")

    
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Детские товары")
    expect(category_dropdown).to_have_value("3")

    
    brand_input = page.locator('//input[@name="brand"]')
    brand_input.fill("Железо")
    expect(brand_input).to_have_value("Железо")

    
    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="ВсеИнструменты")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "ВсеИнструменты"

    
    price_input = page.locator('//input[@placeholder="Цена в рублях"]')
    price_input.scroll_into_view_if_needed()
    price_input.wait_for(state="visible", timeout=10000)
    price_input.fill("100")
    expect(price_input).to_have_value("100")

    product_link_input = page.locator('//input[@name="link"]')
    product_link_input.wait_for(state="visible", timeout=10000)
    product_link_input.fill("https://www.wildberries.ru/catalog/323108096/detail.aspx?targetUrl=SP")
    expect(product_link_input).to_have_value("https://www.wildberries.ru/catalog/323108096/detail.aspx?targetUrl=SP")
    print("Поля заполнены")

    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

   
    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")





