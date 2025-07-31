from pygame import Vector2

from components.animation_state import AnimationState
from components.animation import Animation
from components.direction import Direction
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED, PLAYER_HP
from entitys.entity import Entity
from service.AnimationResource import AnimationResource


START_ANIMATION = "idle"


class Player(Entity):
    def __init__(self, entity_type, pos: Vector2):
        super().__init__(entity_type)
        
        self.add_component("transform", Transform(pos))
        self.add_component("movement", Movement(PLAYER_SPEED))
        self.add_component("direction", Direction())
        self.add_component("health", Health(PLAYER_HP))
        self.add_component("state", AnimationState(self.entity_type, START_ANIMATION))
        self.add_component("animation", Animation(AnimationResource().get_animation_frames(self.entity_type, START_ANIMATION)))
