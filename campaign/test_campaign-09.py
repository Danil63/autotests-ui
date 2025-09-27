import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.mark.campaign
def test_campaignn_03(page_with_state_comp: Page):
    page = page_with_state_comp


    print("AUTO-TEST CPM + услуга")

    create_product_button = page.locator("//a[text()='Создать']")
    create_product_button.wait_for(state="visible", timeout=10000)
    create_product_button.click()  

    name_input = page.locator('//input[@name="title"]')
    name_input.wait_for(state="visible", timeout=10000)
    name_input.fill("AUTO-TEST CPM + услуга")
    expect(name_input).to_have_value("AUTO-TEST CPM + услуга")

    format_sdelki = page.locator('//button[text()="Фиксированная"]')
    format_sdelki.wait_for(state="visible", timeout=10000)
    format_sdelki.scroll_into_view_if_needed()
    format_sdelki.click()


    product_dropdown = page.get_by_role("combobox", name="Выберите предмет рекламы")
    product_dropdown.wait_for(state="visible", timeout=10000)
    product_dropdown.click()

    tabs = page.locator('//button[text()="Услуги"]').click()
    page.wait_for_timeout(1000)

    option_to_select = page.get_by_text("Замена экрана в телефоне").first
    option_to_select.wait_for(state="visible", timeout=10000)
    option_to_select.click()

    expect(product_dropdown).to_contain_text("Замена экрана в телефоне")

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
    description_input.fill("Мойка окон — это важный этап в уходе за жилыми и коммерческими помещениями, который напрямую влияет не только на внешний облик здания, но и на уровень освещённости, общее восприятие пространства и даже на настроение людей, находящихся внутри. Чистые окна обеспечивают максимальный приток естественного света, что делает помещение более светлым, уютным и визуально просторным. Процесс мойки окон включает в себя удаление пыли, грязи, следов дождя, насекомых, копоти, а также последствий строительных или ремонтных работ. Важно учитывать, что загрязнения на стекле могут быть как поверхностными, так и въевшимися, требующими специальных чистящих средств и профессионального подхода. Существуют различные технологии и методы мойки окон — от ручной чистки тряпками и скребками до применения профессионального инвентаря, таких как телескопические штанги, парогенераторы, водоочистительные установки и моющие роботы. При этом для высотных зданий или труднодоступных окон особенно актуальна альпинистская мойка, выполняемая специалистами с соответствующей ёподготовкой и страховкой. Помимо внешней стороны, мойка окон включает в себя и внутреннюю поверхность стеклопакетов, а также рамы, подоконники и фурнитуру. Для достижения наилучшего результата часто используют двухэтапную мойку: сначала — с применением моющих растворов для устранения сильных загрязнений, затем — с чистой водой и микрофиброй для блеска без разводов. Важно также грамотно подбирать средства в зависимости от типа поверхности — например, пластиковые и деревянные рамы требуют разного подхода. Использование абразивов или слишком агрессивной химии может привести к повреждению покрытия, помутнению стекла или образованию царапин. В связи с этим профессиональные клининговые компании предлагают не только комплексную мойку окон, но и консультации по уходу за оконными конструкциями. Регулярная мойка — весной и осенью — помогает поддерживать эстетику и продлевает срок службы окон. Особое внимание стоит уделить мойке после сильных погодных условий, таких как пыльные бури, ливни с грязью или снегопады, оставляющие на стекле солевые и минеральные разводы. В домашних условиях популярны экологичные средства — уксус, лимонная кислота, сода, нашатырный спирт — однако для достижения профессионального результата часто требуется техника и опыт. При этом важно соблюдать технику безопасности, особенно при мойке снаружи на этажах выше первого. Также при мойке важно не только качество, но и время — быстрое и аккуратное удаление загрязнений без повреждения отделки. последнее время популярность набирают автоматические роботы для мойки окон, которые крепятся к стеклу с помощью вакуумного присоса, перемещаются по поверхности, распыляют воду и очищают стекло, экономя силы и время владельцев. Однако даже такие устройства требуют внимания, правильной настройки и технического обслуживания. Мойка окон также может включать полировку стекол, обработку антистатическими составами или защитными покрытиями, которые отталкивают пыль и капли воды, что позволяет дольше сохранять результат чистки.")
    expect(description_input).to_have_value("Мойка окон — это важный этап в уходе за жилыми и коммерческими помещениями, который напрямую влияет не только на внешний облик здания, но и на уровень освещённости, общее восприятие пространства и даже на настроение людей, находящихся внутри. Чистые окна обеспечивают максимальный приток естественного света, что делает помещение более светлым, уютным и визуально просторным. Процесс мойки окон включает в себя удаление пыли, грязи, следов дождя, насекомых, копоти, а также последствий строительных или ремонтных работ. Важно учитывать, что загрязнения на стекле могут быть как поверхностными, так и въевшимися, требующими специальных чистящих средств и профессионального подхода. Существуют различные технологии и методы мойки окон — от ручной чистки тряпками и скребками до применения профессионального инвентаря, таких как телескопические штанги, парогенераторы, водоочистительные установки и моющие роботы. При этом для высотных зданий или труднодоступных окон особенно актуальна альпинистская мойка, выполняемая специалистами с соответствующей ёподготовкой и страховкой. Помимо внешней стороны, мойка окон включает в себя и внутреннюю поверхность стеклопакетов, а также рамы, подоконники и фурнитуру. Для достижения наилучшего результата часто используют двухэтапную мойку: сначала — с применением моющих растворов для устранения сильных загрязнений, затем — с чистой водой и микрофиброй для блеска без разводов. Важно также грамотно подбирать средства в зависимости от типа поверхности — например, пластиковые и деревянные рамы требуют разного подхода. Использование абразивов или слишком агрессивной химии может привести к повреждению покрытия, помутнению стекла или образованию царапин. В связи с этим профессиональные клининговые компании предлагают не только комплексную мойку окон, но и консультации по уходу за оконными конструкциями. Регулярная мойка — весной и осенью — помогает поддерживать эстетику и продлевает срок службы окон. Особое внимание стоит уделить мойке после сильных погодных условий, таких как пыльные бури, ливни с грязью или снегопады, оставляющие на стекле солевые и минеральные разводы. В домашних условиях популярны экологичные средства — уксус, лимонная кислота, сода, нашатырный спирт — однако для достижения профессионального результата часто требуется техника и опыт. При этом важно соблюдать технику безопасности, особенно при мойке снаружи на этажах выше первого. Также при мойке важно не только качество, но и время — быстрое и аккуратное удаление загрязнений без повреждения отделки. последнее время популярность набирают автоматические роботы для мойки окон, которые крепятся к стеклу с помощью вакуумного присоса, перемещаются по поверхности, распыляют воду и очищают стекло, экономя силы и время владельцев. Однако даже такие устройства требуют внимания, правильной настройки и технического обслуживания. Мойка окон также может включать полировку стекол, обработку антистатическими составами или защитными покрытиями, которые отталкивают пыль и капли воды, что позволяет дольше сохранять результат чистки.")


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