import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

@allure.step("Инициализация страницы Авторизации")
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.enter_text(self.locators.EMAIL_FIELD, email)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD_FIELD, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()