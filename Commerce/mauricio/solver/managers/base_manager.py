from typing import Union

class BaseManager:

    def __init__(self, file_name: str, folder: str) -> None:
        self._data = {}
        file = open(f"{folder}/{file_name}.csv", "r", encoding="utf-8")
        self._labels = self._read_line(file.readline())[1:]
        for line in file:
            id_, line_data = self._extract_info(line)
            self._data[id_] = line_data
    
    def _read_line(self, text: str) -> str:
        return text.strip("\n").split(", ")

    def _extract_info(self, infos: str) -> tuple:
        id_, *data = self._read_line(infos)
        formated = {}
        for label, info in zip(self._labels, data):
            formated[label] = self._convert_type(info)
        return int(id_), formated
    
    def _convert_type(self, info: str) -> Union[str, int, float]:
        if info.isdigit():
            return int(info)
        elif self._is_float(info):
            return float(info)
        return info

    def _is_float(self, value: str) -> bool:
        return value.replace(".", "", 1).isdigit()