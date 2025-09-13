# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные тела запроса заказа
order_body = {
    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+34916123451",
    "rentTime": 5,
    "deliveryDate": "2025-09-09",
    "comment": "Привет, Абдурахмангаджи!"
}