import pytest
import pygame

@pytest.fixture(autouse=True, scope="session")
def pygame_setup():
    pygame.init()
    yield
    pygame.quit()