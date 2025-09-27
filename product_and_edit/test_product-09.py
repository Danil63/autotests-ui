import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.product
def test_product_03(page_with_state: Page):
    page = page_with_state

    print("Создание услуги с заполнением всех обязательных полей + удаление продукта")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()

    service_switch = page.locator('//button[@data-state="inactive"]')   
    service_switch.wait_for(state="visible", timeout=10000)
    service_switch.click() 

    
    file_input = page.locator('//input[@type="file"]')
    file_input.set_input_files("/Users/mbookpro403gmail.com/Documents/Мишки/67d10c6320754737bb43b30fdfe99d72.jpg-profi_max.jpg")
    page.wait_for_timeout(1000)
    print("Картинка загружена")

    page.wait_for_timeout(3000)

   
    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("Замена экрана в телефоне")
    expect(name_input).to_have_value("Замена экрана в телефоне")

   
    description_input = page.locator('//textarea[@name="description"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.fill (
    """ Замена экрана в телефоне — одна из самых востребованных процедур ремонта мобильных устройств. Экран часто повреждается при 
    падениях, ударах или сильном нажатии, что приводит к появлению трещин, отсутствию изображения или некорректной работе сенсора. 
    В процессе замены специалист аккуратно разбирает корпус, отсоединяет повреждённый дисплейный модуль и устанавливает новый, 
    совместимый с конкретной моделью телефона. Важно использовать качественные комплектующие, так как дешёвые аналоги могут 
    быстро выйти из строя или искажать картинку. После установки нового экрана проводится проверка: оценивается яркость, цветопередача 
    и отзывчивость сенсора. Замена экрана позволяет вернуть устройству полный функционал и продлить срок его службы, а своевременное 
    обращение в сервисный центр помогает избежать дополнительных поломок, связанных с попаданием влаги или пыли через трещины.
    """)
    
    category_dropdown = page.locator("//div[label[contains(text(), 'Категория')]]//select")
    category_dropdown.select_option(label="Другое")
    expect(category_dropdown).to_have_value("27")

    page.wait_for_timeout(1000)


    create_product_button = page.locator('//button[text()="Создать"]')
    create_product_button.scroll_into_view_if_needed()
    create_product_button.click()

    page.wait_for_url("https://app.rizz.market/app/advertiser/products", timeout=30000)
    print("Польз на месте")
    

   