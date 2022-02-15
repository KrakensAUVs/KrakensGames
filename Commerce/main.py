import csv
import helpers as hlp
import time

# Carregando arquivos CSV

start_csv_load = time.time()

consumers = hlp.superInitConsumers("consumers.csv") #carregando o a lista de mapas dos consumidores
products = hlp.superInitProducts("products.csv") #carregando a lista de mapas dos produtos
orders = hlp.superInitOrders("orders.csv") #carregando a lista de mapas das orderns de compra

end_csv_load = time.time()

print(f"Tempo de carregamento CSV foi de: {end_csv_load - start_csv_load}")

fields = ['Order ID','Consumer ID','Product ID','Order Amount','Product Amount','Product Price','Order Total','Consumer Wallet','Foi Realizada','Product Amount After','Consumer Wallet After']

dictionary = []

start_loop = time.time()
for order in orders:
    map = {}
    if hlp.checkOrder(order, products, consumers):
        order.foi_realizada = True
        map['Order ID'] = f"{order.id}"
        map['Consumer ID'] = f"{order.consumer_id}"
        map['Product ID'] = f"{order.product_id}"
        map['Order Amount'] = f"{order.amount}"
        map['Foi Realizada'] = 'True'
        for product in products:
            if order.product_id == product.id:
                map['Product Amount'] = f"{product.amount}"
                map['Product Price'] = f"{product.price}"
                __product_price = product.price
                product.amount = product.amount - order.amount
                map['Product Amount After'] = f"{product.amount}"
                break
        for consumer in consumers:
            if order.consumer_id == consumer.id:
                map['Consumer Wallet'] = f"{consumer.wallet}"
                consumer.wallet = round(consumer.wallet - order.amount * __product_price, 2)
                map['Order Total'] = f"{round(order.amount * __product_price, 2)}"
                map['Consumer Wallet After'] = f"{consumer.wallet}"
                break
        dictionary.append(map)
    else:
        map['Order ID'] = f"{order.id}"
        map['Consumer ID'] = f"{order.consumer_id}"
        map['Product ID'] = f"{order.product_id}"
        map['Order Amount'] = f"{order.amount}"
        map['Foi Realizada'] = 'False'
        for product in products:
            if order.product_id == product.id:
                map['Product Amount'] = f"{product.amount}"
                map['Product Price'] = f"{product.price}"
                __product_price = product.price
                map['Product Amount After'] = f"{product.amount}"
                break
        for consumer in consumers:
            if order.consumer_id == consumer.id:
                map['Consumer Wallet'] = f"{round(consumer.wallet, 2)}"
                map['Order Total'] = f"{round(order.amount * __product_price, 2)}"
                map['Consumer Wallet After'] = f"{round(consumer.wallet, 2)}"
                if not consumer.foi_afetado:
                    consumer.foi_afetado = True
                    consumer.compras_af = consumer.compras_af + 1
                    break
                else:
                    consumer.compras_af = consumer.compras_af + 1
                    break
        dictionary.append(map)
end_loop = time.time()
print(f"Tempo de execução das ordens: {end_loop - start_loop}")

consumers_af = 0
orders_af = 0

for consumer in consumers:
    if consumer.foi_afetado:
        consumers_af = consumers_af + 1

for order in orders:
    if not order.foi_realizada:
        orders_af = orders_af + 1

print(f"Número de consumidores afetados: {consumers_af}")
print(f"Número de ordens afetadas: {orders_af}")

"""filename = 'orders_check.csv'

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields, dialect='excel')

    writer.writeheader()

    writer.writerows(dictionary)"""
