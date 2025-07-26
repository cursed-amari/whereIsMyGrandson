from pygame import Vector2, Surface

from components.animation import Animation
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED
from entitys.entity import Entity


class Player(Entity):
    def __init__(self, pos: Vector2, frames: list[Surface]):
        self.add_component("transform", Transform(pos))
        self.add_component("movement", Movement(PLAYER_SPEED))
        self.add_component("animation", Animation(frames))
        self.add_component("health", Health(100))
