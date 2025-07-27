import os

import pygame

from service.utils import split_tilemap, transform_surface


class AssetLoader:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def load_tile_map(self, path: str, row: int, col: int, size: tuple[float, float] = False) -> list:
        """
        Загружает tileMap по абсолютному пути
        :param path: Абсолютный путь к tileMap
        :param row: количество строк в tileMap
        :param col: количество колонок в tileMap
        :param size: Размер Tuple(x, y) в котором должно быть изображене, если изменение не требуется False
        :return: list[Surface]
        """

        if path in self._cache:
            return self._cache[path]

        if os.path.exists(path):
            if os.path.isabs(path):
                list_surface = split_tilemap(path, row, col)
                if size:
                    list_surface = transform_surface(list_surface, size)
                self._cache[path] = list_surface
                return list_surface
            else:
                raise ValueError("Требуется абсолютный путь")
        else:
            raise ValueError("Путь не найден")

    def load_image(self, path: str, size: tuple[float, float] = False) -> pygame.Surface:
        """
        Загружает изображение по абсолютному пути
        :param path: Абсолютный путь к изображению
        :param size: Размер Tuple(x, y) в котором должно быть изображене, если изменение не требуется False
        :return: Surface
        """
        if path in self._cache:
            return self._cache[path]

        if os.path.exists(path):
            if os.path.isabs(path):
                image = pygame.image.load(path).convert_alpha()
                if size:
                    image = transform_surface(image, size)
                self._cache[path] = image
                return image
            else:
                raise ValueError("Требуется абсолютный путь")
        else:
            raise ValueError("Путь не найден")





