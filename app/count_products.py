from toolbox import read_new_line, create_product_list

with open('products.csv', "r", encoding='utf-8') as data:
    labels = read_new_line(data)
    line = read_new_line(data)

    product_list = create_product_list(labels, line, data)
