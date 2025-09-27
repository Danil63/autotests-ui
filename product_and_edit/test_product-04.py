import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_04(page_with_state: Page):
    page = page_with_state

    print("AUTO-TEST Бартер БЕЗ авто")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()


    service_switch = page.locator('//button[@data-state="inactive"]')   
    service_switch.wait_for(state="visible", timeout=10000)
    service_switch.click() 
    
    file_input = page.locator('//input[@type="file"]')
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/pervyj-ekran-remont-molnii-sumki.jpg")
    page.wait_for_timeout(2000)
    print("Картинка загружена")
   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("Ремонт замков на сумках")
    expect(name_input).to_have_value("Ремонт замков на сумках")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill("c")
    expect(description_input).to_have_value("c")

    
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Одежда")
    expect(category_dropdown).to_have_value("9")


    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")
    
