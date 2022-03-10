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
    print('CSV created!')


def print_data(consumers_list):
    invalids_orders = []
    for i in range(1, len(consumers_list) - 1):
        if consumers_list[i].error_number() > 0:
            invalid = {
                'consumer_id': consumers_list[i].consumer_id,
                'consumer_name': consumers_list[i].consumer_name,
                'errors_number': consumers_list[i].error_number(),
                #  'errors': consumers_list[i].get_errors()
            }
            invalids_orders.append(invalid)
    generate_csv(invalids_orders)
