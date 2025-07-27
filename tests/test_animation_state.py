from components.animation_state import AnimationState


def test_animation_state_initialization():
    state = AnimationState("player", "idle")
    assert state.name == "player"
    assert state.current_state == "idle"
    assert state.previous_state is None


def test_state_transitions():
    state = AnimationState("player", "idle")

    state.set_current_state("walk")
    assert state.current_state == "walk"
    assert state.previous_state == "idle"

    state.switch_to_previous_state()
    assert state.current_state == "idle"
    assert state.previous_state == "walk"