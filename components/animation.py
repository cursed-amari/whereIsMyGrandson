from pygame import Surface


class Animation:
    def __init__(self, frames: list[Surface], frame_rate=6):
        self.frames = frames
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.timer = 0
        self.speed_modifier = 1

    def get_frame(self):
        return self.frames[self.current_frame]
