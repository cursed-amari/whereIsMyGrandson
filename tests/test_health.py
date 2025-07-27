from components.health import Health

def test_health_initialization():
    health = Health(100)
    assert health.max_health == 100
    assert health.current_health == 100

def test_health_damage():
    health = Health(100)
    health.current_health = 75
    assert health.current_health == 75