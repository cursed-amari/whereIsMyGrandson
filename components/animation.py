from pygame import Surface


class Animation:
    def __init__(self, frames: list[Surface], frame_rate=6):
        self.frames = frames
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.timer = 0

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer >= 1 / self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0

    def get_frame(self):
        return self.frames[self.current_frame]
