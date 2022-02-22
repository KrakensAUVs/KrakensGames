from typing import Union
from managers.base_manager import BaseManager

class ConsumersManager(BaseManager):
    def __init__(self, folder: str) -> None:
        super().__init__("consumers", folder)

    def check_wallet(self, id_:int, total: float) -> bool:
        return self._data[id_]["wallet"] > total

    def wallet(self, id_: int, val: float = None) -> Union[None, float]:
        if not val:
            return self._data[id_]["wallet"]
        self._data[id_]["wallet"] = val

    def valid_order(self, id_: int, val: int) -> None:
        new_wallet = self._data[id_]["wallet"] - val
        self.wallet(id_, new_wallet)
    