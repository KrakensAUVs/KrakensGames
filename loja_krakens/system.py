from classes import Arquivo

if __name__ == '__main__':
  
  orders = Arquivo.ler(1,"orders.csv")
  consumers = Arquivo.ler(1, "consumers.csv")
  products = Arquivo.ler(1, "products.csv")    

  Arquivo.buscar(1, consumers, 8)

