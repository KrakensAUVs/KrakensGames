from typing import Union
from managers.base_manager import BaseManager

class ProductsManager(BaseManager):
    def __init__(self, folder: str) -> None:
        super().__init__("products", folder)
    
    def check_amount(self, id_: int, amount: int) -> bool:
        return self._data[id_]["amount"] > amount

    def amount(self, id_: int, val: int = None) -> Union[None, int]:
        if not val:
            return self._data[id_]["amount"]
        self._data[id_]["amount"] = val

    def price(self, id_: int, val: float = None) -> Union[None, float]:
        if not val:
            return self._data[id_]["price"]
        self._data[id_]["price"] = val   

    def valid_order(self, id_: int, val: int) -> None:
        new_amount = self._data[id_]["amount"] - val
        self.amount(id_, new_amount)