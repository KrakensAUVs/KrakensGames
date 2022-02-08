from toolbox import load_csv, generate_csv
from results import amount_test

products_list = load_csv('products')
orders_list = load_csv('orders')
consumers_list = load_csv('consumers')

invalids_orders = amount_test(products_list, orders_list, consumers_list)

generate_csv(invalids_orders)
