from selenium.webdriver.common.by import By

class BaseLocators:
    ORDER_FEED_BUTTON_HEADER = (By.XPATH, "//a[@href='/feed']")
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, "//a[.//p[text()='Конструктор']]")