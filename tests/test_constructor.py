import allure
from test_data import MAIN_PAGE_URL, ORDER_FEED_URL

@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Переход к конструктору из ленты заказов")
    def test_go_to_constructor_from_order_feed(self, constructor_page, order_feed_page):
        with allure.step("Переход к ленте заказов"):
            order_feed_page.open(ORDER_FEED_URL)

        with allure.step("Переход к конструктору (главной)"):
            constructor_page.click_to_constructor()

        with allure.step("Проверка URL конструктора"):
            assert constructor_page.current_url() == MAIN_PAGE_URL

    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, constructor_page):
        with allure.step("Открытие конструктора (главной)"):
            constructor_page.open(MAIN_PAGE_URL)

        with allure.step("Клик по ингредиенту"):
            constructor_page.click_ingredient(0)

        with allure.step("Проверка отображения деталей ингредиента"):
            assert constructor_page.is_ingredient_details_visible()

    @allure.title("Закрытие деталей ингредиента")
    def test_close_ingredient_details(self, constructor_page):
        with allure.step("Открытие конструктора (главной)"):
            constructor_page.open(MAIN_PAGE_URL)

        with allure.step("Клик по ингредиенту"):
            constructor_page.click_ingredient(0)

        with allure.step("Закрытие деталей ингредиента"):
            constructor_page.close_ingredient_details()

        with allure.step("Проверка скрытия деталей ингредиента"):
            assert not constructor_page.is_ingredient_details_visible()

    @allure.title("Каунтер ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases_after_adding(self, constructor_page):
        with allure.step("Открытие конструктора"):
            constructor_page.open(MAIN_PAGE_URL)

        with allure.step("Получение начального кол-ва"):
            initial_count = constructor_page.get_ingredient_counter(0)

        with allure.step("Добавление ингредиента в заказ"):
            constructor_page.add_ingredient(0)

        with allure.step("Ожидание увеличения каунтера"):
            constructor_page.wait_for_ingredient_counter_increase(0, initial_count)

        with allure.step("Проверка увеличения каунтера"):
            assert constructor_page.get_ingredient_counter(0) == initial_count + 2

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_create_order(self, constructor_page, login_fixture):
        with allure.step("Добавление ингредиента в заказ"):
            constructor_page.add_ingredient(0)
        with allure.step("Оформление заказа"):
            order_number = constructor_page.create_order()
        with allure.step("Проверка наличия номера заказа"):
            assert order_number.isdigit(), "Номер заказа не содержит только цифры"