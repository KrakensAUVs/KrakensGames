from typing import Union
from managers.base_manager import BaseManager

class OrdersManager(BaseManager):
    def __init__(self, folder: str) -> None:
        super().__init__("orders", folder)
        self.__key_list = list(self._data.keys())
        self.__actual = self.__key_list[0]
        self.__finish = False
    
    def have_order(self) -> bool:
        return not self.__finish
        
    def get_order(self) -> int:
        order = { "id": self.__actual, **self._data[self.__actual]}
        if self.__actual != self.__key_list[-1]:
            pos = self.__key_list.index(self.__actual)
            self.__actual = self.__key_list[pos+1]
        else:
            self.__finish = True
        return order
