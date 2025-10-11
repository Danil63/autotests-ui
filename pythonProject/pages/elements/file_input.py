from elements.base_element import BaseElement

class FileInput(BaseElement):
    def set_input_files(self, file_path: str):
        self.locator.set_input_files(file_path)
        print(f"📂 Файл '{file_path}' загружен в '{self.name}'")