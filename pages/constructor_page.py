import allure
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By

@allure.step("Инициализация страницы Конструктора (Главной)")
class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()
        self.base_locators = BaseLocators()

    @allure.step("Переход в Конструктор через кнопку в хедере")
    def click_to_constructor(self):
        self.click_element(self.base_locators.CONSTRUCTOR_BUTTON_HEADER)

    @allure.step("Получение списка ингредиентов")
    def get_ingredient_items(self, timeout=15):
        return self.find_elements(self.locators.INGREDIENT_ITEMS, timeout)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self, index=0):
        ingredients = self.get_ingredient_items()
        self.scroll_into_view(ingredients[index])
        self.click_element((By.XPATH, f"//a[starts-with(@href, '/ingredient/')][{index + 1}]"))

    @allure.step("Получение кол-ва ингредиента")
    def get_ingredient_counter(self, index=0):
        self.wait_for_element_to_be_visible(self.locators.INGREDIENT_COUNTER)
        return int(self.find_elements(self.locators.INGREDIENT_COUNTER)[index].text)

    @allure.step("Ожидание увеличения каунтера ингредиента")
    def wait_for_ingredient_counter_increase(self, index=0, initial_count=0, timeout=10):
        self.wait_for_condition((lambda _: self.get_ingredient_counter(index) > initial_count),timeout)
        return True

    @allure.step("Проверяем видно модальное окно с деталями заказа")
    def is_ingredient_details_visible(self):
        return self.is_element_visible(self.locators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Закрытие модального окна по кнопке")
    def close_ingredient_details(self):
        self.click_element(self.locators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step("Добавление ингредиента")
    def add_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEMS)
        ingredient = ingredients[index]

        self.scroll_into_view(ingredient)
        order_area = self.find_element(self.locators.ORDER_AREA)

        self.drag_and_drop(ingredient, order_area)

    @allure.step("Создание заказа")
    def create_order(self):
        self.click_element(self.locators.CREATE_ORDER_BUTTON)
        self.wait_for_order_modal_to_appear()
        self.wait_for_modal_loading()
        order_text = self.find_element(self.locators.ORDER_NUMBER).text
        with allure.step("Закрытие модального окна создания заказа"):
            self.click_element(self.locators.ORDER_MODAL_CLOSE_BUTTON)
        return order_text

    @allure.step("Ожидание появления модального окна с заказом")
    def wait_for_order_modal_to_appear(self, timeout=10):
        self.wait_for_element_to_be_visible(self.locators.ORDER_MODAL, timeout)

    @allure.step("Ожидание завершения загрузки модального окна создания заказа")
    def wait_for_modal_loading(self, timeout=10):
        self.wait_for_element_to_be_invisible(self.locators.ORDER_MODAL_LOADING, timeout)

