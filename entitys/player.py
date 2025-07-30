from pygame import Vector2

from components.animation_state import AnimationState
from components.direction import Direction
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED, PLAYER_HP
from entitys.entity import Entity


class Player(Entity):
    def __init__(self, pos: Vector2):
        super().__init__()
        self.entity_type = "player"
        self.add_component("transform", Transform(pos))
        self.add_component("movement", Movement(PLAYER_SPEED))
        self.add_component("direction", Direction())
        self.add_component("health", Health(PLAYER_HP))
        self.add_component("state", AnimationState(self.entity_type, "idle"))
