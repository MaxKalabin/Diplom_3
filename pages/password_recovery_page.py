import allure
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

@allure.step("Инициализация страницы Восстановления пароля")
class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryLocators()

    @allure.step("Переход на страницу входа")
    def click_login_button_on_main(self):
        self.click_element(self.locators.LOGIN_BUTTON_MAIN)

    @allure.step("Переход на страницу восстановления пароля")
    def click_recovery_button_on_login_page(self):
        self.click_element(self.locators.RECOVERY_BUTTON_LOGIN_PAGE)

    @allure.step("Проверка отображения страницы восстановления пароля")
    def is_at_password_recovery_page(self):
        return self.is_element_visible(self.locators.RECOVERY_HEADER)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.enter_text(self.locators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recovery_submit_button(self):
        self.click_element(self.locators.RECOVERY_SUBMIT_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        return self.is_element_visible(self.locators.ACTIVE_PASSWORD_FIELD)