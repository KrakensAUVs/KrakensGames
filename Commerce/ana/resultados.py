from classes import *

def escolher_arqs(orders, consumers, products):
  resposta = input('Organizados (ORG) ou embaralhados (EMB)?')

  arquivo = Arquivo()
  
  if resposta == 'ORG':
    orders = arquivo.ler("original/orders.csv")
    consumers = arquivo.ler("original/consumers.csv")
    products = arquivo.ler("original/products.csv")
  if resposta == 'EMB':
    orders = arquivo.ler("shuffle/orders.csv")
    consumers = arquivo.ler("shuffle/consumers.csv")
    products = arquivo.ler("shuffle/products.csv")


def Executar(resultados):
  #Variáveis
  i = 0

  #Inicialização de classes
  arquivo = Arquivo()
  conferir = Conferir()

  #Leitura de arquivos
  resposta = input('Organizados (ORG) ou embaralhados (EMB)?')
  
  if resposta == 'ORG':
    orders = arquivo.ler("original/orders.csv")
    consumers = arquivo.ler("original/consumers.csv")
    products = arquivo.ler("original/products.csv")
  if resposta == 'EMB':
    orders = arquivo.ler("shuffle/orders.csv")
    consumers = arquivo.ler("shuffle/consumers.csv")
    products = arquivo.ler("shuffle/products.csv")

  #Loop de conferência dos pedidos
  for pedido in orders:

    if i > 0:
      # Inicializando as classes
      order_id = int(pedido[0])
      order = Order(order_id, orders)
      produto = Product(order.product_id, products)
      consumer = Consumer(order.consumer_id, consumers)

      # Conferindo quantidade em estoque e se o usuário tem dinheiro disponível na carteira
      if conferir.qtd_estoque(order.qtd, produto.estoque) and conferir.money_disp(consumer.wallet, produto.valor, order.qtd):
        
        #Atualizando os dados do produto e do consumidor
        arquivo.atualizar(order.product_id, products, 3, produto.estoque-order.qtd)

        arquivo.atualizar(order.consumer_id, consumers, 4, consumer.wallet-(order.qtd*produto.valor))

      else:

        # Caso a compra não seja válida, confere na lista de resultados se o usuário em questão já foi listado
        if conferir.resultado_existente(order.consumer_id, resultados) == 0:

          # Adicionando uma linha, caso o usuário ainda não tenha sido listado
          resultados.append([str(order.consumer_id), consumer.name, '1'])

        else:

          # Procurando o usuário já listado e adicionando uma compra não válida a sua linha

          arquivo.atualizar(order.consumer_id, resultados, 2, -1)

    #Variáveis de controle de leitura  
    i = i+1
