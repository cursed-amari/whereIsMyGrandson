from pygame import Vector2
from components.transform import Transform

def test_transform_initialization():
    transform = Transform(Vector2(100, 200))
    assert transform.position == Vector2(100, 200)

def test_position_updates():
    transform = Transform(Vector2(100, 200))
    transform.position = Vector2(150, 300)
    assert transform.position.x == 150
    assert transform.position.y == 300