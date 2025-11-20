from . import command
from .command import Expression, CommandUsageError, NewCommand
from core.functional import program

@NewCommand(
    "/exit!", "Exites.", 
    "/exit!"
)
def Exit(*args, **kwargs) -> None:
    exit(0)
    return


@NewCommand(
    "/reboot", "Reboots", 
    "/reboot"
)
def Reboot(*args, **kwargs) -> None:
    program.reboot()
    return