class AnimationState:
    def __init__(self, name: str, initial_state: str):
        self.name = name
        self.current_state = initial_state
        self.previous_state = None

    def set_current_state(self, state):
        self.previous_state = self.current_state
        self.current_state = state

    def switch_to_previous_state(self):
        self.current_state, self.previous_state = self.previous_state, self.current_state

