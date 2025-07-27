from pygame import Vector2, Surface

from components.animation_manager import AnimationManager
from components.animation_state import AnimationState
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED, PLAYER_HP
from entitys.entity import Entity


class Player(Entity):
    def __init__(self, pos: Vector2):
        super().__init__()
        self.add_component("transform", Transform(pos))
        self.add_component("movement", Movement(PLAYER_SPEED))
        self.add_component("state", AnimationState("player", "idle"))
        self.add_component("animation", AnimationManager(self.get_component("state")))
        self.get_component("animation").load_all_animations()
        self.get_component("animation").create_mirror_for_all()
        self.add_component("health", Health(PLAYER_HP))
