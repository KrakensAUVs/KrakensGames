import pandas


def read_new_line(file_data):
    line = file_data.readline().split(',')
    line = [i.split('\n')[0].replace(" ", "", 1) for i in line]
    return line


def create_product(labels, data):
    product = {
        labels[1]: data[1],
        labels[2]: data[2],
        labels[3]: data[3],
        labels[4]: data[4]
    }
    return product


def create_product_list(labels, line, data):
    product_list = [labels]

    while len(line) != 1:
        if len(line) != 1:
            product = create_product(labels, line)
            product_list.append(product)
        line = read_new_line(data)
    return product_list


def read_order(labels, data):
    order = {
        labels[0]: data[0],
        labels[1]: data[1],
        labels[2]: data[2],
        labels[3]: data[3]
    }
    return order


def create_order_list(labels, line, data):
    order_list = [labels]

    while len(line) != 1:
        if len(line) != 1:
            order = read_order(labels, line)
            order_list.append(order)
        line = read_new_line(data)
    return order_list


def read_client(labels, data):
    client = {
        labels[1]: data[1],
        labels[2]: data[2],
        labels[3]: data[3],
        labels[4]: data[4],
    }
    return client


def create_client_list(labels, line, data):
    client_list = [labels]

    while len(line) != 1:
        if len(line) != 1:
            order = read_client(labels, line)
            client_list.append(order)
        line = read_new_line(data)
    return client_list


def generate_csv(order_error_list):
    df = []
    for i in range(len(order_error_list)):
        df.append([order_error_list[i].user_id, order_error_list[i].user_name, order_error_list[i].order_id,
                   len(order_error_list[i].order_id), order_error_list[i].product_id, order_error_list[i].product_name])
    df = pandas.DataFrame(df)
    print({"Total_errors": len(order_error_list) - 1})
    df.to_csv("./errors.csv", sep=',', index=True,
              index_label=['row', 'user_id', 'user_name', 'orders_id', 'invalid_orders', 'products_id',
                           'products_names'])
    print(df)


class OrdersErrors:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.order_id = []
        self.product_id = []
        self.product_name = []

    def add_error(self, order_id, product_id, product_name):
        self.order_id.append(order_id)
        self.product_id.append(product_id)
        self.product_name.append(product_name)


class Consumer:
    def __init__(self, user_id, user_name, wallet):
        self.user_id = user_id
        self.user_name = user_name
        self.wallet = wallet

    def subtract(self, quantity):
        self.wallet = float(self.wallet) - float(quantity)


class Products:
    def __init__(self, product_id, product_name, product_amount, product_price):
        self.product_amount = product_amount
        self.product_name = product_name
        self.product_id = product_id
        self.product_price = product_price

    def subtract(self, quantity):
        self.product_amount = float(self.product_amount) - float(quantity)
