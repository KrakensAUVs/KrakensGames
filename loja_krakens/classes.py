import csv

class Arquivo:

  def ler (self, arq):
    with open(arq) as arquivo:
      leitura = csv.reader(arquivo)
      array = list(leitura)
    return array
  
  def buscar (self, documento, id):
    print(documento[id][1])

class Consumer:
  
  @property
  def nome(self, arq, id):
    nome = arq[id][1]
    return nome
  
  @property
  def wallet(self, arq, id):
    wallet = arq[id][4]
    return wallet

class Conferir:

  def qtd_estoque(self, qtd, estoque):
    if qtd <= estoque:
      return 1
    else:
      return 0
  
  def money_disp(self, wallet, valor, qtd):
    if wallet >= (valor*qtd):
      return 1
    else:
      return 0
  
  def resultado_existente(self, consumer_id, resultados):

    n = 0

    for resultado in resultados:
      if n > 1:
        id_cons = int(resultado[0])
        if id_cons == consumer_id:
          return 1
      n = n+1  
    return 0

    
    