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


def test_get_frame(sample_frames):
    anim = Animation(sample_frames)
    assert anim.get_frame() == sample_frames[0]

    anim.current_frame = 2
    assert anim.get_frame() == sample_frames[2]