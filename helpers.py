import allure
import random
import string
import requests

from test_data import API_URL, USER_ENDPOINT, LOGOUT_ENDPOINT, CREATE_USER_ENDPOINT, ORDERS_ENDPOINT


@allure.step("Генерация случайного email")
def generate_email():
    return f"max_kalabin_19_{random.randint(1000, 9999)}@yandex.ru"

@allure.step("Генерация случайного пароля")
def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

@allure.step("Генерация случайного имени")
def generate_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

@allure.step("Создание пользователя через API")
def create_user(payload):
    url = f"{API_URL}{CREATE_USER_ENDPOINT}"
    response = requests.post(url, json=payload)
    return response

@allure.step("Выход пользователя")
def logout_user(token):
    headers = {"Authorization": token}
    return requests.post(f"{API_URL}{USER_ENDPOINT}{LOGOUT_ENDPOINT}", headers=headers)

@allure.step("Удаление пользователя через API")
def delete_user(token):
    headers = {"Authorization": token}
    response = requests.delete(f"{API_URL}{USER_ENDPOINT}", headers=headers)
    return response

@allure.step("Создание заказа через API")
def create_order(ingredients, token=None):
    url = f"{API_URL}{ORDERS_ENDPOINT}"
    headers = {"Authorization": token} if token else {}
    response = requests.post(url, json={"ingredients": ingredients}, headers=headers)
    return response