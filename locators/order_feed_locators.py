from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, "[class^='OrderFeed_list']")
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "[class^='Modal_orderBox']")
    ORDER_ITEMS = (By.CSS_SELECTOR, ".OrderHistory_textBox__3lgbs .text_type_digits-default")
    ORDER_IN_PROGRESS_ITEMS = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li.text_type_digits-default")

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")


