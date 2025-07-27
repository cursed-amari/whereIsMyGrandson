import os

from service.utils import split_tilemap


class AssetLoader:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def load_tile_map(self, path: str, row: int, col: int) -> list:
        """
        Загружает tileMap по абсолютному пути
        :param path: Абсолютный путь к tileMap
        :param row: количество строк в tileMap
        :param col: количество колонок в tileMap
        :return:
        """

        if path in self._cache:
            return self._cache[path]

        if os.path.isabs(path):
            list_surface = split_tilemap(path, row, col)
            self._cache[path] = list_surface
            return list_surface
        else:
            raise ValueError("Требуется абсолютный путь")




