from playwright.sync_api import expect

class BaseElement:
    def __init__(self, page, test_id: str, name: str):
        self.page = page
        self.locator = page.get_by_test_id(test_id)
        self.name = name

    def check_visible(self):
        expect(self.locator).to_be_visible()
        print(f"✅ Элемент '{self.name}' виден")

    def click(self):
        self.locator.click()
        print(f"🖱️ Клик по элементу '{self.name}'")

    def check_have_text(self, text: str):
        expect(self.locator).to_have_text(text)
        print(f"✅ '{self.name}' содержит текст: {text}")