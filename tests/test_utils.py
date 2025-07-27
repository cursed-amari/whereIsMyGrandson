import pytest
import pygame
import re

from pygame import Surface

from service.utils import sort_path, split_tilemap, transform_surface, mirror_surface


def test_sort_path():
    paths = ["file{2}.png", "file{1}.png", "file{3}.png"]
    sort_path(paths)
    assert paths == ["file{1}.png", "file{2}.png", "file{3}.png"]


def test_tilemap_splitting(tmp_path):
    test_file = tmp_path / "test.png"
    pygame.image.save(Surface((30, 10)), test_file)

    tiles = split_tilemap(str(test_file), 3, 1)
    assert len(tiles) == 3
    assert tiles[0].get_size() == (10, 10)


def test_surface_transformation():
    surf = Surface((10, 10))
    transformed = transform_surface(surf, (20, 20))
    assert transformed.get_size() == (20, 20)

    mirrored = mirror_surface(surf)
    assert mirrored.get_size() == (10, 10)


def test_list_handling():
    surfs = [Surface((10, 10)) for _ in range(3)]

    transformed = transform_surface(surfs, (5, 5))
    assert all(s.get_size() == (5, 5) for s in transformed)

    mirrored = mirror_surface(surfs)
    assert len(mirrored) == 3