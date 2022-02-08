class Consumers:
    def __init__(self, consumer_id, consumer_name, consumer_age, consumer_cep, consumer_wallet):
        self.consumer_id = consumer_id
        self.consumer_name = consumer_name
        self.consumer_age = consumer_age
        self.consumer_CEP = consumer_cep
        self.consumer_wallet = consumer_wallet

    def subtract_wallet(self, quantity):
        self.consumer_wallet = float(self.consumer_wallet) - float(quantity)
