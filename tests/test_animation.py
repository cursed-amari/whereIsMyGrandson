import pytest
from pygame import Surface
from components.animation import Animation


@pytest.fixture
def sample_frames():
    return [Surface((10, 10)) for _ in range(3)]


def test_animation_initialization(sample_frames):
    anim = Animation(sample_frames, frame_rate=6)
    assert anim.current_frame == 0
    assert anim.timer == 0
    assert anim.frames == sample_frames
    assert anim.frame_rate == 6


def test_animation_update(sample_frames):
    anim = Animation(sample_frames, frame_rate=10)  # 0.1s per frame

    # Not enough time elapsed
    anim.update(0.05)
    assert anim.current_frame == 0
    assert anim.timer == 0.05

    # Time for one frame
    anim.update(0.05)
    assert anim.current_frame == 1
    assert anim.timer == 0

    # Wrap around frames
    anim.update(0.1)
    anim.update(0.1)
    assert anim.current_frame == 0


def test_get_frame(sample_frames):
    anim = Animation(sample_frames)
    assert anim.get_frame() == sample_frames[0]

    anim.current_frame = 2
    assert anim.get_frame() == sample_frames[2]