from classes import Order, Consumer, Product

def load_csv(csv_name):
    data_list = []
    file_data = open(f'{csv_name}.csv', 'r', encoding='utf-8')
    for csv_product_line in file_data:
        class_selection = {
            'products': Product,
            'orders': Order,
            'consumers': Consumer
        }
        data_list.append(class_selection.get(f'{csv_name}')(*csv_product_line.strip("\n").split(", ")))
    return data_list

product_list = load_csv("products")
order_list = load_csv("orders")
consumer_list = load_csv("consumers")

stock = []
user_amount = []
name = []
wallet = []
price = []
price_order = []
username = []

for i in range(len(order_list) - 1):
    stock.append(product_list[int(order_list[i + 1].product_id)].amount)            # a quantidade de produtos em estoque, ordenado pelo product_id no orders
    user_amount.append(int(order_list[(i + 1)].amount))                             # a quantidade de pedidos
    name.append(product_list[int(order_list[i + 1].product_id)].name)               # nome dos produtos pedidos
    wallet.append(consumer_list[int(order_list[i + 1].consumer_id)].wallet)         # quantidade de dinheiro do cliente
    price.append(product_list[int(order_list[i + 1].product_id)].price)             # preço do pedido
    username.append(consumer_list[int(order_list[i + 1].consumer_id)].name)         # nome do consumidor

for i in range(len(user_amount)):
    
    price_total_order = int(user_amount[i])*float(price[i])

    if(int(user_amount[i]) <= int(stock[i])):                # se a loja possui a quantidade de produtos do pedido
        #print(f"{i+1}) Possui em estoque! Order Quant: {user_amount[i]} Stock: {stock[i]} Name: {name[i]}")

        if(float(wallet[i]) > price_total_order):           # se o comprador possui mais dinheiro que o pedidos              
            wallet[i] = float(wallet[i]) - float(price_total_order)
            print(f"{i+1}) Pedido concluido! Wallet: {wallet[i]} Order Price: {price_total_order:.2f} Name: {username[i]}")     

        else: 
            print(f"{i+1}) ERRO! Saldo insuficiente. Wallet: {wallet[i]} Order Price: {price_total_order:.2f} Name: {username[i]}")

    else:
        print(f"{i+1}) ERRO! Produto não disponivel em estoque. UA: {user_amount[i]} S: {stock[i]} Name: {username[i]}")