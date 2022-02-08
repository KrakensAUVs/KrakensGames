import csv

class Arquivo:
  def ler (self, arq):
    with open(arq) as arquivo:
      leitura = csv.reader(arquivo)
      array = list(leitura)
    return array
  
  def buscar (self, documento, id):
    print(documento[id])

class Consumer:
  cliente = Arquivo.ler(1, "consumers.csv")

  @property
  def nome(self, cliente, id):
    nome = cliente[id][2]
    return nome

  @property
  def idade(self, cliente, id):
    idade = cliente[id][3]
    return idade

  @property
  def cep(self, cliente, id):
    cep = cliente[id][4]
    return cep
  
  @property
  def wallet(self, cliente, id):
    wallet = cliente[id][5]
    return wallet

class Order:
  def __init__(self, wallet, qtd, estoque, valor):
    self.__wallet = wallet
    self.__qtd = qtd
    self.__estoque = estoque
    self.__valor = valor
  
  @property
  def wallet(self):
      return self.__wallet
  
  @property
  def qtd(self):
      return self.__qtd

  @property
  def estoque(self):
      return self.__estoque
  
  @property
  def valor(self):
      return self.__valor
    
    