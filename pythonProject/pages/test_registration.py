import pytest

@pytest.mark.registration
@pytest.mark.regression
def test_registration_flow(registration_page):
    registration_page.open()

    registration_page.title.check_visible()
    registration_page.form.register("user@example.com", "tester", "12345")
    print("✅ Тест регистрации завершен успешно")