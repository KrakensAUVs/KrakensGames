from managers.products_manager import ProductsManager
from managers.consumers_manager import ConsumersManager
from managers.orders_manager import OrdersManager

class Solver:
    def __init__(self, folder: str = 'original') -> None:
        self.__orders = OrdersManager(folder)
        self.__consumers = ConsumersManager(folder)
        self.__products = ProductsManager(folder)
        self.__invalids = {}

        self.__run_solve()

    @property
    def clients(self):
        return len(list(self.__invalids.keys()))

    @property
    def ocurrencies(self):
        total = 0
        for _, value in self.__invalids.items():
            total += len(value)
        return total
    
    @property
    def amount(self):
        total = 0
        for _, value in self.__invalids.items():
            total += len([el for el in value if el["type"] == "amount"])
        return total

    @property
    def wallet(self):
        total = 0
        for _, value in self.__invalids.items():
            total += len([el for el in value if el["type"] == "wallet"])
        return total

    def __run_solve(self):
        while self.__orders.have_order():
            order = self.__orders.get_order()
            self.__compute_order(order)
    

    def __compute_order(self, order):
        c_id, p_id = int(order["consumer_id"]), int(order["product_id"])
        if self.__products.check_amount(p_id, order["amount"]):
            total_price = self.__products.price(p_id)*order["amount"]
            if self.__consumers.check_wallet(c_id, total_price):
                self.__products.valid_order(p_id, order["amount"])
                self.__consumers.valid_order(c_id, total_price)
                return True
            else:
                self.__invalid_order(c_id, order["id"], "wallet")
                return False
        else:
            self.__invalid_order(c_id, order["id"], "amount")
            return False
    
    def __invalid_order(self, consumer_id: int, order_id: int, type: str):
        entry = self.__invalids.get(consumer_id, [])
        entry.append({
            "order_id": order_id, 
            "type": type
        })

        self.__invalids[consumer_id] = entry
