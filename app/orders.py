class Orders:
    def __init__(self, order_id, consumer_id, product_id, order_amount):
        self.order_id = order_id
        self.consumer_id = consumer_id
        self.product_id = product_id
        self.order_amount = order_amount


class WrongOrders:
    def __init__(self, order_id, consumer_id, consumer_name, product_id, product_name):
        self.order_id = order_id
        self.consumer_id = consumer_id
        self.consumer_id = consumer_name
        self.product_id = product_id
        self.product_id = product_name

    def add_new_error(self):
        pass

    def append_error_user(self):
        pass
