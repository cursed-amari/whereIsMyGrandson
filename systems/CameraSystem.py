from random import random

from pygame import Vector2

from core.settings import (SCREEN_WIDTH,
                           SCREEN_HEIGHT,
                           SCREEN_ZOOM,
                           SCREEN_MAX_ZOOM,
                           SCREEN_MIN_ZOOM,
                           SCREEN_ZOOM_STEP,
                           SCREEN_SHAKE_FORCE)
from entitys.entity import Entity


class CameraSystem:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, screen_width: int = SCREEN_WIDTH, screen_height: int = SCREEN_HEIGHT):
        self.screen_center = Vector2(screen_width // 2, screen_height // 2)
        self.offset = Vector2(0, 0)
        self.current_zoom = SCREEN_ZOOM
        self._shake_timer = 0
        self._current_shake = Vector2(0, 0)

    def follow_entity(self, target: Entity, smoothness: float = 0.1):
        if not target.has_component("transform"):
            return
        desired_offset = target.get_component("transform").position - self.screen_center * (1 / self.current_zoom)
        self.offset = (desired_offset - self.offset) * smoothness

    def zoom_in(self):
        self.current_zoom = min(SCREEN_MAX_ZOOM, self.current_zoom + SCREEN_ZOOM_STEP)

    def zoom_out(self):
        self.current_zoom = max(SCREEN_MIN_ZOOM, self.current_zoom - SCREEN_ZOOM_STEP)

    def reset_zoom(self):
        self.current_zoom = SCREEN_ZOOM

    def apply_shake(self, duration: float = 0.5):
        self._shake_timer = duration

    def update(self, dt: float):
        if self._shake_timer > 0:
            self._shake_timer -= dt
            self._current_shake = Vector2(
                (random() * 2 - 1) * SCREEN_SHAKE_FORCE,
                (random() * 2 - 1) * SCREEN_SHAKE_FORCE
            )
        else:
            self._current_shake = Vector2(0, 0)


