from itertools import product
from classes import *
from resultados import *
import csv

if __name__ == '__main__':

  #Inicialização de classes
  arquivo = Arquivo()
  conferir = Conferir()

  #Leitura de arquivos
  orders = arquivo.ler("orders.csv")
  consumers = arquivo.ler("consumers.csv")
  products = arquivo.ler("products.csv")

  #Início do array de registro dos resultados
  resultados = [['consumer_id', 'Nome', 'Compras Inválidas']]

  Executar(orders, consumers, products, resultados, conferir)
  
  #Escrita do array de resultados no arquivo CSV para facilitar leitura
  with open('resultados.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(resultados)
  
  #Apresentação dos resultados
  print("Pessoas afetadas: ")
  print(int(len(resultados))-1)
  print("Para acessar os usuário afetados e quantas compras inválidas cada usuário teve, acesse o arquivo resultados.csv")

  resp = input("Deseja abrir o arquivo aqui? (s ou n)")

  if resp == "s":
    resultado_leitura = arquivo.ler("resultados.csv")
    print(resultado_leitura)


