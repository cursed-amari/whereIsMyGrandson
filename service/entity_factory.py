from pygame import Vector2

from components.animation import Animation
from components.animation_state import AnimationState
from components.direction import Direction
from components.health import Health
from components.movement import Movement
from components.transform import Transform
from core.settings import PLAYER_SPEED, PLAYER_HP
from entitys.entity import Entity
from service.AnimationResource import AnimationResource


START_ANIMATION = "idle"


class EntityFactory:
    @staticmethod
    def create_player(pos: Vector2) -> Entity:
        player = Entity("player")
        player.add_component("transform", Transform(pos))
        player.add_component("movement", Movement(PLAYER_SPEED))
        player.add_component("direction", Direction())
        player.add_component("health", Health(PLAYER_HP))
        player.add_component("state", AnimationState(player.entity_type, START_ANIMATION))
        player.add_component("animation", Animation(
            AnimationResource().get_animation_frames(player.entity_type, START_ANIMATION))
                             )

        return player
