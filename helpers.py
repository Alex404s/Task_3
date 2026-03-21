import random
import string
import allure
import requests
from .data import URL


@allure.step('Генератор рандомной строки')
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


@allure.step('Генератор рандомного email @yandex.ru')
def generate_random_email(length):
        random_email = f"{generate_random_string(length)}@{"yandex.ru"}"        
        return random_email


@allure.step('Удаление пользователя')
def delete_user(accessToken):
        response_del = requests.delete(f"{URL.url_stellarburgers}{URL.api_user}", headers={'Authorization': accessToken})
        return response_del


@allure.step('Создание пользователя и возврат данных авторизации')
def new_user():
    login_pass = []
    email = generate_random_email(10)
    password = generate_random_string(10)
    name = generate_random_string(10)        
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(f"{URL.url_stellarburgers}{URL.api_register}", data=payload)
    if response.status_code == 200:
        login_pass.append(response.json())
        login_pass.append(password)
    return login_pass    


@allure.step('Создание заказа')
def create_order(accessToken):        
        ingredient_id = get_ingredient_id(1)
        payload = {
            "ingredients": ingredient_id
        }
        requests.post(f"{URL.url_stellarburgers}{URL.api_orders}",
                                 headers={'Authorization': accessToken},
                                 data=payload)
        

@allure.step('Получение id ингредиента')
def get_ingredient_id(ingredient_number):
        response_ingredients = requests.get(f"{URL.url_stellarburgers}{URL.api_ingredients}")
        response_ingredients_text = response_ingredients.json()
        ingredient_id = response_ingredients_text["data"][ingredient_number]["_id"]
        return ingredient_id