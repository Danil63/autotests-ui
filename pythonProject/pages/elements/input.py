from elements.base_element import BaseElement
from playwright.sync_api import expect

class Input(BaseElement):
    def fill(self, value: str):
        self.locator.fill(value)
        print(f"⌨️ В поле '{self.name}' введено: {value}")

    def check_have_value(self, value: str):
        expect(self.locator).to_have_value(value)
        print(f"✅ Поле '{self.name}' имеет значение: {value}")