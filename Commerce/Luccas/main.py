import csv
import helpers as hlp

#Iniciando variáveis
consumers_file_name = "consumers.csv"
orders_file_name = "orders.csv"
products_file_name = "products.csv"
save_file_name = 'orders_check_teste.csv'
fields = ['Order ID','Consumer ID','Product ID','Order Amount','Product Amount','Product Price','Order Total','Consumer Wallet','Foi Realizada','Product Amount After','Consumer Wallet After']

# Carregando arquivos CSV...
consumers, orders, products = hlp.super_init(consumers_file_name, orders_file_name, products_file_name) #carrega os arquivos csv

# Computando...
consumers, orders, products, __result = hlp.check_all(consumers, orders, products) #checa todas as ordens e uma lista de mapas com o resultado de cada ordem ralizada ou não

# Gerando resultados...
hlp.gen_csv_results_file(save_file_name, __result, fields) #gera um arquivo csv com o resultado das ordens
hlp.show_affected(consumers, orders) #mostra o número de pessoas e ordens afetadas
