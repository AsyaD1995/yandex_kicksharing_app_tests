import data 
import sender_stand_request

# делаем автотест для проверки кода от сервера
def test_order_status():
    order_response = sender_stand_request.get_order_id()
    assert order_response.status_code == 200, "Что-то не так"