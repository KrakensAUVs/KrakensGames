from itertools import product
from classes import *
from resultados import *
import csv

if __name__ == '__main__':

  #Início do array de registro dos resultados
  resultados = [['consumer_id', 'Nome', 'Compras Inválidas']]

  Executar(resultados)
  
  #Escrita do array de resultados no arquivo CSV para facilitar leitura
  Arquivo().escrever(resultados, 'resultados.csv')
  
  #Apresentação dos resultados
  print("Pessoas afetadas: ")
  print(int(len(resultados))-1)
  print("Para acessar os usuário afetados e quantas compras inválidas cada usuário teve, acesse o arquivo resultados.csv")

  resp = input("Deseja abrir o arquivo aqui? (s ou n)")

  leitura = Arquivo()
  if resp == "s":
    resultado_leitura = leitura.ler("resultados.csv")
    print(resultado_leitura)


