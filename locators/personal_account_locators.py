from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    HISTORY_ORDERS_LINK = (By.XPATH, "//a[@href='/account/order-history' and contains(., 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    ORDER_HISTORY_ITEMS = (By.CSS_SELECTOR, ".OrderHistory_profileList__374GU")

    HEADER_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
