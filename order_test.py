# Ирина Симонова, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request as sender


def test_create_order_get_order_by_track():
     response = sender.post_new_order(data.order_body)
     track = response.json()["track"]
     order = sender.get_order_by_track(track)
     assert order.status_code == 200
     