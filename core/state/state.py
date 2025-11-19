from typing import Callable

class State(object):
    def __init__(self, destructor: Callable | None = None):
        self.destructor = destructor
        
    def __del__(self):
        if (self.destructor):
            self.destructor()

state: State = State()