import pandas as pd
from products import Products
from orders import Orders
from consumers import Consumers


def clean_data(data):
    data = data.strip('\n')
    data = data.split(', ')

    return data


def load_csv(csv_name):
    data_list = []
    file_data = open(f'{csv_name}.csv', 'r', encoding='utf-8')
    for csv_product_line in file_data:
        class_selection = {
            'products': Products,
            'orders': Orders,
            'consumers': Consumers
        }
        data_list.append(class_selection.get(f'{csv_name}')(*clean_data(csv_product_line)))

    return data_list


def generate_csv(order_error_list):
    df = pd.DataFrame.from_dict(order_error_list)
    df.to_csv(r'errors.csv', index=False, header=True)
    print(df)

#  I wish that this function be replaced with class
def read_order_with_problem(order_id, product_id, product_amount, product_name, consumer_name):
    order = {
        'order_id': order_id,
        'product_id': product_id,
        'product_amount': product_amount,
        'product_name': product_name,
        'consumer_name': consumer_name
    }
    return order
