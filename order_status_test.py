import data 
import sender_stand_request

# делаем автотест для проверки кода от сервера
def test_order_status():
    response = sender_stand_request.post_new_order(data.order_body)
    track_number = response.json()["track"]
    order_response = sender_stand_request.get_order_id(track_number)
    assert order_response.status_code == 200, "Что-то не так"