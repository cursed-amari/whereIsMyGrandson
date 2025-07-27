import pytest
import pygame
from pygame import Surface

from components.animation import Animation
from components.animation_state import AnimationState
from components.animation_manager import AnimationManager


@pytest.fixture
def animation_state():
    return AnimationState("player", "idle")


@pytest.fixture
def mock_settings_and_loader(mocker):
    # Переопределим ANIMATION_PATH и ENTITY_SIZE
    mocker.patch("components.animation_manager.ANIMATION_PATH", {
        "player_idle": ("/abs/path/player_idle.png", 2, 1),
        "player_walk": ("/abs/path/player_walk.png", 3, 1)
    })
    mocker.patch("components.animation_manager.ENTITY_SIZE", {
        "player": (64, 64)
    })

    # Мокаем AssetLoader().load_tile_map
    mock_loader = mocker.patch("components.animation_manager.AssetLoader", autospec=True)
    mock_loader.return_value.load_tile_map.side_effect = lambda path, r, c, size=None: [
        Surface(size) for _ in range(r * c)
    ]

    # Мокаем mirror_surface
    mocker.patch("components.animation_manager.mirror_surface", lambda frames: frames[::-1])


def test_init_valid(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    assert manager.state == animation_state
    assert isinstance(manager.animation, dict)


def test_init_invalid_state(mocker):
    mocker.patch("components.animation_manager.ANIMATION_PATH", {})
    mocker.patch("components.animation_manager.ENTITY_SIZE", {"player": (64, 64)})

    state = AnimationState("player", "idle")
    with pytest.raises(ValueError, match="idle анимация не найдена"):
        AnimationManager(state)


def test_load_all_animations(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_all_animations()

    keys = manager.get_list_animation()
    assert "player_idle" in keys
    assert "player_walk" in keys
    assert isinstance(manager.get_animation("idle"), Animation)
    assert manager.get_animation("idle").frames[0].get_size() == (64, 64)


def test_load_animation(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_animation("walk")
    assert "player_walk" in manager.animation
    assert isinstance(manager.get_animation("walk"), Animation)


def test_create_mirror(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_animation("walk")
    manager.create_mirror("player_walk")

    assert "player_walk_mirror" in manager.animation
    assert isinstance(manager.get_animation("walk"), Animation)
    assert isinstance(manager.animation["player_walk_mirror"], Animation)


def test_create_mirror_for_all(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_all_animations()
    manager.create_mirror_for_all()

    assert "player_idle_mirror" in manager.animation
    assert "player_walk_mirror" in manager.animation


def test_get_current_animation(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_all_animations()
    current = manager.get_current_animation()
    assert isinstance(current, Animation)


def test_get_current_animation_missing(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    with pytest.raises(ValueError, match="Текущего состояния .* не найденно"):
        manager.get_current_animation()


def test_get_animation_invalid(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_all_animations()
    with pytest.raises(ValueError, match="Имя .* не найденно"):
        manager.get_animation("jump")


def test_get_list_animation(animation_state, mock_settings_and_loader):
    manager = AnimationManager(animation_state)
    manager.load_all_animations()
    anim_list = manager.get_list_animation()
    assert isinstance(anim_list, tuple)
    assert "player_idle" in anim_list

