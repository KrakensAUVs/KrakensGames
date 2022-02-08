from classes import Arquivo

if __name__ == '__main__':

  arquivo = Arquivo()
  
  orders = arquivo.ler("orders.csv")
  consumers = arquivo.ler("consumers.csv")
  products = arquivo.ler("products.csv")    

  arquivo.buscar(consumers, 8)

