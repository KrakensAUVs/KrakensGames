from toolbox import load_csv, print_data
from results import amount_test

products_list = load_csv('products')
orders_list = load_csv('orders')
consumers_list = load_csv('consumers')

amount_test(products_list, orders_list, consumers_list)

print_data(consumers_list)
