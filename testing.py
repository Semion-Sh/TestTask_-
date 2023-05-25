import unittest
from main import create_orders
from Config import API_KEY, SECRET_KEY


class TestCreateOrders(unittest.TestCase):
    def test_create_orders(self):

        order_data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        orders = create_orders(API_KEY, SECRET_KEY, order_data)

        self.assertEqual(len(orders), 5)  # Проверка количества созданных ордеров
        self.assertEqual(orders[0]['side'], 'SELL')  # Проверка стороны ордера
        # Проверка суммарного объема созданных ордеров
        total_volume = sum(float(order['executedQty']) for order in orders)
        self.assertAlmostEqual(total_volume, 10000.0, delta=0.01)

        # Проверка цен и объемов каждого ордера
        for order in orders:
            price = float(order['price'])
            self.assertGreaterEqual(price, 200.0)
            self.assertLessEqual(price, 300.0)

            volume = float(order['executedQty'])
            self.assertGreaterEqual(volume, 1950.0)
            self.assertLessEqual(volume, 2050.0)


if __name__ == '__main__':
    unittest.main()