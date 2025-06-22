import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from selenium.webdriver.support import expected_conditions as EC

@allure.step("Инициализация страницы Личного Кабинета")
class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators()
        self.login_locators = LoginLocators()

    @allure.step("Переход в личный кабинет")
    def click_header_account_link(self):
        self.click_element(self.locators.HEADER_ACCOUNT_LINK)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.LOGOUT_BUTTON))

    @allure.step("Проверка отображения личного кабинета")
    def is_at_personal_account(self):
        return self.is_element_visible(self.locators.LOGOUT_BUTTON, timeout=5)

    @allure.step("Переход к истории заказов")
    def click_history_orders(self):
        self.click_element(self.locators.HISTORY_ORDERS_LINK)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(self.locators.LOGOUT_BUTTON)

    @allure.step("Проверка успешного выхода")
    def is_logged_out(self):
        return self.is_element_visible(self.login_locators.LOGIN_BUTTON, timeout=5)

    @allure.step("Возврат номера последнего заказа в истории заказов")
    def number_in_history(self):
        order_elements = self.find_elements(self.locators.ORDER_HISTORY_ITEMS)
        order_text = order_elements[0].text.strip()
        return order_text
