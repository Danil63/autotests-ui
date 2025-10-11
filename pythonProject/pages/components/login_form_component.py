from elements.input import Input
from elements.button import Button

class LoginFormComponent:
    def __init__(self, page):
        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')
        self.login_button = Button(page, 'login-form-submit-button', 'Login')

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        print("🔓 Авторизация выполнена")