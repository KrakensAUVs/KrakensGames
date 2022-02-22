# classe dos consumidores
class Consumer:
    def __init__(self, consumer_id, name, age, cep, wallet):
        self.__consumer_id = consumer_id
        self.__name = name
        self.__age = age
        self.__cep = cep
        self.__wallet = wallet

    @property
    def consumer_id(self):
        return self.__consumer_id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def cep(self):
        return self.__cep

    @property
    def wallet(self):
        return self.__wallet 

# classe dos produtos
class Product:
    def __init__(self, product_id, name, serial_number, amount, price):
        self.__product_id = product_id
        self.__name = name
        self.__serial_number = serial_number
        self.__amount = amount
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price

# classe dos pedidos
class Order:
    def __init__(self, order_id, consumer_id, product_id, amount):
        self.__order_id = order_id
        self.__consumer_id = consumer_id
        self.__product_id = product_id
        self.__amount = amount

    @property
    def order_id(self):
        return self.__order_id

    @property
    def consumer_id(self):
        return self.__consumer_id

    @property
    def product_id(self):
        return self.__product_id

    @property
    def amount(self):
        return self.__amount