from . import common, glue
from modules import screen, logger
from modules.commands import command
from tasks import task
import telebot


@command.NewCommand(
    "screenpoll", 
    "Manages screen polling", 
    "/screenpoll start [time] [s|m]"
    "\n"
    "/screenpoll stop"
    "\n"
    "/screenpoll status"
)
def ManageScreenPoll(*args, **kwargs):
    subcommand = args[0]
    reply = "OK"
    
    if subcommand == "start":
        tm = int(args[1])
        spec = args[2]
        if spec == 's': pass
        elif spec == 'm': tm *= 60
        else: raise command.CommandUsageError(f"Unexpected time specifier {spec}")
        screen.poller.start_polling_async(tm, glue.send_screen)
        
    elif subcommand == "stop":
        screen.poller.stop_polling()
    
    elif subcommand == "status":
        reply = screen.poller.get_polling_status()
    
    else: raise command.CommandUsageError(f"Cannot identify operation {subcommand}")
    
    return reply