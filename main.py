from binance.exceptions import BinanceAPIException
from Config import API_KEY, SECRET_KEY
from binance.client import Client
import random
import time


request = {
    "volume": 10000.0,  # Объем в долларах
    "number": 5,  # На сколько ордеров нужно разбить этот объем
    "amountDif": 50.0,
    # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
    "side": "SELL",  # Сторона торговли (SELL или BUY)
    "priceMin": 200.0,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
    "priceMax": 300.0  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
}


def create_orders(API_KEY, SECRET_KEY, order_data):
    client = Client(API_KEY, SECRET_KEY)

    volume = order_data["volume"]
    number = order_data["number"]
    amount_dif = order_data["amountDif"]
    side = order_data["side"]
    price_min = order_data["priceMin"]
    price_max = order_data["priceMax"]

    price_range = price_max - price_min
    volume_per_order = volume / number

    orders = []
    for i in range(number):
        order_volume = volume_per_order + random.uniform(-amount_dif, amount_dif)
        order_price = price_min + random.uniform(0, price_range)

        try:
            order = client.create_test_order(
                symbol="BTCUSDT",
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=order_volume,
                price=order_price
            )
            # Добавление созданного ордера в список
            orders.append(order)
            print(f"Ордер {i + 1} создан: {order}")
        except BinanceAPIException as e:
            print(f"Ошибка при создании ордера {i + 1}: {e}")
        time.sleep(1)

    return orders


create_orders(API_KEY, SECRET_KEY, request)
