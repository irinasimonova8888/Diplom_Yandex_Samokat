# Ирина Симонова, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import configuration
import requests

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

#определение функции для получение заказа по треку заказа
def get_order_by_track(track):
     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track)) 


response = post_new_order(data.order_body)
track = response.json()["track"]
order = get_order_by_track(track)
if order.status_code == 200: print ("Тест пройден успешно")
else: print("Тест провален")