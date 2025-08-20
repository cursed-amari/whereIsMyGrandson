# tests/systems/test_CameraSystem.py
import pytest
import pygame
from unittest.mock import MagicMock, patch

from systems.CameraSystem import CameraSystem
from entitys.entity import Entity
from components.transform import Transform

@pytest.fixture
def camera_system():
    return CameraSystem(screen_width=800, screen_height=600)

def test_follow_entity(camera_system):
    """
    Follow entity test
    """
    entity = Entity("player")
    transform = Transform(pygame.Vector2(100, 100))
    entity.add_component("transform", transform)
    camera_system.follow_entity(entity, smoothness=0.2)
    assert camera_system._target == entity
    assert camera_system.position == pygame.Vector2(100, 100)

def test_zoom_in(camera_system):
    initial_zoom = camera_system.current_zoom
    camera_system.zoom_in()
    assert camera_system.current_zoom == initial_zoom + 0.1  # Assuming SCREEN_ZOOM_STEP=0.1 from settings

def test_world_to_screen(camera_system):
    camera_system.position = pygame.Vector2(0, 0)
    screen_pos = camera_system.world_to_screen(pygame.Vector2(100, 100))
    assert screen_pos == pygame.Vector2(400 + 100, 300 + 100)  # screen_center (400,300) + pos * zoom (1.0)

def test_update_follow(camera_system):
    entity = MagicMock()
    entity.has_component.return_value = True
    entity.get_component.return_value.position = pygame.Vector2(200, 200)
    camera_system._target = entity
    camera_system.position = pygame.Vector2(0, 0)
    camera_system.update(1.0)  # dt=1, smoothness=0.1 -> position += (200-0)*0.1 = +20
    assert camera_system.position == pygame.Vector2(20, 20)

def test_apply_shake(camera_system):
    camera_system.apply_shake(0.5)
    assert camera_system._shake_timer == 0.5

@patch('random.random')
def test_update_shake(mock_random, camera_system):
    mock_random.return_value = 0.5  # For predictability
    camera_system._shake_timer = 0.1
    camera_system.update(0.05)  # Reduce timer to 0.05
    # Shake: (0.5*2-1)*FORCE = 0 * FORCE = 0, but random called
    assert mock_random.called