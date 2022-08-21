import json

import requests as requests
BASE_URL = 'http://localhost:8000/api/v1'


# создание продукта
def post_product():
    payload = {
        "title": "Помидор 4",
        "description": "Лучшие помидоры на рынке"
    }
    response = requests.post(BASE_URL+'/products/',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    print(response.json())


# получение продуктов
def get_product():
    response = requests.get(BASE_URL + '/products/',
                            headers={'Content-Type': 'application/json'})
    print(response.json())


# обновление продукта
def patch_product():
    payload = {'description': 'Самые сочные и ароматные помидорки'}
    response = requests.patch(BASE_URL+'/products/1/',
                              headers={'Content-Type': 'application/json'},
                              json=payload)
    print(response.json())


# удаление продукта
def delete_product():
    response = requests.delete(BASE_URL+'/products/1/',
                               headers={'Content-Type': 'application/json'})
    print(response.json())


# поиск продуктов по названию и описанию
def get_search_products():
    response = requests.get(BASE_URL + '/products/?search=помидор',
                            headers={'Content-Type': 'application/json'})
    print(response.json())


# создание склада
def post_stock():
    payload = {
        "address": "мой адрес не дом и не улица, мой адрес сегодня такой: www.ленинград-спб.ru3",
        "positions": [
            {
                "product": 2,
                "quantity": 250,
                "price": 120.50
            },
            {
                "product": 3,
                "quantity": 100,
                "price": 180
            }
        ]
    }
    response = requests.post(BASE_URL+'/stocks/',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    print(response.json())

if __name__ == '__main__':
    post_stock()