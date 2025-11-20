from . import command
from .command import Expression, CommandUsageError, NewCommand
from core.functional import program
import os

@NewCommand(
    "/exit!", "Exites.", 
    "/exit!"
)
def Exit(*args, **kwargs) -> None:
    os.abort()
    return


@NewCommand(
    "/reboot", "Reboots", 
    "/reboot"
)
def Reboot(*args, **kwargs) -> None:
    program.reboot()
    return