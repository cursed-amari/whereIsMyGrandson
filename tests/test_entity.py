from pygame import Vector2

from entitys.entity import Entity
from components.transform import Transform
import pytest


def test_component_management():
    entity = Entity("entity")
    transform = Transform(Vector2(0, 0))

    entity.add_component("transform", transform)
    assert entity.has_component("transform")
    assert entity.get_component("transform") == transform

    with pytest.raises(ValueError):
        entity.get_component("missing")

    assert not entity.has_component("missing")