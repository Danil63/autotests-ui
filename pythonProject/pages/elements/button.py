from elements.base_element import BaseElement

class Button(BaseElement):
    def is_disabled(self):
        return self.locator.is_disabled()