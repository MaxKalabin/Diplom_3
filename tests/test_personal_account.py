import allure
from test_data import MAIN_PAGE_URL, PROFILE_PAGE_URL, ORDER_HISTORY_URL

@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет после авторизации открывает страницу с верным URL")
    def test_go_to_personal_account_after_login_profile_page_url(self, login_page, personal_account_page, user_fixture,
                                                password_recovery_page):
        with allure.step("Открытие главной страницы"):
            login_page.open(MAIN_PAGE_URL)

        with allure.step("Переход на страницу логин"):
            password_recovery_page.click_login_button_on_main()

        with allure.step("Авторизация пользователя"):
            login_page.login(user_fixture['user_data']['email'], user_fixture['user_data']['password'])

        with allure.step("Переход в личный кабинет"):
            personal_account_page.click_header_account_link()

        with allure.step("Проверка URL личного кабинета"):
            assert personal_account_page.current_url() == PROFILE_PAGE_URL

    @allure.title("Переход в личный кабинет после авторизации открывает страницу с кнопкой Выйти из аккаунта")
    def test_go_to_personal_account_after_login_header_personal_account(self, login_page, personal_account_page, user_fixture,
                                                password_recovery_page):
        with allure.step("Открытие главной страницы"):
            login_page.open(MAIN_PAGE_URL)

        with allure.step("Переход на страницу логин"):
            password_recovery_page.click_login_button_on_main()

        with allure.step("Авторизация пользователя"):
            login_page.login(user_fixture['user_data']['email'], user_fixture['user_data']['password'])

        with allure.step("Переход в личный кабинет"):
            personal_account_page.click_header_account_link()

        with allure.step("Проверка наличия кнопки 'Logout'"):
            assert personal_account_page.is_at_personal_account()

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, personal_account_page, user_fixture, password_recovery_page, login_page):
        with allure.step("Открытие главной страницы"):
            login_page.open(MAIN_PAGE_URL)

        with allure.step("Переход на страницу логин"):
            password_recovery_page.click_login_button_on_main()

        with allure.step("Авторизация пользователя"):
            login_page.login(user_fixture['user_data']['email'], user_fixture['user_data']['password'])

        with allure.step("Переход в личный кабинет"):
            personal_account_page.click_header_account_link()

        with allure.step("Клик по ссылке 'История заказов'"):
            personal_account_page.click_history_orders()

        with allure.step("Проверка URL истории заказов"):
            assert personal_account_page.current_url() == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта через кнопку «Выход»")
    def test_logout(self, personal_account_page, user_fixture, password_recovery_page, login_page):
        with allure.step("Открытие главной страницы"):
            login_page.open(MAIN_PAGE_URL)

        with allure.step("Переход на страницу логин"):
            password_recovery_page.click_login_button_on_main()

        with allure.step("Авторизация пользователя"):
            login_page.login(user_fixture['user_data']['email'], user_fixture['user_data']['password'])

        with allure.step("Переход в личный кабинет"):
            personal_account_page.click_header_account_link()

        with allure.step("Клик по кнопке 'Выход'"):
            personal_account_page.logout()

        with allure.step("Проверка успешности выхода"):
            assert personal_account_page.is_logged_out(), "Выход из аккаунта не выполнен"