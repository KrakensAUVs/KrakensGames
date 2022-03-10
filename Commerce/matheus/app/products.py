class Products:
    def __init__(self, product_id, product_name, serial_number, product_amount, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.serial_number = serial_number
        self.product_amount = product_amount
        self.product_price = product_price

    def subtract_amount(self, quantity):
        if float(quantity) <= float(self.product_amount):
            self.product_amount = float(self.product_amount) - float(quantity)
            return True
        else:
            return False
