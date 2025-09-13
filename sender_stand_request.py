# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения к северу
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests 

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_ORDER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# получаем заказ и возвращзаем в функцию его номер
def get_order_id(track_number):
    # получаем заказ
    track_id = post_new_order(data.order_body)
    # деалаем из json заказа строку с остатком адреса для get
    track_url = '?'+'t='+str(track_id.json()["track"])
    # вызываем get для провеки статусазаказа
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track_url, headers=data.headers)
    return response