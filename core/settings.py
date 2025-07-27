import os


SOURCES_ROOT = os.getcwd()

PLAYER_SPEED = 600
PLAYER_HP = 100
ANIMATION_PATH = {
    "player_idle": (SOURCES_ROOT + "/src/animation/player/player_idle.png", 6, 1),
    "player_walk": (SOURCES_ROOT + "/src/animation/player/player_walk.png", 6, 1),
}
ENTITY_SIZE = {
    "player": (128, 128),
}


