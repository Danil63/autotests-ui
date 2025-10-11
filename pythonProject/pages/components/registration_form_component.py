from elements.input import Input
from elements.button import Button

class RegistrationFormComponent:
    def __init__(self, page):
        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.submit_button = Button(page, 'registration-form-submit-button', 'Register')

    def register(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        print("📝 Регистрация выполнена")