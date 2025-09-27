import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.CompBarter
def test_campaignn_01(page_with_state_comp: Page):
    page = page_with_state_comp
    # дальше работаешь с page

    print("AUTO-TEST Бартер БЕЗ авто")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()  

    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("AUTO-TEST Бартер БЕЗ авто")
    expect(name_input).to_have_value("AUTO-TEST Бартер БЕЗ авто")

    product_dropdown = page.get_by_role("combobox", name="Выберите предмет рекламы")
    product_dropdown.wait_for(state="visible", timeout=10000)
    product_dropdown.click()

    option_to_select = page.get_by_text("Гвоздь для пистолета").first
    option_to_select.wait_for(state="visible", timeout=10000)
    option_to_select.click()
    expect(product_dropdown).to_contain_text("Гвоздь для пистолета")

    product = page.locator('//div[@class="relative flex cursor-default select-none rounded-sm px-2 py-1.5 text-sm outline-none aria-selected:bg-accent aria-selected:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 items-start gap-2"]').first
    product.wait_for(state="visible", timeout=10000)

    link_UTM_input = page.locator('//input[@name="productLink"]')
    link_UTM_input.wait_for(state="visible", timeout=10000)
    link_UTM_input.fill("https://www.wildberries.ru/catalog/323108096/detail.aspx")
    expect(link_UTM_input).to_have_value("https://www.wildberries.ru/catalog/323108096/detail.aspx")


    content_format_button = page.locator('//button[text()="Добавить"]')
    content_format_button.wait_for(state="visible", timeout=10000)
    content_format_button.click()

    page.wait_for_timeout(2000)
    
    post_checkbox = page.get_by_role("checkbox", name="Пост").first
    post_checkbox.wait_for(state="visible", timeout=10000)
    post_checkbox.click()

    reels_checkbox = page.get_by_role("checkbox", name="Reels").first
    reels_checkbox.click()

    story_checkbox = page.get_by_role("checkbox", name="История").first
    story_checkbox.click()


    content_format_button = page.locator('//button[@class="items-center justify-center text-sm ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none border border-input bg-white text-slate-900 disabled:opacity-100 disabled:bg-white disabled:text-slate-900/30 h-10 rounded-2lg px-3 py-2 flex gap-2 font-normal"]').nth(1)
    content_format_button.wait_for(state="visible", timeout=10000)
    content_format_button.click()

   
    dropdown_button = page.locator("div", has_text="Знаменитости").first
    dropdown_button.scroll_into_view_if_needed
    page.wait_for_timeout(2000)
    dropdown_button.click()


    description_input = page.locator('//textarea[@class="flex w-full rounded-md border border-input bg-background px-3 py-2 text-base md:text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 min-h-72"]')
    description_input.wait_for(state="visible", timeout=10000)
    description_input.scroll_into_view_if_needed
    description_input.fill("Отредактированное описание")
    expect(description_input).to_have_value("Отредактированное описание")



    # прайс тот же
    price_input = page.locator('//input[@placeholder="Сумма"]').first
    price_input.wait_for(state="visible", timeout=10000)
    price_input.scroll_into_view_if_needed()
    price_input.fill("11")
    expect(price_input).to_have_value("11 ₽")

    integration_input = page.locator('//input[@placeholder="Кол-во"]')
    integration_input.wait_for(state="visible", timeout=10000)
    integration_input.scroll_into_view_if_needed()
    integration_input.fill("1")
    expect(integration_input).to_have_value("1")

    auto_approval = page.locator('//button[@role="switch"]').nth(1)
    auto_approval.wait_for(state="visible", timeout=10000)
    auto_approval.scroll_into_view_if_needed()
    auto_approval.click()


    create_campaign_button = page.locator('//button[@class="inline-flex items-center justify-center text-sm ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none bg-purple text-white disabled:opacity-100 disabled:bg-slate-900/5 disabled:text-slate-900/30 h-10 rounded-2lg px-3 py-2 font-normal flex-1"]').first
    create_campaign_button.wait_for(state="visible", timeout=10000)
    create_campaign_button.scroll_into_view_if_needed
    create_campaign_button.click()
    page.wait_for_timeout(5000)


    value_content_format = page.locator('//div[@class="flex flex-wrap items-center gap-2 text-sm"]').first
    value_content_format.wait_for(state="visible", timeout=10000)
    expect(value_content_format).to_contain_text("Пост")
    expect(value_content_format).to_contain_text("Reels")
    expect(value_content_format).to_contain_text("История") 

    value_category = page.locator('//div[@class="inline-flex items-center rounded-full border border-slate-200 px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-slate-950 focus:ring-offset-2 dark:border-slate-800 dark:focus:ring-slate-300 text-slate-950 dark:text-slate-50"]')
    value_category.wait_for(state="visible", timeout=10000)
    expect(value_category).to_contain_text("Дети и родители")   
    
    marketing_platform = page.locator('//dd[text()="ВсеИнструменты"]')
    print("Платформа маркетинга верная")

    page.wait_for_timeout(2000)

   

    