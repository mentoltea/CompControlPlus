import state
from command import Expression, CommandUsageError, NewCommand
from typing import Any
# import subprocess, os
from tasks import task

def EnsureState():
    if not hasattr(state.state, "cmd"):
        state.state.cmd = state.Object() # pyright: ignore[reportAttributeAccessIssue]

@NewCommand(
    "/cmd-reset", "Resets cmd module state", 
    "/cmd-reset"
)
def ResetState(*args, **kwargs) -> None:
    state.state.cmd = state.Object() # pyright: ignore[reportAttributeAccessIssue]

@NewCommand(
    "/cmd-new", "Creates new cursor", 
    "/cmd-new"
)
def CmdNew(*args, **kwargs) -> None:
    TODO
    
def CheckCursor() -> bool:
    EnsureState()
    return hasattr(state.state.cmd, "cursor") # pyright: ignore[reportAttributeAccessIssue]

@NewCommand(
    "/cmd-send", "Sends a line to cursor", 
    "/cmd-send"
)
def CmdSend(*args, **kwargs) -> str:
    TODO
    

