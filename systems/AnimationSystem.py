from components.animation import Animation
from components.animation_state import AnimationState
from service.AnimationResource import AnimationResource


class AnimationSystem:
    def __init__(self, animation_resource: AnimationResource):
        self.resource = animation_resource

    def update(self, entities: list, dt: float):
        for entity in entities:
            if not entity.has_component(AnimationState) or not entity.has_component(Animation):
                continue

            anim = entity.get_component(Animation)

            anim.timer += dt * anim.speed
            if anim.timer >= 1 / anim.frame_rate:
                anim.current_frame = (anim.current_frame + 1) % len(anim.frames)
                anim.timer = 0
