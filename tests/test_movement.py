from pygame import Vector2
from components.movement import Movement

def test_movement_initialization():
    movement = Movement(300)
    assert movement.speed == 300
    assert movement.velocity == Vector2(0, 0)

def test_velocity_updates():
    movement = Movement(300)
    movement.velocity = Vector2(1, -1)
    assert movement.velocity.x == 1
    assert movement.velocity.y == -1