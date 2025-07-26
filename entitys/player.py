from pygame import Vector2, Surface

from components.animation import Animation
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED, PLAYER_HP
from entitys.entity import Entity
from service.state import State


class Player(Entity):
    state = State.idle

    def __init__(self, pos: Vector2, frames: list[Surface]):
        super().__init__()
        self.add_component("transform", Transform(pos))
        self.add_component("movement", Movement(PLAYER_SPEED))
        self.add_component("animation", Animation(frames))
        self.add_component("health", Health(PLAYER_HP))
