import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.base_locators import BaseLocators

@allure.step("Инициализация страницы ленты заказов")
class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()
        self.base_locators = BaseLocators()

    @allure.step("Переход на ленту заказов")
    def click_order_feed(self):
        self.is_element_visible(self.base_locators.ORDER_FEED_BUTTON_HEADER)
        self.click_element(self.base_locators.ORDER_FEED_BUTTON_HEADER)

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_total_orders_counter(self):
        counter_element = self.wait_for_element_to_be_visible(self.locators.TOTAL_ORDERS_COUNTER)
        return int(counter_element.text.strip())

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        counter_element = self.wait_for_element_to_be_visible(self.locators.TODAY_ORDERS_COUNTER)
        return int(counter_element.text.strip())

    @allure.step("Проверка видимости модального окна с деталями заказа")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_DETAILS_MODAL)

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.find_elements(self.locators.ORDER_CARD, 10)[0].click()

    @allure.step("Проверка наличия заказа #{order_number} на ленте заказов")
    def is_order_in_feed(self, order_number):
        order_elements = self.find_elements(self.locators.ORDER_ITEMS)
        for element in order_elements:
            full_number = element.text.strip().replace("#", "")
            if full_number.endswith(order_number) or full_number == order_number:
                return True
        assert False, f"Заказ {order_number} не найден на ленте заказов"

    @allure.step("Проверка наличия заказа #{order_number} в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        order_elements = self.find_elements(self.locators.ORDER_IN_PROGRESS_ITEMS, 10)
        for element in order_elements:
            full_number = element.text.strip().replace("#", "")
            if full_number.endswith(order_number) or full_number == order_number:
                return True

        assert False, f"Заказ {order_number} не найден в разделе 'В работе'"

    @allure.step("Ожидание появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda _: self.is_order_in_progress(order_number),
            f"Заказ {order_number} не найден в разделе 'В работе' за {timeout} секунд" )