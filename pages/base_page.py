import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие URL {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Поиск элементов")
    def find_elements(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        try:
            element = self.wait_for_element_to_be_clickable(locator)
            self.scroll_into_view(element)
            element.click()
        except ElementClickInterceptedException:
            with allure.step("Обнаружено оверлей модального окна, пытаемся обойти его"):
                self.force_click(locator)

    @allure.step("Принудительный клик через JS")
    def force_click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Ждем {timeout} секунд до того как элемент {locator} станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
        f"Элемент {locator} не стал видимым за {timeout} секунд")

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_be_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
            f"Элемент {locator} не исчез за {timeout} секунд")

    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Скролл страницы к {element}")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Возвращаем текущую страницу")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, source, target):
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dragStartEvent = new MouseEvent('dragstart', { bubbles: true });
            source.dispatchEvent(dragStartEvent);
            const dragOverEvent = new MouseEvent('dragover', { bubbles: true, cancelable: true });
            target.dispatchEvent(dragOverEvent);
            const dropEvent = new MouseEvent('drop', { bubbles: true });
            target.dispatchEvent(dropEvent);
            const dragEndEvent = new MouseEvent('dragend', { bubbles: true });
            source.dispatchEvent(dragEndEvent);
        """, source, target)
