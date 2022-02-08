from toolbox import read_new_line, create_order_list

with open('orders.csv', "r", encoding='utf-8') as data:
    labels = read_new_line(data)
    line = read_new_line(data)
    order_list = create_order_list(labels, line, data)
