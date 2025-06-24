import allure
import pytest
from selenium import webdriver

from helpers import delete_user, generate_email, generate_password, generate_name, create_user
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage
from test_data import ACCESS_TOKEN, MAIN_PAGE_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1400,900')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

@allure.step("Создание и удаление пользователя")
@pytest.fixture()
def user_fixture():
    user_data = {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }

    response = create_user(user_data)
    access_token = response.json()[ACCESS_TOKEN]

    yield {
        "user_data": user_data,
        "token": access_token
    }

    with allure.step("Удаление пользователя после теста"):
        delete_user(access_token)

@allure.step("Логинимся в пользователя")
@pytest.fixture
def login_fixture(login_page, password_recovery_page, user_fixture):
    with allure.step("Открытие главной страницы"):
        login_page.open(MAIN_PAGE_URL)

    with allure.step("Переход на страницу логина"):
        password_recovery_page.click_login_button_on_main()

    with allure.step("Авторизация пользователя"):
        login_page.login(user_fixture['user_data']['email'], user_fixture['user_data']['password'])

    return user_fixture

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)

@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)

@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)