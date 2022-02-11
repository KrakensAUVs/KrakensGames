from itertools import product
from classes import Arquivo, Conferir
import csv

if __name__ == '__main__':

  #Inicialização de classes
  arquivo = Arquivo()
  conferir = Conferir()

  #Variáveis
  i = 0
  n = 0

  #Leitura de arquivos
  orders = arquivo.ler("orders.csv")
  consumers = arquivo.ler("consumers.csv")
  products = arquivo.ler("products.csv")

  #Início do array de registro dos resultados
  resultados = [['consumer_id', 'Nome', 'Compras Inválidas']]

  #Loop de conferência dos pedidos
  for pedido in orders:

    if i > 0:
      #Informações necessárias do pedido
      consumer_id = int(pedido[1])
      product_id = int(pedido[2])
      qtd = int(pedido[3])

      #Variáveis de informações necessárias para a conferência
      estoque = int(products[product_id][3])
      wallet = float(consumers[consumer_id][4])
      valor = float(products[product_id][4])

      #Conferindo quantidade em estoque e se o usuário tem dinheiro disponível na carteira
      if conferir.qtd_estoque(qtd, estoque) and conferir.money_disp(wallet, valor, qtd):
        #Atualizando os dados do produto e do consumidor
        products[product_id][3] = estoque -  qtd
        consumers[consumer_id][4] = wallet - valor
      else:
        #Caso a compra não seja válida, confere na lista de resultados se o usuário em questão já foi listado
        if conferir.resultado_existente(consumer_id, resultados) == 0:
          #Adicionando uma linha, caso o usuário ainda não tenha sido listado
          resultados.append([str(consumer_id), consumers[consumer_id][1], '1'])
        else:
          #Procurando o usuário já listado e adicionando uma compra não válida a sua linha
          for resultado in resultados:
            if n > 1 and int(resultado[0]) == consumer_id:
              resultado[2] = int(resultado[2])+1
            n = n+1

    #Variáveis de controle de leitura  
    i = i+1
    n = 0
  
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


