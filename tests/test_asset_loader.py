import pytest
import pygame
from pygame import Surface

from service.asset_loader import AssetLoader


def test_singleton_pattern():
    loader1 = AssetLoader()
    loader2 = AssetLoader()
    assert loader1 is loader2


def test_cache_system(tmp_path):
    loader = AssetLoader()
    test_file = tmp_path / "test.png"
    pygame.image.save(Surface((30, 10)), test_file)

    frames1 = loader.load_tile_map(str(test_file), 3, 1)
    frames2 = loader.load_tile_map(str(test_file), 3, 1)

    assert frames1 is frames2
    assert len(frames1) == 3


def test_path_validation():
    loader = AssetLoader()
    with pytest.raises(ValueError):
        loader.load_tile_map("relative/path.png", 1, 1)
