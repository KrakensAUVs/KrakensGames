from count_products import product_list
from orders import order_list
from consumers import client_list
from toolbox import OrdersErrors, Consumer, generate_csv, Products

vector_number = 0
number_id = 1
order_error_list = [OrdersErrors]
consumers_list = [Consumer]
products = [Products]  # product list
consumer_vector = 0

while number_id != len(order_list):

    order_amount = order_list[number_id].get('amount')
    order_id = order_list[number_id].get('id')

    consumer_id = order_list[number_id].get('consumer_id')
    consumer_name = client_list[int(order_list[number_id].get('consumer_id'))].get('name')
    consumer_wallet = client_list[int(order_list[number_id].get('consumer_id'))].get('wallet')

    product_price = product_list[int(order_list[1].get('product_id'))].get('price')
    product_id = order_list[number_id].get('product_id')
    product_name = product_list[int(order_list[number_id].get('product_id'))].get('name')
    product_amount = product_list[int(order_list[1].get('product_id'))].get('amount')

    if order_amount > product_amount:
        if number_id == 1:
            order_error_list[vector_number] = OrdersErrors(consumer_id, consumer_name)
        if consumer_name == order_error_list[vector_number].user_name:
            order_error_list[vector_number].add_error(order_id, product_id, product_name)
        else:
            order_error_list.append(OrdersErrors(consumer_id, consumer_name))
            vector_number += 1
            order_error_list[vector_number].add_error(order_id, product_id, product_name)
    else:
        if float(consumer_wallet) < (float(product_price) * int(order_amount)):
            if number_id == 1:
                order_error_list[0] = OrdersErrors(consumer_id, consumer_name)
                order_error_list[0].add_error(order_id, product_id, product_name)
            if consumer_name == order_error_list[vector_number].user_name:
                order_error_list[vector_number].add_error(order_id, product_id, product_name)
            else:
                order_error_list.append(OrdersErrors(consumer_id, consumer_name))
                vector_number += 1
                order_error_list[vector_number].add_error(order_id, product_id, product_name)
        else:
            if consumer_vector == 0:
                consumers_list[consumer_vector] = Consumer(consumer_id, consumer_name, consumer_wallet)
                products[consumer_vector] = Products(product_id, product_name, product_amount, product_price)
            else:
                consumers_list.append(Consumer(consumer_id, consumer_name, consumer_wallet))
                products.append(Products(product_id, product_name, product_amount, product_price))
            consumers_list[consumer_vector].subtract((float(product_price) * int(order_amount)))
            products[consumer_vector].subtract(int(order_amount))
            consumer_vector += 1
    number_id += 1
generate_csv(order_error_list)
