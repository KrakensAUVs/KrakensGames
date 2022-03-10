def amount_test(products_list, order_list, consumers_list):
    for i in range(1, len(order_list) - 1):
        order = {
            'product': int(order_list[i].product_id),
            'amount': int(order_list[i].order_amount),
            'consumer': int(order_list[i].consumer_id),
            'id': int(order_list[i].order_id)
        }
        product = {
            'price': products_list[order.get('product')].product_price,
            'name': products_list[order.get('product')].product_name
        }
        if products_list[order.get('product')].subtract_amount(order.get('amount')) \
                and consumers_list[order.get('consumer')].subtract_wallet(order.get('amount') *
                                                                          float(product.get('price'))):
            pass
        else:
            consumers_list[order.get('consumer')].add_order_error(order.get('id'), order.get('product'),
                                                                  product.get('name'))
