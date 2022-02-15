import csv

class Arquivo:

  def ler (self, arq):
    with open(arq) as arquivo:
      leitura = csv.reader(arquivo)
      array = list(leitura)
    return array
  
  def buscar (self, documento, id):
    print(documento[id])


class Conferir:

  def qtd_estoque(self, qtd, estoque):
    return True if qtd <= estoque else False
  
  def money_disp(self, wallet, valor, qtd):
    return True if wallet >= (valor*qtd) else False
  
  def resultado_existente(self, consumer_id, resultados):
    n = 0
    for resultado in resultados:
      if n > 1:
        id_cons = int(resultado[0])
        if id_cons == consumer_id:
          return 1
      n = n+1  
    return 0

    
    