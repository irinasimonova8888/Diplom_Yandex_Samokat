import configuration
import data
import requests

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

#определение функции для получение заказа по треку заказа
def get_order_by_track(track):
     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track)) 
