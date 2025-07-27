import pytest
from pygame import Surface

from components.animation import Animation
from components.animation_state import AnimationState
from components.animation_manager import AnimationManager
from service.asset_loader import AssetLoader


class MockAssetLoader:
    def load_tile_map(self, path, rows, cols):
        return [Surface((10, 10))] * (rows * cols)


@pytest.fixture
def animation_state():
    return AnimationState("player", "idle")


def test_animation_manager_init(animation_state, mocker):
    mocker.patch("core.settings.ANIMATION_PATH", {"player_idle": ("path", 1, 1)})
    manager = AnimationManager(animation_state)
    assert manager.state == animation_state


def test_animation_loading(animation_state, mocker):
    mocker.patch("core.settings.ANIMATION_PATH", {
        "player_idle": ("idle.png", 1, 1),
        "player_walk": ("walk.png", 1, 1)
    })

    class MockAssetLoader:
        def __init__(self):
            self._cache = {}

        def load_tile_map(self, path: str, row: int, col: int) -> list:
            return [Surface((10, 10)) for _ in range(row * col)]

    mocker.patch("components.animation_manager.AssetLoader",
                 return_value=MockAssetLoader())

    manager = AnimationManager(animation_state)
    manager.load_all_animations()

    assert "player_idle" in manager.animation
    assert "player_walk" in manager.animation
    assert isinstance(manager.get_current_animation(), Animation)


def test_error_handling(animation_state, mocker):
    mocker.patch("components.animation_manager.ANIMATION_PATH", {})
    with pytest.raises(ValueError):
        AnimationManager(animation_state)

    mocker.patch("components.animation_manager.ANIMATION_PATH", {})
    with pytest.raises(ValueError):
        manager = AnimationManager(animation_state)
        manager.get_current_animation()