import os


SOURCES_ROOT = os.getcwd()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_ZOOM = 1
SCREEN_MIN_ZOOM = 0.5
SCREEN_MAX_ZOOM = 2.0
SCREEN_ZOOM_STEP = 0.1
SCREEN_SHAKE_FORCE = 1
DRAWING_RANGE = 400

PLAYER_SPEED = 600
PLAYER_HP = 100
ANIMATION_PATH = {
    "player_idle": (SOURCES_ROOT + "/src/animation/player/player_idle.png", 6, 1),
    "player_walk": (SOURCES_ROOT + "/src/animation/player/player_walk.png", 6, 1),
}
ENTITY_SIZE = {
    "player": (128, 128),
}


