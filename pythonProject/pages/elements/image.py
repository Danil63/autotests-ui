from elements.base_element import BaseElement

class Image(BaseElement):
    def check_visible(self):
        super().check_visible()
        print(f"🖼️ Изображение '{self.name}' отображается")