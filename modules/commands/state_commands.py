from core import state
from .command import Expression, CommandUsageError, NewCommand
from typing import Any

@NewCommand(
    "/reset!", "Resets global `state`. BE SURE WHAT YOU'RE DOING.", 
    "/reset! YES"
)
def ResetGlobalState(*args, **kwargs) -> None:
    if (len(args) != 1 or args[0] != "YES"):
        raise CommandUsageError("Check usage to know how to reset global state")
    
    del state.state
    state.state = state.State()