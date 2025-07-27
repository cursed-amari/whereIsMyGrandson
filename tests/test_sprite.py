from pygame import Surface
from components.sprite import Sprite

def test_sprite_initialization():
    surf = Surface((10, 10))
    sprite = Sprite(surf)
    assert sprite.image == surf