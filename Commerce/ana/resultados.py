from classes import *

def Buscar(arq, id, col):
  n = 0
  for item in arq:
    if n > 1 and int(arq[1]) == id:
      return item[col]
    n = n+1

def Executar(orders, consumers, products, resultados, conferir):
  #Variáveis
  i = 0
  n = 0

  #Loop de conferência dos pedidos
  for pedido in orders:

    if i > 0:
      #order_id = int(pedido[0])
      #order = Order(order_id, orders)

      #Informações necessárias do pedido
      consumer_id = int(pedido[1])
      #consumer_id = order.consumer_id
      product_id = int(pedido[2])
      qtd = int(pedido[3])

      #Variáveis de informações necessárias para a conferência
      estoque = int(products[product_id][3])
      wallet = float(consumers[consumer_id][4])
      valor = float(products[product_id][4])

      #Conferindo quantidade em estoque e se o usuário tem dinheiro disponível na carteira
      if conferir.qtd_estoque(qtd, estoque) and conferir.money_disp(wallet, valor, qtd):
        
        #Atualizando os dados do produto e do consumidor
        aux = estoque - qtd
        products[product_id][3] = str(aux)

        aux = wallet - (qtd*valor)
        consumers[consumer_id][4] = str(aux)

      else:

        #Caso a compra não seja válida, confere na lista de resultados se o usuário em questão já foi listado
        if conferir.resultado_existente(consumer_id, resultados) == 0:

          #Adicionando uma linha, caso o usuário ainda não tenha sido listado
          resultados.append([str(consumer_id), consumers[consumer_id][1], '1'])

        else:

          #Procurando o usuário já listado e adicionando uma compra não válida a sua linha
          for resultado in resultados:
            if n > 1 and int(resultado[0]) == consumer_id:
              aux = int(resultado[2])+1
              resultado[2] = str(aux)

            n = n+1

    #Variáveis de controle de leitura  
    i = i+1
    n = 0
