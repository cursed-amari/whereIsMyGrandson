from pygame import Vector2
from entitys.player import Player
from components.animation_state import AnimationState
from components.movement import Movement
import pytest


def test_player_components():
    player = Player(Vector2(0, 0))

    assert player.has_component("transform")
    assert player.has_component("movement")
    assert player.has_component("state")
    assert player.has_component("animation")
    assert player.has_component("health")

    state = player.get_component("state")
    assert isinstance(state, AnimationState)
    assert state.name == "player"
    assert state.current_state == "idle"

    movement = player.get_component("movement")
    assert movement.speed > 0
