import allure
from test_data import ORDER_FEED_URL

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие модального окна с деталями заказа")
    def test_open_order_details_modal(self, order_feed_page, login_fixture):
        with allure.step("Открытие ленты заказов"):
            order_feed_page.open(ORDER_FEED_URL)
        with allure.step("Клик по первому заказу"):
            order_feed_page.click_first_order()
        with allure.step("Проверка отображения модального окна с деталями"):
            assert order_feed_page.is_order_details_modal_visible()

    @allure.title("Заказ отображается в истории заказов юзера")
    def test_user_order_appear_in_history(self, constructor_page, order_feed_page, personal_account_page, login_fixture):
        with allure.step("Создание заказа через конструктор"):
            constructor_page.add_ingredient(0)
            order_number = constructor_page.create_order()

        with allure.step("Переход в историю заказов"):
            personal_account_page.click_header_account_link()
            personal_account_page.click_history_orders()

        with (allure.step("Проверка наличия заказа в истории")):
            history_order_number = personal_account_page.number_in_history()
            assert order_number in history_order_number, \
                f"Заказ {order_number} не найден в истории. Найдено: {history_order_number}"

    @allure.title("Заказ отображается в Ленте заказов")
    def test_user_order_appear_in_feed(self, constructor_page, order_feed_page, login_fixture):
        with allure.step("Создание заказа через конструктор"):
            constructor_page.add_ingredient(0)
            order_number = constructor_page.create_order()

        with allure.step("Переход на ленту заказов"):
            order_feed_page.click_order_feed()

        with allure.step("Проверка наличия заказа на ленте"):
            assert order_feed_page.is_order_in_feed(order_number)

    @allure.title("Отображение номера заказа в разделе 'В работе'")
    def test_order_appears_in_progress(self, constructor_page, order_feed_page, personal_account_page,
                                                     login_fixture):
        with allure.step("Создание заказа через конструктор"):
            constructor_page.add_ingredient(0)
            order_number = constructor_page.create_order()

        with allure.step("Переход на ленту заказов"):
            order_feed_page.click_order_feed()
            order_feed_page.wait_for_order_in_progress(order_number)

        with allure.step("Проверка наличия заказа на ленте"):
            assert order_feed_page.is_order_in_progress(order_number)

    @allure.title("Увеличение общего счетчика заказов")
    def test_total_orders_counter_increases(self, constructor_page, order_feed_page, login_fixture):
        with allure.step("Получение начального значения общего счетчика"):
            order_feed_page.click_order_feed()
            initial_total = order_feed_page.get_total_orders_counter()

        with allure.step("Создание заказа через конструктор"):
            constructor_page.click_to_constructor()
            constructor_page.add_ingredient(0)
            constructor_page.create_order()

        with allure.step("Переход на ленту заказов"):
            order_feed_page.click_order_feed()

        with allure.step("Проверка увеличения общего счетчика"):
            assert order_feed_page.get_total_orders_counter() == initial_total + 1

    @allure.title("Увеличение дневного счетчика заказов")
    def test_today_orders_counter_increases(self, constructor_page, order_feed_page, login_fixture):
        with allure.step("Получение начального значения общего счетчика"):
            order_feed_page.click_order_feed()
            initial_today = order_feed_page.get_today_orders_counter()

        with allure.step("Создание заказа через конструктор"):
            constructor_page.click_to_constructor()
            constructor_page.add_ingredient(0)
            constructor_page.create_order()

        with allure.step("Переход на ленту заказов"):
            order_feed_page.click_order_feed()

        with allure.step("Проверка увеличения общего счетчика"):
            assert order_feed_page.get_today_orders_counter() == initial_today + 1