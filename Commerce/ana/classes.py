import csv
from resultados import Buscar

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

class Consumer:
  def __init__(self, id, arq):
    self.id = id
    self.arq = arq
  
  @property
  def name (self):
    Buscar(self.arq, self.id, 1)
  
  @property
  def wallet (self):
    Buscar(self.arq, self.id, 4)

class Order:
  def __init__(self, id, arq):
    self.id = id
    self.arq = arq
  
  @property
  def consumer_id (self):
    Buscar(self.arq, self.id, 1)
  
  @property
  def product_id (self):
    Buscar(self.arq, self.id, 2)

  @property
  def qtd (self):
    Buscar(self.arq, self.id, 3)


class Product:
  def __init__(self, id, arq):
    self.id = id
    self.arq = arq
  
  @property
  def estoque (self):
    Buscar(self.arq, self.id, 3)
  
  @property
  def valor (self):
    Buscar(self.arq, self.id, 4)

    
    