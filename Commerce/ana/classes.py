import csv

class Export_data():  
  def export(self, arq, id, col):
    n = 0
    for item in arq:
      if n > 0 and int(item[0]) == id:
        if col < 0:
          return item
        else:
          return item[col]
      n = n+1

class Arquivo(Export_data):

  def ler (self, arq):
    with open(arq) as arquivo:
      leitura = csv.reader(arquivo)
      array = list(leitura)
    return array
  
  def buscar (self, documento, id):
    print(self.export(documento, id, -1))
  
  def escrever (self, resultados, titulo):
    with open(titulo, 'w', newline='') as file:
      mywriter = csv.writer(file, delimiter=',')
      mywriter.writerows(resultados)
  
  def atualizar (self, id, arq, col, dado):
    n = 0
    for linha in arq:
      if n > 0 and int(linha[0]) == id:
        if dado < 0:
          linha[col] = int(linha[col])+1
        else:
          linha[col] = dado
      n = n + 1


class Conferir:

  def qtd_estoque(self, qtd, estoque):    
    return True if qtd <= estoque else False
  
  def money_disp(self, wallet, valor, qtd):
    return True if wallet >= (valor*qtd) else False
  
  def resultado_existente(self, consumer_id, resultados):
    n = 0
    for resultado in resultados:
      if n > 0:
        id_cons = int(resultado[0])
        if id_cons == consumer_id:
          return 1
      n = n+1  
    return 0


class Consumer(Export_data):
  def __init__(self, id, arq):
    self.__id = id
    self.__arq = arq
    self.__name = self.export(self.__arq, self.__id, 1)
    self.__wallet = self.export(self.__arq, self.__id, 4)
  
  @property
  def name (self):
    return self.__name
  
  @property
  def wallet (self):
    return float(self.__wallet)

class Order(Export_data):
  def __init__(self, id, arq):
    self.__id = int(id)
    self.__arq = arq
    self.__consumer_id = self.export(self.__arq, self.__id, 1)
    self.__product_id = self.export(self.__arq, self.__id, 2)
    self.__qtd = self.export(self.__arq, self.__id, 3)
  
  @property
  def consumer_id (self):
    return int(self.__consumer_id)
  
  @property
  def product_id (self):
    return int(self.__product_id)

  @property
  def qtd (self):
    return int(self.__qtd)


class Product(Export_data):
  def __init__(self, id, arq):
    self.__id = id
    self.__arq = arq
    self.__estoque = self.export(self.__arq, self.__id, 3)
    self.__valor = self.export(self.__arq, self.__id, 4)
  
  @property
  def estoque (self):
    return int(self.__estoque)
  
  @property
  def valor (self):
    return float(self.__valor)

    
    