class Consumers:
    def __init__(self, consumer_id, consumer_name, consumer_age, consumer_cep, consumer_wallet):
        self.orders_errors = 0
        self.consumer_id = consumer_id
        self.consumer_name = consumer_name
        self.consumer_age = consumer_age
        self.consumer_CEP = consumer_cep
        self.consumer_wallet = consumer_wallet
        self.bad_orders = []

    def subtract_wallet(self, quantity):
        if float(quantity) <= float(self.consumer_wallet):
            self.consumer_wallet = float(self.consumer_wallet) - float(quantity)
            return True
        else:
            return False

    def add_order_error(self, order_id, product_id, product_name):
        bad_orders = {
            'Order_id': order_id,
            'Product_id': product_id,
            'Product_name': product_name
        }
        self.bad_orders.append(bad_orders)

    def error_number(self):
        return len(self.bad_orders)

    def get_errors(self):
        return self.bad_orders
