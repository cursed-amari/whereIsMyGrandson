from PIL import Image
import pygame
import re

from pygame import Surface


def sort_path(paths: list[str]) -> None:
    """
    Сортирует список по {число}
    pattern: \{(\d*)\}
    :param paths: Список путей
    :return: Отсортированный список путей
    """
    def extract_number(path: str) -> int:
        search = re.search(r"\{(\d*)\}", path)
        if search:
            num = search.group(1)
        else:
            raise ValueError(f"Паттерн не найден в путе {path}")
        return int(num)

    paths.sort(key=lambda path: extract_number(path))


def create_horizontal_tilemap(image_paths: list, output_path: str) -> None:
    """
    Объединяет изображения в горизонтальный tilemap и сохраняет его.

    :param image_paths: список путей к изображениям
    :param output_path: путь для сохранения tilemap
    """
    images = [Image.open(path) for path in image_paths]

    heights = [img.height for img in images]
    if len(set(heights)) > 1:
        raise ValueError("Все изображения должны иметь одинаковую высоту")

    total_width = sum(img.width for img in images)
    tilemap = Image.new('RGBA', (total_width, images[0].height))

    x_offset = 0
    for img in images:
        tilemap.paste(img, (x_offset, 0))
        x_offset += img.width

    tilemap.save(output_path)


def split_tilemap(tilemap_path, columns, rows):
    """
    Разбивает tilemap на отдельные поверхности Pygame.

    :param tilemap_path: путь к изображению tilemap
    :param columns: количество столбцов
    :param rows: количество строк
    :return: список поверхностей Pygame
    """
    surface = pygame.image.load(tilemap_path).convert_alpha()
    tile_width = surface.get_width() // columns
    tile_height = surface.get_height() // rows

    tiles = []
    for y in range(rows):
        for x in range(columns):
            rect = pygame.Rect(
                x * tile_width,
                y * tile_height,
                tile_width,
                tile_height
            )
            tile_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
            tile_surface.blit(surface, (0, 0), rect)
            tiles.append(tile_surface)

    return tiles


def transform_surface(surface: Surface | list[Surface], size: tuple[float, float]) -> Surface | list[Surface]:
    if not surface:
        raise ValueError("Либо список surface пустой, либо surface имеет размеры 0, 0")
    if size[0] <= 0 or size[1] <= 0:
        raise ValueError("Размеры должны быть больше 0")

    if isinstance(surface, list):
        if not all(isinstance(surf, Surface) for surf in surface):
            raise TypeError("Все элементы списка должны быть Surface")

        return [pygame.transform.smoothscale(surf, size) for surf in surface]
    elif isinstance(surface, Surface):
        return pygame.transform.smoothscale(surface, size)
    else:
        raise TypeError(f"surface {surface} должен быть либо списком либо Surface")
