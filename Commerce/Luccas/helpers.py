import csv
import os.path
from os import path


class CreateMap:

    def __init__(self):
        self.map = {}
        self.list_of_maps = []

    def create_product(self, product, order):
        self.map['Product Amount'] = f"{product.amount}"
        self.map['Product Price'] = f"{product.price}"
        self.map['Product Amount After'] = f"{product.amount - order.amount}" if order.foi_realizada else f"{product.amount}"

    def create_order(self, order):
        self.map['Order ID'] = f"{order.id}"
        self.map['Consumer ID'] = f"{order.consumer_id}"
        self.map['Product ID'] = f"{order.product_id}"
        self.map['Order Amount'] = f"{order.amount}"
        self.map['Foi Realizada'] = str(order.foi_realizada)

    def create_consumer(self, consumer, order, product_price):
        self.map['Consumer Wallet'] = f"{round(consumer.wallet, 2)}"
        self.map['Order Total'] = f"{round(order.amount * product_price, 2)}"
        self.map['Consumer Wallet After'] = f"{round(consumer.wallet - order.amount * product_price, 2)}" if order.foi_realizada else f"{round(consumer.wallet, 2)}"

    def append_map(self):
        self.list_of_maps.append(self.map)
        self.map = {}

    def get_list_of_maps(self):
        return self.list_of_maps

class Consumer:
    """ Classe para modelar a estrutura de dados para os consumidores.
        Os atributos 'id', 'name', 'age', 'CEP' e 'wallet' são atributos puxados do próprio arquivo CSV.
        Já os atributos 'compras_af' e 'foi_afetado' são atributos criados para controlar quantas compras desse usuário
        foram afetadas e o booleano se foi ou não afetado.
    """

    def __init__(self, id, name, age, CEP, wallet):
        self.id = id
        self.name = name
        self.age = age
        self.CEP = CEP
        self.wallet = wallet
        self.compras_af = 0
        self.foi_afetado = False

class Order:
    """ Classe para modelar a estrutura de dados para as ordens de compra.
        Os atributos 'id', 'consumer_id', 'product_id' e 'amount' são atributos puxados do próprio arquivo CSV.
        Já o atributo 'foi_realizada' foi criado para controlar se aquela ordem foi realizada ou não.
    """

    def __init__(self, id, consumer_id, product_id, amount):
        self.id = id
        self.consumer_id = consumer_id
        self.product_id = product_id
        self.amount = amount
        self.foi_realizada = False

class Product:
    """ Classe para modelar a estrutura de dados para os produtos
        Os atributos 'id', 'name', 'serial_number', 'amount' e 'price' são atributos puxados do próprio arquivo CSV.
    """

    def __init__(self, id, name, serial_number, amount, price):
        self.id = id
        self.name = name
        self.serial_number = serial_number
        self.amount = amount
        self.price = price

class CSVMethod:
    """Classe criada para modelar as funções que carregam o arquivo CSV e inicialização dos objetos.
       'openCSV' tem como parametro o nome do arquivo que se deseja abrir. O método utiliza a função 'DicReader'
       da biblioteca 'csv'. Deste modo, o arquivo CSV é carregado como uma lista de dicionários. Assim, podemos
       acessar cada um das colunas do arquivo CSV e seu respectivo valor.
    """

    def __init__(self):
        pass

    def openCSV(file_name):
        with open(file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            new_table = []
            for row in reader:
                new_table_dict = {}
                for colunm in row:
                    if any(char.isdigit() for char in row[colunm].strip()):
                        if row[colunm].strip().isdigit():
                            new_table_dict[colunm.strip()] = int(row[colunm])
                        elif isFloat(row[colunm].strip()):
                            new_table_dict[colunm.strip()] = float(row[colunm])
                        else:
                            new_table_dict[colunm.strip()] = row[colunm].strip()
                    else:
                        new_table_dict[colunm.strip()] = row[colunm].strip()
                new_table.append(new_table_dict)
            return new_table

    def initConsumers(consumers_csv_list):
        consumers_list = []
        for row in consumers_csv_list:
            consumers_list.append(Consumer(row['id'], row['name'], row['age'], row['CEP'], row['wallet']))
        return consumers_list

    def initOrders(orders_csv_list):
        orders_list = []
        for row in orders_csv_list:
            orders_list.append(Order(row['id'], row['consumer_id'], row['product_id'], row['amount']))
        return orders_list

    def initProducts(products_csv_list):
        products_list = []
        for row in products_csv_list:
            products_list.append(Product(row['id'], row['name'], row['serial_number'], row['amount'], row['price']))
        return products_list

#Funções

def isFloat(test_string):
    return test_string.replace('.', '', 1).isdigit()

def superInitConsumers(file_name):
    consumers_csv_list = CSVMethod.openCSV(file_name)
    return CSVMethod.initConsumers(consumers_csv_list)

def superInitOrders(file_name):
    orders_csv_list = CSVMethod.openCSV(file_name)
    return CSVMethod.initOrders(orders_csv_list)

def superInitProducts(file_name):
    products_csv_list = CSVMethod.openCSV(file_name)
    return CSVMethod.initProducts(products_csv_list)

def super_init(consumers_file, orders_file, products_file):
    return superInitConsumers(consumers_file), superInitOrders(orders_file), superInitProducts(products_file)


def findProduct(id_to_find, product_list):
    for row in product_list:
        if id_to_find == row.id:
            return row
            break

def findConsumer(id_to_find, consumers_list):
    for row in consumers_list:
        if id_to_find == row.id:
            return row
            break

def checkOrder(order, products_list, consumers_list):
    __consumer = findConsumer(order.consumer_id, consumers_list) #buscando o consumidor em questão
    __product = findProduct(order.product_id, products_list) #buscando o produto desejado

    if order.amount <= __product.amount:
        if order.amount * __product.price <= __consumer.wallet:
            #print(f"order id: {order.id} \n- order amount: {order.amount} \n- product amount: {__product.amount} \n- valor total: {order.amount * __product.price} \n- consumer wallet: {__consumer.wallet}")
            return True

    return False


def show_affected(consumers, orders):
    consumers_af = 0
    orders_af = 0

    for consumer in consumers:
        if consumer.foi_afetado:
            consumers_af = consumers_af + 1

    for order in orders:
        if not order.foi_realizada:
            orders_af = orders_af + 1

    print(f"Número de consumidores afetados: {consumers_af}")
    print(f"Número de ordens afetadas: {orders_af}")


def gen_csv_results_file(gen_file_name, data, fields):
    if not path.isfile(gen_file_name):
        with open(gen_file_name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields, dialect='excel')
            writer.writeheader()
            writer.writerows(data)
        print(f"<Arquivo criado em {gen_file_name}>")
    else:
        print(f"<Arquivo já existe em {gen_file_name}>")

def check_all(consumers, orders, products):
    my_map = CreateMap()
    for order in orders:
        if checkOrder(order, products, consumers):
            order.foi_realizada = True
            my_map.create_order(order)
            for product in products:
                if order.product_id == product.id:
                    __product_price = product.price
                    my_map.create_product(product, order)
                    product.amount = product.amount - order.amount
                    break
            for consumer in consumers:
                if order.consumer_id == consumer.id:
                    my_map.create_consumer(consumer, order, __product_price)
                    consumer.wallet = round(consumer.wallet - order.amount * __product_price, 2)
                    break
            my_map.append_map()
        else:
            my_map.create_order(order)
            for product in products:
                if order.product_id == product.id:
                    my_map.create_product(product, order)
                    __product_price = product.price
                    break
            for consumer in consumers:
                if order.consumer_id == consumer.id:
                    my_map.create_consumer(consumer, order, __product_price)
                    if not consumer.foi_afetado:
                        consumer.foi_afetado = True
                        consumer.compras_af = consumer.compras_af + 1
                        break
                    else:
                        consumer.compras_af = consumer.compras_af + 1
                        break
            my_map.append_map()

    return consumers, orders, products, my_map.get_list_of_maps()
