import csv
import helpers as hlp

#Iniciando variáveis
consumers_file_name = "consumers.csv"
orders_file_name = "orders.csv"
products_file_name = "products.csv"
fields = ['Order ID','Consumer ID','Product ID','Order Amount','Product Amount','Product Price','Order Total','Consumer Wallet','Foi Realizada','Product Amount After','Consumer Wallet After']
dictionary = []
my_map = hlp.CreateMap()

# Carregando arquivos CSV
consumers, orders, products = hlp.super_init(consumers_file_name, orders_file_name, products_file_name)

for order in orders:
    if hlp.checkOrder(order, products, consumers):
        order.foi_realizada = True
        my_map.create_order(order)
        for product in products:
            if order.product_id == product.id:
                __product_price = product.price
                my_map.create_product(product, order)
                product.amount = product.amount - order.amount
                break
        for consumer in consumers:
            if order.consumer_id == consumer.id:
                my_map.create_consumer(consumer, order, __product_price)
                consumer.wallet = round(consumer.wallet - order.amount * __product_price, 2)
                break
        my_map.append_map()
    else:
        my_map.create_order(order)
        for product in products:
            if order.product_id == product.id:
                my_map.create_product(product, order)
                __product_price = product.price
                break
        for consumer in consumers:
            if order.consumer_id == consumer.id:
                my_map.create_consumer(consumer, order, __product_price)
                if not consumer.foi_afetado:
                    consumer.foi_afetado = True
                    consumer.compras_af = consumer.compras_af + 1
                    break
                else:
                    consumer.compras_af = consumer.compras_af + 1
                    break
        my_map.append_map()

filename = 'orders_check_new.csv'
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields, dialect='excel')
    writer.writeheader()
    writer.writerows(my_map.get_list_of_maps())


hlp.show_affected(consumers, orders)
