import allure
from helpers import generate_email
from test_data import MAIN_PAGE_URL, RECOVERY_PAGE_URL

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_password_recovery_via_restore_button(self, password_recovery_page):
        with allure.step("Открытие главной страницы"):
            password_recovery_page.open(MAIN_PAGE_URL)

        with allure.step("Переход на страницу логин"):
            password_recovery_page.click_login_button_on_main()

        with allure.step("Переход на страницу восстановления пароля"):
            password_recovery_page.click_recovery_button_on_login_page()

        with allure.step("Проверка URL страницы восстановления пароля"):
            assert password_recovery_page.current_url() == RECOVERY_PAGE_URL

        with allure.step("Проверка наличия заголовка 'Восстановление пароля'"):
            assert password_recovery_page.is_at_password_recovery_page()

    @allure.title("Ввод email и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_recovery(self, password_recovery_page):
        with allure.step("Открытие страницы восстановления пароля"):
            password_recovery_page.open(RECOVERY_PAGE_URL)

        with allure.step("Ввод email"):
            password_recovery_page.enter_email(generate_email())

        with allure.step("Клик по кнопке 'Восстановить'"):
            password_recovery_page.click_recovery_submit_button()

        with allure.step("Проверка наличия поля ввода пароля"):
            assert password_recovery_page.is_element_visible(password_recovery_page.locators.PASSWORD_FIELD)

    @allure.title("Клик по кнопке показать/скрыть пароль активирует поле")
    def test_show_password_activates_field(self, password_recovery_page):
        with allure.step("Открытие страницы восстановления пароля"):
            password_recovery_page.open(RECOVERY_PAGE_URL)

        with allure.step("Ввод email"):
            password_recovery_page.enter_email(generate_email())

        with allure.step("Клик по кнопке 'Восстановить'"):
            password_recovery_page.click_recovery_submit_button()

        with allure.step("Клик по кнопке показать/скрыть пароль"):
            password_recovery_page.click_show_password_button()

        with allure.step("Проверка активности поля пароля"):
            assert password_recovery_page.is_password_field_active()