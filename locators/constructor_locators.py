from selenium.webdriver.common.by import By

class ConstructorLocators:
    INGREDIENT_ITEMS = (By.XPATH, "//a[starts-with(@href, '/ingredient/')]")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class^='counter_counter__num'")

    INGREDIENT_DETAILS_MODAL = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4")
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class^='Modal_modal__close_modified']")

    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "[class^='Modal_modal__title_shadow'")
    ORDER_MODAL_LOADING = (By.CSS_SELECTOR, "div.Modal_modal_opened__3ISw4.Modal_modal__P3_V5")
    ORDER_AREA = (By.CSS_SELECTOR, "[class^='BurgerConstructor_basket']")
    ORDER_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class^='Modal_modal__close_modified']")
    ORDER_MODAL = (By.CSS_SELECTOR, "[class^='Modal_modal__container']")
