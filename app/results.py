from toolbox import read_order_with_problem

#  needs be improved (maybe using Wrong Orders) but it apparently works

def amount_test(product_list, order_list, consumers_list):
    stock = []
    user_amount = []
    name = []
    invalid_orders = []
    for i in range(1, len(order_list) - 1):
        stock.append(product_list[int(order_list[i].product_id)].product_amount) #  Maybe with constants it will removed
        user_amount.append(order_list[(i)].order_amount)                         #  Maybe with constants it will removed
        name.append(product_list[int(order_list[i].product_id)].product_name)    #  Maybe with constants it will removed
        if int(user_amount[i]) > int((stock[i])):
            invalid_orders.append(read_order_with_problem(order_list[i].order_id,
                                                          product_list[int(order_list[i + 1].product_id)].product_id,
                                                          stock[i], name[i], str(
                    consumers_list[int(order_list[i].consumer_id)].consumer_name)))
        else:
            if int(user_amount[i]) * float(product_list[int(order_list[i].product_id)].product_price) > float(
                    consumers_list[int(order_list[i].consumer_id)].consumer_wallet):
                invalid_orders.append(read_order_with_problem(order_list[i].order_id, product_list[int(order_list[i].product_id)].product_id, stock[i], name[i], str(consumers_list[int(order_list[i].consumer_id)].consumer_name)))
            else:
                product_list[int(order_list[i].product_id)].subtract_amount(user_amount[i])
                consumers_list[int(order_list[i].consumer_id)].subtract_wallet(int(user_amount[i]) * float(product_list[int(order_list[i].product_id)].product_price))
    return invalid_orders
