import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_11(page_with_state: Page):
    page = page_with_state

    print("Повторный выбор ранее уже выбранного товара в блоке 'Выберите предмет рекламы' по нажатию на кнопку 'dropdown'")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Обувь")
    expect(category_dropdown).to_have_value("10")  

    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Строительство и ремонт")
    expect(category_dropdown).to_have_value("18") 
    print("Категория меняется корректно")
    