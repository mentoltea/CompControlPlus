from core import state
from .common import DT, ScreenState
import time

def EnsureState():
    if not hasattr(state.state, "screen"):
        state.state.screen = ScreenState() # type: ignore

def GetLocalState() -> ScreenState:
    EnsureState()
    return state.state.screen # type: ignore