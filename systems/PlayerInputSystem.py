import pygame
from pygame import Vector2


class PlayerInputSystem:
    def __init__(self, camera_system, movement_component, direction_component):
        self.camera_system = camera_system
        self.movement = movement_component
        self.direction = direction_component

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_EQUALS:
                    self.camera_system.zoom_in()
                elif event.key == pygame.K_x:
                    self.camera_system.zoom_out()

    def update_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.movement.velocity.y = -1
        if keys[pygame.K_s]:
            self.movement.velocity.y = 1
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.movement.velocity.x = -1
            self.direction.direction = -1
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.movement.velocity.x = 1
            self.direction.direction = 1

