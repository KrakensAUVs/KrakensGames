import csv

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
    consumers_csv_list = CSVMethod.openCSV(file_name)
    return CSVMethod.initOrders(consumers_csv_list)

def superInitProducts(file_name):
    consumers_csv_list = CSVMethod.openCSV(file_name)
    return CSVMethod.initProducts(consumers_csv_list)

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
