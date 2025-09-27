import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_11(page_with_state: Page):
    page = page_with_state

    print("Повторный выбор ранее уже выбранного товара в блоке 'Выберите предмет рекламы' по нажатию на кнопку 'dropdown'")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="Ozon")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "Ozon"

    marketplace_dropdown = page.locator("//div[label[contains(text(), 'Маркетплейс')]]//select")
    marketplace_dropdown.wait_for(state="visible", timeout=10000)
    marketplace_dropdown.select_option(label="Магнит Маркет")
    selected_text = marketplace_dropdown.locator("option:checked").inner_text()
    assert selected_text == "Магнит Маркет"