import pytest
import pygame

@pytest.fixture(autouse=True, scope="session")
def pygame_setup():
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()