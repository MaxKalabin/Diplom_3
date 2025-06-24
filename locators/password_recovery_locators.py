from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    RECOVERY_BUTTON_LOGIN_PAGE = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    RECOVERY_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RECOVERY_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active')]//input[@name='Введите новый пароль']")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")