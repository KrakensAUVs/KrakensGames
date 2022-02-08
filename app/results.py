from toolbox import read_order_with_problem


def amount_test(product_list, order_list, consumers_list):
    stock = []
    user_amount = []
    name = []
    invalid_orders = []
    for i in range(len(order_list) - 1):
        stock.append(product_list[int(order_list[i + 1].product_id)].product_amount)
        user_amount.append(order_list[(i + 1)].order_amount)
        name.append(product_list[int(order_list[i + 1].product_id)].product_name)
        if int(user_amount[i]) > int((stock[i])):
            '''
            print(f"{i + 1}) deu ruim1 UA:{user_amount[i]} S:{stock[i]} N:{name[i]}"
                  f" P:{int(user_amount[i]) * float(product_list[int(order_list[i + 1].product_id)].product_price)}"
                  f" W:{float(consumers_list[int(order_list[i + 1].consumer_id)].consumer_wallet)}")
            '''

            invalid_orders.append(read_order_with_problem(order_list[i + 1].order_id,
                                                          product_list[int(order_list[i + 1].product_id)].product_id,
                                                          stock[i], name[i], str(
                    consumers_list[int(order_list[i + 1].consumer_id)].consumer_name)))
        else:
            if int(user_amount[i]) * float(product_list[int(order_list[i + 1].product_id)].product_price) > float(
                    consumers_list[int(order_list[i + 1].consumer_id)].consumer_wallet):
                '''
                print(f"{i + 1}) deu ruim2 UA:{user_amount[i]} S:{stock[i]} N:{name[i]}"
                      f" P:{int(user_amount[i]) * float(product_list[int(order_list[i + 1].product_id)].product_price)}"
                      f" W:{float(consumers_list[int(order_list[i + 1].consumer_id)].consumer_wallet)}")
                '''

                invalid_orders.append(read_order_with_problem(order_list[i + 1].order_id, product_list[int(order_list[i + 1].product_id)].product_id, stock[i], name[i], str(consumers_list[int(order_list[i + 1].consumer_id)].consumer_name)))
            else:
                '''
                print(f"{i + 1}) deu bom UA:{user_amount[i]} S:{stock[i]} N:{name[i]}"
                      f" P:{int(user_amount[i]) * float(product_list[int(order_list[i + 1].product_id)].product_price)}"
                      f" W:{float(consumers_list[int(order_list[i + 1].consumer_id)].consumer_wallet)}")
                '''
                product_list[int(order_list[i + 1].product_id)].subtract_amount(user_amount[i])
                consumers_list[int(order_list[i + 1].consumer_id)].subtract_wallet(int(user_amount[i]) * float(product_list[int(order_list[i + 1].product_id)].product_price))
    return invalid_orders
