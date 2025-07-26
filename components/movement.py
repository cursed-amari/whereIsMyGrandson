from pygame import Vector2


class Movement:
    def __init__(self, speed: int):
        self.speed = speed
        self.velocity = Vector2()
